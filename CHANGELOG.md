# Bitácora de versiones · Proyecto AJE

> Registro de la evolución del proyecto. Las versiones mayores se **sellan** en una rama de git
> para preservarlas intactas (Documento Fundacional, sección XII). Formato inspirado en
> *Keep a Changelog*; fechas en formato AAAA-MM.

---

## [3.4] — 2026-07 · «Corpus legal completo (27 leyes)» — *rama `v3.4-corpus-completo`, PR*

> **Qué es la v3.4.** El cierre del corpus: se integran las **10 leyes finales** (procesal, datos,
> responsabilidades, ambiental, consumidor, autor, seguridad social). Con ellas, **prácticamente cada
> artículo citado en toda la biblioteca tiene su texto oficial verificado en `fuentes-legales/`**.

### Añadido — 10 fuentes oficiales (Word `.doc` → UTF-8)
- **CNPP** (DOF 28-11-2025), **CNPCF** (15-01-2026), **LFPDPPP** (14-11-2025, *nueva ley 2025*),
  **LGRA** (15-12-2025), **LGEEPA** (19-01-2026), **LFPC** (12-12-2025), **LFPCA** (09-06-2026),
  **LFDA** (14-05-2026), **LSS** (15-01-2026), **CFPC** (abrogado). **Corpus total: 27 leyes.**

### Verificado (✅ verbatim)
- **CNPP:** 1º, 211 · **CNPCF:** 1º · **LFPDPPP:** 1º, 3º · **LGRA:** 1º, 7º · **LGEEPA:** 1º, 3º ·
  **LFPC:** 1º · **LFPCA:** 1º · **LFDA:** 1º, 11 · **LSS:** 1º, 2º · **CFPC:** 1º.

### Hallazgo de vigencia (⟳ en acción)
- El **Código Federal de Procedimientos Civiles (CFPC)** está **ABROGADO**: deja de regir a más tardar el
  **1-abr-2027**, sustituido por el CNPCF. Un **código entero** de salida — el ejemplo definitivo de por
  qué existe la apóstrofe de vigencia. Marcado como tal en el README de fuentes.

---

## [3.3] — 2026-07 · «Corazón corporativo completo (CPEUM + 7 leyes)» — *rama `v3.3-corpus-corporativo`, PR #7 fusionado*

> **Qué es la v3.3.** Se cierran las **8 leyes de prioridad máxima** del derecho corporativo. Con esto,
> el fiscal, el mercantil, el M&A, la competencia, el concursal, el bancario y la inversión extranjera
> quedan respaldados en **fuente primaria verificada** — y, por fin, la **Constitución** en el repo.

### Añadido — 8 fuentes oficiales (Word `.doc` → UTF-8)
- **CPEUM** (DOF 02-06-2026), **Código de Comercio** (14-11-2025), **LFCE** (14-11-2025),
  **LFPPI** (03-04-2026), **LIVA** (12-11-2021), **LCM** (14-11-2025), **LIC** (14-11-2025),
  **LIE** (27-05-2024). Total: **17 leyes** en [`fuentes-legales/`](./fuentes-legales/).

### Verificado (✅ verbatim)
- **CPEUM:** 1º, 27, **31-IV**, 103, 107, 123 · **CCom:** 1º, 3º, 75 · **LFCE:** 1º, 53, 56, 86 ·
  **LFPPI:** 1º, 57, 111 · **LIVA:** 1º (**16%**), 2º-A (**0%**) · **LCM:** 1º, 10 · **LIC:** 2º, 46 ·
  **LIE:** 1º, 5º, 6º, 7º.

### Corregido
- **Art. 31-IV CPEUM:** estaba en ⚠️ desde v3.1 (no teníamos la Constitución). Ahora verificado →
  **11 marcas ⚠️→✅** en 01-Fiscal y 02-Constitucional.
- **12 marcadores ⟳** que habían quedado a media cita (p. ej. «fr. ⟳IV») reubicados al final de la cita.

