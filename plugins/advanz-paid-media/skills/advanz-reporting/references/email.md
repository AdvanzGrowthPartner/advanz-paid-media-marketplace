# Módulo CORREO / EMAIL — reporte de performance de Klaviyo

Reporte del canal de correo para el cliente. Dos motores distintos con métricas y conclusiones propias:
**envíos de campaña (spot)** y **flujos automáticos**. Estándar común (tono, diseño, entrega) en `SKILL.md`.

## Antes de arrancar
1. **Tipo:** cierre de mes o evento/campaña.
2. **Mapa de cuentas del cliente** (ver §Fuentes). Confirmá la métrica de conversión ("Placed Order").
3. **Método = send-time** (fecha de envío), **RPR = ventas ÷ destinatarios**. Es lo que usa la grilla de
   correos del equipo; los per-envío suman al total del canal. NO mezclar con event-time (ver §Gotchas).

## Los dos motores (no mezclar)
- **Envíos spot (campañas):** correos manuales a la base — a **no-compradores** (conversión) y **compradores**
  (recompra). Buscan venta directa. Se miden por RPR, CTOR, conversión/apertura, ticket y **tipo de correo**.
- **Flujos automáticos:** se disparan solos por comportamiento; **se alimentan del tráfico de ads + orgánico**
  (una persona llega por un anuncio/búsqueda, abandona carrito o se suscribe, y el flujo la recupera). Por eso
  su volumen depende de la inversión en medios → **cruce con el reporte de paid**. Rinden mucho más por
  contacto que un envío masivo.

## Estructura del reporte (7 bloques)
1. **Resultados del mes** — KPIs primero (bien espaciados): **Ventas totales atribuidas (Klaviyo)**, N° de
   ventas (pedidos) + ticket promedio, ventas de campañas, ventas de flujos, retorno por envío (RPR),
   apertura promedio (estable/rango), nuevos suscriptores. Después una **caja de tesis** destacada.
2. **Cómo venimos** — barras **apiladas campañas+flujos últimos 6 meses** (send-time) + **agosto año contra
   año** (2 barras). Conclusiones con color + Advanz/Cliente.
3. **Captación (pop-up)** — VA ANTES DE CAMPAÑAS. Embudo **vieron → registraron → suscribieron → compraron
   (ticket)** + **tabla de formularios de registro** uno por uno (vistas, registros, tasa, heatmap). El
   mobile/web y el origen paid/orgánico se cruzan con Klaviyo forms UI / GA4 / paid.
4. **Correos de campaña** — KPIs (ventas, envíos **X / 12** con la regla **8 spot + 4 evento**, CTOR,
   conversión/apertura, RPR). **Torta** del mix por tipo (leyenda a la derecha). **Cohorte horario**
   (día×hora, mapa de calor por RPR) con las mejores ventanas. **Tabla por tipo** con envíos, alcance,
   **ventas (n°), ticket, ventas ($), RPR** (heatmap en ventas$ y RPR).
5. **Los correos: qué vendió cada uno** — vista de **decisión**, no de galería: por correo/campaña →
   **cuánto vendió + veredicto (✅ bueno / ⚠️ mejorar / ❌ malo) + prioridad para el próximo mes** + qué
   producto movió. La lógica: "mandamos un correo de X producto/campaña → ¿qué vendió?". Barra de productos.
6. **Flujos automáticos** — **en orden 1 Bienvenida · 2 Carrito · 3 Post-compra · 4 Recompra** + carritos de
   evento (Flash/Cyber). Tabla con **secuencias, estado, alcance, ventas (n°), ticket, ventas ($), RPR**
   (heatmap). **Tendencia de flujos últimos meses** + **gauge de participación (meta 25–30%)**. "Qué ajustar"
   en 4 bloques ilustrados. Cerrar con la **oportunidad de ecosistema** (ver §Ecosistema).
7. **Próximos pasos & proyección** — bloques ilustrados (no texto): grilla 8+4, reactivar bienvenida, ajustar
   la grilla existente, proyección. Incluir ajuste de la grilla del próximo mes según lo aprendido.

## Taxonomía de campañas (de la Grilla de Correos del cliente)
Categorizá cada envío: **Evento + oferta** (mayor RPR — evento con % explícito), **Producto** (contenido de
un producto ancla), **Contenido** (educativo; vende con día/hora/segmento correctos), **Retail** (empuja a
punto de venta: Jumbo/Tottus/Cruz Verde — no venta web, RPR bajo por diseño), **Marca** (institucional, sin
razón de compra directa). Reglas de la grilla: la base aguanta **6–8 spot/mes** (con 9–11 el revenue cae);
evento+descuento concentra ~57% del revenue; el asunto mueve clic/venta, no apertura.

## Los 4 flujos (ecosistema)
Recorrido: **Bienvenida (capta) → Carrito abandonado (recupera) → Post-compra (fideliza) → Recompra (2ª
venta)**. Todos deben estar activos.
- **Bienvenida** — trigger alta a lista del pop-up; ~3 correos. Suele ser la mayor palanca si está entregando
  parcial.
- **Carrito abandonado** — trigger Checkout Started; ~4 correos; normalmente el **más rentable por contacto**.
- **Post-compra** — trigger Placed Order; **fideliza (cuenta qué hace la marca), por diseño NO busca venta
  nueva** → una apertura alta con $0 es esperable, no una falla.
