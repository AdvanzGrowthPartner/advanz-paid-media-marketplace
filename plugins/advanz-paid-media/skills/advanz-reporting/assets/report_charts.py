# -*- coding: utf-8 -*-
"""
Advanz Reporting — librería de gráficos SVG (con hover) para reportes HTML branded.
Marca-agnóstica y reutilizable en cualquier canal (paid / correo / SEO).

Cómo se usa:
  from report_charts import donut, stacked, cohort, gauge, funnel, hbars, heatcell, TOOLTIP_JS, TT_DIV
  svg = donut([("Producto",1366447,CB['producto']), ...])
  # inyectá el SVG en tu HTML; agregá TT_DIV una vez en el <body> y TOOLTIP_JS antes de </body>.

Reglas de diseño (ver dataviz + design-system.md):
  - Todo elemento con dato lleva class="hv" y data-tip="..."; el tooltip lo maneja TOOLTIP_JS.
  - Números visibles en el gráfico. Texto en tokens de tinta, nunca el color de la serie.
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

def heatcell(v, vmin, vmax, base=(22,163,74)):
    """Devuelve 'background:...;color:...' para una celda de tabla (mapa de calor). base = color saturado."""
    t = 0 if vmax<=vmin else max(0,min(1,(v-vmin)/(vmax-vmin)))
    r=int(255+(base[0]-255)*t); g=int(255+(base[1]-255)*t); b=int(255+(base[2]-255)*t)
    fg = "#12101a" if t<0.6 else "#fff"
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

def cohort(days, bands, cells, vmax, label="", base=(123,47,247), w=560):
    """Cohorte/heatmap día×franja. cells = {(day,band):(valor,n)}. Cubre 'cohorte horario' de campañas."""
    def hc(v):
        t=0 if vmax<=0 else max(0,min(1,v/vmax)); r=int(255+(base[0]-255)*t);g=int(255+(base[1]-255)*t);b=int(255+(base[2]-255)*t)
        return f"rgb({r},{g},{b})", ("#12101a" if t<0.55 else "#fff")
    o=['<table class="cohort"><tr><th></th>']+[f'<th>{b}</th>' for b in bands]+['</tr>']
    for d in days:
        o.append(f'<tr><td class="dl">{d}</td>')
        for b in bands:
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

def funnel(steps, w=560, h=210):
    """Embudo. steps = [(label, value, nota, color)]. Para captación vieron→registro→suscriptor→compra."""
    padl=8;padt=10;padb=46;padr=8; ih=h-padt-padb; iw=w-padl-padr; mx=steps[0][1] or 1
    n=len(steps); gw=iw/n; bw=gw*0.62
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px">']
    for i,(lab,val,note,col) in enumerate(steps):
        x=padl+i*gw+gw/2-bw/2; bh=max(val/mx*ih,4); y=padt+ih-bh
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" fill="{col}" class="hv" data-tip="{lab}: {val}"/>')
        o.append(f'<text x="{x+bw/2:.1f}" y="{y-6:.1f}" text-anchor="middle" font-family="Space Grotesk" font-size="13" font-weight="700" fill="{INK}">{val}</text>')
        o.append(f'<text x="{x+bw/2:.1f}" y="{h-padb+15}" text-anchor="middle" font-size="10" fill="{TXT}">{lab}</text>')
        if note: o.append(f'<text x="{x+bw/2:.1f}" y="{h-padb+29}" text-anchor="middle" font-size="9" fill="{FLOW}">{note}</text>')
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