---

## [3.2] — 2026-07 · «Núcleo corporativo verificado + Apóstrofe de vigencia» — *rama `v3.2-corpus-y-vigencia`, PR #6 fusionado*

> **Qué es la v3.2.** Dos saltos grandes: (1) el **núcleo del derecho corporativo** pasa a **fuente primaria
> verificada** con 7 leyes más cotejadas verbatim; (2) nace la **⟳ apóstrofe de vigencia**, que educa al
> lector para que **nunca** confíe en una cita como eterna y la recontraste en el código.

### Añadido — fuentes oficiales (Word `.doc` → UTF-8)
- **7 leyes nuevas** en [`fuentes-legales/`](./fuentes-legales/), extraídas de los `.doc` oficiales de la
  Cámara de Diputados con un conversor propio ([`tools/doc2txt.py`](./tools/doc2txt.py), parseo del *piece
  table* de Word): **LGSM** (DOF 20-10-2023), **LGTOC** (26-03-2024), **LMV** (14-11-2025), **CCF**
  (14-11-2025), **LFT** (14-05-2026), **CPF** (13-03-2026), **Ley de Amparo** (16-10-2025).

### Verificado (✅ verbatim — número de artículo ↔ contenido)
- **LGSM:** 1º, 25, 58, 87, 88, 89 · **LGTOC:** 5º, 76, 170, 175 · **LMV:** 1, 2, 22 ·
  **CCF:** 1792, 1794, 1803, 2248 · **LFT:** 47, 48, 123, 132 · **CPF:** 7º, 386 (y **390 = «Derogado»**) ·
  **Amparo:** 1º, 5º, 107, 170.

### Añadido — convención ⟳ (apóstrofe de vigencia)
- Marcador **⟳** tras **cada artículo citado** de toda la biblioteca (**982 marcas**), aplicado con un
  script idempotente y seguro (no toca bloques de código).
- **Callout explicativo** bajo el título de los **58 tratados**, con el caso real del **art. 390 CPF derogado**.
- Símbolo definido en el **Protocolo §II**; registro en **§V/§VI**; `CONTROL-DE-CALIDAD` actualizado.

### Nota de calidad
- Verificación automática: **0** marcas dentro de bloques de código y **0** archivos con markdown roto.

---

## [3.1] — 2026-07 · «Referencia Verificada — Fiscal» — *rama `v3.1-verificacion-fiscal`, PR #5 fusionado*

> **Qué es la v3.1.** Primer bloque del sello "**Referencia Verificada plena**" hecho realidad: con los
> textos oficiales del **CFF** y la **LISR** ya disponibles, se cotejó **palabra por palabra** el
> articulado del **nicho fiscal-corporativo** (el nicho objetivo del proyecto). Los números de artículo
> del área fiscal dejan de ser "por confirmar" y pasan a **fuente primaria verificada**.

### Añadido
- **Carpeta `fuentes-legales/`** — textos oficiales vigentes en **UTF-8** (convertidos desde Latin-1) que
  sirven de **fuente primaria** para el sello: **CFF** (última reforma DOF 09-04-2026) y **LISR** (última
  reforma DOF 01-04-2024), con su propio `README.md` y protocolo para añadir más leyes.

### Verificado (✅ verbatim — número de artículo ↔ contenido)
- **CFF:** arts. **1º, 2º, 4º, 5º-A (razón de negocios), 6º, 17-A, 21, 26, 42, 67 (caducidad 5 años),
  69-B (EFOS), 146 (prescripción 5 años)**.
- **LISR:** arts. **9 (ISR PM 30%), 27, 28, 57 (pérdidas = 10 ejercicios), 152 (tarifa PF)**.
- En **01-Derecho-Fiscal** se voltearon **30 marcas ⚠️→✅**; se añadió *Registro de verificación* verbatim
  en **01-Fiscal** e **IV-09 Fiscal Corporativo**; se registró todo en el **Protocolo §V** y §VI.

