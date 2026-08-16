# Expediente de ingesta

### Qué documento contesta qué, campo por campo

> **Cuándo se abre este archivo:** una sola vez, el día que se carguen los once documentos oficiales.
> Después queda como registro de dónde salió cada dato.
>
> **Estado:** los once documentos **no están en el repositorio**. Se verificó con `find` sobre todo el
> workspace: no hay ningún `.pdf` salvo los que genera `tools/build_impreso.py`. Todo lo de abajo está
> en **⛔ FALTA**.

---

## I. Cómo cargarlos

Los nombres declarados son estos. Se guardan tal cual en `PROYECTO-REMONTADA/documentos/`:

```
29-ReglamentoGeneralExamenes_UNAM_210425.pdf
calendario-2027-l.pdf
Comprobante (2).pdf
Expediente de titulacion_v9.pdf
HORARIO 1702.pdf
Lineamientos Internos para la Titulación de Licenciatura (definitivos).pdf
MATERIAS PLAN DE ESTUDIO 2254.pdf
Oficina del Abogado General - UNAM_ Legislacion.pdf
REGLAMENTO EXTRAORDINARIOS.pdf
REGLAS DE OPERACION TITULACION.pdf
SIAE [Panel de Control].pdf
```

Dos advertencias operativas:

**Son PDF de imágenes.** Eso significa que no tienen texto seleccionable y hay que leerlos como
imágenes, página por página. Si alguno resulta ilegible a la resolución en que fue escaneado, se dirá
en lugar de adivinar el contenido. Un número de materia mal leído es peor que un hueco declarado.

**Ninguno se resume "en general".** De cada uno se extraen **campos concretos**, los de abajo. Un
resumen narrativo de un reglamento es inútil para decidir; lo que decide es el dato exacto.

---

## II. El documento que más importa

De los once, hay uno que determina la mitad de las respuestas:

> ### `SIAE [Panel de Control].pdf` + `MATERIAS PLAN DE ESTUDIO 2254.pdf`

El primero dice **dónde estás**; el segundo, **por dónde se puede pasar**. Sin esos dos, no existe
diagnóstico, no existe meta de promedio y no existe ruta de tres semestres — existen adjetivos.

Si solo pudiera cargarse un documento hoy, es el `SIAE`.

---

## III. Campos a extraer, documento por documento

### 1. `SIAE [Panel de Control].pdf` — el historial académico

Es la base de todo el diagnóstico y de toda la aritmética de promedio.

| Campo | Para qué |
|---|---|
| Lista completa de asignaturas **acreditadas**, con clave, nombre, calificación y periodo | Promedio actual y materias ya cerradas |
| Lista completa de asignaturas **no acreditadas** (reprobadas, NP, no inscritas) | El rezago real, con nombre y clave |
| Para cada no acreditada: **cuántas veces** se ha presentado y en qué modalidad (ordinario / extraordinario) | Riesgo reglamentario — ver documento 2 |
| **Créditos** acreditados y créditos totales del plan | Porcentaje de avance, y elegibilidad de servicio social y titulación |
| **Promedio** que reporta el propio sistema | Punto de partida verificado, no calculado por mí |
| **Semestre** en que aparece inscrito y situación (regular / irregular) | Qué puede inscribir el periodo entrante |
| Cualquier **bloqueo o adeudo** que muestre el panel | Un bloqueo administrativo invisible arruina una inscripción |

> ⚠️ Necesito la **calificación numérica de cada materia**, no el promedio global. La calculadora
> [`tools/promedio.py`](./tools/promedio.py) necesita el detalle para poder decir cuánto sube el
> promedio cada decisión. Con el promedio global solo se puede decir "sube un poco".

---

### 2. `MATERIAS PLAN DE ESTUDIO 2254.pdf` — el plan y la seriación

Este documento es el único que puede contestar la palabra que **no aparece ni una vez en las 684,692
palabras del repositorio**: *seriación*.

| Campo | Para qué |
|---|---|
| Todas las asignaturas con **clave, nombre, semestre, créditos** y carácter (obligatoria / optativa) | El mapa completo |
| **Seriación obligatoria**: qué asignatura exige cuál como antecedente | El cuello de botella real. Una materia reprobada que sea antecedente de tres bloquea tres |
| **Seriación indicativa**, si el plan la distingue de la obligatoria | Cambia si algo es imposible o solo inconveniente |
| Total de **créditos** para egresar, y cuántos son optativos | Requisito de titulación y de servicio social |
| Si existen **áreas de especialización o preespecialidad** y en qué semestre se eligen | Aquí se decide si el plan permite empujar hacia corporativo |

