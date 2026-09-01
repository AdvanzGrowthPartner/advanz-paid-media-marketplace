# -*- coding: utf-8 -*-
"""
Advanz Reporting — librería de gráficos SVG (con hover) para reportes HTML branded.
Marca-agnóstica y reutilizable en cualquier canal (paid / correo / SEO).

Cómo se usa:
  from report_charts import (donut, stacked, cohort, gauge, speedo, funnel, hbars,
                             hmt, heatcell, TOOLTIP_JS, TT_DIV)
  svg = donut([("Producto",1366447,CB['producto']), ...])
  # inyectá el SVG en tu HTML; agregá TT_DIV una vez en el <body> y TOOLTIP_JS antes de </body>.

Inventario: donut · stacked (barras apiladas) · cohort (heatmap horario) · funnel (embudo real de
  trapecios) · speedo (velocímetro con aguja) · gauge (semicírculo relleno) · hbars (barras horizontales,
  sirve para 'tipos de correo por ventas') · hmt (heatmap sutil de tabla) · heatcell (fondo de celda para
  grillas densas).

Reglas de diseño (ver dataviz + design-system.md):
  - Todo elemento con dato lleva class="hv" y data-tip="..."; el tooltip lo maneja TOOLTIP_JS.
  - Números visibles en el gráfico y en CLP completo (1.366.447, no "1366k"). Texto en tokens de tinta.
  - Tablas: heatmap SUTIL con `hmt` (colorea sólo el número, sin banda de fondo). El fondo de celda
    (`heatcell`) queda para la cohorte horaria, con la saturación topada.
  - Paleta categórica CVD-safe: evento #7b2ff7, producto #0e9bc9, contenido #e8850c, retail #2563eb, marca #d83a7d.
"""
import math

INK="#12101a"; TXT="#211c33"; MUT="#6b6580"; LINE="#e7e2f2"
VIOLET="#7b2ff7"; VLIGHT="#c15dff"; CYAN="#22d3ee"; FLOW="#0891b2"
GREEN="#16a34a"; RED="#dc2626"; AMBER="#d97706"
CB=dict(evento="#7b2ff7", producto="#0e9bc9", contenido="#e8850c", retail="#2563eb", marca="#d83a7d")

# HTML plumbing para el tooltip (poné TT_DIV una vez en <body>, TOOLTIP_JS antes de </body>)
TT_DIV = '<div id="tt"></div>'
TT_CSS = ("#tt{position:fixed;pointer-events:none;background:#12101a;color:#fff;font-size:12px;padding:6px 10px;"
          "border-radius:8px;opacity:0;transition:opacity .1s;z-index:200;font-family:'Space Grotesk',sans-serif;"
          "white-space:nowrap;transform:translate(-50%,-135%)}.hv{cursor:pointer;transition:opacity .12s}.hv:hover{opacity:.8}")
TOOLTIP_JS = ("<script>(function(){var t=document.getElementById('tt');document.addEventListener('mouseover',function(e){"
  "var x=e.target.closest('[data-tip]');if(!x)return;t.textContent=x.getAttribute('data-tip');t.style.opacity='1';});"
  "document.addEventListener('mousemove',function(e){if(t.style.opacity==='1'){t.style.left=e.clientX+'px';t.style.top=e.clientY+'px';}});"
  "document.addEventListener('mouseout',function(e){if(e.target.closest('[data-tip]'))t.style.opacity='0';});})();</script>")

def hmt(v, vmin, vmax):
    """Heatmap SUTIL para celdas de tabla — el ESTÁNDAR. Colorea sólo el NÚMERO (verde=fuerte,
    rojo=débil), sin banda de fondo: la métrica toma relevancia, no el color. Devuelve sólo estilo de
    texto ('color:...;font-weight:...'), sin background. Para un cero/sin dato pasá el string rojo directo.
    Regla de marca (pedido del cliente): las tablas NO llevan banda de color completa."""
    if vmax<=vmin: return "font-weight:600"
    t=max(0,min(1,(v-vmin)/(vmax-vmin)))
    if t>=0.6: return "color:#0f7a3d;font-weight:700"
    if t<=0.22: return "color:#c0392b;font-weight:700"
    return "font-weight:600"

