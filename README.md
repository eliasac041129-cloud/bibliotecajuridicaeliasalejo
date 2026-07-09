# Proyecto AJE · Arquitecto Jurídico Empresarial

> **De una biblioteca a un sistema.** Lo que empezó como la *Biblioteca Jurídica Elias Alejo*
> es hoy, en su **versión 2.0**, un **sistema integral de formación** —jurídica, empresarial,
> profesional y patrimonial— diseñado para transformar la forma de pensar, analizar, decidir y
> actuar de su lector, hasta convertirlo en un **asesor indispensable** para quienes toman las
> decisiones empresariales más importantes.

> **Estado: `v2.2` sellada; `v3.0` en curso (2026-07).** **52 tratados** + Laboratorio (11 ejercicios) +
> Sistema de Repaso + **Glosario Bilingüe**. La v3.0 añade la **capa de enriquecimiento** (glosario
> español⇄inglés, mazo Anki y banco de preguntas ampliados). **Fechado global:** salvo indicación en
> contrario, el contenido está a **2026-07**; **verifica toda norma, tasa, monto y artículo contra su texto
> vigente** (DOF/SAT/SJF). Es un **sistema conceptual y de estudio**: los **números de artículo** están
> marcados ⚠️ y su verificación *verbatim* (para el sello "Referencia Verificada plena") sigue pendiente
> —ver [Control de Calidad](./CONTROL-DE-CALIDAD.md) y el CHANGELOG—.

---

## 📜 Jerarquía de documentos (léelos en este orden)

| Orden | Documento | Qué es |
|-------|-----------|--------|
| 1 | [**00 · Documento Fundacional AJE**](./00_DOCUMENTO_FUNDACIONAL_AJE.md) | **Rector supremo.** Misión, visión, las 5 columnas, los 6 principios rectores. Se relee antes de cada libro y decisión. |
| 2 | [**00 · Manifiesto Editorial**](./00_MANIFIESTO_EDITORIAL.md) | **Anexo de Estándar Editorial.** Cómo se escribe cada libro: estándar V3 (43 secciones), derecho comparado, control de calidad. Subordinado al Fundacional. |
| 3 | [**01 · Hoja de Ruta AJE**](./Columna-II-Hoja-de-Ruta/01_HOJA_DE_RUTA_AJE.md) | **Columna II.** Estrategia profesional: qué hacer, cuándo y por qué — de la universidad a socio o fundador. |
| 4 | [**02 · El Sistema Diario**](./Columna-II-Hoja-de-Ruta/02_PLAN_OPERATIVO_DIARIO_AJE.md) | **Plan operativo.** Qué haces hoy, a qué hora y por cuánto tiempo. Convierte todo el repo en una rutina diaria. |
| 5 | [**03 · Plan de Inglés Jurídico**](./Columna-II-Hoja-de-Ruta/03_PLAN_DE_INGLES_JURIDICO_AJE.md) | **La llave no negociable.** Materializa el Principio 6 (Bilingüismo): rutina, recursos e inglés legal. |
| 6 | [**04 · La Tesis Estratégica**](./Columna-II-Hoja-de-Ruta/04_LA_TESIS_ESTRATEGICA.md) | Convierte la tesis (R&W en el SPA) en activo de carrera: pregunta, hipótesis y esquema. |
| 7 | [Índice Maestro](./INDICE_MAESTRO.md) · [Guía Metodológica](./GUIA-METODOLOGICA.md) · [Mapa Biblioteca↔Materias](./MAPA_BIBLIOTECA-A-MATERIAS.md) · [Protocolo de Verificación](./PROTOCOLO_DE_VERIFICACION.md) · [Control de Calidad](./CONTROL-DE-CALIDAD.md) · [Glosario Bilingüe](./GLOSARIO-BILINGUE.md) · [Avance](./AVANCE.md) · [Changelog](./CHANGELOG.md) | Navegación, método, puente con materias, integridad, QA, bilingüismo, estado y bitácora. |

---

## El sistema: cinco columnas

El Proyecto AJE se compone de cinco sistemas inseparables. **No se construyen todos a la vez**:
se levantan **en secuencia**, según lo que el lector necesita en cada etapa.

| Columna | Nombre | Pregunta que responde | Estado |
|---------|--------|------------------------|--------|
| **I** | **Biblioteca Jurídica** | ¿Qué debo aprender? | ✅ Completa (5 niveles + Ramas Esenciales · 52 tratados) |
| **II** | **Hoja de Ruta** | ¿Qué hacer, cuándo y por qué? | ✅ Completa |
| **III** | **Laboratorio Profesional** | ¿Cómo trabaja de verdad un abogado corporativo? | ✅ Completa (3 tramos · 11 ejercicios) |
| **IV** | **Sistema del Socio** | ¿Cómo se construye una carrera jurídica extraordinaria? | ✅ Completa (6 módulos) |
| **V** | **Patrimonio y Libertad Financiera** | ¿Cómo administrar la riqueza que genera la carrera? | ✅ Completa (6 módulos) |

> **La secuencia, en una frase:** primero **saber** (I) y **saber qué hacer** (II); luego **saber
> hacer** (III); después **saber dirigir la carrera** (IV) y **saber administrar la riqueza** (V).
> Con las cinco construidas, el sistema del Proyecto AJE está **completo**: lo único que queda es
> ejecutarlo un día a la vez (ver [El Sistema Diario](./Columna-II-Hoja-de-Ruta/02_PLAN_OPERATIVO_DIARIO_AJE.md)).

### Estructura del repositorio (las 5 columnas como carpetas paralelas)