> **Por qué esto define la ruta entera.** El orden de recuperación no lo determina la dificultad de la
> materia ni las ganas: lo determina **cuántas asignaturas desbloquea**. Una materia reprobada que sea
> antecedente de tres se recupera primero aunque sea la más difícil y la más aburrida. Sin la tabla de
> seriación, cualquier "ruta de tres semestres" es una lista de deseos ordenada por comodidad.

---

### 3. `REGLAMENTO EXTRAORDINARIOS.pdf` + `29-ReglamentoGeneralExamenes_UNAM_210425.pdf`

El primero es la regla local; el segundo, la general de la UNAM. Cuando difieran, hay que ver cuál
prevalece — y eso lo dice el propio texto, no yo.

| Campo | Para qué |
|---|---|
| **Cuántos extraordinarios** pueden presentarse por periodo | Límite duro de la estrategia. Todo lo demás se calcula sobre esto |
| **Cuántas veces** puede presentarse la misma asignatura, en total | El riesgo terminal: agotar oportunidades |
| Si hay **límite de años** para concluir el plan de estudios | Puede ser el plazo más apremiante de todos y no aparecer en ningún otro documento |
| Requisitos para **inscribir** un extraordinario (fechas, pago, cupo, firma) | Cada uno es un punto de falla |
| Qué pasa con la **calificación** en el historial: si sustituye, si promedia, si queda registro del reprobado | **Determina si conviene extraordinario o repetir el curso.** Es la pregunta de promedio más importante |
| Si existe **derecho a revisión** de examen y en qué plazo | Un plazo que se pierde no se recupera |
| Figuras especiales: **exámenes de regularización**, cursos intersemestrales, recursamiento | Puede haber salidas que no estén en el radar |

> ⚠️ Aquí hay una pregunta que **no debo contestar por intuición** y que cambia toda la estrategia de
> promedio: *¿el 5 reprobado sigue contando en el promedio después de aprobar en extraordinario?* En
> unos planes sí, en otros no. La respuesta está en estos dos documentos y en ningún otro lugar.

---

### 4. `calendario-2027-l.pdf` — las fechas

De aquí sale el calendario maestro completo. Este documento es la razón por la que se perdieron
oportunidades antes.

| Campo | Para qué |
|---|---|
| **Inicio y fin** de cada periodo semestral | Marco de todo |
| Periodos de **inscripción y de altas/bajas**, con día y hora | Las ventanas más cortas y más caras de perder |
| **Periodos de exámenes extraordinarios** (todos los del año, no solo el próximo) | El núcleo del sistema antifallas |
| Fechas de **exámenes finales** ordinarios | Planeación de bloques de estudio |
| **Días inhábiles**, vacaciones y suspensión de labores | No estudiar contra un calendario equivocado |
| Fechas de **entrega de actas** por los profesores | Cuándo reclamar una calificación mal asentada |
| Si el calendario es de **2027** y estamos en agosto de 2026: qué periodo cubre exactamente | 🔎 El nombre del archivo sugiere el ciclo 2027, que en la UNAM suele arrancar a mediados de 2026. **Hay que confirmarlo, no suponerlo** |

> **Todas estas fechas se transcriben con día, mes, año y hora** a la tabla del
> [sistema antifallas](./04_SISTEMA_ANTIFALLAS.md). Ninguna se guarda solo en este documento, y
> ninguna se guarda solo en la cabeza.

---

### 5. Los cuatro documentos de titulación

`Lineamientos Internos para la Titulación de Licenciatura (definitivos).pdf`
`REGLAS DE OPERACION TITULACION.pdf`
`Expediente de titulacion_v9.pdf`
`Oficina del Abogado General - UNAM_ Legislacion.pdf`

| Campo | Para qué |
|---|---|
| **Todas** las modalidades de titulación que ofrece la FES Aragón, no solo tesis | Hay que ver el menú completo antes de casarse con una opción |
| Requisitos **exactos** de la tesis: extensión, formato, asesor, registro de tema, revisores, réplica | El plan de tesis depende de esto |
| Si el **promedio** habilita alguna modalidad (titulación por promedio alto, mención honorífica) | 🔎 Probablemente ya no aplique dado el rezago, pero **hay que verificarlo antes de descartarlo** |
| **Cuándo** puede iniciarse el trámite: ¿al 100% de créditos, antes, después del servicio social? | Determina si la tesis puede escribirse en paralelo o solo al final |
| Quién puede ser **asesor**, cómo se solicita, cuántos asesorados acepta | El primer paso concreto de la tesis |
| **Requisito de idioma**: qué nivel, qué examen, qué constancia, quién lo emite, vigencia | El repositorio no tiene ni una línea sobre esto |
| **Servicio social**: cuántos créditos o porcentaje de avance se exige para iniciarlo, duración, horas, programas válidos, si es requisito previo a la titulación | 0 ocurrencias reales en todo el repositorio |
| Lista completa de **documentos del expediente** y en qué orden se piden | Un documento faltante detiene el trámite meses |
| **Plazos**: cuánto tiempo hay tras egresar para titularse | Puede haber un reloj corriendo sin saberlo |
| Costos de cada trámite | Entra al plan económico |

