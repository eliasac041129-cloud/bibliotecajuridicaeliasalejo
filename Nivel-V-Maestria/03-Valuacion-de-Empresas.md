# [Nivel V · Libro 3] Valuación de Empresas

> Hay una pregunta que está en el **corazón de toda operación corporativa**: **¿cuánto vale?** ¿Cuánto vale
> la empresa que se compra, las acciones que se suscriben, el negocio que se aporta a una JV, la
> participación de la que sale un fondo? El **precio** se negocia (Libro 1), pero el **valor** se **calcula**
> —y quien no sabe calcularlo negocia a ciegas—. Este libro te enseña los **métodos de valuación**: el
> flujo de efectivo descontado (DCF), los múltiplos de comparables, las transacciones precedentes, el valor
> de activos. No para volverte un *valuador* profesional, sino para **entender de dónde sale un número**,
> **cuestionarlo**, y **negociar el precio desde el conocimiento**. Es la culminación de las finanzas
> (Libro 2) aplicada a la pregunta más importante, y la tercera herramienta de la maestría.

**Etiquetas:** maestría · valuación · DCF · múltiplos · comparables · enterprise value · sinergias · prima de control
**Prerrequisitos:** [Libro 2 · Finanzas y Contabilidad para Abogados](./02-Finanzas-y-Contabilidad-para-Abogados.md) (indispensable) + [Libro 1 · Negociación](./01-Negociacion-de-Alto-Nivel.md) + todo el Nivel IV (las operaciones cuyo valor hay que calcular), en especial [M&A](../Nivel-IV-Corporate-Law/01-Fundamentos-de-MA.md) y [PE/VC](../Nivel-IV-Corporate-Law/07-Private-Equity-y-Venture-Capital.md).
**Estándar:** V3 (43 secciones + secciones transversales).
**⏱ Tiempo estimado de dominio:** 5–6 semanas (≈ 55–65 h de estudio activo) + **práctica** (haz un DCF y
una valuación por múltiplos sencillos). Lectura de reconocimiento: 10–12 h. *Estúdialo en bloques: qué es
valuar (valor vs. precio) → el DCF (el método rey) → múltiplos y comparables → transacciones precedentes y
valor de activos → conceptos avanzados (sinergias, prima de control, descuentos) y la valuación en la
práctica.*

> **Aviso de método.** Tratado **práctico y crítico**: la valuación es **parte ciencia, parte arte** —los
> métodos son rigurosos, pero dependen de **supuestos** (proyecciones, tasas) que pueden manipularse—. El
> objetivo no es que valúes como un banquero de inversión, sino que **entiendas la lógica** de cada método,
> sepas **de dónde sale un número** y puedas **cuestionarlo**. Conecta con las finanzas (Libro 2 —es su
> aplicación—), con la negociación (Libro 1 —el valor es el criterio objetivo del precio—) y con el M&A y el
> PE/VC (donde valuar es decisivo).

---

### Nivel de importancia profesional (vista rápida)
```
Litigio              ★★★★☆
Corporate            ★★★★★
M&A                  ★★★★★
Mercado de Valores   ★★★★★
Venture Capital      ★★★★★
Private Equity       ★★★★★
Gobierno Corporativo ★★★★☆
Compliance           ★★☆☆☆
Derecho Bancario     ★★★★☆
Empresa Familiar     ★★★★★
```
*La valuación es la pregunta central de cada operación: ¿cuánto vale? El abogado que entiende cómo se valúa
puede negociar el precio, cuestionar la cifra del otro lado, y detectar cuándo un número es inflado o
injustificado. Decisiva en M&A, PE/VC, litigios de valuación y empresa familiar (sucesión, reparto).*

## 1. Introducción

Toda operación corporativa gira en torno a un número: el **valor**. En un M&A, ¿cuánto vale la empresa que
se compra? En una ronda de VC, ¿cuál es la valuación pre-money que define el porcentaje del inversionista?
En la salida de un fondo, ¿a qué precio se vende? En una JV, ¿cuánto valen las aportaciones de cada socio?
En una empresa familiar, ¿cuánto vale para repartir entre herederos o para vender? En un litigio, ¿cuánto
vale la participación de un socio que se separa? La **valuación** —el proceso de estimar cuánto vale una
empresa o una participación— es, por ello, una de las disciplinas más importantes y transversales de las
finanzas corporativas.

La **valuación** es el conjunto de **métodos** para estimar el **valor económico** de una empresa, un
negocio o una participación. Se apoya directamente en las finanzas que aprendiste en el Libro 2 (el valor
del dinero en el tiempo, el costo de capital, el EBITDA, el EV vs. equity value) y las **aplica** a la
pregunta central: ¿cuánto vale? Hay varios métodos —el flujo de efectivo descontado (DCF), los múltiplos de
comparables, las transacciones precedentes, el valor de activos—, cada uno con su lógica, sus ventajas y sus
limitaciones, y el valuador experto los **combina** para llegar a un **rango** de valor razonable.

