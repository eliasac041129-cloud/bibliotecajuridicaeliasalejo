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
