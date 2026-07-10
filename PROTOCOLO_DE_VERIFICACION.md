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
- **⟳ Apóstrofe de vigencia** — acompaña a **cada artículo citado** en los tratados. No cuestiona el
  contenido (que puede estar ✅), sino su **permanencia en el tiempo**: *«¿sigue vigente y con este
  número hoy? — reitéralo en su código antes de citarlo».* Es el recordatorio de que **✅ verifica a
  una fecha, no para siempre**. Su origen documentado: el **art. 390 del CPF**, que al cotejarse
  resultó **«Derogado»**. Cada tratado abre con un callout que explica el símbolo al lector.

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

| **2026-07 (v3.2)** | **Toda la biblioteca** (7 leyes del núcleo corporativo) | Números de artículo de LGSM, LGTOC, LMV, CCF, LFT, CPF y Ley de Amparo, sin cotejo verbatim (faltaba el texto íntegro) | **✅ COTEJO VERBATIM contra los textos oficiales** (Word `.doc` de la Cámara de Diputados, convertidos a UTF-8 y archivados en [`fuentes-legales/`](./fuentes-legales/)). **LGSM** (DOF 20-10-2023): 1º, 25, 58, 87, 88, 89. **LGTOC** (DOF 26-03-2024): 5º, 76 (letra de cambio), 170 (pagaré), 175 (cheque). **LMV** (DOF 14-11-2025): 1, 2, 22. **CCF** (DOF 14-11-2025): 1792, 1794, 1803, 2248. **LFT** (DOF 14-05-2026): 47, 48, 123, 132. **CPF** (DOF 13-03-2026): 7º, 386 — y **390 = «Derogado»** (origen del símbolo ⟳). **Amparo** (DOF 16-10-2025): 1º, 5º, 107, 170. Además se añadió el marcador **⟳ (apóstrofe de vigencia)** a **cada artículo citado** en toda la biblioteca (982 marcas) y un callout explicativo en los 58 tratados. | **Textos oficiales** (Cámara de Diputados / DOF) en `fuentes-legales/` |

| **2026-07 (v3.3)** | **Toda la biblioteca** (8 leyes del corazón corporativo) | Números de artículo de CPEUM, Código de Comercio, LFCE, LFPPI, LIVA, LCM, LIC y LIE, sin cotejo verbatim; y **art. 31-IV CPEUM** marcado ⚠️ desde v3.1 por no tener la Constitución | **✅ COTEJO VERBATIM contra los textos oficiales** (Word `.doc` de la Cámara de Diputados → UTF-8, en [`fuentes-legales/`](./fuentes-legales/)). **CPEUM** (DOF 02-06-2026): 1º, 27, **31-IV** (contribuir de forma proporcional y equitativa), 103, 107, 123. **CCom** (DOF 14-11-2025): 1º, 3º, 75 (actos de comercio). **LFCE** (DOF 14-11-2025): 1º, 53 (prácticas monopólicas absolutas), 56, 86 (concentraciones). **LFPPI** (DOF 03-04-2026): 1º, 57, 111. **LIVA** (DOF 12-11-2021): 1º (**tasa 16%**), 2º-A (**tasa 0%**) — nota: art. 2º **«Se deroga»**. **LCM** (DOF 14-11-2025): 1º, 10. **LIC** (DOF 14-11-2025): 2º, 46. **LIE** (DOF 27-05-2024): 1º, 5º, 6º, 7º. Con la CPEUM verificada se voltearon **11 marcas ⚠️→✅** del **art. 31-IV** en 01-Fiscal y 02-Constitucional. Se corrigieron además 12 marcadores ⟳ mal colocados a media cita. | **Textos oficiales** (Cámara de Diputados / DOF) en `fuentes-legales/` |

| **2026-07 (v3.4)** | **Toda la biblioteca** (10 leyes finales: procesal, datos, responsabilidades, ambiental, consumidor, autor, seguridad social) | Números de artículo de CNPP, CNPCF, LFPDPPP, LGRA, LGEEPA, LFPC, LFPCA, LFDA, LSS y CFPC, sin cotejo verbatim | **✅ COTEJO VERBATIM contra los textos oficiales** (Word `.doc` → UTF-8, en [`fuentes-legales/`](./fuentes-legales/)). **CNPP** (DOF 28-11-2025): 1º (ámbito), 211 (etapas del procedimiento). **CNPCF** (DOF 15-01-2026): 1º. **LFPDPPP** (DOF 14-11-2025, **nueva ley 2025**): 1º, 3º. **LGRA** (DOF 15-12-2025): 1º, 7º. **LGEEPA** (DOF 19-01-2026): 1º, 3º. **LFPC** (DOF 12-12-2025): 1º. **LFPCA** (DOF 09-06-2026): 1º (juicio ante el TFJA). **LFDA** (DOF 14-05-2026): 1º, 11. **LSS** (DOF 15-01-2026): 1º, 2º. **CFPC**: art. 1º ✅ **pero el CÓDIGO ESTÁ ABROGADO** (deja de regir a más tardar el **1-abr-2027**, sustituido por el CNPCF) — ejemplo supremo del símbolo ⟳. Con esto el corpus llega a **27 leyes** y **prácticamente toda cita de la biblioteca tiene fuente oficial detrás**. | **Textos oficiales** (Cámara de Diputados / DOF) en `fuentes-legales/` |