### Pendiente (para "Referencia Verificada plena")
- Verbatim de las demás leyes (Ley de Amparo, LFT, CPF, LGTOC, LMV, CCF, LFPPI…): subir su texto íntegro
  a `fuentes-legales/` y repetir el cotejo. La **metodología ya está probada** con CFF/LISR.

---

## [3.0] — 2026-07 · «Referencia y enriquecimiento» — *sellada (rama `v3.0-referencia`, PR #3 fusionado)*

> **Qué es la v3.0.** Añade la **capa de enriquecimiento** que separa una biblioteca "completa" de una "de
> referencia": glosario bilingüe, sistema de repaso ampliado y avance de verificación. **Honestidad
> (Principio Supremo):** la v3.0 **no** significa "todo verificado". Persisten **~900 marcas ⚠️** (números
> de artículo) cuya verificación *verbatim* está **gated en el acceso a texto legal íntegro** (las
> herramientas confirman tasas, fechas y hechos de reforma, pero no permiten extraer el articulado
> completo). El sello "**Referencia Verificada plena**" llegará cuando se cierren esas marcas.

### Añadido
- **`GLOSARIO-BILINGUE.md`** — glosario maestro **español ⇄ inglés** (~180 términos en 13 áreas) + sección
  de **"falsos amigos"** (crédito fiscal ≠ *tax credit*, rescisión ≠ *rescission*, sede ≠ *venue*, etc.).
  Materializa el **Principio 6 (bilingüismo)**.
- **Sistema de Repaso ampliado:** mazo **Anki** con +44 tarjetas (Procesal Penal, Familiar, Agrario y
  bilingües) y **banco de preguntas** con las secciones 13–15 de las nuevas materias.
- **CONTROL-DE-CALIDAD** actualizado a **52 tratados**.

### Verificado (✅, avance)
- Lote adicional cotejado por búsqueda de frase exacta: **LGSM art. 1 y art. 88** (registrado en el
  Protocolo §V). Suma a lo ya verificado en v2.1 (ISR/IVA, fechas de reforma, etc.).

### Pendiente (para "Referencia Verificada plena")
- Verificación *verbatim* de los **~900 números de artículo** (CFF, LISR, LGSM, LGTOC, LMV, CCF, LFT, CPF,
  Ley de Amparo, LFPPI, LGEEPA, Ley Agraria…) —requiere fuente de texto legal íntegro navegable—; **banco
  de jurisprudencia** verificada en el SJF; bibliografías con edición/año.

---

## [2.2] — 2026-07 · «Materias faltantes: currículum completo» — *sellada (rama `v2.2`)*

> Completa el **plan de estudios** con las materias que faltaban para **titularse** y ejercer con solidez.
> La Biblioteca pasa de **49 a 52 tratados**.

### Añadido
- **3 tratados nuevos** en Ramas Esenciales, al estándar V3 (47 secciones = 43 + 4 transversales; datos
  duros ⚠️; sello 2026-07):
  - **12 · Derecho Procesal Penal** — el sistema acusatorio a fondo (etapas, prisión preventiva, salidas,
    prueba, recursos, amparo y ejecución) y la **defensa white-collar** de directivos y de la persona moral.
  - **13 · Derecho Familiar y Sucesiones** — regímenes patrimoniales, divorcio, sucesión (testamentaria e
    intestamentaria), **empresa familiar** y planeación patrimonial (puente con la Columna V).
  - **14 · Derecho Agrario** — propiedad social (ejido/comunidad), reforma de 1992, dominio pleno y acceso a
    la tierra: riesgo de titularidad en **real estate, energía e infraestructura**.
- **Documentos rectores** actualizados: README de Ramas Esenciales (12–14), Índice Maestro (52 tratados),
  README y Avance (conteo 52).

