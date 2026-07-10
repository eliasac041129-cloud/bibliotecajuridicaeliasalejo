# [Nivel V · Libro 3] ¿Cuánto Vale?: Valuación de Empresas
#### *La pregunta en el corazón de cada operación — y cómo cuestionar el número*

> ⟳ **Apóstrofe de vigencia.** Todo artículo o criterio citado pudo cambiar después de la fecha de su
> fuente. El símbolo **⟳** significa: verifícalo en su fuente vigente
> ([`../../fuentes-legales/`](../../fuentes-legales/)) antes de citarlo.

**Etiquetas:** maestría · valuación · DCF · múltiplos · comparables · EV vs. equity · sinergias · prima de control
**Prerrequisitos:** [Libro 2 · Finanzas](./02-Finanzas-y-Contabilidad-para-Abogados.md) (indispensable) y [Libro 1 · Negociación](./01-Negociacion-de-Alto-Nivel.md); del Nivel IV, [M&A](../Nivel-IV-Corporate-Law/01-Fundamentos-de-MA.md) y [PE/VC](../Nivel-IV-Corporate-Law/07-Private-Equity-y-Venture-Capital.md).
**⏱ Dominio:** 5–6 semanas (≈ 55–65 h) **+ práctica** (haz un DCF y una valuación por múltiplos sencillos).

> Hay una pregunta en el **corazón de toda operación**: **¿cuánto vale?** El **precio** se negocia (Libro
> 1), pero el **valor** se **calcula** —y quien no sabe calcularlo negocia a ciegas—. Este libro te enseña
> los métodos (DCF, múltiplos, activos) no para volverte valuador, sino para **entender de dónde sale un
> número, cuestionarlo y negociar el precio desde el conocimiento**.

---

## 1. Valor no es precio

Dos analistas valúan la misma empresa: uno dice $800 millones, el otro $1,300. Ninguno miente; usan
supuestos distintos (proyecciones, tasas, comparables). ¿Cuál es "el" valor? **Ninguno y los dos**: la
valuación no es una verdad exacta, sino una **estimación** dentro de un rango. Y aquí está la distinción
más importante de toda la disciplina, en palabras de Warren Buffett: **"el precio es lo que pagas; el valor
es lo que recibes"**.

La **valuación** estima el **valor económico** de una empresa o participación. El **valor** es una
estimación (lo que algo "debería valer" según un método y unos supuestos); el **precio** es lo que
efectivamente se **paga** (resultado de la negociación entre partes concretas y del mercado). El valor es
**objetivo en su método pero subjetivo en sus supuestos**; el precio depende del **poder de negociación**,
de las **sinergias** del comprador concreto y de las circunstancias del deal. La valuación **informa** el
precio —da el rango y los criterios objetivos para negociar—, pero **no lo determina**. Por eso el abogado
que entiende valuación no acepta un número como veredicto: lo usa como **munición** para negociar, cuestiona
la cifra del otro lado, detecta cuándo un valor está inflado o deprimido, y participa en la decisión que más
valor mueve: **cuánto se paga**.

## 2. Qué es valuar: los tres enfoques

Todos los métodos se agrupan en tres enfoques, según de dónde sacan el valor:

- **Enfoque de ingresos (el más sólido):** valúa por la **capacidad de generar flujos futuros** —el
  **DCF**—. Una empresa vale por lo que **producirá**, no por lo que posee.
- **Enfoque de mercado (el más usado):** valúa por **comparación** con lo similar —los **múltiplos**
  (comparables de mercado y transacciones precedentes)—.
- **Enfoque de activos:** valúa por lo que la empresa **tiene** —para empresas en crisis o patrimoniales,
  no para empresas operativas en marcha—.

