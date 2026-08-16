# Pendiente de documentos

### Registro vivo de lo que no puede construirse todavía

> **Qué es esto.** La lista honesta de lo que el prompt maestro pide y **no está escrito**, con la razón
> exacta. Cada línea dice qué documento la desbloquea. Se actualiza cada vez que entre un documento.
>
> Esto no es una excusa. Es la aplicación del
> [Principio 1](../00_DOCUMENTO_FUNDACIONAL_AJE.md): *"Si no se está seguro de un dato, se dice
> explícitamente en lugar de inventarlo."* Un plan de tres semestres construido sobre una seriación
> supuesta se ve idéntico a uno real hasta el día de la inscripción.

**Fecha de este registro:** 16 de agosto de 2026. **Documentos cargados: 11 de 11.** ✅

> ### Corrección: los documentos SÍ estaban
>
> Estaban en la rama `main` del repositorio. Yo busqué en el árbol de trabajo de `RAMA-DEFINITIVA` y
> concluí que no existían. **Fue un fallo mío, y del tipo exacto que este proyecto documenta:** consultar
> una fuente en lugar de la autoritativa y decidir sobre el resultado. Es la Regla 1 del
> [sistema antifallas](./04_SISTEMA_ANTIFALLAS.md), incumplida en el mismo commit que la propuso.
>
> Los once están leídos, con texto extraíble y sin necesidad de OCR. El diagnóstico real está en
> [`11_DIAGNOSTICO_ACADEMICO.md`](./11_DIAGNOSTICO_ACADEMICO.md) y las fechas en
> [`12_CALENDARIO_MAESTRO.md`](./12_CALENDARIO_MAESTRO.md).

---

## I. Lo que está en ⛔ FALTA

| # | Lo que pide el prompt | Por qué no puede escribirse | Lo desbloquea |
|---|---|---|---|
| 1 | **Diagnóstico académico** (§XIV.1, §XXVIII.1): materias pendientes, cuántas, cuáles | No hay historial. No sé cuántas materias debe ni cuáles | `SIAE [Panel de Control].pdf` |
| 2 | **Objetivo matemático de promedio** (§XIV.4, §XXVIII.2) | No hay calificaciones. Sin ellas, cualquier meta es un número inventado — y el prompt lo prohíbe expresamente: *"NO me prometas un promedio que matemáticamente sea imposible"* | `SIAE` + reglamentos de exámenes |
| 3 | **Mapa de seriación** (§XIV.1, §XXVIII.3) | La palabra *seriación* aparece **0 veces** en el repositorio. No conozco los antecedentes obligatorios del plan 2254 | `MATERIAS PLAN DE ESTUDIO 2254.pdf` |
| 4 | **Estrategia de extraordinarios** (§XIV.3): cuántos, cuáles, en qué orden | No sé el límite por periodo ni las oportunidades ya agotadas. Recomendar un número sería la falla A del sistema antifallas, cometida por escrito | `REGLAMENTO EXTRAORDINARIOS.pdf` + `29-Reglamento…` + `SIAE` |
| 5 | **Ruta de tres semestres** (§XXVI, §XXVIII.4) | Depende de 1, 3 y 4. La estructura está lista; le faltan los datos | Los tres anteriores |
| 6 | **Calendario maestro con fechas** (§XV) | Cero fechas reales disponibles | `calendario-2027-l.pdf` |
| 7 | **Requisitos de titulación** (§XVI) | El repositorio delega esto al lector desde hace dos versiones. Sigue delegado | Los cuatro documentos de titulación |
| 8 | **Servicio social** (§XVII) | **0 ocurrencias** en sentido académico en 684,692 palabras. No sé cuándo puede iniciarse ni qué exige | `Lineamientos` + `REGLAS DE OPERACION` |
| 9 | **Requisito de inglés para titularse** (§XVIII) | El plan de inglés existe, pero **ninguna línea** del repositorio menciona el requisito institucional | Documentos de titulación |
| 10 | **Cronograma fechado de tesis** (§XVI) | Los 7 capítulos ya existen. Las fechas dependen de los plazos de titulación | Documentos de titulación + calendario |
| 11 | **Horario confirmado** | El de [`HOY.md`](./HOY.md) se construyó sobre la jornada declarada en el §VII. Si algún día termina antes, aparecen horas nuevas | `HORARIO 1702.pdf` |