La idea rectora del libro, y la distinción más importante que debes interiorizar: **valor no es lo mismo
que precio.** El **valor** es una **estimación** (lo que algo "debería valer" según un método y unos
supuestos); el **precio** es lo que efectivamente se **paga** (el resultado de una negociación entre un
comprador y un vendedor concretos). El valor es **objetivo en su método pero subjetivo en sus supuestos**
(dos analistas pueden valuar la misma empresa distinto según sus proyecciones y tasas); el precio es **lo
que el mercado o las partes acuerdan**. Como dijo Warren Buffett: "*el precio es lo que pagas; el valor es
lo que recibes*". La valuación **informa** el precio (da el rango, el criterio objetivo para negociar), pero
no lo determina: el precio final depende del **poder de negociación**, las **sinergias** del comprador
concreto, y las circunstancias del deal.

Para el abogado corporativo, ¿por qué importa valuar si no es su trabajo "oficial" (lo hacen banqueros y
valuadores)? Porque **entender** la valuación le permite **cuestionar** el número del otro lado (¿por qué
ese múltiplo?, ¿esas proyecciones son realistas?, ¿esa tasa de descuento es razonable?), **negociar el
precio** desde el conocimiento (no a ciegas), **detectar** cuándo un valor está inflado o injustificado, y
**asesorar** a su cliente sobre si el precio es justo. El abogado que no entiende valuación deja la batalla
del precio —la más importante— en manos de otros. Por eso la valuación, junto con la negociación y las
finanzas, es una herramienta de la **maestría**: porque permite al jurista participar en la decisión que más
importa: **cuánto se paga**.

## 2. Objetivos del libro

Al terminar, el lector será capaz de:

- **Distinguir valor de precio** y entender que la valuación es **parte ciencia, parte arte** (rigurosa en
  el método, sensible a los supuestos).
- **Dominar la lógica del DCF (flujo de efectivo descontado)** —el método "rey"—: proyectar flujos,
  estimar el **valor terminal**, descontar al **WACC**, y entender por qué es el método más sólido
  conceptualmente y, a la vez, el más sensible a los supuestos.
- **Aplicar la valuación por múltiplos**: de **comparables de mercado** (empresas públicas similares) y de
  **transacciones precedentes** (deals comparables), elegir los múltiplos correctos (EV/EBITDA, P/E),
  y entender sus ventajas (rapidez, "lo que paga el mercado") y limitaciones (¿hay comparables buenos?).
- **Conocer el valor de activos** (valor en libros, valor de liquidación, valor de reposición) y cuándo se
  usa (empresas en crisis, *asset-heavy*).
- **Combinar métodos** para llegar a un **rango de valuación** razonable (el "campo de fútbol" —*football
  field*—) y entender por qué ningún método es "la verdad".
- **Manejar los conceptos avanzados**: las **sinergias** (por qué un comprador estratégico paga más), la
  **prima de control** (por qué el control vale más que una minoría), el **descuento por iliquidez/minoría**,
  y la valuación de empresas especiales (*startups*, empresas en pérdidas, empresas en crisis).
- **Cuestionar una valuación**: detectar supuestos inflados, comparables malos, proyecciones heroicas, y
  saber **qué preguntas hacer** para validar (o demoler) un número.
- **Aplicar la valuación en la práctica**: en el M&A (negociar el precio), el PE/VC (rondas, retorno), los
  litigios (valuación de participaciones) y la empresa familiar (sucesión, reparto).

## 3. Importancia profesional

La valuación es la pregunta **central** de las operaciones corporativas, y entenderla es lo que permite al
abogado **participar en la decisión del precio** —la más importante de cualquier deal—. Aunque la valuación
"técnica" la hacen banqueros de inversión y valuadores, el abogado que la **entiende** agrega un valor
enorme: cuestiona la cifra del otro lado, valida la del propio, negocia el precio con argumentos sólidos
(criterios objetivos —Libro 1—), y detecta cuándo alguien intenta inflar (o deprimir) el valor. El abogado
que no entiende valuación se limita a "lo legal" mientras la batalla del precio —donde están los millones—
la libran otros.

Para **tu perfil** —M&A, PE/VC, operaciones complejas—, la valuación es **omnipresente**: el M&A es comprar
valor (negociar el precio sobre la valuación); el VC fija valuaciones pre/post-money en cada ronda; el PE
compra barato y vende caro (la *multiple expansion*); la salida de un fondo es una valuación; una JV valúa
aportaciones. Sin entender valuación, el abogado de estas áreas no puede asesorar bien sobre el precio
—queda relegado—.

Hay además aplicaciones **más allá del M&A** que amplían tu valor: en **litigios** (valuar la participación
de un socio que se separa, daños por incumplimiento, expropiaciones); en **empresa familiar** (valuar para
la **sucesión**, el reparto entre herederos, o la venta —relevante para tu perfil—); en **reestructuras**
(valuar para fusiones, escisiones —la relación de canje—); y en **fiscal** (valuaciones para efectos
fiscales). La valuación es una habilidad **transversal** que el abogado corporativo de élite usa en
múltiples contextos. Por eso, junto con las finanzas y la negociación, corona la maestría: porque permite al
abogado **dominar la conversación sobre el valor** —el lenguaje en que se deciden los millones—.

