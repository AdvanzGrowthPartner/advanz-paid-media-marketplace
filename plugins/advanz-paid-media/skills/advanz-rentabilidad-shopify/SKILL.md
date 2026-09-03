---
name: advanz-rentabilidad-shopify
description: "Motor de rentabilidad 100% de una tienda Shopify que corre el equipo Advanz para ver, en minutos, de qué vive el margen y por dónde se fuga la plata. Conecta la tienda por MCP (Shopify + GA4/Meta/Google si están) y barre TODO —ventas netas, AOV, margen de contribución por producto (COGS), volumen vs margen, el producto-fuga, ROAS de equilibrio, recompra/LTV, descuentos y devoluciones que comen margen, mix y concentración— con criterio real (checklist + benchmarks) y reglas anti-falsos-positivos (sin COGS cargado NO inventa margen). Entrega el resultado en NARRATIVA para dueño (qué pasa · por qué · qué te cuesta · qué hacer), con el detalle técnico en anexo. Dos capas: motor interno del equipo y los entregables REPORTE (reporte 360) y MARGEN (calculadora de ROAS de equilibrio) que corre el propio prospecto. Úsala cuando digan: rentabilidad de Shopify, margen por producto, reporte 360, ROAS de equilibrio, breakeven, unit economics, dónde se fuga la plata en la tienda, qué producto me deja menos, REPORTE o MARGEN de Shopify, o al conectar el MCP de Shopify para analizar rentabilidad."
user-invokable: true
---

# Rentabilidad de Shopify (método Advanz · motor completo vía MCP)

Este es el motor que usa Advanz para leer la rentabilidad real de una tienda Shopify de
punta a punta en minutos. No es un checklist que se lee: **conecta la tienda, recolecta la
data, la evalúa con criterio y devuelve una historia** que cualquier dueño entiende — con
el detalle técnico disponible pero fuera del camino.

La pregunta que responde: **un ROAS alto no dice si ganas; lo dice tu margen.** Y casi
siempre el producto que más vende no es el que más margen deja — se escala el equivocado y
no se nota hasta fin de mes.

## Principio rector (no negociable)
Nada se inventa. Cada hallazgo se **deriva** de un dato real de la tienda (producto,
métrica, período citables). La IA/MCP estructura y acelera, **nunca origina**. El único
error irreversible en rentabilidad: **inventar un margen.** Si el costo del producto (COGS)
no está cargado, `gross_profit` viene vacío → se marca **"no verificado"** y se pide cargar
el costo, nunca se estima. Lee `references/reglas-anti-error.md` antes de reportar.

## Cobertura: el análisis es 100% o no es
Se evalúan TODAS las áreas. Ninguna se omite en silencio; si falta un dato (típico: COGS),
se marca **"no verificado"** y se dice por qué (diagnóstico de datos, Paso 5).

| Bloque | Qué cubre |
|---|---|
| Foto general | Ventas totales y netas, pedidos, AOV, ventana (90d) |
| Margen por producto | COGS cargado, ganancia bruta y margen de contribución $/% por SKU, ranking |
| Volumen vs margen | El cruce clave: top en unidades vs top en margen → el **producto-fuga** |
| ROAS de equilibrio | Margen de contribución → breakeven (1÷margen) y MER objetivo, contra el ROAS real de paid |
| Recompra / LTV | Ventas de clientes nuevos vs recurrentes, tasa de recompra, LTV:CAC (si hay CAC) |
| Descuentos | Descuento promedio por producto que se come el margen |
| Devoluciones | Tasa de devolución por producto (si el dato está) y su impacto en margen |
| Envío & fulfillment | Costo de envío vs cobrado, umbral de envío gratis vs margen |
| Mix & concentración | Pareto de ventas y de margen, dependencia de 1 SKU |
| Salud de datos | COGS faltante, moneda, período, fuentes conectadas |

El detalle de cada check (umbral pass/warning/fail, severidad, quick wins) vive en
`references/checklist-completo.md`. **Úsalo como criterio, no lo reinventes.**

## Paso 0 · Elegir capa
- **Motor interno (default):** análisis completo de rentabilidad para el equipo Advanz.
  Alimenta consultoría, reporte al cliente y la máquina de contenido (deja un hallazgo
  grabable: el producto-fuga, el ROAS de equilibrio real).
- **Entregable prospecto — REPORTE:** entrega `assets/entregable-REPORTE.md`, el prompt del
  reporte 360 para que el prospecto lo corra en su tienda (el "comenta REPORTE y te lo mando").
- **Entregable prospecto — MARGEN:** entrega `assets/entregable-MARGEN.md`, la calculadora de
  ROAS de equilibrio (unit economics), para auto-diagnóstico sin conectar nada.