### Pendiente (hoja de ruta, continúa de v2.1)
- Verificación *verbatim* de números de artículo; banco de jurisprudencia (SJF); bibliografías con edición/
  año; glosario bilingüe; mazo Anki completo; más ejercicios de Laboratorio.

---

## [2.1] — 2026-07 · «Ramas Esenciales, actualización normativa y sello de calidad» — *sellada (rama `v2.1`)*

> **Sello v2.1 = "versión de estudio".** Consistente, sin defectos de forma y con los datos de **alto
> riesgo** (tasas, fechas y hechos de reforma) **verificados y trazables** (ver
> [CONTROL-DE-CALIDAD.md](./CONTROL-DE-CALIDAD.md) y el Protocolo §V). **No** es todavía una "referencia
> verificada para citar/imprimir": eso llegará en la **v2.2**, al cerrar la verificación *verbatim* de los
> números de artículo.

Amplía la Columna I con las **materias transversales que faltaban** (para poder titularse y ejercer
cualquier rama, no solo el corporativo) y corrige errores de actualidad detectados. La Biblioteca pasa
de **38 a 49 tratados**.

### Añadido
- **Nueva sección `Columna-I-Biblioteca/Ramas-Esenciales/`** con **11 tratados nuevos** al estándar V3
  (43 secciones + 4 transversales cada uno; datos duros marcados ⚠️ y sello de fecha 2026-07):
  **01 Derecho Fiscal (base)** —cimiento del nicho fiscal-corporativo—, **02 Constitucional y Amparo**,
  **03 Administrativo**, **04 Procesal Civil y Mercantil**, **05 Laboral**, **06 Penal Económico y
  Compliance**, **07 Propiedad Intelectual**, **08 DIP y Arbitraje**, **09 Protección de Datos**,
  **10 Ambiental** y **11 Ética Profesional**. Incluye un **README-índice** con la guía de *cuándo*
  estudiar cada rama (no es una escalera, es un mapa).

- **Enriquecimiento del Nivel I:** se inyectaron las **4 secciones transversales V3** (¿Por qué importa al
  corporativo?, Cómo piensa un socio, Errores que cuestan millones, Nivel de importancia ★) a los **13
  tratados fundacionales**, que estaban en el estándar de 30 secciones.
- **Nueva carpeta `Sistema-de-Repaso/`** (retención): **mazo Anki (`flashcards-anki.csv`)** importable con
  ~130 tarjetas de todas las materias, y **banco de preguntas** por área con respuestas modelo, más una
  guía de repaso espaciado.
- **Columna III · Laboratorio → Tramo 3:** nuevo **Ejercicio 11 · El Redline** (marcar el borrador de la
  contraparte), la destreza más usada por el asociado junior. El Laboratorio pasa a **3 tramos · 11
  ejercicios**.

### Corregido
- **COFECE/IFT → CNA:** la reforma de simplificación orgánica (2024) y la reforma a la **LFCE** (en vigor
  17-jul-2025) **extinguieron la COFECE y el IFT** y crearon la **Comisión Nacional Antimonopolio (CNA)**.
  Añadido recuadro de *Actualización Normativa Crítica* en el tratado IV-10 (Competencia), nota en I-03
  (Teoría del Estado) y registro en el **Protocolo de Verificación** (§V). Menciones análogas señaladas
  en Constitucional/Amparo, Administrativo y Datos (extinción del **INAI** por la misma reforma).
- **Conteo** unificado: **49 tratados** (38 en Niveles I–V + 11 Ramas Esenciales) y Laboratorio con **11
  ejercicios**, en README, Índice Maestro, Avance y Mapa.

### Control de calidad (sello v2.1)
- **Pasada de QA** documentada en [CONTROL-DE-CALIDAD.md](./CONTROL-DE-CALIDAD.md): 49 tratados íntegros,
  **0 enlaces internos rotos**, markdown sano, 1 typo corregido.
- **Homologación del estándar** de secciones transversales y **fechado global (2026-07)** documentados
  (Plantilla + QA).
