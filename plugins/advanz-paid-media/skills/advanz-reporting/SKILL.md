---
name: advanz-reporting
description: >-
  Genera reportes de performance para clientes de Advanz (ecommerce DTC/B2C) en HTML branded, listos para
  compartir con el cliente. Usa SIEMPRE que el usuario diga "reporte de cierre de mes", "reporte de
  performance", "cierre de [cliente]", "reporte mensual", "reporte de [evento/campaña]", "armá el reporte",
  "actualizá el reporte con la matriz", o pegue una matriz de performance y pida un reporte; también cuando
  pida sumar canales (Meta, Google, Email/Klaviyo, SEO/GA4), creativos, comparativas mes-a-mes o año-a-año,
  funnel, productos o clientes nuevos vs recurrentes. Cubre cierres mensuales y reportes de evento/campaña.
  SOLO ecommerce DTC/B2C. Es marca-agnóstica: el motor y el estándar no cambian, cambia el mapa de cuentas
  del cliente. Amazing Care (amazingcare.cl) es el primer caso validado.
metadata:
  type: reporting
---

# Advanz Reporting — Reportes de performance para cliente

Motor estándar para producir el **reporte de performance que Advanz comparte con el cliente**: cierre de mes
o reporte de evento/campaña. Un solo HTML branded, autocontenido, simple y escaneable.

La regla de oro: **el reporte es para el CLIENTE, no para el analista.** Si algo no aporta a una decisión o
no se entiende de un vistazo, no va. Preferí menos secciones bien contadas que un tablero exhaustivo.

## Antes de arrancar — confirmá 3 cosas
1. **Tipo:** cierre de mes o reporte de evento/campaña (cambia la ventana y las comparativas).
2. **La matriz:** pedí la matriz de performance actualizada del cliente. Es la **fuente de verdad** de
   inversión y conversiones por canal. No armes el reporte sin ella.
3. **Comparativa:** mes-a-mes siempre; año-a-año (YoY) si hay data — controla estacionalidad y es la lectura
   más honesta de "cómo venimos". Ver `references/estructura.md`.

## Principios no negociables (los que más se piden corregir)
Estos cuatro son la causa del 90% de las iteraciones. Internalizalos antes de escribir una línea:

- **Marco neutral-growth.** NUNCA asumir resultados buenos ni malos, NUNCA echar culpas ni responsabilidades.
  Cada dato = **hecho objetivo + señal + próximo paso**. Prohibido "mejor mes", "fuerte", "rentable", "sano",
  "cuello de botella", "el problema es", "no llega/no mandan". Ver `references/tono-voz.md`.
- **Español neutro.** Sin voseo ("tenés/querés" → "tienes/quieres") y sin chilenismos/localismos ("asado",
  "fondas", "cueca", "plata", "acá"). Es para compartir con cliente.
- **Sin tecnicismos.** Traducí la jerga a lenguaje de negocio: ROAS→"retorno", CPA→"costo por venta",
  AOV→"ticket promedio", MER→"retorno total", impression share→"cuánto de la búsqueda capturamos", CTR, funnel
  →"recorrido de compra". Glosario en `references/tono-voz.md`.
