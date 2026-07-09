# Protocolo de Verificación — Integridad del Contenido

> **Por qué existe este documento.** El [Principio Supremo](./00_DOCUMENTO_FUNDACIONAL_AJE.md)
> del proyecto es la **Integridad Intelectual y Verificación**: nunca presentar como cierto un
> dato (artículo, fecha, tesis, autor, cifra) que no se ha confirmado. Como la Biblioteca se
> construyó con apoyo de IA, **este riesgo es real y demostrado**: en una sola revisión de muestra
> se encontró un error fáctico (la fecha de creación de la S.A.S. — ver registro abajo). Este
> protocolo convierte ese principio en una **disciplina concreta y auditable**.

> **Regla de oro para el lector (léela como advertencia permanente).** Mientras un dato concreto no
> esté marcado como ✅ verificado en este protocolo, **trata todo número de artículo, fecha, tesis
> o cifra de la Biblioteca como "por confirmar"** contra el texto legal vigente y fuentes
> oficiales. El valor de los tratados está en el **razonamiento y los sistemas conceptuales**, no
> en sus citas exactas, que pueden contener errores o haber quedado desactualizadas.

---

## I. Qué debe verificarse (los "datos duros")

Estos elementos son los que **nunca** deben afirmarse de memoria; siempre se verifican o se marcan:

| Tipo de dato | Riesgo | Fuente para verificar |
|--------------|--------|------------------------|
| **Número de artículo** de una ley | Alto: cambian con reformas; fáciles de confundir | Texto vigente de la ley (DOF / sitios oficiales) |
| **Fechas** (de leyes, reformas, hechos históricos) | Alto: error demostrado (SAS) | Fuente oficial / histórica confiable |
| **Tesis y jurisprudencia** (rubro, número, época) | Muy alto: inventarlas destruye credibilidad | Semanario Judicial de la Federación (SJF) |
| **Cifras y montos** (tarifas, topes legales) | Alto: cambian cada año | Normativa y publicaciones oficiales vigentes |
| **Nombres** (autores, casos, instituciones) | Medio | Fuentes académicas confiables |
| **Vigencia** de una norma | Alto: puede estar derogada/reformada | Texto vigente |

---

## II. El sistema de marcado (semáforo de confianza)

Todo dato duro debería llevar, idealmente, una de estas marcas:

- **✅ Verificado** — confirmado contra fuente oficial (idealmente con la fuente y la fecha).
- **⚠️ Por verificar** — afirmado con base en conocimiento general; **debe confirmarse antes de
  usarse en un contexto real**. Es la marca por defecto cuando hay duda.
- **❌ Corregido** — se detectó un error y se corrigió (queda registrado en la sección V).

> **La conducta correcta cuando hay duda:** no inventar y no afirmar con falsa seguridad. Escribir
> el concepto y añadir *"(verificar el número/fecha contra el texto vigente)"*. Es exactamente lo
> que se modeló en el Laboratorio (Ejercicio 01, el memo) y en la corrección de la SAS. **Preferir
> el concepto sólido a la cita decorativa no confirmada.**

---

## III. El sello de "fechado" (porque el Derecho cambia)

El Derecho se reforma. Un dato correcto hoy puede ser falso en dos años. Por eso:

> **Recomendación:** cada tratado debería indicar **"contenido conceptual; verificar normas contra
> su texto vigente a la fecha de consulta"**. El proyecto no garantiza que las normas citadas estén
> actualizadas a una fecha posterior a su redacción. El lector siempre coteja contra la versión
> vigente.

---

## IV. La regla para todo contenido NUEVO

De aquí en adelante, **ningún tratado o módulo nuevo** debe afirmar un dato duro sin verificarlo o
sin marcarlo ⚠️. Antes de dar por terminado un texto, se pasa esta checklist mínima:

- [ ] ¿Cada número de artículo está verificado o marcado ⚠️?
- [ ] ¿Cada fecha está verificada o marcada ⚠️?
- [ ] ¿Hay alguna tesis/jurisprudencia citada? Si sí, ¿está confirmada en el SJF o marcada?
- [ ] ¿Las cifras/montos llevan nota de "verificar vigente"?
- [ ] ¿El texto prefiere el concepto sólido sobre la cita no confirmada?


---

## V. Registro de correcciones (auditoría)

Cada error detectado y corregido queda aquí, con fecha y fuente. Es la prueba viva de que el
Principio Supremo se aplica, no solo se predica.

