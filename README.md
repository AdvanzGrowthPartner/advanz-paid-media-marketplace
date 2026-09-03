# Advanz Paid Media — Cowork Plugin

Marketplace privado de Advanz Growth Partner con el toolkit completo del equipo: paid ads, CRO, SEO, lifecycle, copy, research, video y dev stack. Pensado para acelerar el trabajo de ecommerce en Chile y LATAM.

## Plugin incluido

### `advanz-paid-media` (v2.2.0) — 83 skills + 10 agents

#### Paid Ads — Audit & Optimization (claude-ads, 20 skills)

Auditoría profunda multi-plataforma con 250+ checks, scoring ponderado y agents en paralelo.

- **Orquestador:** `ads` (comandos `/ads audit`, `/ads plan <vertical>`, `/ads google`)
- **Por plataforma:** `ads-google`, `ads-meta`, `ads-tiktok`, `ads-youtube`, `ads-linkedin`, `ads-microsoft`, `ads-apple`
- **Funcionales:** `ads-audit`, `ads-budget`, `ads-plan`, `ads-math`, `ads-test`, `ads-dna`, `ads-competitor`, `ads-landing`
- **Creativas:** `ads-create`, `ads-creative`, `ads-generate`, `ads-photoshoot`

#### Paid Ads — General (3)
- `paid-ads` — gestión de campañas en Meta, Google y TikTok Ads
- `ad-creative` — generación de estructuras de creativos
- `ab-test-setup` — diseño de tests A/B con significancia estadística

#### Copy & Contenido (8)
- `copywriting` — copy de venta para landing, ads y email
- `copy-editing` — revisión y pulido de copy
- `social-content` — contenido para redes sociales
- `email-sequence` — secuencias de email marketing (Klaviyo)
- `cold-email` — emails fríos B2B
- `content-strategy` — planificación de contenido
- `marketing-ideas` — generación de ideas de campañas y ángulos
- `product-marketing-context` — contexto de marketing de producto

#### CRO & Conversión (8)
- `page-cro` — optimización de landing pages
- `popup-cro` — popups y modales
- `form-cro` — optimización de forms
- `signup-flow-cro` — onboarding de signup
- `onboarding-cro` — activación post-signup
- `paywall-upgrade-cro` — paywalls y upgrades
- `lead-magnets` — diseño de imanes de leads
- `free-tool-strategy` — engineering as marketing

#### SEO (5)
- `seo-audit` — auditoría SEO técnica y on-page
- `ai-seo` — optimización para LLMs (AEO/GEO)
- `schema-markup` — datos estructurados
- `programmatic-seo` — pSEO con templates
- `site-architecture` — arquitectura de sitios y URLs
- `aso-audit` — App Store Optimization

#### Estrategia & Planning (5)
- `marketing-psychology` — frameworks de persuasión
- `launch-strategy` — lanzamientos de producto
- `pricing-strategy` — estrategia de precios y packaging
- `monetization` — modelos de monetización digital
- `community-marketing` — comunidades y advocacy

#### Lifecycle & Retention (3)
- `churn-prevention` — flujos de cancelación y save offers
- `referral-program` — programas de referidos y afiliados
- `revops` — operaciones de revenue y handoff marketing-ventas

#### Sales (1)
- `sales-enablement` — pitch decks, one-pagers, demo scripts

#### Research & Inteligencia (5)
- `customer-research` — investigación de audiencia
- `competitor-profiling` — análisis profundo de competidores
- `competitor-alternatives` — comparativas vs competencia
- `directory-submissions` — submission a directorios
- `firecrawl-scraper` — scraping general

#### Apify Suite (3)
- `apify-competitor-intelligence` — scraping de competencia
- `apify-influencer-discovery` — descubrimiento y validación de influencers
- `apify-trend-analysis` — análisis de tendencias en redes

#### Analytics & Reporting (4)
- `analytics-tracking` — GA4, Meta Pixel, GTM
- `analytics-product` — PostHog, Mixpanel, funnels
- `advanz-reporting` — reportes de performance para cliente en HTML branded (cierre de mes / evento); estándar Advanz: estructura de bloques, tono neutral, fuentes por MCP (matriz, Shopify, Klaviyo, GA4, Google/Meta Ads) y design system
- `advanz-auditoria-google` — motor de auditoría 100% de Google Ads vía MCP (performance + técnica: estructura, keywords, Quality Score, términos, negativas, anuncios, PMax, pujas, presupuesto, conversiones, productos); salida en **narrativa/dashboard branded** para dueño (qué pasa · por qué · qué te cuesta · qué hacer) con reglas anti-falsos-positivos. Dos capas: motor interno del equipo + entregable AUDITORÍA para el prospecto. Multi-fuente (Google Ads + GA4 + Merchant/Shopify)

#### Image & Video Generation (3)
- `image` — generación e optimización de imágenes para marketing
- `video` — producción de video con IA y frameworks programáticos
- `fal-generate` — fal.ai para imágenes y videos

#### Video con HyperFrames (5)
- `hyperframes` — orquestador principal de HyperFrames
- `hyperframes-cli` — CLI de HyperFrames
- `hyperframes-registry` — registro de componentes
- `gsap` — animaciones GSAP
- `website-to-hyperframes` — convertir webs en videos

#### Dev Stack (10)
Para los proyectos de desarrollo del equipo:
- `react-nextjs-development` — React + Next.js 14+
- `nextjs-supabase-auth` — auth con Supabase
- `frontend-ui-dark-ts` — sistema UI dark mode
- `shadcn` — componentes shadcn/ui
- `postgres-best-practices` — Postgres / Supabase
- `vercel-deployment` — deploys en Vercel
- `vercel-ai-sdk-expert` — Vercel AI SDK
- `ai-engineer` — apps LLM, RAG, agents
- `agent-memory-mcp` — sistema de memoria persistente

### Agents (10) — usados por `/ads audit` en paralelo

**Auditoría (6):** `audit-budget`, `audit-compliance`, `audit-creative`, `audit-google`, `audit-meta`, `audit-tracking`

**Creativas (4):** `copy-writer`, `creative-strategist`, `format-adapter`, `visual-designer`

## Instalación en Cowork

```
/plugin marketplace add AdvanzGrowthPartner/advanz-paid-media-marketplace
/plugin install advanz-paid-media@advanz-paid-media-marketplace
```

## Actualización

Si ya tenías el plugin instalado, refrescá el marketplace para tener la última versión:

```
/plugin marketplace update advanz-paid-media-marketplace
/plugin update advanz-paid-media
```

## Stack de referencia

Shopify · Klaviyo · Triple Whale · Rebuy · GemPages · Loox · Gorgias · n8n · GTM · GoHighLevel · Meta Ads · Google Ads · TikTok Ads

## Atribución

Este marketplace integra y empaqueta skills de varios autores open source. Todo el material respeta las licencias originales:

- **claude-ads** (20 skills + 10 agents) — [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) (MIT)
- **Marketing skills** (~28 skills) — [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- **Apify skills** — Apify ecosystem
- **HyperFrames suite** — HyperFrames maintainers
- **Skills de dev stack** — Anthropic skills marketplace y comunidad

## Uso interno

Plugin pensado para uso interno del equipo Advanz. Para uso externo o redistribución, contactar a matias@advanz.cl.