---

### 6. `HORARIO 1702.pdf` — el horario del grupo

| Campo | Para qué |
|---|---|
| Asignaturas del periodo, con **día y hora de cada sesión** | El horario real, no el promedio |
| **Nombre del profesor** por asignatura | Determina exigencia y forma de evaluación |
| **Aula** y si hay sesiones en línea | Afecta el traslado |
| Si hay **huecos** entre clases y de cuánto | 🔎 Un hueco de 2 h en la facultad vale más que 2 h en casa a las 21:00 |

> El §VII del prompt describe la jornada como 7:00 a 13:00 de lunes a viernes. **Eso hay que
> confirmarlo contra este documento**, porque si un solo día termina a las 11:00 o empieza a las 9:00,
> el horario semanal cambia y aparecen horas que hoy se consideran ocupadas.

---

### 7. `Comprobante (2).pdf`

🔎 El nombre no permite saber qué comprobante es —inscripción, pago, trámite, servicio social—. Se
lee y se clasifica antes de asignarle función. No se supone.

---

## IV. Lo que se produce en cuanto estén cargados

En una sola sesión, y en este orden, porque cada paso depende del anterior:

1. **Diagnóstico académico verificado** — materias pendientes con clave y nombre, veces presentadas,
   oportunidades restantes. Marcado 📄 DOC línea por línea.
2. **Promedio actual real** y, con `tools/promedio.py`, el **promedio máximo alcanzable** en tres
   escenarios: conservador, probable y de techo. Con números, no con adjetivos, y sin prometer un
   promedio que la aritmética no permita.
3. **Mapa de seriación** — grafo de qué desbloquea qué, y de ahí el orden obligatorio de recuperación.
4. **Estrategia de extraordinarios** — cuántos por periodo, cuáles, en qué orden, cuáles conviene
   posponer y cuáles son riesgo terminal por oportunidades agotadas.
5. **Calendario maestro fechado** — todas las fechas de los próximos 18 meses en una sola tabla, con
   sus alarmas.
6. **Ruta de tres semestres** — séptimo, octavo y noveno, con carga por periodo y decisión sobre
   trabajo.
7. **Cronograma de tesis** anclado a las fechas reales de titulación.
8. **Checklist de servicio social e inglés** con sus plazos.

Hasta entonces, esas ocho cosas viven en
[`PENDIENTE-DE-DOCUMENTOS.md`](./PENDIENTE-DE-DOCUMENTOS.md), marcadas **⛔ FALTA**.

---

## V. Registro de ingesta

Se llena al cargar cada documento. Sirve para saber qué se leyó, cuándo, y qué quedó ilegible.

| Documento | Cargado | Leído | Campos extraídos | Ilegible / dudoso |
|---|---|---|---|---|
| `SIAE [Panel de Control].pdf` | ⛔ | — | — | — |
| `MATERIAS PLAN DE ESTUDIO 2254.pdf` | ⛔ | — | — | — |
| `REGLAMENTO EXTRAORDINARIOS.pdf` | ⛔ | — | — | — |
| `29-ReglamentoGeneralExamenes_UNAM_210425.pdf` | ⛔ | — | — | — |
| `calendario-2027-l.pdf` | ⛔ | — | — | — |
| `Lineamientos Internos para la Titulación…pdf` | ⛔ | — | — | — |
| `REGLAS DE OPERACION TITULACION.pdf` | ⛔ | — | — | — |
| `Expediente de titulacion_v9.pdf` | ⛔ | — | — | — |
| `Oficina del Abogado General…pdf` | ⛔ | — | — | — |
| `HORARIO 1702.pdf` | ⛔ | — | — | — |
| `Comprobante (2).pdf` | ⛔ | — | — | — |

---

*Rige el Principio 1 del [Documento Fundacional](../00_DOCUMENTO_FUNDACIONAL_AJE.md): nunca inventar.
Un requisito de titulación inventado no es un error editorial: es un semestre perdido.*