| Fecha | Tratado | Error | Corrección | Fuente |
|-------|---------|-------|------------|--------|
| 2026-06 | III-02 Sociedades (LGSM) | Decía que la **S.A.S.** se creó en "2014" | Corregido a **2016** (reforma a la LGSM publicada en el DOF el 14-mar-2016, en vigor 6 meses después) | Publicaciones jurídicas sobre la reforma de 2016 |
| 2026-07 | IV-10 Competencia; I-03 Teoría del Estado; y menciones dispersas en IV-01, IV-02, IV-03, III-04 | Describían a la **COFECE** y al **IFT** como autoridades **vigentes** | Añadido recuadro de **Actualización Normativa Crítica**: la reforma de **simplificación orgánica (2024)** y la reforma a la **LFCE (en vigor 17-jul-2025)** **extinguieron COFECE e IFT** y crearon la **Comisión Nacional Antimonopolio (CNA)** como autoridad única. Donde el texto diga "COFECE", léase "la autoridad de competencia (hoy la CNA)" | Análisis de firmas (ABA, Hogan Lovells, Chambers, Norton Rose Fulbright), 2025; verificar contra el DOF |

> *(Cuando se detecten y corrijan más errores, se agregan renglones aquí.)*

---

## VI. Backlog de verificación (priorizado por riesgo)

No todos los tratados tienen el mismo riesgo. Los que **más datos duros** contienen (artículos,
fechas, montos) son los que más urge auditar. Orden sugerido de revisión sistemática:

| Prioridad | Tratados | Por qué | Estado |
|-----------|----------|---------|--------|
| 🔴 Alta | Nivel III (Mercantil): Sociedades, Títulos de Crédito, Mercado de Valores, Concurso | Densos en artículos y leyes específicas (LGSM, LGTOC, LMV) | ⬜ Pendiente (1 error ya corregido) |
| 🔴 Alta | Nivel IV (Corporate): los que citan leyes mexicanas y montos | Cifras y normas que cambian | ⬜ Pendiente |
| 🔴 Alta | **Ramas Esenciales (01–11)**: Fiscal, Constitucional/Amparo, Administrativo, Procesal, Laboral, Penal, PI, DIP/Arbitraje, Datos, Ambiental, Ética | Muy densos en artículos, tasas, plazos y montos de materias que **se reforman cada año** (CFF, LISR, LIVA, Ley de Amparo, LFT, CPF, LFPPI, LFPDPPP, LGEEPA, etc.). Redactados marcando ⚠️ todo dato duro y con sello de fecha, pero **la verificación puntual está pendiente** | ⬜ Pendiente (redactados con ⚠️ y sello 2026-07) |
| 🟠 Media | Nivel II (Civil profundo) | Artículos del Código Civil | ⬜ Pendiente |
| 🟠 Media | Nivel I: Personas, Bienes, Obligaciones, Contratos | Artículos del Código Civil | ⬜ Pendiente |
| 🟡 Baja | Nivel I conceptuales (Lógica, Argumentación, Metodología, Teoría del Estado) | Poco dato duro; sobre todo conceptos | ⬜ Pendiente |
| 🟢 Mínima | Columnas III-V (Laboratorio, Socio, Patrimonio) | Conceptuales/de método; ya marcan ⚠️ y "no asesoría" | ✅ Diseñadas con marcas |

> **Algunos datos de referencia ya confirmados** (✅), para sembrar el registro:
> - La **LGSM** (Ley General de Sociedades Mercantiles) fue publicada en **1934**. ✅
> - La **S.A.P.I.** se introdujo con la **Ley del Mercado de Valores de 2005** (en vigor 2006). ✅
>
> *(Aun así, verifica los artículos específicos contra el texto vigente: las leyes se reforman.)*

---

## VII. Cómo se usa este protocolo

- **Como lector:** antes de citar un dato de la Biblioteca en un examen, trabajo o documento real,
  confírmalo. Si el tratado da un artículo o fecha, **ve a la fuente oficial** y verifícalo. Esto
  además es excelente práctica jurídica: el abogado serio **siempre** va a la fuente.
- **Como autor (tú o quien continúe el proyecto):** aplica la checklist de la sección IV a todo
  contenido nuevo, y registra aquí cualquier corrección.
- **Como auditor:** toma un tratado del backlog (sección VI), verifica sus datos duros uno por uno,
  marca ✅/⚠️/❌ y registra las correcciones en la sección V.

> **La idea que debe quedarte:** el mayor riesgo de una biblioteca construida con IA no es que le
> falte contenido — es que un dato falso se lea como verdadero. Este protocolo es el escudo contra
> eso. Y te entrena en el reflejo más importante del abogado de élite: **nunca afirmes lo que no
> has verificado.** Una sola cita falsa puede costar un caso, un cliente y tu reputación.

---

*Protocolo de Verificación · Proyecto AJE. Materializa el Principio Supremo del Documento
Fundacional. Documento vivo: actualízalo con cada corrección y cada verificación.*