- **Verificación de datos de alto riesgo** (tasas, fechas, hechos de reforma) en 10/11 Ramas + IV-10,
  registrada en el Protocolo §V.

### Pendiente (hoja de ruta v2.2)
- **Verificación *verbatim* de números de artículo** (CFF, LISR, LGSM, etc.) —requiere fuente de texto
  legal íntegro—; banco de jurisprudencia (SJF); materias faltantes (Procesal Penal, Familiar, Agrario);
  bibliografías con edición/año; glosario bilingüe; mazo Anki completo; más ejercicios de Laboratorio.

---

## [2.0] — 2026 · «De biblioteca a sistema» — *sellada (rama `v2.0`)*

El proyecto deja de ser "una biblioteca" y se convierte en un **sistema integral de cinco
columnas**, gobernado por seis principios rectores. Estado al sellar: **5 columnas completas**
(Biblioteca con 38 tratados, Hoja de Ruta + Sistema Diario + Inglés + Tesis Estratégica,
Laboratorio con su 1er tramo de 6 ejercicios, Sistema del Socio con 7 módulos, Patrimonio con 6
módulos) + Protocolo de Verificación + Mapa Biblioteca↔Materias, reorganizado en carpetas
`Columna-I` … `Columna-V`.

### Añadido
- **`00_DOCUMENTO_FUNDACIONAL_AJE.md`** — documento **rector supremo**: misión reformulada (el
  asesor indispensable, no "el más famoso"), visión, identidad del Consejo, el Estudiante con
  honestidad, las **cinco columnas** y su secuencia, los **seis principios rectores**
  (1-SUPREMO Integridad Intelectual y Verificación, 2-Integridad Ética, 3-Realismo y Ejecución,
  4-Valor, 5-Conexión, 6-Bilingüismo), estándar académico/editorial, regla suprema, las 12
  preguntas antes de escribir y cómo se construye el proyecto.
