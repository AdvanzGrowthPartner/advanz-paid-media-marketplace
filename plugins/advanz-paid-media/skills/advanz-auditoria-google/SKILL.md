---
name: advanz-auditoria-google
description: "Motor de auditoría 100% de Google Ads (performance + técnica) que corre el equipo Advanz para auditar cuentas en minutos. Conecta la cuenta por MCP (Google Ads + GA4 + Merchant/Shopify si están) y barre TODO —estructura, campañas, grupos, keywords, términos de búsqueda, anuncios, copies, imágenes, sitelinks y assets, pujas, presupuestos, atribución, configuración de conversiones, PMax, productos/feed— con criterio real (80+ checks, benchmarks, scoring) y reglas anti-falsos-positivos. Entrega el resultado en NARRATIVA para dueño (qué pasa · por qué · qué te cuesta · qué hacer), con el detalle técnico en anexo. Dos capas: motor interno del equipo y el entregable AUDITORÍA que corre el propio prospecto. Úsala cuando digan: auditar Google Ads, auditoría de Google, revisar/diagnosticar una cuenta de Google Ads, puntos de fuga, dónde se va la plata en Google, AUDITORÍA de Google, reporte de Google Ads, o al conectar el MCP de Google Ads."
user-invokable: true
---

# Auditoría de Google Ads (método Advanz · motor completo vía MCP)

Este es el motor que usa Advanz a diario para auditar una cuenta de Google Ads de punta
a punta en minutos. No es un checklist que se lee: **conecta la cuenta, recolecta la data,
la evalúa con criterio y devuelve una historia** que cualquier dueño entiende — con el
detalle técnico disponible pero fuera del camino.

## Principio rector (no negociable)
Nada se inventa. Cada hallazgo se **deriva** de un dato real de la cuenta (campaña,
métrica, período citables). La IA/MCP estructura y acelera, **nunca origina**. Un falso
positivo —decir que algo está mal cuando está bien— es el único error irreversible:
**ante la duda, NO se reporta.** Lee `references/reglas-anti-error.md` antes de reportar.

## Cobertura: la auditoría es 100% o no es
Se evalúan TODAS las áreas. Ninguna se omite en silencio; si falta acceso a un dato, se
marca **"no verificado"** y se dice por qué (diagnóstico de datos, Paso 5).

| Bloque | Qué cubre |
|---|---|
| Estructura | Naming, nº de campañas por objetivo, marca vs no-marca, PMax presente, solape Search↔PMax |
| Wasted spend | Términos de búsqueda, negativas (listas + account level), cola 0-conv, close variants |
| Keywords & QS | Match types, Quality Score y sus 3 componentes, canibalización, 0-impresiones |
| Anuncios & assets | RSA (nº titulares/descripciones, ad strength, pinning), sitelinks, callouts, snippets, imágenes, PMax asset groups (imágenes/logos/video), copies vs keyword |
| Pujas | Estrategia por madurez, tCPA/tROAS razonable vs breakeven, learning phase, ECPC (deprecado) |
| Presupuestos | Campañas topadas, impression share perdido (presupuesto vs ranking), asignación por prioridad |
| Settings & targeting | Ubicaciones, dispositivos, calendario, redes/partners, audiencias, customer match, exclusiones |
| Conversiones/tracking | Acciones primarias vs secundarias, dedup, enhanced conversions, atribución, ventana, consent mode, GA4 link |
| PMax | Asset groups, señales, search themes, exclusiones de marca, canibalización de marca, negativas |
| Productos / feed | Rendimiento por producto (ROAS por SKU), estado del feed y desaprobaciones (GMC/Shopify si están) |
| Landing | Relevancia y velocidad (si hay acceso a la URL) |

El detalle de cada check (umbral pass/warning/fail, severidad, quick wins) vive en el
checklist canónico de 80+ puntos: `references/checklist-completo.md`, que apunta a
`../ads/references/google-audit.md`, `../ads/references/benchmarks.md`,
`../ads/references/scoring-system.md`, `conversion-tracking.md`, `bidding-strategies.md`
y `budget-allocation.md`. **Úsalos como criterio, no los reinventes.**

