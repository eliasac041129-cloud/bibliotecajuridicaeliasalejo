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
| 2026-07 | Ramas Esenciales · 01 Fiscal | Datos duros marcados ⚠️ sin cotejar | **Primera pasada de verificación (✅):** ISR PM **30%**, IVA **16%** y **0%**, régimen de dividendos (factor **1.4286**), clasificación de contribuciones (**art. 2 CFF**), facultades de comprobación (**art. 42 CFF**) y EFOS/EDOS (**art. 69-B CFF**). Añadido *Registro de verificación* en el tratado; resto permanece ⚠️ | **SAT** (Tasas y tarifas del ISR; Concepto de IVA; fichas 156/157 del 69-B), 2026-07 |
| 2026-07 | Ramas Esenciales · 05 Laboral | Fecha de "vacaciones dignas" imprecisa (⚠️) | **Verificado ✅:** reforma publicada en el DOF **27-dic-2022**, en vigor **1-ene-2023**; mínimo del primer año de **6 a 12 días** (arts. 76 y 78 LFT) | Norton Rose, JD Supra, Lexology, Forvis Mazars, 2022-2023 |
| 2026-07 | Ramas Esenciales · 04 Procesal | Fecha del CNPCF marcada ⚠️ | **Verificado ✅:** **CNPCF** publicado en el DOF el **7-jun-2023** (vigor al día siguiente); entrada en vigor **escalonada por entidad, tope 1-abr-2027**; abroga los códigos locales y el CFPC | Fuentes jurídicas (Eco Diario/DOF, JD Supra/Lexology), 2023 |
| 2026-07 | Ramas Esenciales · 07 Propiedad Intelectual | Decía "LFPPI en vigor 2020" sin precisar y **sin** mención de la reforma 2026 | **Verificado ✅:** LFPPI publicada **1-jul-2020**, en vigor **5-nov-2020** (abrogó la LPI de 1991). **❗Hallazgo:** reforma **integral** a la LFPPI publicada en el DOF en **abril de 2026** (reglamento en vigor mediados de 2026) → añadida alerta de actualización en el tratado | Lexology, Holland & Knight, Garrigues (2020); **Creel, NatLaw Review (2026)** |
| 2026-07 | Ramas Esenciales · 02 Constitucional/Amparo | Fechas marcadas ⚠️ | **Verificado ✅:** **Nueva Ley de Amparo en vigor 3-abr-2013**; **reforma judicial publicada en el DOF 15-sep-2024** (elección por voto popular; SCJN de 11 a 9 ministros). Añadidas fechas y detalle al tratado | SSRN (A. Herrera); Hogan Lovells, Norton Rose, DLA Piper, 2024 |
| 2026-07 | Ramas Esenciales · 06 Penal | Fechas del sistema acusatorio/CNPP marcadas ⚠️ | **Verificado ✅:** reforma constitucional **18-jun-2008**, **plena vigencia 18-jun-2016**; **CNPP publicado en el DOF el 5-mar-2014**. Añadidas fechas al tratado | USAID, Americas Quarterly, IBJ (2008/2016); Refworld (texto oficial CNPP) |
| 2026-07 | Ramas Esenciales · 08 DIP/Arbitraje | Fechas de convenciones marcadas ⚠️ | **Verificado ✅:** **Convención de Nueva York** hecha el **10-jun-1958**, ratificada por México en **1971** (DOF 22-jun-1971); **Ley Modelo UNCITRAL de 1985** incorporada al Código de Comercio en **1993**. Añadidas fechas al tratado | UNCITRAL/ONU; Global Arbitration Review; Global Legal Insights |
| 2026-07 | Ramas Esenciales · 09 Datos | INAF: sucesor impreciso; GDPR/LFPDPPP marcados ⚠️ | **Verificado ✅:** **GDPR aplicable 25-may-2018** (adoptado 27-abr-2016); **LFPDPPP de 2010**. **Precisado:** el INAI se extinguió y sus funciones pasaron a la **Secretaría Anticorrupción y Buen Gobierno** (desde **21-mar-2025**), con nueva **Ley General de Protección de Datos** | Comisión Europea; DLA Piper; GT Law, Recording Law (2025) |
| 2026-07 | Ramas Esenciales · 10 Ambiental | LGEEPA marcada ⚠️; sin mención de reforma en curso | **Verificado ✅:** **LGEEPA en vigor desde 1988**. **❗Hallazgo:** **iniciativa presidencial (mayo 2026)** para una **nueva LGEEPA** que reemplazaría la de 1988 → añadida alerta en el tratado | JD Supra; Holland & Knight (2026) |
| 2026-07 (v3.0) | III-02 Sociedades (LGSM) | Artículos ⚠️ | **Verificado ✅ (lote):** **LGSM art. 1** (los 7 tipos de sociedad mercantil), **art. 88** (capital autorizado de la S.A.); LGSM con última reforma **DOF 14-mar-2016** | Fuentes jurídicas y académicas (LGSM DOF 2016) |
| **2026-07 (v3.1)** | **Ramas Esenciales · 01 Fiscal** e **IV-09 Fiscal Corporativo** | Números de artículo del CFF y la LISR marcados ⚠️ (sin cotejo verbatim, faltaba el texto legal íntegro) | **✅ COTEJO VERBATIM (número ↔ contenido) contra el texto oficial vigente**, ahora archivado en [`fuentes-legales/`](./fuentes-legales/). **CFF (DOF 09-04-2026):** art. **1º** (obligación de contribuir), **2º** (clasificación), **4º** (crédito fiscal), **5º-A** (razón de negocios/antiabuso), **6º** (causación), **17-A** (actualización), **21** (recargos), **26** (responsables solidarios), **42** (facultades de comprobación), **67** (caducidad, **5 años**), **69-B** (EFOS), **146** (prescripción, **5 años**). **LISR (DOF 01-04-2024):** art. **9** (ISR PM **30%**), **27** (requisitos de deducciones), **28** (no deducibles), **57** (pérdidas = **diez ejercicios siguientes**), **152** (tarifa PF). En 01-Fiscal se voltearon **30 marcas ⚠️→✅**. | **Textos oficiales del CFF y la LISR** (Cámara de Diputados / DOF), convertidos a UTF-8 y archivados en `fuentes-legales/` |