Y una idea que el abogado debe interiorizar: **no existe "un" valor objetivo único**. El valor está "vivo"
—depende de **para quién** (el *standalone* vs. el valor para un comprador con **sinergias**), **qué se
compra** (el **control** vale más que una minoría; lo **líquido** más que lo ilíquido), **cuándo** (los
múltiplos suben y bajan con el ciclo; las tasas afectan el WACC) y **para qué** (vender —infla—, comprar
—deprime—, litigio, fiscal)—. Ante "esta empresa vale X", la pregunta experta es: **"¿valor para quién,
calculado cómo, con qué supuestos y para qué propósito?"**.

## 3. El DCF: el método rey (y el más peligroso)

El **DCF (flujo de efectivo descontado)** captura la idea fundamental: *una empresa vale el valor presente
del efectivo que generará en el futuro*. Tres componentes:

```
Valor (EV) = VP de los flujos del periodo explícito (5-10 años)
           + VP del VALOR TERMINAL (los flujos "a perpetuidad" — la MAYOR parte, 60-80%)
   (todo descontado al WACC)   →   Equity Value = EV − deuda neta
```

1. **La proyección de flujos libres** (EBITDA − impuestos − CapEx − cambios en capital de trabajo): la
   primera fuente de manipulación (proyecciones realistas vs. heroicas).
2. **El valor terminal:** el valor más allá del periodo explícito (crecimiento a perpetuidad o múltiplo de
   salida). **Suele ser la mayor parte del valor y la más sensible** —ahí se "construye" el DCF—.
3. **El WACC** (tasa de descuento): refleja el riesgo. Más bajo → mayor valor; pequeños cambios lo mueven
   mucho.

Su fortaleza: es **conceptualmente el más correcto** (valúa por fundamentos, no por comparación). Su
debilidad: ***garbage in, garbage out*** —la **apariencia de precisión matemática disfraza** la enorme
sensibilidad a supuestos que pueden manipularse—.

> 🧭 **Detente y piensa.** El banquero del vendedor te presenta un DCF de $1,500. ¿Dónde miras primero para saber si es sólido o inflado? En los **tres puntos donde se infla un DCF**: las **proyecciones** (¿un crecimiento del 15% cuando el histórico es 5%?), el **valor terminal** (¿usa un crecimiento perpetuo mayor que el de la economía —insostenible— y representa el 80% del valor?) y el **WACC** (¿una tasa baja para el riesgo real?). Recalculado con supuestos realistas, ese DCF puede caer a $950. El abogado que cuestiona los supuestos defiende a su cliente de pagar de más —cientos de millones—.

## 4. La valuación por múltiplos

Si el DCF valúa por los fundamentos, los **múltiplos** valúan por **comparación**: si empresas similares se
valúan a 8x EBITDA, una empresa comparable debería rondar ese múltiplo. El más usado es **EV/EBITDA** (el
P/E va con el equity value y la utilidad neta; EV/Ventas para empresas sin utilidad). Dos tipos, clave
distinguirlos:

- **Comparables de mercado (*trading comps*):** los múltiplos de **empresas públicas similares**. Reflejan
  la valuación **actual del mercado**; son **precios de minoría** (no incluyen prima de control); dependen
  de que los comparables sean **de verdad similares** (sector, tamaño, crecimiento, riesgo).
- **Transacciones precedentes:** los múltiplos **pagados en deals comparables** recientes. **Incluyen la
  prima de control** y las sinergias que los compradores pagaron —por eso dan múltiplos **mayores** que los
  comparables de mercado—.

El arte está en elegir comparables **de verdad similares** y entender **por qué** un múltiplo es alto o bajo
(refleja crecimiento, riesgo, márgenes) —no aplicar el promedio ciegamente—. Ventaja: rápidos y basados en
datos reales; desventaja: dependen de buenos comparables y **heredan los errores del mercado** (burbujas).
Los múltiplos y el DCF son **complementarios**: idealmente coinciden; si difieren mucho, hay que entender
por qué (¿el mercado está caro?, ¿las proyecciones del DCF son irreales?).

## 5. Valor de activos y el *football field*