## 4. Historia y origen

La idea de **valuar** —estimar cuánto vale algo que produce ingresos futuros— es antigua (los romanos
valuaban tierras y rentas), pero la **valuación moderna** se desarrolla con las finanzas del siglo XX. El
hito conceptual es la idea del **valor intrínseco** basado en los **flujos futuros**: si un activo
producirá flujos de efectivo en el futuro, su valor hoy es el **valor presente** de esos flujos. Esta idea
—que ya viste en el Libro 2 (el valor del dinero en el tiempo)— es la base del **DCF** y fue formalizada
por **John Burr Williams** (*The Theory of Investment Value*, 1938) y popularizada en la **inversión en
valor** por **Benjamin Graham** (el maestro de Warren Buffett), cuya obra *Security Analysis* (1934)
distinguió el **valor intrínseco** del **precio de mercado** —la distinción central de este libro—.

La **valuación por múltiplos** (valuar por comparación con empresas o transacciones similares) se desarrolló
con los **mercados de capitales** (al haber empresas públicas con precios observables, se podía comparar) y
se volvió la herramienta práctica más usada en la banca de inversión por su rapidez. El **CAPM** (años
1960) dio una forma de estimar el **costo del equity** (la tasa de descuento del DCF), y el desarrollo de
las finanzas corporativas (Modigliani-Miller, etc.) refinó el **WACC**. La valuación de **opciones**
(Black-Scholes, 1973) abrió la valuación de activos con flexibilidad e incertidumbre (las "opciones
reales").

En la **práctica del M&A y la banca de inversión**, la valuación se sistematizó en un conjunto de métodos
estándar (DCF, comparables de mercado, transacciones precedentes, y para LBO, el *LBO analysis*) que se
presentan juntos en el "***football field***" (un gráfico que muestra el **rango** de valor según cada
método). **Aswath Damodaran** (NYU), el "decano de la valuación", popularizó y democratizó el conocimiento
de la valuación con sus obras y materiales accesibles. Hoy la valuación es una disciplina madura, central en
la banca de inversión, el PE/VC, la auditoría (valuación de activos), y los litigios —y una competencia que
el abogado corporativo debe **entender**, aunque no la ejecute técnicamente—.

## 5. Evolución histórica

La valuación ha evolucionado en tres movimientos:

**1) Del valor de los activos al valor de los flujos futuros.** La valuación "primitiva" miraba lo que una
empresa **tenía** (sus activos —valor en libros—). La valuación moderna entiende que el valor de una empresa
**en marcha** no está en sus activos, sino en su capacidad de **generar flujos de efectivo en el futuro**
(una empresa vale por lo que **producirá**, no por lo que **posee**). De ahí el predominio del **DCF** y los
**múltiplos** (basados en la rentabilidad —EBITDA, utilidad—) sobre el valor de activos (relegado a empresas
en crisis o *asset-heavy*).

**2) Del arte intuitivo al método riguroso (pero aún con arte).** La valuación pasó de la intuición del
comerciante a **métodos rigurosos** con fundamento financiero (DCF, CAPM, múltiplos). Pero —y esto es
crucial— **nunca dejó de tener un componente de arte**: el DCF depende de **proyecciones** (el futuro es
incierto) y de la **tasa de descuento** (sensible); los múltiplos dependen de elegir **comparables buenos**.
La valuación es **rigurosa en el método pero sensible en los supuestos** —y por eso se puede **manipular**
(proyecciones optimistas, tasa baja, comparables convenientes inflan el valor)—. El valuador maduro entiende
esta tensión.

**3) De un solo número a un rango y un escrutinio crítico.** La valuación madura abandonó la pretensión de
un "número exacto" y adoptó la lógica del **rango** (el *football field*): distintos métodos dan distintos
valores, y la "verdad" es un **rango razonable**, no un punto. A la vez, creció el **escrutinio crítico**:
tras burbujas y fraudes (las puntocom, las valuaciones infladas de *startups*), se entiende mejor que las
valuaciones **pueden estar equivocadas o manipuladas**, y que hay que **cuestionar los supuestos**. La
valuación moderna es **humilde** (sabe que es una estimación) y **crítica** (escruta los supuestos).

## 6. Contexto económico

La valuación es, en esencia, **economía financiera aplicada**. Tres ideas la gobiernan:

- **El valor es el valor presente de los flujos futuros (el principio fundamental).** Económicamente, el
  valor de cualquier activo que produce ingresos es la **suma de los flujos de efectivo que generará en el
  futuro, traídos a valor presente** (descontados a una tasa que refleja su riesgo). Este principio —del
  Libro 2— es la base del DCF y la lógica subyacente de **toda** valuación: una empresa vale por su
  capacidad de generar efectivo futuro. *Corolario:* lo que **mueve** el valor es el **crecimiento** de los
  flujos, su **riesgo** (la tasa de descuento) y su **sostenibilidad** —no los activos contables—.
