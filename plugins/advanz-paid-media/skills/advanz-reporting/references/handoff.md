# Handoff — cómo este reporte alimenta a los agentes de ejecución

Esta skill **no termina en el HTML**. El reporte es la capa de *lectura*; su producto accionable es una
**lista de decisiones estructurada** que otras skills/agentes de ejecución (paid-ops, email/Klaviyo,
SEO/GEO, CRO, copy) pueden tomar y ejecutar sin volver a leer todo el reporte. Un reporte que no deja
acciones claras no está terminado.

## Regla
Cada **conclusión con color** y cada **próximo paso** del reporte se traduce en una o más **acciones**.
La acción es la unidad de handoff: la ve el cliente (en el HTML) y la consume el agente de ejecución
(en el sidecar). Las dos vistas salen de la misma lista — no se escriben dos veces.

## Qué se emite (además del HTML)
Un sidecar JSON junto al `.html`, con el mismo nombre: **`<cliente>-<canal>-<mes>.acciones.json`**
(ej. `amazing-email-agosto.acciones.json`). Es la interfaz con los agentes.

```json
{
  "cliente": "<slug>",
  "canal": "paid | email | seo",
  "periodo": "YYYY-MM",
  "tesis": "una frase — el titular del mes",
  "acciones": [
    {
      "id": "email-flujos-bienvenida",
      "owner": "advanz | cliente",
      "area": "flujos | campañas | captacion | creativos | puja | contenido | tecnico | producto | oferta",
      "accion": "reactivar el flujo de bienvenida (3 correos completos)",
      "porque": "la bienvenida pasó de $616k a $133k influidos; es la mayor palanca del canal",
      "evidencia": "flows_table + flow_trend",
      "prioridad": "alta | media | baja",
      "impacto_estimado": "acerca los flujos de 17% a ~25% del canal",
      "ejecuta": "advanz-klaviyo-flows"
    }
  ]
}
```

Campos:
- **owner** — `advanz` (lo ejecuta el equipo) o `cliente` (depende del cliente: ideas, oferta, marca,
  aprobaciones). Mapea 1:1 al split 🏢/🤝 del reporte.
- **evidencia** — qué gráfico/tabla lo respalda (nombre del chart o de la tabla). Ata la acción al dato:
  ningún ítem sin evidencia.
- **ejecuta** — el **slug de la skill/agente de ejecución** que puede tomarla (ver mapa abajo). Si ninguna
  aplica, `null` (queda como decisión humana). NUNCA se dispara la ejecución desde acá: la skill de
  reporting **propone**; un agente/orquestador decide y ejecuta.

## Mapa acción → agente de ejecución (por canal)
Genérico; ajustá los slugs a las skills instaladas en el plugin del cliente.

| Canal | area | Agente de ejecución (ejemplo) | Qué haría con la acción |
|---|---|---|---|
| Email | flujos | `advanz-klaviyo-flows` | Construir/reparar el flujo (bienvenida, carrito, post-compra, recompra). |
| Email | campañas | `advanz-klaviyo-campaigns` | Cargar la grilla del mes (8+4), asuntos, segmentos, horarios. |
| Email | captacion | `advanz-klaviyo-forms` | Ajustar pop-up: copy, oferta, trigger, mobile/web. |
| Paid | creativos | `advanz-creative-brief` / `advanz-video` | Briefear piezas del ángulo/etapa que falta. |
| Paid | puja / campañas | `advanz-meta-ops` / `advanz-google-ops` | Reasignar presupuesto, escalar lo eficiente, cortar fatiga. |
| SEO | contenido | `advanz-seo-content` | Cluster/pillar, briefs de las keywords con espacio. |
| SEO | tecnico | `advanz-seo-tech` | Core Web Vitals, indexación, schema. |
| SEO | GEO | `advanz-seo-geo-engine` | Mejorar citas en LLMs / AI Overviews. |
| Web | — | `advanz-cro` | Fuga del recorrido de compra detectada en el reporte. |

## Cómo se arma (proceso)
1. Al cerrar cada bloque del reporte, por cada conclusión/próximo paso agregá un ítem a la lista.
2. La **evidencia** es obligatoria — si no hay gráfico/tabla que lo sostenga, no es una acción, es una
   opinión (y no va).
3. Separá por **owner**: los `advanz` van a "🏢 Advanz ejecuta" + "ejecución inmediata"; los `cliente` a
   "🤝 Cliente ejecuta" (ideas, oferta, marca, estrategia global, aprobaciones).
4. Emití el sidecar JSON al lado del HTML. El HTML es para el cliente; el JSON, para el siguiente agente.
5. **La skill de reporting no ejecuta**: entrega el diagnóstico + la lista. Disparar la ejecución es rol de
   un agente/orquestador con la autorización correspondiente.
