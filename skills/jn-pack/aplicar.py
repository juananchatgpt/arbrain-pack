#!/usr/bin/env python3
"""Aplica tu pack (capa común + capa del cliente) encima de un Arbrain, sin pisar nada del cliente.

    python3 aplicar.py <arbrain> <comun> [<cliente>]            # aplica
    python3 aplicar.py <arbrain> <comun> [<cliente>] --revisar  # solo dice qué haría

Qué hace:
  - Copia skills/ a .claude/skills/, negocio/ a mi-negocio/pack/ y marca/ a mi-marca/.
    Si el común y el cliente traen el mismo archivo, gana el del cliente.
  - Pone MEMORIA.md (común y cliente) en un bloque marcado dentro de .claude/memory/MEMORY.md,
    que el chat de la app y Claude Code cargan siempre. El resto de MEMORY.md no se toca.
  - Anota lo que escribió, con su huella, en mi-negocio/pack/.manifiesto.json. En la siguiente pasada solo
    reemplaza un archivo si sigue tal cual lo dejó el pack: si el cliente lo cambió, lo respeta y avisa.
  - Lo que el pack ya no trae lo mueve a ~/Arbrain-respaldos/pack-<fecha>/ (nunca borra).
  - Guarda el resultado en un commit de la rama mi-arbrain, solo con los archivos del pack.
Solo usa la biblioteca estándar de Python 3.9+ (macOS, Linux y Windows).

Líneas de salida: PACK_ESCRIBE, PACK_RESPETA, PACK_RETIRA, PACK_AVISO y, al final, PACK_OK o PACK_FALLA.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

MANIFIESTO = "mi-negocio/pack/.manifiesto.json"
FUENTE = "mi-negocio/pack/.fuente"  # aquí viven los clones del pack; git los ignora
INICIO = "<!-- pack:inicio · lo escribe el pack, no lo edites a mano -->"
FIN = "<!-- pack:fin -->"
MAPA = {"skills": ".claude/skills", "negocio": "mi-negocio/pack", "marca": "mi-marca"}


def huella(ruta: Path) -> str:
    # Sin \r: en Windows git puede reescribir los finales de línea, y eso no es un cambio del cliente
    return hashlib.sha256(ruta.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def falla(motivo: str) -> int:
    print(f"PACK_FALLA {motivo}")
    return 1


def leer_json(ruta: Path) -> dict:
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def git(raiz: Path, *args: str, entrada: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(raiz), *args], input=entrada, capture_output=True, text=True, encoding="utf-8")


def archivos(capa: Path, prefijo: str, prohibidas: set[str]) -> dict[str, Path]:
    """Destino relativo en Arbrain -> archivo de origen, para una capa."""
    salida: dict[str, Path] = {}
    for carpeta, destino in MAPA.items():
        base = capa / carpeta
        if not base.is_dir():
            continue
        for origen in sorted(p for p in base.rglob("*") if p.is_file()):
            rel = origen.relative_to(base)
            if rel.name in (".gitkeep", ".DS_Store") or any(parte.startswith(".git") for parte in rel.parts):
                continue
            if carpeta == "skills":
                skill = rel.parts[0]
                if len(rel.parts) == 1 or not skill.startswith(prefijo + "-") or skill in prohibidas:
                    print(f"PACK_AVISO skill «{skill}» de {capa.name} ignorada: debe ser una carpeta que empiece por «{prefijo}-»")
                    continue
            salida[f"{destino}/{rel.as_posix()}"] = origen
    return salida


def bloque_memoria(comun: Path, cliente: Path | None, nombre: str) -> str:
    partes = []
    for capa, titulo in ((comun, f"Pack {nombre}"), (cliente, "Este cliente")):
        if capa is None:
            continue
        ruta = capa / "MEMORIA.md"
        if ruta.is_file() and ruta.read_text(encoding="utf-8").strip():
            partes.append(f"### {titulo}\n\n{ruta.read_text(encoding='utf-8').strip()}")
    if not partes:
        return ""
    return INICIO + "\n## Mi pack\n\n" + "\n\n".join(partes) + "\n" + FIN


def poner_bloque(texto: str, bloque: str) -> str:
    if INICIO in texto and FIN in texto:
        antes, resto = texto.split(INICIO, 1)
        despues = resto.split(FIN, 1)[1]
        if not bloque:
            return antes.rstrip() + "\n" + despues.lstrip("\n")
        return antes + bloque + despues
    if not bloque:
        return texto
    return texto.rstrip() + "\n\n" + bloque + "\n"


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # la consola de Windows no es UTF-8
    revisar = "--revisar" in argv
    rutas = [a for a in argv if not a.startswith("--")]
    if len(rutas) not in (2, 3):
        return falla("uso: aplicar.py <arbrain> <comun> [<cliente>] [--revisar]")
    raiz, comun = Path(rutas[0]).expanduser().resolve(), Path(rutas[1]).expanduser().resolve()
    cliente = Path(rutas[2]).expanduser().resolve() if len(rutas) == 3 else None
    if not (raiz / "CAPAS.json").is_file():
        return falla(f"{raiz} no parece un Arbrain (falta CAPAS.json)")
    ajustes = leer_json(comun / "pack.json")
    prefijo, nombre = ajustes.get("prefijo"), ajustes.get("nombre", "del autor")
    if not prefijo:
        return falla(f"falta «prefijo» en {comun / 'pack.json'}")
    if cliente is not None and not cliente.is_dir():
        return falla(f"no existe la capa del cliente {cliente}")
    prohibidas = set(leer_json(raiz / "CAPAS.json").get("skills_del_autor") or [])

    rama = git(raiz, "branch", "--show-current").stdout.strip()
    if rama != "mi-arbrain":
        return falla(f"Arbrain está en la rama «{rama or '?'}», no en mi-arbrain: no aplico nada")

    nuevos = archivos(comun, prefijo, prohibidas)
    if cliente is not None:
        nuevos.update(archivos(cliente, prefijo, prohibidas))  # gana el cliente

    manifiesto = leer_json(raiz / MANIFIESTO)
    previos: dict[str, str] = manifiesto.get("archivos") or {}
    semilla = raiz / (leer_json(raiz / "CAPAS.json").get("semilla") or "arbrain/cerebro/semilla")
    registro: dict[str, str] = {}
    tocados: list[str] = []
    escritos = respetados = retirados = 0

    def es_del_pack(destino: Path, rel: str) -> bool:
        """El archivo actual lo dejó el pack (o es la semilla de Arbrain): se puede reemplazar."""
        actual = huella(destino)
        if previos.get(rel) == actual:
            return True
        return (semilla / rel).is_file() and huella(semilla / rel) == actual

    for rel, origen in sorted(nuevos.items()):
        destino = raiz / rel
        nueva = huella(origen)
        if destino.is_file():
            if huella(destino) == nueva:
                registro[rel] = nueva
                continue
            if not es_del_pack(destino, rel):
                if previos.get(rel) != nueva:  # avisa solo si el pack trae algo distinto de lo que el cliente cambió
                    print(f"PACK_RESPETA {rel} (lo cambió el cliente; el pack no lo pisa)")
                    respetados += 1
                if rel in previos:
                    registro[rel] = previos[rel]  # sigue siendo del pack, pero queda su versión
                continue
        print(f"PACK_ESCRIBE {rel}")
        escritos += 1
        registro[rel] = nueva
        tocados.append(rel)
        if not revisar:
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(origen, destino)

    respaldo = Path.home() / "Arbrain-respaldos" / f"pack-{datetime.datetime.now():%Y-%m-%d-%H%M}"
    for rel in sorted(set(previos) - set(nuevos)):
        destino = raiz / rel
        if not destino.is_file():
            continue
        if huella(destino) != previos[rel]:
            print(f"PACK_RESPETA {rel} (el pack ya no lo trae, pero el cliente lo cambió: se queda)")
            respetados += 1
            continue
        print(f"PACK_RETIRA {rel} → {respaldo}")
        retirados += 1
        tocados.append(rel)
        if not revisar:
            (respaldo / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(destino), str(respaldo / rel))
            carpeta = destino.parent  # quita las carpetas que quedaron vacías (una skill retirada, por ejemplo)
            while carpeta != raiz and carpeta.name not in ("skills", "pack", "mi-marca") and not any(carpeta.iterdir()):
                carpeta.rmdir()
                carpeta = carpeta.parent

    memoria = raiz / ".claude/memory/MEMORY.md"
    if memoria.is_file():
        texto = memoria.read_text(encoding="utf-8")
        nuevo_texto = poner_bloque(texto, bloque_memoria(comun, cliente, nombre))
        if nuevo_texto != texto:
            print("PACK_ESCRIBE .claude/memory/MEMORY.md (bloque del pack)")
            tocados.append(".claude/memory/MEMORY.md")
            if not revisar:
                memoria.write_text(nuevo_texto, encoding="utf-8")
    else:
        print("PACK_AVISO no hay .claude/memory/MEMORY.md: Arbrain aún no sembró su memoria; vuelve a aplicar después")

    def commit_de(capa: Path | None) -> str:
        return git(capa, "rev-parse", "--short", "HEAD").stdout.strip() if capa else ""

    nombre_cliente = ""
    if cliente is not None:  # «pack-acme» en su dirección de GitHub → «acme»
        origen = git(cliente, "remote", "get-url", "origin").stdout.strip().rstrip("/")
        nombre_cliente = origen.rsplit("/", 1)[-1].removesuffix(".git").removeprefix("pack-") if origen else cliente.name
    version = ajustes.get("version", "?")
    resumen = f"comun={version}" + (f" cliente={nombre_cliente}@{commit_de(cliente) or '?'}" if cliente else "")
    if revisar:
        print(f"PACK_OK revisar {resumen} escribiria={escritos} respetaria={respetados} retiraria={retirados}")
        return 0

    (raiz / MANIFIESTO).parent.mkdir(parents=True, exist_ok=True)
    (raiz / MANIFIESTO).write_text(json.dumps({
        "comun": {"version": version, "commit": commit_de(comun)},
        "cliente": {"nombre": nombre_cliente, "commit": commit_de(cliente)} if cliente else None,
        "archivos": registro,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    excluir = raiz / ".git/info/exclude"
    if excluir.parent.is_dir():
        actual = excluir.read_text(encoding="utf-8") if excluir.is_file() else ""
        if FUENTE + "/" not in actual:
            excluir.write_text(actual.rstrip("\n") + ("\n" if actual else "") + FUENTE + "/\n", encoding="utf-8")

    # Al commit entra solo lo del pack, aunque el cliente tenga otros cambios a medias. Incluye lo que ya está tal cual lo
    # trae el pack pero sin guardar (una pasada anterior que se cortó); lo que cambió el cliente no.
    del_pack = sorted({MANIFIESTO, *tocados, *(r for r, h in registro.items() if (raiz / r).is_file() and huella(raiz / r) == h)})
    lista = "\n".join(del_pack) + "\n"
    git(raiz, "--literal-pathspecs", "add", "-A", "--pathspec-from-file=-", entrada=lista)
    preparados = set(git(raiz, "diff", "--cached", "--name-only", "-z").stdout.split("\0"))
    if preparados & set(del_pack):
        hecho = git(raiz, "--literal-pathspecs", "commit", "-q", "-m", f"Pack: {resumen}", "--pathspec-from-file=-", entrada=lista)
        if hecho.returncode != 0:
            return falla(f"no pude guardar el commit: {hecho.stderr.strip()}")
    print(f"PACK_OK {resumen} escritos={escritos} respetados={respetados} retirados={retirados}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