---

## II. Lo que sí está construido

Porque su materia prima ya estaba disponible: la jornada declarada en el §VII, el contenido del
repositorio y las conductas descritas en los §V, §VI y §XXIII.

| Documento | Qué resuelve |
|---|---|
| [`00_RECTOR.md`](./00_RECTOR.md) | Qué es la carpeta, la regla anti-procrastinación, qué no duplica |
| [`02_EXPEDIENTE_DE_INGESTA.md`](./02_EXPEDIENTE_DE_INGESTA.md) | Los campos exactos a extraer de cada PDF |
| [`04_SISTEMA_ANTIFALLAS.md`](./04_SISTEMA_ANTIFALLAS.md) | §XV completo. **No dependía de ningún documento** |
| [`HOY.md`](./HOY.md) | §XXVIII.6. Con la aritmética real de sueño, traslado y estudio |
| [`03_DIAGNOSTICO_DE_EJECUCION.md`](./03_DIAGNOSTICO_DE_EJECUCION.md) | §V, §VI, §XXI, §XXV |
| [`05_SISTEMA_SEMANAL_Y_DIARIO.md`](./05_SISTEMA_SEMANAL_Y_DIARIO.md) | §VII, §IX, §X, §XI, §XII, §XXVIII.5 |
| [`06_RUTA_DE_LA_BIBLIOTECA.md`](./06_RUTA_DE_LA_BIBLIOTECA.md) | §IV, §XX |
| [`07_PLAN_DE_TESIS.md`](./07_PLAN_DE_TESIS.md) | §III, §XVI — la parte que no depende de plazos |
| [`08_FORMACION_DEL_HOMBRE.md`](./08_FORMACION_DEL_HOMBRE.md) | §XXIII, §XI, §XII |
| [`09_PLAN_ECONOMICO.md`](./09_PLAN_ECONOMICO.md) | §VIII, §XIII, §XXIV, §XXVII |
| [`10_TABLERO_SEMANAL.md`](./10_TABLERO_SEMANAL.md) | §XXVIII.12 |
| [`tools/promedio.py`](./tools/promedio.py) | La maquinaria de §XIV.4, lista y probada, esperando datos |

**Aproximadamente la mitad del encargo está entregada.** Es, además, la mitad que no depende de que
llegue nada: el sistema antifallas y el horario podrían empezar a usarse mañana.

---

## III. Lo que hay que hacer, en orden

1. **Cargar los once PDF** en `PROYECTO-REMONTADA/documentos/`. Si no se pueden todos, el `SIAE` y el
   plan `2254` primero: desbloquean 5 de las 11 líneas.
2. Extraer los campos del [expediente de ingesta](./02_EXPEDIENTE_DE_INGESTA.md), marcando cada dato
   📄 DOC con archivo y página.
3. Correr [`tools/promedio.py`](./tools/promedio.py) con las calificaciones reales.
4. Llenar el calendario maestro y capturar las alarmas. **Cuarenta minutos, una sola vez.**
5. Recién entonces, escribir la ruta de tres semestres.

> **Y una advertencia sobre el orden.** El paso 4 —capturar nueve fechas con sus alarmas— es el de
> mayor rendimiento de toda la lista y el más barato. Si por cualquier razón el proyecto se detiene
> otra vez, que sea después del paso 4. Cuarenta minutos de captura valen más, hoy, que las 684,692
> palabras de biblioteca ya escritas.

---

*Se actualiza con cada documento que entre. Cuando esta tabla quede vacía, este archivo se borra.*
