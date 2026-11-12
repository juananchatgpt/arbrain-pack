#!/usr/bin/env node

import { readFile, access } from 'node:fs/promises'
import { constants } from 'node:fs'
import { resolve, join, dirname, extname } from 'node:path'

const site = process.argv[2]
if (!site) {
  console.error('Uso: validate-landing.mjs <sitio>')
  process.exit(2)
}

const root = resolve(site)
const errors = []
const warnings = []
const required = ['BRIEF.md', 'marca.json', 'ASSET-MANIFEST.json', 'LIMITACIONES.md', 'ACCEPTANCE.json']

for (const file of required) {
  if (!(await exists(join(root, file)))) errors.push(`falta ${file}`)
}

let brand = null
try {
  brand = JSON.parse(await readFile(join(root, 'marca.json'), 'utf8'))
  if (!isRecord(brand)) errors.push('marca.json debe contener un objeto')
} catch (error) {
  errors.push(`marca.json no es JSON válido: ${error instanceof Error ? error.message : String(error)}`)
}

for (const source of ['pagina.html', 'index.html']) {
  const path = join(root, source)
  if (!(await exists(path))) continue
  const html = await readFile(path, 'utf8')
  if (!/<html\b/i.test(html)) warnings.push(`${source}: no se detecta elemento html completo`)
  if (/<img\b(?![^>]*\balt=)/i.test(html)) errors.push(`${source}: hay una imagen sin atributo alt`)
  for (const reference of localReferences(html)) {
    if (!(await exists(join(root, reference)))) errors.push(`${source}: referencia local rota: ${reference}`)
  }
}

if (brand && !('incertidumbres' in brand || 'desconocidos' in brand)) {
  warnings.push('marca.json no declara incertidumbres/desconocidos; comprueba que los huecos del brief no se hayan rellenado')
}

const result = {
  valid: errors.length === 0,
  site: root,
  errors,
  warnings,
}
console.log(JSON.stringify(result, null, 2))
process.exit(result.valid ? 0 : 1)

function localReferences(html) {
  const refs = []
  const pattern = /\b(?:src|href)\s*=\s*["']([^"']+)["']/gi
  for (const match of html.matchAll(pattern)) {
    const value = match[1]
    if (!value || value.includes('{{') || value.includes('}}') || value.startsWith('#') || /^(?:https?:|mailto:|tel:|data:|javascript:)/i.test(value)) continue
    const clean = value.split('?')[0].split('#')[0]
    if (clean && extname(clean)) refs.push(clean.replace(/^\/+/, ''))
  }
  return [...new Set(refs)]
}

function isRecord(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value)
}

async function exists(path) {
  try {
    await access(path, constants.F_OK)
    return true
  } catch {
    return false
  }
}