def heatcell(v, vmin, vmax, base=(123,47,247), cap=0.62):
    """Fondo de celda con mapa de calor — SÓLO para grillas densas tipo cohorte horario (día×hora),
    donde el patrón se lee por intensidad. NO usar en tablas de KPIs/tipos: ahí va `hmt` (sin banda).
    `cap` topa la saturación para que ni la celda más fuerte quede chillona."""
    t = 0 if vmax<=vmin else max(0,min(1,(v-vmin)/(vmax-vmin)))*cap
    r=int(255+(base[0]-255)*t); g=int(255+(base[1]-255)*t); b=int(255+(base[2]-255)*t)
    fg = "#12101a" if t<0.42 else "#fff"
    return f"background:rgb({r},{g},{b});color:{fg}"

def donut(data, center_top="", center_sub="", size=196, r=68, sw=30):
    """data = [(label, value, color)]. Segmentos con hover; leyenda va aparte (a la derecha)."""
    total=sum(v for _,v,_ in data) or 1; C=2*math.pi*r; cx=cy=size/2; start=0.0; segs=[]
    for lab,v,col in data:
        frac=v/total; seg=frac*C; deg=-90+start/C*360
        segs.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}" '
          f'stroke-dasharray="{seg-2.5:.2f} {C-seg+2.5:.2f}" transform="rotate({deg:.2f} {cx} {cy})" '
          f'class="hv" data-tip="{lab}: {frac*100:.0f}%"/>')
        start+=seg
    ct=(f'<text x="{cx}" y="{cy-3}" text-anchor="middle" font-family="Space Grotesk" font-size="21" font-weight="700" fill="{INK}">{center_top}</text>'
        f'<text x="{cx}" y="{cy+15}" text-anchor="middle" font-size="10" fill="{MUT}">{center_sub}</text>') if center_top else ""
    return f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}">'+''.join(segs)+ct+'</svg>'

def stacked(cats, series, mx=None, w=580, h=230, unit=""):
    """Barras apiladas. series = [(nombre,color,[valores...]), ...]. Ideal: tendencia MoM campañas+flujos."""
    padl=38;padb=44;padt=14;padr=10; iw=w-padl-padr; ih=h-padb-padt
    tot=[sum(s[2][i] for s in series) for i in range(len(cats))]
    mx=mx or max(tot)*1.12
    n=len(cats); gw=iw/n; bw=min(52,gw*0.52)
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px">']
    step=max(1,round(mx/4))
    gy=0
    while gy<=mx:
        yy=padt+ih-(gy/mx*ih)
        o.append(f'<line x1="{padl}" y1="{yy:.1f}" x2="{w-padr}" y2="{yy:.1f}" stroke="{LINE}"/>')
        o.append(f'<text x="{padl-7}" y="{yy+3:.1f}" text-anchor="end" font-size="9.5" fill="{MUT}">{gy}</text>')
        gy+=step
    for i,c in enumerate(cats):
        x=padl+i*gw+gw/2-bw/2; yb=padt+ih
        for nombre,col,vals in series:
            bh=vals[i]/mx*ih; yb-=bh
            o.append(f'<rect x="{x:.1f}" y="{yb:.1f}" width="{bw:.1f}" height="{max(bh,1):.1f}" rx="3" fill="{col}" class="hv" data-tip="{c} · {nombre}: {vals[i]}{unit}"/>')
            yb-=2
        o.append(f'<text x="{x+bw/2:.1f}" y="{yb-4:.1f}" text-anchor="middle" font-family="Space Grotesk" font-size="10.5" font-weight="700" fill="{INK}">{tot[i]}</text>')
        o.append(f'<text x="{x+bw/2:.1f}" y="{h-padb+15}" text-anchor="middle" font-size="10" fill="{TXT}">{c}</text>')
    o.append('</svg>'); return ''.join(o)

