# Estructura del reporte PAID / Negocio — bloque por bloque

Orden estándar, de mayor a menor jerarquía. Para cierre de mes van los 8; para evento se recorta (ver al
final). Cada bloque: qué muestra, de dónde sale, cómo se lee.

**Forma común (igual que email y SEO):** KPIs primero → **caja de tesis** → **gráficos, no listas** (del
motor `assets/report_charts.py`) → **conclusiones con color + split 🏢 Advanz / 🤝 Cliente** (máx. 2 líneas)
→ próximos pasos (Cliente vs. Advanz + ejecución inmediata) → **proyección al final, sección propia**.
Cada conclusión y próximo paso se vuelca al **handoff** (`references/handoff.md`). Charts: tendencia y
año-contra-año con `stacked`; roles de canal y productos con `hbars`; cuota de búsqueda con `speedo`; recorrido
de compra con `funnel`; tablas con heatmap **sutil** `hmt`; números en **CLP completo**.

## 1 · El mes en una mirada
- **Tesis** (una frase, arriba de todo): resume el mes y apunta al próximo salto. Ej.: "Agosto fue el mes de
  mayor facturación del año; el próximo salto no pasa por invertir más, sino por más contenido y mejor ticket
  en la web."
- **5–6 KPIs** (tiles) de la matriz: Facturación neta, Ventas, Retorno (ROAS) con su equilibrio, Ticket
  promedio, Inversión, Clientes nuevos. Cada KPI con su variación vs. mes pasado.
- Read corto (1–2 frases).
- **No mencionar márgenes** salvo que el cliente lo pida. No poner líneas ambiguas tipo "71% de las ventas"
  sin explicar qué significan.

## 2 · Cómo venimos
Dos comparativas lado a lado:
- **Mes a mes** (vs. mes anterior): "cómo nos fue este mes". Ojo: en meses con evento estacional siempre luce
  alto; aclararlo.
- **Año a año** (vs. mismo mes del año pasado): "cómo venimos como negocio". Controla estacionalidad. Es la
  lectura más honesta.
- Mostrá el **ROAS con números** (ej. "4,4 → 2,9"), no la palabra "estable".
- La lectura clave suele ser **escala vs. eficiencia**: al escalar inversión, el retorno por peso baja
  (rendimientos decrecientes: la demanda barata se agota primero y se entra a público más frío). Se presenta
  neutral + próximo paso: recuperar eficiencia sin frenar el volumen.

## 3 · De dónde vino la venta
Tabla de canales por **rol**, no lista de campañas:
- Google (demanda que ya existe), Meta (volumen/alcance), Email (base propia), SEO/orgánico (intención, gratis).
- Cada uno con su aporte (inversión + conversiones de matriz para pago; influencia para email; visitas para SEO).
- **Cuota en búsqueda**: dos "gauges" — cuánto capturamos en marca vs. en categoría genérica.

## 4 · Campañas y anuncios
- **Tabla de campañas** (Meta + Google): inversión, compras/conv, ROAS por campaña. Agrupá para que sea legible
  (no 12 filas). Conversiones a nivel canal = matriz; por campaña = plataforma (nota al pie).
- **Mejores anuncios**: 4–6 tarjetas con **miniatura (captura)**, ROAS, compras, CTR. Sacá el patrón (qué tipo
  de contenido rinde).

## 5 · Qué se vendió
- Top productos en **tarjetas con foto** (de Shopify): facturación bruta + órdenes; tendencia vs. mes anterior
  si aporta.
- Read: qué sostiene el ticket, qué sabor/categoría rota más, reactivaciones.

## 6 · Comportamiento en la tienda
- **Funnel** visual: visitas → carrito → pagar → compra, con % en cada paso (Shopify).
- **Nuevos vs. recurrentes**: barra split + tasa de recompra, vs. mes anterior.
- Read: dónde está la fuga y cómo conecta con CRO web.

## 7 · Contenido
- Qué entró (videos MELI/retail, UGC), qué rinde (oferta al frente convierte más).
- **Fatiga y volumen**: frecuencia (cuántas veces se vio cada anuncio) + anuncios activos propios vs.
  competencia (Meta Ad Library). Es, en el fondo, la palanca de eficiencia detrás del ROAS.
- Enfoque **estratégico** (ángulos, etapas del recorrido, públicos sin cubrir), no prescriptivo ("hacé X videos").

## 8 · Próximos pasos
Dos columnas, igual que los otros canales:
- **🏢 Advanz ejecuta** — 3–4 focos con **postura** (recomendación clara), ordenados por impacto:
  reasignación de presupuesto, escalar lo eficiente, cortar fatiga, piezas del ángulo/etapa que falta.
- **🤝 Cliente ejecuta** — **decisiones / hipótesis a validar** (estrategia de retail/marketplaces,
  presupuesto del próximo evento, oferta, prioridad comercial) — como preguntas, no afirmaciones.
- **Ejecución inmediata Advanz→Cliente** — lo que sale directo de los gráficos del mes.
- Cada ítem se vuelca al **handoff** con su evidencia y el agente de ejecución (`references/handoff.md`).

## 9 · Proyección (al final, sección propia)
Escenarios base vs. óptimo para el próximo período con la base del cálculo (ventas, ticket, inversión,
creativos necesarios). No va mezclada en próximos pasos: cierra el reporte.

## Variante: reporte de evento/campaña
Recortar a: Resumen del evento (vs. período previo del mismo largo) · Código/promo · Canales · Creativos ·
Contenido · Proyección al cierre del evento (base del cálculo + escenarios + qué necesitamos: ventas, ticket,
inversión, creativos). Misma jerarquía y mismo tono.