| **2026-07 (v4.0)** | **Cierre "Referencia Verificada"** | Semáforo desalineado (857 ⚠️ pese a tener las 27 leyes); escaparate desactualizado; tratado de Datos con marco viejo; sin tablero, formatos ni jurisprudencia | **Semáforo:** verificador [`tools/semaforo.py`](./tools/semaforo.py) volteó **68 citas de artículo** ⚠️→✅ (confirmadas vigentes en el texto oficial; los ~789 ⚠️ restantes son **fechas/tasas/cifras/conceptos** que deben seguir ⚠️). **Datos (09):** reconciliado con la **nueva LFPDPPP (DOF 14-11-2025)** — autoridad = Secretaría Anticorrupción y Buen Gobierno (art. 2-XV, 38-39), ARCO (art. 21); la LFPDPPP 2010 quedó **abrogada**. **Escaparate:** README e INDICE actualizados a v4.0. **Nuevos activos:** [`MAPA-DE-ARTICULOS.md`](./MAPA-DE-ARTICULOS.md) (14 leyes, 266 artículos), [`Banco-de-Formatos/`](./Banco-de-Formatos/) (6 plantillas) y [`Banco-de-Jurisprudencia/`](./Banco-de-Jurisprudencia/). | Textos oficiales en `fuentes-legales/`; SJF para jurisprudencia |

> *(Cuando se detecten y corrijan más errores, se agregan renglones aquí.)*

---

## VI. Backlog de verificación (priorizado por riesgo)

No todos los tratados tienen el mismo riesgo. Los que **más datos duros** contienen (artículos,
fechas, montos) son los que más urge auditar. Orden sugerido de revisión sistemática:

| Prioridad | Tratados | Por qué | Estado |
|-----------|----------|---------|--------|
| 🔴 Alta | Nivel III (Mercantil): Sociedades, Títulos de Crédito, Mercado de Valores, Concurso | Densos en artículos y leyes específicas (LGSM, LGTOC, LMV) | 🟢 **Verbatim v3.2:** LGSM (1/25/58/87/88/89), LGTOC (5/76/170/175), LMV (1/2/22); **v3.3:** Código de Comercio (1/3/75), LCM (1/10), LIC (2/46) cotejados contra `fuentes-legales/`. ✅ Núcleo mercantil/concursal/bancario completo |
| 🔴 Alta | Nivel IV (Corporate): los que citan leyes mexicanas y montos | Cifras y normas que cambian | 🟢 Base fiscal (v3.1) y mercantil (v3.2) verbatim; ⟳ en todas las citas |
| 🔴 Alta | **Ramas Esenciales (01–11)**: Fiscal, Constitucional/Amparo, Administrativo, Procesal, Laboral, Penal, PI, DIP/Arbitraje, Datos, Ambiental, Ética | Muy densos en artículos, tasas, plazos y montos de materias que **se reforman cada año** (CFF, LISR, LIVA, Ley de Amparo, LFT, CPF, LFPPI, LFPDPPP, LGEEPA, etc.). Redactados marcando ⚠️ todo dato duro y con sello de fecha | 🟡 **En proceso (2026-07).** **Fechas/hechos de reforma verificados ✅** en **10 de 11 tratados**: 01-Fiscal (tasas ISR/IVA; arts. 2, 42, 69-B), 02-Constitucional (Amparo 2013; reforma judicial 15-sep-2024), 04-Procesal (CNPCF 7-jun-2023), 05-Laboral (vacaciones 2022/2023), 06-Penal (acusatorio 2008/2016; CNPP 2014), 07-PI (LFPPI 2020 **+ reforma 2026**), 08-DIP/Arbitraje (NY 1958/1971; UNCITRAL 1985/1993), 09-Datos (GDPR 2018; INAI→Secretaría Anticorrupción 2025), 10-Ambiental (LGEEPA 1988 **+ iniciativa 2026**); 03-Admin (COFECE→CNA, ya registrado). **✅ Verbatim COMPLETADO (v3.1–v3.2):** 01-Fiscal (CFF, LISR), 02-Amparo (Ley de Amparo), 05-Laboral (LFT), 06-Penal (CPF), y las mercantiles/civil (LGSM, LGTOC, LMV, CCF), todas cotejadas palabra por palabra contra el texto oficial en `fuentes-legales/`. **✅ Verbatim AMPLIADO (v3.3):** CPEUM (incl. **31-IV**), LIVA (16%/0%), LFPPI, LFCE, LCM, LIC, LIE, Código de Comercio. **✅ Verbatim COMPLETADO (v3.4):** CNPP, CNPCF, LFPDPPP, LGRA, LGEEPA, LFPC, LFPCA, LFDA, LSS, CFPC (abrogado 2027). **Corpus = 27 leyes; prácticamente toda cita de la biblioteca ya tiene su texto oficial en `fuentes-legales/`.** **Pendiente:** solo afinado de 11-Ética (conceptual, sin datos duros críticos) y leyes muy de nicho si llegaran a citarse. Nota: **⟳ (apóstrofe de vigencia)** aplicada a cada cita de toda la biblioteca |
| 🟠 Media | Nivel II (Civil profundo) | Artículos del Código Civil | 🟢 CCF disponible en `fuentes-legales/` (DOF 14-11-2025); muestra verbatim ✅ (1792/1794/1803/2248) |
| 🟠 Media | Nivel I: Personas, Bienes, Obligaciones, Contratos | Artículos del Código Civil | 🟢 CCF disponible en `fuentes-legales/`; cotejo por muestra ✅ |
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
