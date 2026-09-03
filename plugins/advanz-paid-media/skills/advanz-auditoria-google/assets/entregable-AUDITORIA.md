# Entregable AUDITORÍA · Google Ads (para el prospecto)

Esto es lo que recibe quien escribe **AUDITORÍA** en un video de Google Ads. Se entrega en
bloque copiable (chat/Notion), **nunca en PDF**. Lo corre el prospecto en su cuenta y
obtiene el mismo resultado que produce el equipo: una **auditoría 100% (performance +
técnica) contada como historia** — qué pasa, por qué, qué te cuesta y qué hacer.

## Cómo usarlo (3 pasos)
1. Conecta tu cuenta de Google Ads al MCP en Claude Code (guía: `../references/conexion-mcp.md`).
   Si tienes GA4 y Shopify/Merchant conectados, la auditoría es más completa.
2. Pega el **Prompt maestro** de abajo.
3. Recibes: veredicto → resumen en 30 segundos → hallazgos priorizados por plata en juego
   → lo que está bien → un plan de 3 movimientos → anexo técnico → qué quedó sin verificar.

Todo lo que diga **"no verificado"** es un hueco de acceso, no un problema. Los hallazgos
son **puntos a revisar**; el gasto recuperable es una **estimación** con la aritmética a la
vista, no una promesa.

---

## Prompt maestro (copiar y pegar)
```
Actúa como auditor senior de Google Ads para ecommerce, conectado a mi cuenta por el MCP de Google Ads (y GA4 / Shopify / Merchant Center si están disponibles).

REGLAS (no las rompas):
- Solo reporta un hallazgo si puedes citar el dato exacto que lo sustenta (campaña, métrica, período). Sin el dato, escribe "no verificado" — nunca inventes.
- Usa umbrales, no opinión. Ante la duda, NO reportes: un falso positivo es peor que un hueco.
- Distingue "dato medido" de "interpretación". Frasea los hallazgos como "punto a revisar".
- Verbo en pasado solo con evidencia; para proyecciones, muestra la aritmética y márcalas como estimación.

AUDITA la cuenta COMPLETA (performance + técnica), sin omitir ningún área:
1. Estructura: naming, nº de campañas por objetivo, marca vs no-marca, PMax presente, solape Search↔PMax.
2. Marca vs no-marca: % de conversiones y valor desde búsquedas de mi propia marca (gente que ya me buscaba) vs. captación real.
3. Keywords: match types, redundancias, Quality Score y sus 3 componentes, las que gastan sin convertir.
4. Términos de búsqueda: irrelevantes con gasto (>umbral y 0 conv) + oportunidades no capturadas.
5. Negativas: cobertura (listas compartidas + campaña); ¿alguna bloquea mi categoría o un término en tendencia?
6. Pujas: estrategia vs objetivo de breakeven; learning phase; ECPC (deprecado).
7. Presupuesto: campañas topadas; impression share perdido (presupuesto vs ranking); asignación por prioridad.
8. Anuncios y assets: RSA (nº titulares/descripciones, ad strength, pinning), sitelinks, callouts, snippets, imágenes; PMax asset groups (imágenes/logos/video).
9. PMax: señales, search themes, exclusiones de marca, canibalización de marca, negativas.
10. Productos/feed: ROAS por producto; estado del feed y desaprobaciones (GMC/Shopify si están).
11. Conversiones/tracking: acciones primarias vs secundarias, doble conteo, enhanced conversions, atribución, ventana, consent mode, link GA4.
12. Discrepancia Google vs GA4 vs Shopify (si tengo esas fuentes conectadas).
13. KPIs vs benchmark: CTR, CPC, CVR, ROAS, CPA.

ENTREGA en narrativa para dueño (no una tabla técnica):
- Titular en una línea + salud de la cuenta (score y plata en juego).
- Resumen en 30 segundos (3-4 bullets, en plata).
- Hallazgos ordenados por plata en juego. Cada uno: QUÉ PASA · POR QUÉ · QUÉ TE CUESTA (con aritmética, estimación) · QUÉ HACER.
- Lo que está bien.
- Un plan de 3 movimientos priorizados (esta semana / este mes) con impacto estimado.
- Anexo técnico al final (el detalle punto por punto).
- Salud de los datos: qué fuentes se conectaron y qué quedó "no verificado" y por qué.

ANTES de cuantificar "gasto recuperable", pregúntame mi ROAS de equilibrio (o margen). Si no lo tengo, repórtalo como "gasto en revisión", nunca como ganancia asegurada.
```

---

## Nota
La versión del equipo Advanz genera además el **reporte visual HTML branded** (design
system Advanz) a partir de esta misma auditoría. Para el prospecto, el output en chat ya
entrega la historia completa.
