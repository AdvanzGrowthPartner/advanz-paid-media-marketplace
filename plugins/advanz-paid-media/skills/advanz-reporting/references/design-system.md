# Design system y entrega

## Base
Partí SIEMPRE de `assets/plantilla.html`: trae el CSS completo (tokens de marca + todos los componentes) y el
esqueleto de header + nav. Copiala a la carpeta del cliente y llená los bloques según `estructura.md`.

## Marca Advanz
- Tipografías: **Poppins** (texto) + **Space Grotesk** (títulos, números). Vía Google Fonts.
- Paleta: violeta `#7b2ff7`→`#c15dff`, cyan `#22d3ee`, fondo `#f6f4fb`, tinta `#12101a`. Verde/rojo solo para
  chips de variación (dato, no juicio).
- El **degradado en el título/tesis** es identidad de marca intencional (aunque un linter de diseño lo marque,
  se mantiene). Lo mismo el borde de acento en los `.read`.

## Componentes (clases del CSS)
- `.tesis` — titular arriba, con `<span>` en degradado para la frase clave.
- `.grid`/`.kpi` — grilla de KPIs del resumen.
- `.tiles`/`.mc` — cuadritos de métricas (canales, medios, "qué necesitamos").
- `.tw`+`table`, `.chip` (up/nt/dn) — tablas y variaciones.
- `.read` — bloque de lectura (1–2 frases).
- `.gcols`/`.gauge` — barras de cuota de búsqueda (impression share).
- `.crvg`/`.crv` — tarjetas de anuncios con miniatura (`.cvimg`), ROAS y métricas.
- `.pgrid`/`.pcard` — tarjetas de producto con foto.
- `.funnel`/`.fn`/`.fbar` — embudo del recorrido de compra.
- `.split`/`.lg` — barra nuevos vs recurrentes.
- `.act` — pasos numerados de "próximos pasos".
- `.cols` — dos columnas (para MoM vs YoY).

## Imágenes: embeber en base64 (autocontenido)
Los reportes anteriores embeben las imágenes para que el archivo se vea aunque se abra sin internet. Flujo:
1. En el HTML, poné placeholders cortos en los `src`: `src="PROD1"`, `src="AD1"`, etc. (no metas base64 gigante
   a mano ni URLs largas en el HTML).
2. Corré un script Python que descarga cada URL y reemplaza el placeholder por el data URI. Patrón:

```python
import base64, urllib.request
f = r"<ruta del html>"; html = open(f, encoding="utf-8").read()
imgs = { "PROD1": "<url>", "AD1": "<url>", ... }   # Shopify CDN (productos) / fbcdn (anuncios)
def mime(b):
    if b[:8]==b"\x89PNG\r\n\x1a\n": return "image/png"
    if b[:3]==b"\xff\xd8\xff": return "image/jpeg"
    return "image/jpeg"
for k,u in imgs.items():
    req=urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0","Referer":"https://www.facebook.com/"})
    d=urllib.request.urlopen(req,timeout=30).read()
    html=html.replace(f'src="{k}"', f'src="data:{mime(d)};base64,{base64.b64encode(d).decode()}"')
open(f,"w",encoding="utf-8").write(html)
```
- **Fotos de producto**: URL del CDN de Shopify (`graphql_query` → `featuredImage.url`); agregá `&width=420`.
- **Miniaturas de anuncios**: `ads_get_creatives` con `fields:["thumbnail_url","image_url"]` → URL fbcdn (dura
  unos días; re-fetchear si expiró). Detectá el tipo por magic-number (algunas `.png?stp=dst-jpg` vienen jpeg).
- Verificá al final que no queden placeholders (`grep 'src="PROD\|src="AD'`).

## Entrega (reglas Advanz)
- Guardá **local** en `empresa/clientes/<cliente>/reportes/` como `YYYY-MM-DD_reporte-<tipo>.html`.
  **NO** publicar como Artifact (ver [[entregables_html_local]]).
- Enviá el `.html` como archivo (SendUserFile).
- Al aprobar, dejá una copia **`-FINAL`** para diferenciar de las versiones de trabajo.
- El archivo termina pesando ~700KB–1MB por las imágenes embebidas: es lo esperado.

## Responsive / técnico
- `max-width` del wrap ~1000px; grids con `auto-fit minmax(...)`; media query a 640px pasa grids a 2 columnas y
  `.cols`/`.gcols` a 1. Tablas dentro de `.tw` con `overflow-x:auto`.