- **El valor depende del riesgo (la tasa de descuento).** A mayor **riesgo** de los flujos futuros, mayor la
  **tasa de descuento** (el WACC), y **menor** el valor presente. Por eso una empresa **estable y predecible**
  (bajo riesgo) vale más, a igual flujo, que una **volátil e incierta** (alto riesgo). Y por eso el **riesgo
  país** (mayor en mercados emergentes) reduce las valuaciones. El valor y el riesgo están **inversamente**
  relacionados.
- **El valor es subjetivo en parte (depende de quién y para qué).** Aunque los métodos son objetivos, el
  valor **depende del valuador y del comprador**: un **comprador estratégico** con **sinergias** valúa la
  empresa en más (porque vale más **para él**); el **control** vale más que una minoría (prima de control);
  una participación **ilíquida** vale menos (descuento por iliquidez). El valor "objetivo" (*standalone*) es
  un punto de partida, pero el valor **para un comprador concreto** puede ser muy distinto —y eso explica por
  qué el precio pagado a menudo supera el valor *standalone*—.

## 7. Contexto político y regulatorio

La valuación tiene relevancia regulatoria en varios contextos donde el **valor** tiene consecuencias
jurídicas:

- **Mercado de valores (LMV / CNBV):** en las **OPAs** (ofertas públicas de adquisición), la ley exige que
  el precio sea **justo** y, a menudo, una **opinión de un experto independiente** (*fairness opinion*)
  sobre la valuación, para proteger a los accionistas minoritarios. La valuación de empresas públicas está
  bajo escrutinio regulatorio.
- **Deberes fiduciarios (gobierno corporativo — Libro 8 del Nivel IV):** el consejo, al aprobar una venta,
  debe basarse en una valuación adecuada (la ***fairness opinion*** es parte del proceso informado —Van
  Gorkom—); valuar mal puede ser un incumplimiento del deber de diligencia.
- **Fiscal (CFF, LISR):** las operaciones entre **partes relacionadas** deben hacerse a **valor de mercado**
  (precios de transferencia); las reorganizaciones y aportaciones tienen efectos fiscales que dependen del
  valor; la autoridad puede cuestionar valuaciones que busquen eludir impuestos.
- **Reorganizaciones (LGSM):** las **fusiones y escisiones** requieren valuar para fijar la **relación de
  canje** (cuántas acciones de una sociedad equivalen a las de otra) —Libro 3 del Nivel IV—.
- **Litigios:** la valuación es central en disputas de **separación de socios** (cuánto se le paga al que
  sale), **daños** (lucro cesante, valor perdido), **expropiaciones** (indemnización justa), y **familiares**
  (reparto, sucesión). Los **peritos valuadores** son figura clave, y sus valuaciones se litigan.
- **Contabilidad (NIF/IFRS):** ciertas partidas se registran a **valor razonable** (*fair value*), lo que
  exige valuar (instrumentos financieros, *impairment* del goodwill).

## 8. Contexto social

La valuación tiene una dimensión social y de **justicia** que el abogado debe apreciar. Cuando se valúa una
empresa, hay **mucho en juego para personas reales**: el accionista minoritario que sale (¿le pagan un
precio justo o lo expropian con una valuación deprimida?), los herederos que reparten (¿la valuación es
ecuánime entre ellos?), los trabajadores cuyo futuro depende de la operación, el empresario que vende el
fruto de su vida. Una valuación **manipulada** (inflada para vender caro, o deprimida para sacar barato a un
socio) puede ser un instrumento de **injusticia o despojo** —y el abogado que entiende valuación puede
**proteger** a su cliente de ello (detectar y cuestionar la manipulación)—.

Hay también una dimensión de **poder e información**: quien controla (o entiende) la valuación tiene poder
en la negociación. Históricamente, las valuaciones complejas (hechas por banqueros) han dado ventaja a quien
las encarga (que puede orientar los supuestos). El abogado que **entiende** la valuación **nivela** ese
poder para su cliente —puede cuestionar los supuestos, pedir métodos alternativos, exigir una *fairness
opinion* independiente—. El "analfabetismo en valuación" deja al cliente a merced de quien presenta el
número.

Finalmente, las **burbujas** y los **fraudes** de valuación (las puntocom, las *startups* sobrevaluadas, las
valuaciones infladas que precedieron a colapsos) tienen un enorme costo social (inversionistas que pierden,
ahorros destruidos, recursos mal asignados). Entender que las valuaciones **pueden estar equivocadas o
infladas** —y mantener un escepticismo saludable— es parte de la responsabilidad del profesional. El
abogado y el valuador íntegros entienden que su deber es con una valuación **honesta y bien fundada**, no
con el número que el cliente quiere oír.