El **valor de activos** valúa por lo que la empresa **tiene**: valor **en libros** (contable, histórico —
rara vez el real), de **liquidación** (venta forzada —un valor "piso"—) o de **reposición**. **No** sirve
para empresas operativas en marcha (que valen por sus flujos), sino para empresas **en crisis/concurso**
(¿vale más viva o muerta?) o ***asset-heavy*** (inmobiliarias, holdings patrimoniales).

Y la lección de la valuación madura: **ningún método es "la verdad"**. La valuación seria **combina** los
métodos y presenta un **rango** —el ***football field***, un gráfico donde cada método marca su banda—:

```
DCF                      |━━━━━━━━━━|
Comparables de mercado      |━━━━━━━|
Transacciones precedentes      |━━━━━━━━|   (incluyen prima de control)
Valor de activos         |━━━|  (piso)
                         └────── RANGO RAZONABLE ──────┘  (donde convergen)
```

La **convergencia** da confianza; la **divergencia** es informativa (hay que entender por qué). El rango da
**flexibilidad para negociar**: el vendedor argumenta el extremo alto, el comprador el bajo. Quien presenta
"el valor es exactamente X" (un punto) miente o no entiende.

## 6. Los ajustes: sinergias, prima de control, descuentos

Los métodos dan el valor "base"; los ajustes explican por qué el **precio** difiere del valor *standalone*:

- **Sinergias:** el valor adicional de **combinar** dos empresas (ahorros, ventas cruzadas). Por eso un
  **comprador estratégico** valúa la empresa en más que su *standalone* (y más que un comprador financiero).
- **Prima de control:** el sobreprecio por adquirir el **control** (que permite decidir), típicamente
  20-40% sobre el precio de minoría del mercado.
- **Descuentos:** por **iliquidez** (una participación en empresa privada, difícil de vender, vale menos) y
  por **minoría** (sin control, vale menos por acción) —decisivos en litigios y empresa familiar—.

> 🧭 **Detente y piensa.** Un comprador estratégico calcula que la empresa vale $1,000 *standalone*, pero con sus sinergias vale $1,400 para él. ¿Cuánto debe ofrecer? Depende de la **competencia**: si es el **único** comprador con esas sinergias, ancla en el *standalone* (~$1,000) y **captura** las sinergias él; si **compiten varios**, el precio sube hacia $1,400. La batalla del precio en M&A estratégico es, en el fondo, **quién se queda con las sinergias** —y el vendedor siempre argumenta "págame las sinergias que tú vas a crear"—. El abogado que entiende esto negocia su reparto; el que no, las regala.

## 7. Comparado y régimen mexicano

Los **métodos** son universales; su **uso jurídico** varía. En **EE. UU./Delaware** hay un riquísimo *case
law* sobre valuación en litigios (***appraisal rights***: el accionista disidente pide a la corte que fije
el "valor justo" de sus acciones): *Weinberger v. UOP* (1983) modernizó la metodología admisible, y *DFC
Global* (2017) y *Dell* (2017) elevaron el peso del **precio del deal** como evidencia de valor cuando el
proceso fue competitivo —reduciendo el "*appraisal arbitrage*"—. En **México**, la valuación tiene
consecuencias jurídicas en: las ***fairness opinions*** y el precio justo en **OPAs** (LMV/CNBV ⟳); la
**relación de canje** en fusiones/escisiones y el **derecho de separación** (LGSM ⟳); el **valor de
mercado** en precios de transferencia (CFF ⟳); y los **peritajes** en litigios de separación de socios,
daños y expropiación. El **riesgo país** (mayor en mercados emergentes) aumenta el WACC y **reduce** las
valuaciones respecto a mercados desarrollados.

## 8. Casos reales — y qué aprendió el mercado

- **La burbuja puntocom (2000):** empresas de internet sin utilidades con valuaciones estratosféricas
  basadas en "métricas" dudosas, hasta el colapso.
- **Las *fairness opinions* y sus límites:** el banco que da la opinión a veces **también** cobra por
  cerrar el deal (conflicto de interés).
- **Los unicornios y los *down rounds*:** valuaciones privadas de startups que no resistieron el escrutinio
  del mercado público.