def cohort(days, bands, cells, vmax, label="", base=(123,47,247), w=560, cap=0.62):
    """Cohorte/heatmap horario. cells = {(day,band):(valor,n)}. Orientación estándar (pedido del cliente):
    FRANJA HORARIA en las FILAS (vertical) y DÍAS en las COLUMNAS (horizontal). Color topado por `cap`
    para que quede sutil. Las celdas sin envío van vacías (no probamos ahí)."""
    def hc(v):
        t=(0 if vmax<=0 else max(0,min(1,v/vmax)))*cap
        r=int(255+(base[0]-255)*t);g=int(255+(base[1]-255)*t);b=int(255+(base[2]-255)*t)
        return f"rgb({r},{g},{b})", ("#12101a" if t<0.42 else "#fff")
    o=['<table class="cohort"><tr><th></th>']+[f'<th>{d}</th>' for d in days]+['</tr>']
    for b in bands:
        o.append(f'<tr><td class="dl">{b}</td>')
        for d in days:
            if (d,b) in cells:
                val,n=cells[(d,b)]; bg,fg=hc(val)
                o.append(f'<td class="cc hv" style="background:{bg};color:{fg}" data-tip="{d} {b}: {val} ({n})">{val}</td>')
            else:
                o.append('<td class="cc empty"></td>')
        o.append('</tr>')
    o.append('</table>'); return ''.join(o)

def hbars(items, mx=None, w=560, rowh=36, fmt="{:,}"):
    """Barras horizontales. items = [(label, value, color, sublabel)]. Para ventas por flujo / productos."""
    padl=155;padr=70; mx=mx or (max(v for _,v,_,_ in items) or 1); iw=w-padl-padr; h=rowh*len(items)+8
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px">']
    for i,(l,v,c,sub) in enumerate(items):
        y=8+i*rowh+rowh/2; bw=v/mx*iw
        o.append(f'<text x="{padl-8}" y="{y+4}" text-anchor="end" font-size="11.5" fill="{INK}">{l}</text>')
        o.append(f'<rect x="{padl}" y="{y-10}" width="{max(bw,2):.1f}" height="20" rx="4" fill="{c}" class="hv" data-tip="{l}: {fmt.format(v)}"/>')
        o.append(f'<text x="{padl+max(bw,3)+7:.1f}" y="{y+4}" font-family="Space Grotesk" font-size="11.5" font-weight="700" fill="{INK}">{sub or fmt.format(v)}</text>')
    o.append('</svg>'); return ''.join(o)

def funnel(steps, w=560, h=300, fmt=None, gamma=0.42):
    """Embudo REAL (trapecios centrados que se angostan) — no barras. steps = [(label, value, nota, color)].
    Para captación vieron→registro→suscriptor→compra. `gamma`<1 abre la base para que un último paso muy
    chico (ej. 4 compras) siga siendo visible. `fmt` formatea el número (default: miles con punto)."""
    fmt = fmt or (lambda v: format(int(v),",d").replace(",","."))
    cx=w/2; top=14; band=54; gap=14; maxw=min(360,w-180); mx=steps[0][1] or 1
    def wd(v): return max(maxw*(v/mx)**gamma, 46)
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px">']; y=top
    for i,(lab,val,note,col) in enumerate(steps):
        w1=wd(val); w2=wd(steps[i+1][1]) if i+1<len(steps) else w1*0.5
        x1=cx-w1/2; x2=cx-w2/2; yb=y+band
        pts=f"{x1:.1f},{y:.1f} {x1+w1:.1f},{y:.1f} {x2+w2:.1f},{yb:.1f} {x2:.1f},{yb:.1f}"
        o.append(f'<polygon points="{pts}" fill="{col}" class="hv" data-tip="{lab}: {fmt(val)}"/>')
        o.append(f'<text x="{cx}" y="{y+band/2-1:.1f}" text-anchor="middle" font-family="Space Grotesk" font-size="15" font-weight="700" fill="#fff">{fmt(val)}</text>')
        o.append(f'<text x="{cx+w1/2+10:.1f}" y="{y+band/2-3:.1f}" font-size="11" font-weight="600" fill="{INK}">{lab}</text>')
        if note: o.append(f'<text x="{cx+w1/2+10:.1f}" y="{y+band/2+12:.1f}" font-size="10" fill="{FLOW}">{note}</text>')
        y=yb+gap
    o.append('</svg>'); return ''.join(o)