## 9. Contexto empresarial

Desde la óptica del negocio, la valuación es la base de las **decisiones de inversión y de las
operaciones**. El abogado corporativo debe entenderla porque condiciona todo lo que estructura:

- **En el M&A:** la valuación define el **rango de precio** y es la base de la negociación; el comprador
  valúa para saber **cuánto ofrecer** (incluyendo las **sinergias** que justifican pagar más), el vendedor
  para saber **cuánto pedir**. La *fairness opinion* respalda la decisión del consejo.
- **En el VC:** la valuación **pre-money** define el porcentaje del inversionista (Libro 7); valuar
  *startups* (sin flujo ni historia) es un arte especial.
- **En el PE:** la tesis es comprar a un múltiplo y vender a uno mayor (***multiple expansion***); la
  valuación es central a la entrada y la salida.
- **En la empresa familiar:** valuar es clave para la **sucesión** (repartir entre herederos de forma
  justa), la **entrada de un fondo** (a qué valuación), o la **venta**. Una valuación bien hecha previene
  conflictos familiares.
- **En las reestructuras:** las **fusiones y escisiones** requieren valuar para la **relación de canje**.
- **En los litigios:** valuar la participación de un socio que se separa, los daños, etc.
- **En las decisiones internas:** ¿conviene esta inversión? (¿su valor presente supera su costo? —VPN—);
  ¿esta línea de negocio crea o destruye valor? (¿su ROIC supera el WACC?).

El abogado que entiende valuación puede **conversar con el banquero y el cliente** sobre el número,
**cuestionar** los supuestos, y **asesorar** sobre si el precio es justo —en lugar de aceptar pasivamente la
cifra que le presentan—. Esta es la diferencia entre el abogado que **ejecuta** una operación a un precio
que otros fijaron y el que **participa** en la decisión del valor. Por eso la valuación, culminando las
finanzas (Libro 2) y armando la negociación (Libro 1), es una herramienta de la **maestría**: porque pone al
abogado en el centro de la conversación que más importa —**cuánto vale y cuánto se paga**—.

## 10. Definiciones doctrinales

La doctrina de la valuación define los conceptos centrales así:

- **Valuación:** el proceso de **estimar el valor económico** de una empresa, negocio, activo o
  participación, mediante métodos financieros. La doctrina la define como una **estimación fundamentada**,
  no una verdad exacta.
- **Valor vs. precio:** el **valor** es una **estimación** (lo que algo "debería valer" según un método y
  supuestos); el **precio** es lo que efectivamente se **paga** (resultado de la negociación y el mercado).
  La distinción más importante de la disciplina.
- **Valor intrínseco:** el valor "verdadero" de una empresa según sus **fundamentos** (su capacidad de
  generar flujos), independiente del precio de mercado. Base de la **inversión en valor** (Graham, Buffett).
- **DCF (*Discounted Cash Flow* / flujo de efectivo descontado):** método que valúa una empresa como el
  **valor presente de sus flujos de efectivo futuros**, descontados a una tasa (el WACC). El método "rey"
  por su solidez conceptual.
- **Valor terminal:** en el DCF, el valor de la empresa **más allá** del periodo de proyección explícita
  (los flujos "a perpetuidad" o el valor de salida). Suele ser la **mayor parte** del valor —y la más
  sensible—.
- **Múltiplo:** una razón que expresa el valor como "número de veces" una métrica (**EV/EBITDA**, **P/E**,
  EV/Ventas). Permite valuar por **comparación**.
- **Comparables (*comps*):** empresas o transacciones **similares** cuyo valor/múltiplo se usa como
  referencia. Dos tipos: **comparables de mercado** (empresas públicas similares) y **transacciones
  precedentes** (deals comparables).
- **Sinergias:** el **valor adicional** que se crea al combinar dos empresas (ahorros de costos, ventas
  cruzadas) —y que justifica que un comprador estratégico pague **más** que el valor *standalone*—.
- **Prima de control:** el **sobreprecio** que se paga por adquirir el **control** de una empresa (vs. una
  participación minoritaria), porque el control permite decidir.
- **Descuento por iliquidez / por minoría:** la **reducción** de valor de una participación **ilíquida**
  (difícil de vender, p. ej., acciones de una empresa privada) o **minoritaria** (sin control).

## 11. Definiciones legales y marco normativo

La valuación es una disciplina financiera, pero tiene **relevancia jurídica** en varios contextos regulados:

- **Mercado de valores (LMV / CNBV):** en las **OPAs**, exigencias sobre el **precio justo** y la
  **opinión de experto independiente** (*fairness opinion*) para proteger a los minoritarios; valuación de
  emisoras.
- **Deberes fiduciarios (LMV / LGSM / gobierno corporativo):** el consejo debe decidir **informado** sobre
  el valor (la *fairness opinion* como parte del proceso —Van Gorkom, Libro 8 del Nivel IV—).