- **El *appraisal* de Delaware (Weinberger, Dell, DFC Global):** las cortes valúan empresas y arbitran
  entre los DCF de las partes.

**¿Qué aprendió el mercado?**

- *Puntocom / unicornios* → las valuaciones **pueden desconectarse de los fundamentos** (manías); el
  análisis de los fundamentos (DCF) y el escepticismo son la defensa.
- *Fairness opinions* → la valuación "independiente" debe serlo **de verdad**; vigila los conflictos de
  quien valúa.
- *Appraisal de Delaware* → el **precio de un deal competitivo y bien procesado** es fuerte evidencia del
  valor; el DCF independiente protege cuando el proceso fue deficiente.

## 9. Cómo razona un socio

> *"Cuando el otro lado me pone una valuación sobre la mesa, no pienso 'qué bonito modelo', sino '¿quién la
> hizo, para qué, y qué supuestos esconde?'. Si es el banquero del vendedor, sé que va a inflar, y voy
> directo a los tres puntos donde se infla un DCF: las proyecciones, el valor terminal (que es el 80% del
> valor) y el WACC (medio punto menos y el valor sube 15%). Y nunca acepto un solo método: pido el football
> field completo, porque si solo me enseñan el DCF —el más manipulable— y me ocultan los múltiplos, algo
> huele mal. Mi regla de oro es la de Buffett: el valor es lo que recibes, el precio es lo que pagas. La
> valuación no me dice el precio; me da el rango y los argumentos para pelearlo. Y en las operaciones
> estratégicas, mi obsesión son las sinergias: el vendedor siempre quiere que le pague las que yo voy a
> crear. El abogado que no entiende valuación se sienta a 'revisar cláusulas' mientras la batalla de los
> millones —el precio— la pelean otros."*

## 10. Errores que cuestan millones

1. **Confundir valor con precio.** Aceptar la valuación como "verdad" o creer que el precio refleja el valor
   real. *Prevención:* el valor estima, la negociación fija; usa la valuación como munición.
2. **No cuestionar los supuestos del DCF.** Aceptar proyecciones infladas, valor terminal optimista o WACC
   bajo. *Prevención:* interroga cada supuesto; pide análisis de sensibilidad.
3. **Usar comparables malos o un solo método.** *Prevención:* comparables de verdad similares; *football
   field* con varios métodos.
4. **Ignorar sinergias, prima de control o descuentos.** No entender por qué el precio difiere del
   *standalone*. *Prevención:* domina los ajustes (M&A estratégico, litigios, empresa familiar).
5. **No vigilar la independencia/sesgo de quien valúa.** Aceptar la valuación de la parte interesada.
   *Prevención:* exige independencia; identifica la dirección del sesgo y el propósito.

## 11. Debate abierto (para desarrollar criterio)

- ¿**DCF o múltiplos**? ¿Es el DCF "ciencia" o "basura sofisticada" (*garbage in, garbage out*)?
- En un litigio de *appraisal*, ¿determina el **valor justo** el **precio del deal** (el mercado) o un
  **DCF** independiente? (El debate de Delaware.)
- ¿Se deben **pagar las sinergias** al vendedor, o las captura el comprador que las crea?
- ¿Son legítimos los **descuentos por minoría/iliquidez**, o se prestan al **despojo** del socio que sale?

## 12. Herramientas de trabajo

**Del valor al precio:**
```
VALOR STANDALONE (DCF + múltiplos = football field, un RANGO)
   + sinergias (comprador estratégico) + prima de control (adquisición de control)
   − descuentos (minoría / iliquidez, en participaciones)
   ↓ NEGOCIACIÓN (poder relativo, competencia de postores, urgencia)
   = PRECIO (lo que efectivamente se paga)
```