- **Recompra** — trigger post-compra a ciclo (30/60/90 días); volumen sube con la base de compradores.
- Carritos de **evento** (Flash/Cyber) se encienden por campaña. El circuito de **códigos** (tipo Nutrikit,
  tag NO USAR) es operativo/transaccional → **excluir del consolidado comercial**.

### §Ecosistema — la oportunidad a comentar
El eslabón con más espacio suele ser el paso de **fidelización a venta**: sumar al post-compra un módulo de
**reposición por consumo** ("se te está acabando", día 30–45 según el producto) y **cross-sell** (compró
electrolitos → ofrecer Fibra/Energy) convierte el post-compra en motor de la 2ª compra sin perder el
contenido de marca. Meta: llevar los flujos del aporte actual hacia **25–30% del canal**.

## Fuentes (MCP Klaviyo) — send-time salvo que se indique
| Dato | Herramienta | Notas |
|---|---|---|
| Métrica de conversión | `get_metrics` | "Placed Order" (Shopify). Amazing Care: `RP5iQ9`. |
| Campañas del mes (por campaña) | `get_campaign_report` | `group_by:["campaign_id","campaign_message_name","send_channel"]`, `filters: equals(send_channel,"email")`, stats + `value_statistics:[conversion_value,average_order_value,revenue_per_recipient]`. `send_time`/audiencias vienen en `campaign_details`. |
| Total mes / tendencia (por mes) | `get_campaign_report` + `get_flow_report` por mes | Un call por mes con `group_by:["send_channel"]` (campañas) y `["flow_id","flow_name","send_channel"]` (flujos), sumás. Es la forma consistente de la tendencia 6-meses. |
| Flujos del mes | `get_flow_report` | `flow_aggregation` da el total por flujo. Excluir tag "NO USAR". |
| Lista de flujos + estado + trigger | `get_flows` | `fields:["name","status","trigger_type","archived"]`. |
| Contenido del correo (asunto/preview/plantilla) | `get_campaigns`(include campaign-messages) → `get_email_template` | Para prints: el hero sale de `<img>` del template HTML (CDN Klaviyo `d3k81ch9...`). |
| Captación (formularios) | `query_metric_aggregates` | "Viewed Form" `SQLn6z` y "Submitted Form" `WrC97x`, `by:["form_id"]`, count → vistas/registros/tasa por formulario. |
| Suscriptores nuevos | `query_metric_aggregates` | "Subscribed to Email Marketing" `QYLKnd`, count, mensual. |
| Tendencia de canal (contexto) | `query_metric_aggregates` | "Placed Order" `by:["$attributed_channel"]` (email) o `["$attributed_flow"]`. **Event-time** → solo forma, no mezclar con send-time. |

**Mapa de cuentas — Amazing Care (validado):** Klaviyo métricas: Placed Order `RP5iQ9`, Viewed Form `SQLn6z`,
Submitted Form `WrC97x`, Subscribed Email `QYLKnd`. Flujos: Welcome_AON `S8bwJx`, Carritos_AON `RCsVZf`,
Postcompra `QQjgEa`, Recompra_AON `VNCVuB`, Flash `TXdmwz`, Cyber `QSHsP9`, Nutrikit `SrbL9b`/`R8UBbY` (NO USAR).
Para un cliente nuevo: levantar estos IDs y guardarlos en `<cliente>_account_map`.

## Métricas y fórmulas
- **RPR** (retorno por envío / contacto) = ventas ÷ destinatarios. **CTOR** = clics ÷ aperturas. **Conversión
  sobre apertura** = conversiones ÷ aperturas. **Ticket promedio** = ventas ÷ n° de pedidos (AOV).
- **Aporte de flujos** = ventas de flujos ÷ ventas totales del canal. Referencia sana: 25–40%.
- **Cadencia:** X envíos / 12 (techo contractual 8 spot + 4 evento). "En rango" si ≤ techo y ≥ 6.

## Gotchas de medición
- **Send-time vs event-time:** el reporte usa **send-time** en todo (headline, tablas, tendencia) para que las
  partes sumen al total y coincida con la grilla. `query_metric_aggregates` es **event-time** (mes de venta):
  sirve para la forma de una tendencia larga, NO para números que deban cuadrar con el detalle. Si usás ambos,
  aclaralo en una nota.
- **Flujos ≠ campañas:** repórtalos separados; el aporte de flujos se lee aparte.
- **Circuito de códigos** (Nutrikit / NO USAR): transaccional, excluir del comercial.
- **Prints de correos:** si el CDN de Klaviyo/Shopify está bloqueado por el sandbox, reconstruí la pieza con
  el asunto/oferta/precio reales (embebido) o referenciá la URL; el pantallazo pixel-perfect se embebe desde
  una máquina con acceso al CDN.
- **Mobile/web y origen del suscriptor** (paid vs orgánico): no salen de estos endpoints → cruce con la
  pestaña de formularios de Klaviyo / GA4 / reporte de paid.

## Entrega
1. Preview de validación (Artifact) para iterar en el chat.
2. Al aprobar: `-FINAL` local + **Notion**: subir el `.html` con `notion-create-file-upload` a la página de
   cierre del cliente; si el entorno bloquea la subida, insertar un **resumen nativo** con
   `notion-update-page` (TL;DR + KPIs + conclusiones + próximos pasos + ecosistema) y dejar el HTML para
   adjuntar a mano.