- **Reorganizaciones (LGSM):** valuación para la **relación de canje** en fusiones y escisiones; el
  **derecho de separación** del socio disidente implica valuar su participación.
- **Fiscal (CFF, LISR):** **valor de mercado** en operaciones entre partes relacionadas (precios de
  transferencia); valor en reorganizaciones y aportaciones; la autoridad puede cuestionar valuaciones
  abusivas.
- **Litigios y peritajes:** la valuación de **peritos** en disputas (separación de socios, daños,
  expropiaciones, familiares); las reglas procesales sobre la prueba pericial.
- **Contabilidad (NIF/IFRS):** el **valor razonable** (*fair value*) para ciertas partidas; el ***impairment***
  (deterioro) del goodwill exige valuar.
- **Expropiación / indemnización (constitucional y administrativo):** el derecho a una **indemnización
  justa** implica valuar lo expropiado.

> **Nota de método:** la valuación no es una "rama jurídica" sino una disciplina financiera con
> **consecuencias jurídicas**; el abogado debe **entenderla** para usarla y cuestionarla, apoyándose en
> valuadores/peritos para la ejecución técnica. Verifica el marco aplicable (Manifiesto XI.5).

## 12. Definición sencilla

Imagina que quieres saber **cuánto vale una casa** que produce renta. Tienes varias formas de averiguarlo
—y son, exactamente, los métodos de valuación de empresas—:

- **Método del flujo (DCF):** "esta casa me dará $10 mil de renta al año durante muchos años; ¿cuánto valen
  **hoy** todas esas rentas futuras?" Sumas las rentas futuras **traídas a valor presente** (descontadas).
  Es el método más **lógico** (la casa vale por lo que **producirá**), pero depende de **adivinar** las
  rentas futuras y de qué tasa usas —si te equivocas en los supuestos, el número se distorsiona—.
- **Método de comparables:** "casas **parecidas** en esta zona se venden a 15 veces su renta anual; mi casa
  renta $10 mil, así que vale ~$150 mil." Valúas por **comparación** con lo que vale lo similar. Es
  **rápido** y refleja "lo que paga el mercado", pero necesitas **casas verdaderamente comparables** (misma
  zona, tamaño, estado).
- **Método de transacciones precedentes:** "la casa de **al lado** se **vendió** el mes pasado en $160 mil."
  Usas **ventas reales recientes** de casas similares. Refleja lo que de verdad se pagó (incluye la "prima"
  que pagan los compradores), pero los deals pueden no ser perfectamente comparables.
- **Método de activos:** "si **derribo** la casa y vendo el terreno y los materiales, valen $80 mil." Valúas
  lo que **tiene** (sus partes), no lo que produce. Solo conviene si la casa vale **más muerta que viva**
  (empresa en crisis) o si es pura "tierra" (poca operación).

Y la **lección clave**: **valor no es precio**. Tú **valúas** la casa en ~$150 mil (estimación), pero el
**precio** que finalmente pagas depende de la **negociación**: si hay otro comprador interesado (subes), si
el dueño tiene prisa (bajas), si para ti vale más porque está junto a tu otra casa (sinergia). El valor te
da el **rango** y los **argumentos**; el precio lo decide la **negociación**. Por eso un buen abogado de M&A
**entiende cómo se valúa** —para negociar el precio con argumentos, no a ciegas—.

## 13. Conceptos fundamentales

Fija este vocabulario; es el de la valuación profesional:

**Lo fundamental:**
- **Valor vs. precio:** estimación (valor) vs. lo que se paga (precio). El valor informa el precio, no lo
  determina.
- **Valor intrínseco / fundamental:** el valor según los fundamentos (flujos), vs. el precio de mercado.
- **Valor *standalone* vs. valor para un comprador:** el valor "por sí sola" vs. el valor para un comprador
  concreto (que puede incluir **sinergias**).

**Los métodos de valuación:**
- **DCF (flujo de efectivo descontado):** valor = valor presente de los flujos futuros (descontados al
  **WACC**). Componentes: **proyección de flujos** (típicamente 5-10 años), **valor terminal** (el valor
  más allá —a perpetuidad con crecimiento, o por múltiplo de salida—), y la **tasa de descuento (WACC)**.
- **Múltiplos de comparables de mercado:** valuar aplicando el múltiplo (EV/EBITDA, P/E) de **empresas
  públicas similares**.
- **Transacciones precedentes:** valuar aplicando los múltiplos pagados en **deals comparables** recientes
  (incluyen prima de control).
- **Valor de activos:** valor en **libros**, de **liquidación** (venta forzada) o de **reposición**
  (reconstruir). Para empresas en crisis o *asset-heavy*.
- **LBO analysis (para PE):** ¿cuánto puede pagar un fondo dado un retorno objetivo y la deuda disponible?
  (valuación "al revés" —Libro 7—).
- **El *football field*:** el gráfico que muestra el **rango** de valor según cada método (la "verdad" es
  un rango, no un punto).