**Checklist esencial:**
- [ ] ¿Me dan un **rango** (*football field*) o un número único? ¿Qué **métodos**? ¿**Convergen**?
- [ ] ¿Es **independiente** quien valúa, o tiene conflicto/sesgo? ¿Para qué **propósito** se hizo?
- [ ] **DCF:** ¿proyecciones realistas (vs. histórico)? ¿valor terminal razonable (% y crecimiento)? ¿WACC
  defendible? ¿análisis de sensibilidad?
- [ ] **Múltiplos:** ¿comparables de verdad similares? ¿múltiplo correcto para la métrica? ¿mercado
  caro/barato? ¿minoría (mercado) o control (transacciones)?
- [ ] **Ajustes:** ¿sinergias (¿de quién?)? ¿prima de control? ¿descuentos por minoría/iliquidez
  justificados?
- [ ] ¿Distinguí **EV** de **equity value** (= EV − deuda neta)? ¿Uso el rango como munición para negociar
  (Libro 1)?

**Flashcards:**
- *Valor vs. precio* → estimación (según método/supuestos) vs. lo que se paga (negociación/mercado).
- *Tres métodos* → DCF (flujos) · múltiplos (comparación) · activos (lo que tiene).
- *DCF* → VP de flujos + valor terminal, al WACC. El valor terminal es la mayor parte y la más sensible.
- *Comparables de mercado vs. transacciones precedentes* → precio de minoría vs. precio de control (con prima).
- *EV/EBITDA* → el múltiplo rey del M&A.
- *Football field* → el rango de valor según cada método (la "verdad" es un rango).
- *Sinergias / prima de control* → suben el valor (estratégico / control).
- *Descuentos por minoría/iliquidez* → bajan el valor (participaciones sin control / privadas).
- *Regla de oro* → "valor no es precio; la valuación es tan buena como sus supuestos; usa un rango".

**Simulador (tipo despacho).**
> **Rol:** asesoras al comprador. Te entregan: EBITDA $100, proyecciones de crecimiento del 12% (histórico
> 5%), deuda neta $300, comparables a 6-8x, transacciones precedentes a 8-10x. **Entrega:** valor por
> múltiplos; qué cuestionas del DCF; por qué difieren comparables y transacciones; el equity value; cómo
> negocias. *Pista:* comparables (EV 600-800), transacciones (800-1,000, incluyen prima de control); las
> proyecciones del 12% vs. 5% histórico están **infladas**; equity value = EV − 300; ancla en el extremo
> **bajo** (comparables) y cuestiona el DCF del vendedor.

## 13. Bibliografía por niveles

- **Referente mundial:** Aswath Damodaran, *Investment Valuation* (y sus materiales en línea, gratuitos); *The Little Book of Valuation*.
- **Tratado de la consultoría:** Koller, Goedhart & Wessels (McKinsey), *Valuation*.
- **Clásicos (valor vs. precio):** Graham & Dodd, *Security Analysis*; Graham, *The Intelligent Investor*.
- **Base financiera:** Brealey, Myers & Allen, *Principios de Finanzas Corporativas*.
- **Estándares y litigio:** International Valuation Standards (IVS); *case law* de Delaware sobre *appraisal* (*Weinberger v. UOP*, *DFC Global*, *Dell*).

## 14. Ruta al siguiente libro (cierra el Nivel V)

Ya sabes **cuánto vale** lo que se negocia y cómo **cuestionar** una valuación. Falta la última herramienta
de la maestría: pensar **estratégicamente** —ver el tablero completo y anticipar los movimientos de los
demás—.

- **Siguiente (cierra el Nivel V y la biblioteca):** *[Libro 4 · Estrategia Corporativa y Game Theory](./04-Estrategia-Corporativa-y-Game-Theory.md)* — la estrategia (Porter, las cinco fuerzas, la ventaja competitiva) y la teoría de juegos (decidir cuando el resultado depende de lo que hagan los demás). La valuación responde "¿cuánto vale?"; la estrategia responde "**¿por qué y para qué?**" (¿esta adquisición crea ventaja competitiva?, ¿cómo reaccionarán los competidores?). Y la teoría de juegos ilumina la negociación, las subastas y las guerras de ofertas.
