# Control de Calidad — Registro de la pasada de QA (v2.1)

> **Qué es.** Registro auditable del control de calidad hecho antes de sellar la versión **v2.1**. Sigue la
> filosofía del [Protocolo de Verificación](./PROTOCOLO_DE_VERIFICACION.md): lo que se revisa, se documenta.
> **Fecha de la pasada: 2026-07.**

---

## 1. Alcance revisado

- **52 tratados** de la Columna I (38 en Niveles I–V + 14 en Ramas Esenciales). *Actualizado en v2.2 con
  los tratados 12 (Procesal Penal), 13 (Familiar y Sucesiones) y 14 (Agrario), verificados con 47 secciones,
  0 enlaces rotos y markdown sano.*
- Documentos rectores, Laboratorio (11 ejercicios), Sistema de Repaso.

## 2. Resultados (✅ = correcto)

| Chequeo | Resultado |
|---------|-----------|
| **Integridad de archivos** | ✅ Los 52 tratados completos, sin truncamientos. |
| **Enlaces internos (`.md`)** | ✅ **0 enlaces rotos** (se resolvieron todas las referencias cruzadas). |
| **Markdown** | ✅ Sano (todos los bloques de código ` ``` ` cerrados). |
| **Typos** | ✅ Corregido 1 ("doned es" → "donde es", ejercicio 11 del Laboratorio). |
| **Secciones por tratado** | ⚠️ Ver punto 3 (dos formatos conviven; documentado y homologado por norma). |

## 3. Estándar de secciones (aclaración y homologación)

La pasada detectó **tres formatos** conviviendo. Se **homologan por norma** (ver
[PLANTILLA-LIBRO.md](./PLANTILLA-LIBRO.md)) así:

| Grupo | Tratados | Encabezados `##` | Estándar |
|-------|----------|------------------|----------|
| **Ramas Esenciales (01–14) + IV-09, IV-10** | 16 | **47** | V3 pleno: 43 numeradas + **4** transversales ✦ al cierre. |
| **V3 "primera hornada"** (Nivel II, III, IV-01–08, V) | 23 | **46** | V3: 43 numeradas + **3** transversales ✦ al cierre; la 4ª —*Nivel de importancia profesional*— aparece como **bloque de estrellas al inicio** ("vista rápida"). **Formato válido.** |
| **Nivel I · Fundamentos** | 13 | 32 | Estándar fundacional de 30 secciones + **bloque de 4 secciones transversales V3** añadido al cierre (como subsecciones). **Formato válido.** |

> **Norma de homologación (v2.1):** la transversal *"Nivel de importancia profesional"* es **obligatoria**,
> pero puede presentarse **como bloque de estrellas al inicio** ("vista rápida") **o** como sección ✦ al
> cierre —o ambas—. Las tres presentaciones son **V3-conformes**. No se exige duplicar el bloque de
> estrellas donde ya aparece arriba. La eventual migración del Nivel I al V3 pleno (43 secciones) queda
> como tarea de una versión futura.

## 4. Estado de la verificación de datos (resumen; detalle en el Protocolo §V)

- ✅ **Verificado contra fuentes** (tasas, fechas y hechos de reforma): ISR 30 % · IVA 16 %/0 % · arts. 2,
  42, 69-B CFF · Ley de Amparo 2013 · reforma judicial 15-sep-2024 · CNPCF 7-jun-2023 · vacaciones dignas
  2022/2023 · penal 2008/2016 · CNPP 2014 · LFPPI 2020 (**+ reforma 2026**) · NY 1958/1971 · UNCITRAL
  1985/1993 · GDPR 2018 · INAI→Secretaría Anticorrupción 2025 · LGEEPA 1988 (**+ iniciativa 2026**).
- ✅ **VERBATIM COMPLETADO en el nicho fiscal (v3.1):** con los textos oficiales del **CFF** (DOF 09-04-2026)
  y la **LISR** (DOF 01-04-2024) ya en [`fuentes-legales/`](./fuentes-legales/), se cotejó **palabra por
  palabra** el articulado fiscal: **CFF** arts. 1º, 2º, 4º, 5º-A, 6º, 17-A, 21, 26, 42, 67, 69-B, 146;
  **LISR** arts. 9, 27, 28, 57, 152. En 01-Fiscal se voltearon **30 marcas ⚠️→✅**. Detalle en Protocolo §V.
- ✅ **VERBATIM AMPLIADO al núcleo corporativo (v3.2):** con 7 textos oficiales más en
  [`fuentes-legales/`](./fuentes-legales/) se cotejó palabra por palabra: **LGSM** (1º/25/58/87/88/89),
  **LGTOC** (5º/76/170/175), **LMV** (1/2/22), **CCF** (1792/1794/1803/2248), **LFT** (47/48/123/132),
  **CPF** (7º/386; **390 = «Derogado»**) y **Ley de Amparo** (1º/5º/107/170). Fechas de vigencia en el README de fuentes.
- ✅ **Nueva convención ⟳ (apóstrofe de vigencia):** añadida a **cada artículo citado** de toda la biblioteca
  (**982 marcas**) más un callout explicativo en los **58 tratados**. Recuerda al lector que **✅ verifica a
  una fecha, no para siempre**, y lo obliga a recontrastar el artículo en su código. Verificado: 0 marcas
  dentro de bloques de código, 0 archivos con markdown roto.
- ✅ **CORAZÓN CORPORATIVO COMPLETO (v3.3):** 8 leyes más cotejadas verbatim en
  [`fuentes-legales/`](./fuentes-legales/) — **CPEUM** (1º/27/**31-IV**/103/107/123), **Código de
  Comercio** (1º/3º/75), **LFCE** (1º/53/56/86), **LFPPI** (1º/57/111), **LIVA** (1º=**16%**, 2º-A=**0%**),
  **LCM** (1º/10), **LIC** (2º/46), **LIE** (1º/5º/6º/7º). Con la CPEUM en mano se voltearon **11 marcas
  ⚠️→✅** del **art. 31-IV** (la base constitucional del deber de contribuir, antes sin fuente) y se
  corrigieron 12 marcadores ⟳ mal colocados. **17 leyes** ya son fuente primaria verificada.
- ⚠️ **Pendiente (para "referencia verificada" plena):** el verbatim de las leyes **aún no subidas**
  (LFPDPPP, LGEEPA, CNPP, CNPCF, LGRA, LFPC…). Metodología ya probada; basta subir su texto a
  `fuentes-legales/` y repetir el cotejo.

## 5. Fechado global

> **Salvo indicación en contrario, todo el contenido está fechado a 2026-07.** El Derecho se reforma;
> verifica siempre las normas, tasas, montos, plazos y artículos contra su **texto vigente** a la fecha de
> consulta (DOF, SAT, SJF). Esta obra es un **sistema conceptual y de estudio**, no una fuente
> autoritativa de citas.

## 6. Qué significa el sello v2.1

- **v2.1 es una "versión de estudio" sellada:** consistente, sin defectos de forma, con datos de alto
  riesgo (fechas, tasas, hechos de reforma) verificados y trazables.
- **NO es aún una "referencia verificada para imprimir/citar":** eso llegará cuando se cierre la
  verificación verbatim de artículos (punto 4) en una **v2.2**.

## 7. Pendientes para v2.2 (hoja de ruta de mejora)

1. Verificación verbatim de números de artículo (grupo crítico).
2. Banco de jurisprudencia real verificada en el SJF.
3. Materias faltantes: Procesal Penal a fondo, Familiar, Agrario.
4. Bibliografías con edición/año; glosario maestro bilingüe.
5. Mazo Anki completo por tratado; calendario de estudio; más ejercicios de Laboratorio (VC,
   financiamiento, SPA modelo anotado).
6. (Opcional) Migrar el Nivel I al V3 pleno de 43 secciones.

---

*Control de Calidad · Proyecto AJE · pasada de 2026-07 para el sello v2.1. Documento vivo: actualízalo en
cada nueva pasada de QA.*