**Las métricas y conceptos del Libro 2 (que se aplican):**
- **EBITDA, EV vs. equity value, deuda neta, WACC, flujo de efectivo libre** (todo del Libro 2).
- **Flujo de efectivo libre (*Free Cash Flow*):** el efectivo que genera la empresa **después** de
  reinvertir (CapEx) y del capital de trabajo —lo que de verdad queda para los proveedores de capital—. Es
  lo que se descuenta en el DCF.

**Los ajustes y conceptos avanzados:**
- **Sinergias:** valor adicional de combinar (justifica pagar más; ¿quién las captura —se reparten en el
  precio—?).
- **Prima de control:** sobreprecio por el control (vs. minoría).
- **Descuento por iliquidez:** menor valor de una participación difícil de vender (empresa privada).
- **Descuento por minoría:** menor valor de una participación sin control.
- **Valuación de *startups*:** sin flujo ni historia → métodos especiales (múltiplos de etapa, VC method,
  potencial de mercado).
- **Valor presente neto (VPN/NPN):** para decisiones de inversión (valor presente de los flujos − inversión
  inicial; si es positivo, crea valor).

Con este vocabulario, entramos al **desarrollo absoluto**, donde diseccionamos cada método.

## 14. Desarrollo absoluto

Esta es la sección central. La desarrollamos en cinco bloques: **(A)** **qué es valuar** (valor vs. precio,
los enfoques); **(B)** el **DCF** (el método rey —flujos, valor terminal, WACC—); **(C)** la **valuación
por múltiplos** (comparables de mercado y transacciones precedentes); **(D)** el **valor de activos y la
combinación de métodos** (el *football field*); y **(E)** los **conceptos avanzados** (sinergias, prima de
control, descuentos, *startups*) y la **valuación en la práctica**. Estúdialos en orden: primero la
filosofía, luego el método más sólido, después el más usado, la combinación, y los refinamientos.

### 14.A · Qué es valuar (valor vs. precio y los enfoques)

Antes de los métodos, hay que entender **qué es** valuar y **qué no es**.

**Valor no es precio (la distinción fundamental, repasada y profundizada).** El **valor** es una
**estimación** de cuánto "debería valer" algo según un método y unos supuestos; el **precio** es lo que
efectivamente se **paga**, resultado de la negociación entre partes concretas y de las fuerzas del mercado.
Consecuencias prácticas:
- **El valor es un rango, no un punto.** Distintos métodos (y distintos supuestos) dan distintos valores;
  la valuación seria produce un **rango razonable** (el *football field*), no un número exacto. Quien
  presenta "el valor es exactamente X" miente o no entiende.
- **El precio puede diferir del valor.** Un comprador con **sinergias** paga más que el valor *standalone*;
  un vendedor con prisa acepta menos; una **subasta** competitiva sube el precio sobre el valor; el **poder
  de negociación** mueve el precio dentro (o fuera) del rango de valor.
- **La valuación informa, no determina.** La valuación da el **rango** y los **argumentos** (criterios
  objetivos —Libro 1—) para negociar el precio; pero el precio final lo decide la **negociación**. El
  abogado usa la valuación como **munición** para negociar el precio, no como un veredicto.

**Los tres grandes enfoques de valuación.** Todos los métodos se agrupan en tres enfoques, según de dónde
sacan el valor:
- **Enfoque de ingresos (*income approach*):** valúa por la **capacidad de generar flujos futuros** —el
  **DCF** es su método estrella—. Es el más **sólido conceptualmente** (una empresa vale por lo que
  producirá), pero el más **sensible a los supuestos** (proyecciones, tasa).
- **Enfoque de mercado (*market approach*):** valúa por **comparación** con lo que vale lo similar —los
  **múltiplos** (comparables de mercado y transacciones precedentes)—. Es **rápido** y refleja "lo que paga
  el mercado", pero depende de tener **comparables buenos**.
- **Enfoque de activos (*asset/cost approach*):** valúa por lo que la empresa **tiene** (sus activos netos)
  —valor en libros, de liquidación, de reposición—. Relevante para empresas **en crisis** (vale más muerta
  que viva) o ***asset-heavy*** (inmobiliarias, holdings), no para empresas operativas en marcha.

**Por qué el valor está "vivo" (depende de quién, cuándo y para qué).** Un punto crucial que el abogado debe
entender: **no existe "un" valor objetivo único** de una empresa. El valor depende de:
- **Para quién:** el valor *standalone* (por sí sola) vs. el valor para un **comprador estratégico** (con
  **sinergias**, vale más) vs. para un **comprador financiero** (PE, sin sinergias operativas).
- **Qué se compra:** el **control** vale más (prima de control) que una **minoría** (descuento por minoría);
  una participación **líquida** vale más que una **ilíquida** (descuento por iliquidez).
- **Cuándo:** el valor cambia con las **condiciones de mercado** (los múltiplos suben y bajan con el ciclo),
  las **tasas de interés** (afectan el WACC) y la **situación de la empresa**.