## Paso 0 · Elegir capa
- **Motor interno (default):** auditoría completa para el equipo Advanz. Alimenta
  consultoría, reporte al cliente y la máquina de contenido (deja un hallazgo grabable).
- **Entregable prospecto:** entrega `assets/entregable-AUDITORIA.md`, para que el propio
  prospecto la corra en su cuenta (el "escríbeme AUDITORÍA y te lo mando").

## Paso 1 · Pre-flight (multi-fuente)
1. **Google Ads (obligatorio):** confirmar MCP conectado; `customers_list_accessible_customers`;
   elegir customer ID (mapear el nombre del cliente si lo dan).
2. **GA4 (analytics-mcp, si está):** para discrepancia de conversiones y comportamiento.
3. **Merchant Center / Shopify (si están):** para estado de feed, precios y oferta legible.
4. **Ventanas:** performance ≥ 30 días; términos de búsqueda `LAST_30_DAYS` (límite GAQL);
   lecturas por producto en PMax **≥ 60–90 días** (a 30d la atribución viene fraccionada).
5. Registrar qué fuentes quedaron conectadas → se reporta en "Salud de los datos".

## Paso 2 · Recolección
Corre el set de `references/queries-gaql.md` (cubre todas las áreas del bloque de arriba).
Respeta las notas de compatibilidad: `search_term_view` no admite `campaign.status`
(filtrar en aplicación); dedup de keywords por (ad_group + texto + match type); métricas
de impression share en query aparte; no usar `LAST_90_DAYS` con `DURING` en search terms.
Ver `../ads/references/gaql-notes.md`.

## Paso 3 · Evaluación con criterio
Evalúa cada área contra el checklist (pass/warning/fail) y los benchmarks. Distingue
**dato medido de interpretación**. Aplica las heurísticas anti-falso-positivo (ej.: BROAD
+ Manual CPC = BMM legacy, no falla; term "wasted" solo si >umbral de gasto y 0 conv;
atribución modelada/fraccionada se marca "a revisar", no veredicto).

## Paso 4 · Priorizar por plata en juego
Ordena TODO por plata en juego (gasto recuperable / valor perdido). El gasto recuperable
es **estimación con aritmética a la vista** — y necesita el **ROAS de equilibrio**: si no
se tiene el margen/breakeven, pídelo; sin él, se reporta como "gasto en revisión", nunca
como ganancia asegurada.

## Paso 5 · Output en NARRATIVA (el entregable principal)
Arma la salida siguiendo `references/narrativa-output.md`: titular en lenguaje de dueño →
resumen en 30 segundos → hallazgos contados como historia (qué pasa · por qué · qué te
cuesta · qué hacer) → lo que está bien → el plan (3 movimientos) → **anexo técnico
colapsable** (los 80 checks, tablas, datos crudos) → **salud de los datos** (qué se
conectó y qué quedó "no verificado"). La historia va arriba; lo técnico, disponible pero
sin pesar.

## Paso 6 · Cierre (según capa)
- **Motor interno:** entrega la narrativa + ofrece empaquetar el hallazgo principal en
  ficha de contenido (formato lean del Contenido SOP).
- **Entregable prospecto:** entrega `assets/entregable-AUDITORIA.md` en bloque copiable.
  **Nunca PDF.**

## Voz (cuando el output es para comunicar o para el dueño)
- **Español neutro (tú).** Sin voseo ni chilenismos.
- **Primera persona plural del método Advanz:** "Así auditamos…", "Lo primero que revisamos…".
- La **IA/MCP es el cómo**, nunca el titular. Prohibido "le pedí a una IA que…".
- Traduce lo técnico: nada de jerga sin explicar. El héroe es el método y el hallazgo.

## Recursos
- `references/checklist-completo.md` — mapa de cobertura y criterio (80+ checks).
- `references/queries-gaql.md` — set reproducible de consultas por área.
- `references/narrativa-output.md` — contrato del output en storytelling (+ ejemplo).
- `references/reglas-anti-error.md` — blindaje contra falsos positivos.
- `references/conexion-mcp.md` — conectar Google Ads + GA4 + Merchant/Shopify.
- `assets/entregable-AUDITORIA.md` — Capa 2: el paquete para el prospecto.