> *(Cuando se detecten y corrijan más errores, se agregan renglones aquí.)*

---

## VI. Backlog de verificación (priorizado por riesgo)

No todos los tratados tienen el mismo riesgo. Los que **más datos duros** contienen (artículos,
fechas, montos) son los que más urge auditar. Orden sugerido de revisión sistemática:

| Prioridad | Tratados | Por qué | Estado |
|-----------|----------|---------|--------|
| 🔴 Alta | Nivel III (Mercantil): Sociedades, Títulos de Crédito, Mercado de Valores, Concurso | Densos en artículos y leyes específicas (LGSM, LGTOC, LMV) | ⬜ Pendiente (1 error ya corregido) |
| 🔴 Alta | Nivel IV (Corporate): los que citan leyes mexicanas y montos | Cifras y normas que cambian | ⬜ Pendiente |
| 🔴 Alta | **Ramas Esenciales (01–11)**: Fiscal, Constitucional/Amparo, Administrativo, Procesal, Laboral, Penal, PI, DIP/Arbitraje, Datos, Ambiental, Ética | Muy densos en artículos, tasas, plazos y montos de materias que **se reforman cada año** (CFF, LISR, LIVA, Ley de Amparo, LFT, CPF, LFPPI, LFPDPPP, LGEEPA, etc.). Redactados marcando ⚠️ todo dato duro y con sello de fecha | 🟡 **En proceso (2026-07).** **Fechas/hechos de reforma verificados ✅** en **10 de 11 tratados**: 01-Fiscal (tasas ISR/IVA; arts. 2, 42, 69-B), 02-Constitucional (Amparo 2013; reforma judicial 15-sep-2024), 04-Procesal (CNPCF 7-jun-2023), 05-Laboral (vacaciones 2022/2023), 06-Penal (acusatorio 2008/2016; CNPP 2014), 07-PI (LFPPI 2020 **+ reforma 2026**), 08-DIP/Arbitraje (NY 1958/1971; UNCITRAL 1985/1993), 09-Datos (GDPR 2018; INAI→Secretaría Anticorrupción 2025), 10-Ambiental (LGEEPA 1988 **+ iniciativa 2026**); 03-Admin (COFECE→CNA, ya registrado). **✅ Verbatim de números de artículo COMPLETADO para 01-Fiscal** (CFF y LISR cotejados palabra por palabra contra el texto oficial en `fuentes-legales/`, v3.1). **Pendiente:** verbatim de artículos de las demás leyes (Ley de Amparo, LFT, CPF, LFPPI, LGTOC, LMV, etc.) —requiere subir su texto íntegro a `fuentes-legales/`— y afinado de 11-Ética (conceptual, sin datos duros críticos) |
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