- **`01_HOJA_DE_RUTA_AJE.md`** — Columna II: estrategia profesional con 6 fases (de "apagar el
  incendio" a "asesor indispensable/élite"), plan de 90 días, guion de contactos e indicadores.
- **`02_PLAN_OPERATIVO_DIARIO_AJE.md`** — El Sistema Diario: capa operativa que convierte todo el
  repo en una rutina diaria (jerarquía de prioridad, día mínimo innegociable, semana modelo hora
  por hora, tablero de hábitos, revisión semanal y protocolo de recaída).
- **`INDICE_MAESTRO.md`** — mapa navegable de todo el repositorio.
- **`CHANGELOG.md`** — esta bitácora.
- **`03_PLAN_DE_INGLES_JURIDICO_AJE.md`** (Columna II), **`MAPA_BIBLIOTECA-A-MATERIAS.md`** y
  **`PROTOCOLO_DE_VERIFICACION.md`** — la palanca del inglés, el puente con las materias y la
  disciplina de integridad del contenido (con registro de correcciones; p. ej., fecha de la SAS).
- **Reorganización en 5 columnas paralelas** (carpetas `Columna-I` … `Columna-V`), con enlaces
  internos corregidos.
- **Columna IV · Módulo 07 · Honorarios** — cómo cobrar, cotizar y negociar.
- **Nivel IV · Libro 10 · Competencia Económica y Control de Concentraciones** — tratado V3 (38º de
  la Biblioteca): los tres pilares (cárteles, abuso de dominancia, concentraciones) y, sobre todo,
  el **control de concentraciones** como condición de cierre del M&A (umbrales, standstill,
  gun-jumping, remedios, COFECE/IFT). Bajo el Protocolo de Verificación (umbrales y plazos ⚠️).
- **Nivel IV · Libro 9 · Fiscal Corporativo y Planeación Fiscal de Operaciones** — tratado V3
  (37º de la Biblioteca) sobre la dimensión fiscal de las operaciones: lógica del ISR corporativo,
  share vs. asset deal, neutralidad en fusiones/escisiones, elusión vs. evasión y dimensión
  internacional. Construido bajo el Protocolo de Verificación (datos perecederos marcados ⚠️).
- **Columna V · Patrimonio y Libertad Financiera** — completa: documento rector (con advertencia
  de que es formación conceptual, no asesoría) + **6 módulos**: 01 Mentalidad patrimonial · 02
  Finanzas personales del abogado · 03 Construcción de patrimonio · 04 Principios de inversión · 05
  Protección y estructura · 06 El plan realista a la libertad. **Con esta columna se cierra el
  sistema de cinco columnas del Proyecto AJE.**
- **Columna IV · Sistema del Socio** — completa: documento rector + **6 módulos** sobre cómo se
  construye una carrera jurídica de élite: 01 La pirámide del despacho · 02 Gestionar hacia arriba ·
  03 Generación de negocio (rainmaking) · 04 La economía del despacho · 05 Marca personal y
  reputación · 06 Rutas de carrera. Modelo central: las tres monedas (ejecución, confianza,
  generación).
- **Columna III · Laboratorio Profesional** — **completo (2 tramos · 10 ejercicios)**: Tramo 1
  (ciclo de M&A): 01 Memorándum · 02 Cláusula · 03 Term sheet · 04 R&W + disclosure · 05 Due
  diligence · 06 Closing checklist. Tramo 2 (comunicación y soporte): 07 Correo y minuta · 08 Actas,
  asambleas y resoluciones · 09 Opinión legal · 10 Presentación al cliente y al consejo. Los 10
  recorren una misma operación ("Proyecto Caramelo").

### Cambiado
- **`00_MANIFIESTO_EDITORIAL.md`** pasa de ser "la Constitución" a **Anexo de Estándar
  Editorial**, subordinado al Documento Fundacional: regula solo *cómo se escribe* la
  biblioteca (estándar V3).
- **`README.md`** reescrito: presenta el Proyecto AJE, la jerarquía de documentos y las cinco
  columnas con su estado.
- **`AVANCE.md`** ahora abre con el tablero de estado de las cinco columnas.

### Principio destacado de esta versión
- **Integridad Intelectual y Verificación (Principio Supremo):** al construirse con apoyo de IA,
  la obra se prohíbe inventar jurisprudencia, artículos, autores o datos; marca lo verificable y
  prefiere el concepto sólido a la cita decorativa.

---

## [1.0] — 2026 · «La Biblioteca» — *sellada (rama `v1.0`)*

Primera obra completa: la **Biblioteca Jurídica Elias Alejo**, hoy la **Columna I** del sistema.
Congelada e intacta en la rama [`v1.0`](https://github.com/eliasac041129-cloud/bibliotecajuridicaeliasalejo/tree/v1.0).

### Contenido
- **36 tratados** organizados en **5 niveles**:
  - **Nivel I · Fundamentos** — 13 tratados (estándar fundacional de 30 secciones).
  - **Nivel II · Derecho Civil Profundo** — 4 tratados (estándar V3).
  - **Nivel III · Derecho Mercantil** — 7 tratados (estándar V3).
  - **Nivel IV · Corporate Law** — 8 tratados (ampliado al perfil del lector: M&A, due
    diligence, estructuras, documentación SPA/SHA/APA, derecho bancario y financiamiento,
    contratos estratégicos y joint ventures, PE/VC, gobierno corporativo/compliance/ESG).
  - **Nivel V · Maestría** — 4 tratados (negociación, finanzas, valuación, estrategia).
- Documentos de apoyo: Manifiesto Editorial (estándar V3, 43 secciones + transversales),
  Plantilla de Libro, Guía Metodológica y tablero de Avance.

---

> **Cómo leer esta bitácora:** la V1.0 es la foto congelada de la biblioteca; la V2.0 construye
> el sistema completo encima, sin tocar la V1.0. Para volver a la versión sellada, consulta la
> rama `v1.0`.
