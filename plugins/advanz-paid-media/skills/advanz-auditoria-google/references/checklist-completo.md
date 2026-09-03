# Checklist completo (mapa de cobertura y criterio)

La auditoría es 100% o no es. El criterio canónico (umbral pass/warning/fail, severidad,
quick wins) NO se reinventa aquí: vive en el checklist de 80+ puntos del plugin. Este
archivo mapea las áreas a su fuente y agrega los ángulos propios de Advanz.

## Fuente canónica (usar como criterio)
- `../ads/references/google-audit.md` — los 80+ checks (G01–G61 + PMax/AI/Demand Gen/CTV).
- `../ads/references/benchmarks.md` — benchmarks de ecommerce (CTR, CVR, ROAS, CPC, QS…).
- `../ads/references/scoring-system.md` — pesos por categoría y cálculo del Health Score 0–100.
- `../ads/references/conversion-tracking.md` — detalle de tracking/atribución.
- `../ads/references/bidding-strategies.md` — criterio de pujas por madurez/objetivo.
- `../ads/references/budget-allocation.md` — asignación y campañas topadas.
- `../ads/references/gaql-notes.md` — compatibilidades GAQL y anti-falsos-positivos.

## Cobertura por categoría (peso del score)
| Categoría | Peso | Checks |
|---|---|---|
| Conversiones / tracking | 25% | G42–G49, G-CT1..3, G-CTV1 |
| Wasted spend / negativas | 20% | G13–G19, G-WS1 |
| Estructura de cuenta | 15% | G01–G12 |
| Keywords & Quality Score | 15% | G20–G25, G-KW1/2 |
| Anuncios & assets | 15% | G26–G35, G-AD1/2, G-PM1..6, G-AI1, G-DG1..3 |
| Settings & targeting | 10% | G50–G61 |
| Pujas & presupuesto | (dentro de settings) | G36–G41 |

## Ángulos propios de Advanz (encima del checklist)
1. **Marca vs no-marca / incrementalidad.** No basta separar campañas (G05/G07): cuantificar
   qué % de conversiones y valor vienen de términos de marca (gente que ya te buscaba) vs.
   captación real, y leer el retorno mezclado a esa luz. Es el hallazgo comunicacional #1.
2. **Plata en juego como orden maestro.** Todo hallazgo se prioriza por gasto recuperable /
   valor perdido, con aritmética y ROAS de equilibrio (pedirlo si no está).
3. **Oferta legible / feed (GMC + Shopify).** Por qué un producto no sale "en oferta":
   casi nunca es config, es que el ahorro no califica. Cruce precio/feed cuando haya acceso.
4. **Discrepancia Google vs GA4 vs Shopify.** Cuadrar conversiones entre fuentes; si divergen,
   anotarlo, no esconderlo.
5. **Narrativa antes que tabla.** El resultado se cuenta como historia (ver `narrativa-output.md`).

## Regla de completitud
Ninguna categoría se omite en silencio. Lo que no se pueda verificar por falta de fuente
se reporta como **"no verificado"** con el motivo, en "Salud de los datos".