- **Para qué:** una valuación para **vender** (busca el valor más alto defendible), para **comprar** (el más
  bajo), para un **litigio** (el "justo"), para **fines fiscales** (el de mercado) —el propósito orienta el
  enfoque—.
*La lección:* cuando alguien te diga "esta empresa vale X", la pregunta del abogado experto es:
"**¿valor para quién, calculado cómo, con qué supuestos, y para qué propósito?**". Esa pregunta revela si el
número es sólido o conveniente.

### 14.B · El DCF (el método rey: flujos, valor terminal, WACC)

El **DCF (flujo de efectivo descontado)** es el método **más sólido conceptualmente** y la base de toda la
valuación, porque captura la idea fundamental: **una empresa vale el valor presente del efectivo que
generará en el futuro**. Domina su lógica (no para calcularlo como banquero, sino para **entenderlo y
cuestionarlo**).

**Los tres componentes del DCF.**
1. **La proyección de los flujos de efectivo libres (*Free Cash Flow*).** Se **proyecta** el efectivo que
   la empresa generará en los próximos **5-10 años** (el "periodo explícito"). El flujo de efectivo libre =
   EBITDA − impuestos − CapEx (inversión) − cambios en capital de trabajo (lo que de verdad queda para los
   proveedores de capital). *Aquí está la primera fuente de manipulación:* las proyecciones dependen de
   **supuestos** (crecimiento de ventas, márgenes, inversión) que pueden ser **realistas o heroicos**.
   Proyecciones optimistas → valor inflado.
2. **El valor terminal (la parte más grande y más sensible).** La empresa no "termina" al final del periodo
   de proyección: sigue generando flujos "a perpetuidad". El **valor terminal** captura ese valor más allá
   del periodo explícito, de dos formas: **(i) crecimiento a perpetuidad** (los flujos crecen a una tasa
   constante "para siempre" —método de Gordon—); o **(ii) múltiplo de salida** (aplicar un múltiplo
   EV/EBITDA al EBITDA del último año). *Dato crucial:* el valor terminal suele ser **la MAYOR parte** del
   valor total del DCF (60-80%) —y es **muy sensible** a sus supuestos (la tasa de crecimiento perpetuo, el
   múltiplo de salida)—. Por eso el DCF se puede "mover" mucho ajustando el valor terminal.
3. **La tasa de descuento (el WACC).** Los flujos futuros se **descuentan** al **WACC** (costo promedio
   ponderado de capital —Libro 2—), que refleja el **riesgo** y el **costo de oportunidad**. *Tercera fuente
   de sensibilidad:* una tasa de descuento **más baja** → **mayor** valor presente → valor inflado; una más
   alta → menor valor. Pequeños cambios en el WACC mueven mucho el valor.

**La fórmula conceptual (sin tecnicismos):**
```
Valor (EV) = VP de los flujos del periodo explícito + VP del valor terminal
   (todo descontado al WACC)
   Luego: Equity Value = EV − deuda neta
```

**Las fortalezas del DCF.**
- Es **conceptualmente el más correcto:** valúa por los **fundamentos** (la capacidad de generar efectivo),
  no por comparación o por lo que la empresa tiene.
- Es **flexible:** permite modelar distintos escenarios (optimista, base, pesimista) y entender qué
  **mueve** el valor.
- **No depende de comparables** (útil cuando no hay empresas o deals verdaderamente comparables).

**Las debilidades del DCF (lo que el abogado debe cuestionar).**
- **"Basura entra, basura sale" (*garbage in, garbage out*):** el DCF es tan bueno como sus **supuestos**.
  Proyecciones infladas, valor terminal optimista o WACC bajo producen un valor inflado **que parece
  riguroso** (la precisión matemática **disfraza** la incertidumbre de los supuestos).
- **El valor terminal domina:** como es la mayor parte del valor y la más sensible, el DCF puede
  "construirse" para llegar al número deseado ajustándolo.
- **Sensibilidad a la tasa:** pequeños cambios en el WACC mueven mucho el valor.
*Por eso el abogado experto, ante un DCF, pregunta:* ¿Las **proyecciones** son realistas (comparadas con el
desempeño histórico y la industria)? ¿El **valor terminal** usa supuestos razonables (tasa de crecimiento
perpetuo no mayor que la economía; múltiplo de salida de mercado)? ¿El **WACC** es defendible? Un **análisis
de sensibilidad** (cómo cambia el valor al variar los supuestos) revela qué tan "robusto" es el número.

**La lección.** El DCF es el método **más poderoso y más peligroso**: poderoso porque captura el valor
fundamental; peligroso porque su **apariencia de precisión** esconde la **enorme sensibilidad** a supuestos
que pueden manipularse. El abogado no construye el DCF (lo hace el banquero/valuador), pero debe
**entender sus tres componentes** y **cuestionar los supuestos** —porque ahí, en las proyecciones, el valor
terminal y el WACC, es donde se infla o se deprime el valor, y donde el abogado que entiende puede defender
a su cliente—.