- **Simple y escaneable.** Tesis/titular arriba (el lector se lleva la idea en 5 segundos), datos en tiles y
  tablas, reads de 1–2 frases, y **postura** en los próximos pasos (recomendación, no "hay una señal de que
  podría convenir"). No texto denso.

Y una regla de proceso de Advanz: **mostrá el borrador para validación antes de dar por final.** Iterá en el
chat; recién ahí guardás.

## Flujo
1. **Intake.** Confirmá tipo + pedí la matriz + definí comparativas y el mapa de cuentas del cliente
   (`references/datos.md`). Si el cliente no tiene mapa aún, levantá los IDs y guardalos en memoria.
2. **Traer data.** Tirá los MCPs en paralelo. Qué canal sale de dónde, exactamente, en `references/datos.md`.
3. **Cuadrar.** Cruzá la matriz con Shopify/plataformas. Si divergen, **la matriz manda** para el titular
   financiero y las conversiones; anotá la divergencia, no la escondas. Cuidado con las trampas de medición.
4. **Construir.** Usá `assets/plantilla.html` (design system Advanz) y la estructura de
   `references/estructura.md`. Embebé imágenes en base64 con el script (`references/design-system.md`).
5. **Validar y guardar.** Mostrá el borrador. Al aprobar, guardá en la carpeta del cliente con fecha
   (`YYYY-MM-DD_reporte-...html`) y una copia `-FINAL` para diferenciar de las de trabajo.

## Estructura del reporte (resumen)
El orden estándar, de mayor a menor jerarquía. Detalle bloque por bloque en `references/estructura.md`.

1. **El mes en una mirada** — tesis arriba + 5-6 KPIs de la matriz.
2. **Cómo venimos** — mes-a-mes + año-a-año, con la lectura escala vs. eficiencia.
3. **De dónde vino la venta** — canales por rol: Meta, Google, Email, SEO/orgánico + cuota en búsqueda.
4. **Campañas y anuncios** — tabla de campañas + los mejores anuncios con su captura (miniatura).
5. **Qué se vendió** — top productos con foto.
6. **Comportamiento en la tienda** — funnel + nuevos vs recurrentes.
7. **Contenido** — qué entró, qué rinde, fatiga y volumen vs. competencia.
8. **Próximos pasos** — 3-4 focos con postura + decisiones/hipótesis a validar con el cliente.

No todos los reportes llevan los 8. Para evento: foco en resultados del evento, código/promo, canales,
creativos y proyección. Ajustá según el tipo, pero mantené el orden de jerarquía.

## Reglas de datos (resumen)
- **Matriz** = inversión y **conversiones por canal** (Meta/Google/Email/…) + venta neta, ticket, CAC, ROAS.
  Es el titular financiero.
- **Plataformas** (Meta, Google) = KPIs de medios (alcance, CTR, CPC, frecuencia, impression share, ROAS por
  campaña/anuncio). NO uses las conversiones de plataforma como oficiales — esas salen de la matriz.
- **Shopify** = tienda: ventas, funnel, productos, nuevos vs recurrentes, códigos de descuento.
- **Klaviyo** = email: campañas + flujos + KPIs (revenue influido, open rate). Atribución propia → "influyó".
- **GA4** = orgánico/canales e intención. Es el proxy de SEO mientras no haya Search Console.
- **Meta Ad Library** = volumen de anuncios activos vs. competencia (para la fatiga/volumen).
Detalle, IDs y gotchas de medición en `references/datos.md`.

## Design system y entrega
Plantilla y componentes en `assets/plantilla.html`; cómo usarlos, embeber imágenes y entregar en
`references/design-system.md`. En una línea: HTML branded Advanz (Poppins + Space Grotesk, violeta+cyan),
imágenes **embebidas en base64** (autocontenido), guardado **local** en la carpeta del cliente (NO como
Artifact), y enviado como archivo.

## Gotchas que ahorran vueltas
- La matriz y Shopify **divergen** (Shopify last-click vs. matriz reconciliada). Matriz manda; Shopify solo
  para el detalle operativo (funnel, productos, clientes).
- **Email (Klaviyo)** se solapa con otros canales → siempre "influyó en $X", nunca sumado a la venta total.
- **Meta** suele estar en **USD** ≠ CLP de la tienda; convertí (FX ≈ 1.000 CLP/USD salvo dato mejor) y avisalo.
- **Search Console** hoy no está por MCP → SEO se mide con GA4; dejalo anotado como pendiente.
- **Retail / marketplaces**: si el cliente invierte en retail media + marketplaces + pauta, puede haber
  canibalización. Se plantea como **hipótesis a validar con el cliente**, nunca como afirmación.
- El **techo de CAC** solo se menciona si el cliente lo pide (puede leerse como juicio).