def speedo(pct, lo, hi, mx=40, w=320, h=200, color=VIOLET):
    """Velocímetro (aguja) con zona verde [lo,hi] sobre un arco 0..mx — variante preferida para
    'participación de flujos' (meta 25–30%): comunica 'estás lejos/cerca de lo sano' mejor que el gauge.
    `gauge` sigue disponible para un semicírculo relleno simple."""
    cx=w/2; cy=h-26; r=118
    def pt(frac,rr=r): a=math.pi*(1-frac); return cx+rr*math.cos(a), cy-rr*math.sin(a)
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px">']
    x0,y0=pt(0);x1,y1=pt(1)
    o.append(f'<path d="M {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{LINE}" stroke-width="18" stroke-linecap="round"/>')
    xa,ya=pt(lo/mx);xb,yb=pt(hi/mx)
    o.append(f'<path d="M {xa:.1f} {ya:.1f} A {r} {r} 0 0 1 {xb:.1f} {yb:.1f}" fill="none" stroke="{GREEN}" stroke-width="18" class="hv" data-tip="Zona sana: {lo}–{hi}%"/>')
    for t in range(0,int(mx)+1,max(1,int(mx//4))):
        xa2,ya2=pt(t/mx,r-14); xa3,ya3=pt(t/mx,r+2)
        o.append(f'<line x1="{xa2:.1f}" y1="{ya2:.1f}" x2="{xa3:.1f}" y2="{ya3:.1f}" stroke="{MUT}" stroke-width="1.5"/>')
        xl,yl=pt(t/mx,r-26); o.append(f'<text x="{xl:.1f}" y="{yl+3:.1f}" text-anchor="middle" font-size="9" fill="{MUT}">{t}%</text>')
    nx,ny=pt(pct/mx,r-20)
    o.append(f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{color}" stroke-width="4" stroke-linecap="round"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{color}"/>')
    o.append(f'<text x="{cx}" y="{cy-52}" text-anchor="middle" font-family="Space Grotesk" font-size="30" font-weight="700" fill="{INK}">{pct}%</text>')
    if pct<lo: o.append(f'<text x="{cx}" y="{cy-34}" text-anchor="middle" font-size="10.5" fill="{RED}">a {lo-pct} pts de lo sano</text>')
    o.append('</svg>'); return ''.join(o)

def gauge(pct, lo, hi, w=300, h=160, color=FLOW):
    """Gauge semicircular con banda de meta [lo,hi]. Para participación de flujos (meta 25–30%)."""
    cx=w/2; cy=h-18; r=112
    def pt(f): a=math.pi*(1-f); return cx+r*math.cos(a), cy-r*math.sin(a)
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px">']
    x0,y0=pt(0);x1,y1=pt(1); o.append(f'<path d="M {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{LINE}" stroke-width="16" stroke-linecap="round"/>')
    xa,ya=pt(lo/50);xb,yb=pt(hi/50); o.append(f'<path d="M {xa:.1f} {ya:.1f} A {r} {r} 0 0 1 {xb:.1f} {yb:.1f}" fill="none" stroke="#bfe9d4" stroke-width="16"/>')
    xv,yv=pt(pct/50); o.append(f'<path d="M {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {xv:.1f} {yv:.1f}" fill="none" stroke="{color}" stroke-width="16" stroke-linecap="round" class="hv" data-tip="{pct}% (meta {lo}–{hi}%)"/>')
    o.append(f'<text x="{cx}" y="{cy-16}" text-anchor="middle" font-family="Space Grotesk" font-size="32" font-weight="700" fill="{INK}">{pct}%</text>')
    o.append(f'<text x="{cx}" y="{cy+2}" text-anchor="middle" font-size="10" fill="{MUT}">meta {lo}–{hi}%</text></svg>')
    return ''.join(o)