## Paso 1 · Pre-flight (multi-fuente)
1. **Shopify (obligatorio):** confirmar MCP conectado; `get-shop-info` (nombre, dominio,
   **moneda**, timezone). La moneda importa: no se mezcla con el gasto de paid en otra moneda.
2. **COGS:** verificar si el costo por producto está cargado (Productos → variante → Costo, o
   `InventoryItem.unitCost` por GraphQL). Sin COGS no hay margen real — se declara, no se estima.
3. **GA4 / Meta / Google Ads (si están):** para cruzar el ROAS real de paid contra el ROAS
   de equilibrio (el MER). Sin ellos, se entrega el breakeven y se pide el ROAS real.
4. **Ventana:** 90 días por defecto (estabiliza recompra y estacionalidad). Si la tienda es
   nueva, usar el máximo disponible y decirlo.
5. Registrar qué fuentes quedaron conectadas → se reporta en "Salud de los datos".

## Paso 2 · Recolección
Corre el set de `references/queries-shopifyql.md` (cubre todas las áreas del bloque de
arriba). Respeta las notas: `gross_profit` sale del COGS cargado al momento de la venta —
si viene vacío o en cero para todo, el costo no está cargado (no es margen 0). Para el
detalle de costo actual por variante, usar el fallback GraphQL `InventoryItem.unitCost`.

## Paso 3 · Evaluación con criterio
Evalúa cada área contra el checklist (pass/warning/fail) y los benchmarks. Distingue
**dato medido de interpretación**. Aplica las heurísticas anti-falso-positivo (ej.: producto
"fuga" solo si está en el top de volumen **y** en el fondo de margen sobre un umbral de
ventas; recompra baja no es "malo" en categorías de compra única; margen negativo puede ser
un loss-leader intencional — se marca "a revisar", no "error").

## Paso 4 · Priorizar por plata en juego
Ordena TODO por plata en juego: cuánto margen se está dejando en la mesa o quemando. El
**producto-fuga** (alto volumen, bajo margen) suele ser el nº 1 — es capital de pauta
escalando el producto que menos deja. El ROAS de equilibrio convierte cada campaña en
"gana o pierde": sin el margen no hay veredicto, se reporta como "en revisión".

## Paso 5 · Output en NARRATIVA (el entregable principal)
Arma la salida siguiendo `references/narrativa-output.md`: titular en lenguaje de dueño (de
qué vive tu margen) → salud de rentabilidad (score + plata en juego) → resumen en 30
segundos → hallazgos contados como historia (qué pasa · por qué · qué te cuesta · qué hacer)
→ lo que está bien → el plan (3 movimientos) → **anexo técnico colapsable** (tabla de
productos, márgenes, datos crudos) → **salud de los datos** (COGS, moneda, qué quedó "no
verificado"). La historia va arriba; lo técnico, disponible pero sin pesar.

## Paso 6 · Cierre (según capa)
- **Motor interno:** entrega la narrativa + ofrece empaquetar el hallazgo principal en ficha
  de contenido (formato lean del Contenido SOP: fichas R1 ROAS de equilibrio / R2 reporte 360).
- **Entregable prospecto:** entrega `assets/entregable-REPORTE.md` o `entregable-MARGEN.md`
  en bloque copiable. **Nunca PDF.**

## Voz (cuando el output es para comunicar o para el dueño)
- **Español neutro (tú).** Sin voseo ni chilenismos.
- **Primera persona plural del método Advanz:** "Así leemos tu rentabilidad…", "Lo primero
  que miramos es de qué vive tu margen…".
- La **IA/MCP es el cómo**, nunca el titular. Prohibido "le pedí a una IA que…".
- Traduce lo técnico: ROAS → "retorno"; margen de contribución → "lo que te queda después de
  costo, envío y comisión"; breakeven → "el retorno mínimo para no perder". El héroe es el
  método y el hallazgo.

## Recursos
- `references/checklist-completo.md` — mapa de cobertura y criterio (áreas + umbrales).
- `references/queries-shopifyql.md` — set reproducible de consultas por área (ShopifyQL + GraphQL).
- `references/narrativa-output.md` — contrato del output en storytelling (+ ejemplo).
- `references/reglas-anti-error.md` — blindaje contra falsos positivos (COGS, moneda, loss-leader).
- `references/conexion-mcp.md` — conectar el MCP de Shopify (+ GA4/Meta/Google si están).
- `assets/entregable-REPORTE.md` — Capa 2: el reporte 360 que corre el prospecto.
- `assets/entregable-MARGEN.md` — Capa 2: la calculadora de ROAS de equilibrio.
- `assets/plantilla-reporte.html` — plantilla del dashboard branded de rentabilidad.