```
bibliotecajuridicaeliasalejo/
│
├── README.md                          ← estás aquí
├── 00_DOCUMENTO_FUNDACIONAL_AJE.md    ← rector supremo
├── 00_MANIFIESTO_EDITORIAL.md         ← anexo de estándar editorial
├── INDICE_MAESTRO.md                  ← mapa navegable de todo
│
├── Columna-I-Biblioteca/              ← QUÉ aprender (52 tratados: 38 en Niveles I-V + 14 Ramas Esenciales)
│   ├── Nivel-I-Fundamentos/
│   ├── Nivel-II-Derecho-Civil-Profundo/
│   ├── Nivel-III-Derecho-Mercantil/
│   ├── Nivel-IV-Corporate-Law/
│   └── Nivel-V-Maestria/
│
├── Columna-II-Hoja-de-Ruta/           ← QUÉ hacer y cuándo
│   ├── 01_HOJA_DE_RUTA_AJE.md
│   ├── 02_PLAN_OPERATIVO_DIARIO_AJE.md   (el Sistema Diario)
│   └── 03_PLAN_DE_INGLES_JURIDICO_AJE.md
│
├── Columna-III-Laboratorio/           ← CÓMO se trabaja (entregables)
├── Columna-IV-Sistema-del-Socio/      ← CÓMO se construye la carrera
├── Columna-V-Patrimonio/              ← CÓMO se administra la riqueza
│
└── (apoyo) GUIA-METODOLOGICA · MAPA_BIBLIOTECA-A-MATERIAS ·
            PROTOCOLO_DE_VERIFICACION · PLANTILLA-LIBRO · AVANCE · CHANGELOG
```

> Los documentos **00** (constitución) y los de apoyo viven en la raíz porque son **transversales**
> a todo el sistema; las **cinco columnas** son carpetas paralelas, cada una con su documento
> rector `00_...` interno.

---

## Columna I · La Biblioteca Jurídica (cinco niveles)

El corazón de conocimiento del proyecto. **No prepara estudiantes para aprobar: forma abogados.**
No enseña artículos, enseña **pensamiento jurídico**; no enseña memoria, enseña **criterio**.

| Nivel | Nombre | Objetivo formativo |
|------|--------|--------------------|
| **I** | [Fundamentos](./Columna-I-Biblioteca/Nivel-I-Fundamentos/) | Construir la **arquitectura mental** del Derecho: por qué existen las instituciones. |
| **II** | [Derecho Civil Profundo](./Columna-I-Biblioteca/Nivel-II-Derecho-Civil-Profundo/) | Dominar el derecho privado común: obligaciones, contratos, responsabilidad, garantías. |
| **III** | [Derecho Mercantil](./Columna-I-Biblioteca/Nivel-III-Derecho-Mercantil/) | Convertirse en especialista: sociedades, títulos de crédito, mercado de valores, concursos. |
| **IV** | [Corporate Law](./Columna-I-Biblioteca/Nivel-IV-Corporate-Law/) | El verdadero objetivo: M&A, due diligence, financiamiento, contratos estratégicos, PE/VC, gobierno corporativo. |
| **V** | [Maestría](./Columna-I-Biblioteca/Nivel-V-Maestria/) | Pensar como socio de un despacho internacional: finanzas, valuación, negociación, estrategia. |

> La progresión es **acumulativa**: cada nivel expande, conecta y profundiza lo anterior.
> No se repiten conceptos; se elevan.

---

## Los seis principios rectores (resumen)

1. **(SUPREMO) Integridad Intelectual y Verificación** — nunca inventar; marcar lo que debe
   verificarse contra el texto vigente; sustancia sobre apariencia.
2. **Integridad Ética** — la reputación es el mayor activo; crear valor, no engañar.
3. **Realismo y Ejecución** — la ambición atada a acciones concretas y de hoy; bloques pequeños.
4. **Valor (no dinero)** — el dinero es consecuencia del valor profesional creado.
5. **Conexión** — nada se estudia aislado; todo es un único sistema intelectual.
6. **Bilingüismo** — la élite del Derecho corporativo opera en inglés; el inglés es la llave.

---

## Estructura de cada libro (Estándar Editorial V3)

Los libros nuevos siguen el **Estándar V3: 43 secciones** + **4 secciones transversales
obligatorias** (¿Por qué importa para un abogado corporativo? · Cómo piensa un socio de un
despacho internacional · Errores que cuestan millones · Nivel de importancia profesional).
El detalle está en [PLANTILLA-LIBRO.md](./PLANTILLA-LIBRO.md).

> Los 13 tratados del **Nivel I** se construyeron sobre el estándar fundacional de 30 secciones
> (plenamente válido); los nuevos volúmenes adoptan el V3, y el Nivel I se enriquecerá hacia el
> V3 progresivamente.

---

## Cómo se construye (el medio importa)

- **Control de versiones (git/GitHub).** La **V1.0 está sellada en la rama `v1.0`** (foto
  congelada de la biblioteca completa); el desarrollo de la V2.0 continúa en `main` sin dañarla.
- **Construcción incremental en bloques pequeños**, con *commit* y *push* tras cada bloque.
- **Navegabilidad y trazabilidad:** índice maestro, prerrequisitos y conexiones declaradas.
- **Honestidad del medio:** se construye con apoyo de IA, bajo el Principio Supremo de
  Integridad Intelectual — la herramienta acelera, no sustituye la verificación ni el criterio.

---

## Estado de avance

Consulta [AVANCE.md](./AVANCE.md) (tablero de control de la biblioteca y de las columnas) y
[CHANGELOG.md](./CHANGELOG.md) (bitácora de versiones V1 → V2).

---

*Equipo editorial conceptual: cátedra de Derecho (UNAM, ITAM), práctica de M&A de despachos
internacionales y mexicanos líderes, academia jurídica comparada, edición jurídica profesional
y diseño instruccional de aprendizaje acelerado.*
