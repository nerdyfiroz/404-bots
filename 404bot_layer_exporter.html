<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404BOT — Layer Exporter</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root { --ink: #0e0e0e; --page: #111114; --card: #18181c; --muted: #55556A; --accent: #FF6B35; }
  html, body { width: 100%; min-height: 100vh; background: var(--page); color: #f0f0f0; font-family: 'Space Grotesk', system-ui, sans-serif; }
  body { padding: 32px 28px 80px; }

  h1 { font-size: 32px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 6px; }
  .sub { font-size: 14px; color: var(--muted); margin-bottom: 36px; }

  /* ── Palette selector ── */
  .palette-row { display: flex; gap: 12px; margin-bottom: 36px; flex-wrap: wrap; }
  .palette-btn {
    padding: 10px 22px; border-radius: 40px; border: 2px solid #333;
    background: transparent; color: #aaa; font-family: inherit;
    font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.15s;
    letter-spacing: 0.04em;
  }
  .palette-btn:hover { border-color: #888; color: #f0f0f0; }
  .palette-btn.active { color: white; }

  /* ── Main layout ── */
  .layout { display: grid; grid-template-columns: 420px 1fr; gap: 32px; align-items: start; }
  @media (max-width: 900px) { .layout { grid-template-columns: 1fr; } }

  /* ── Preview panel ── */
  .preview-panel { position: sticky; top: 24px; }
  .preview-box {
    aspect-ratio: 1; width: 100%; border-radius: 18px; overflow: hidden;
    border: 2px solid #222; background: #0e0e0e; margin-bottom: 16px;
    position: relative;
  }
  .preview-box canvas { width: 100%; height: 100%; display: block; }
  .preview-label {
    text-align: center; font-size: 12px; color: var(--muted);
    letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 20px;
  }
  .preview-label span { color: var(--accent); font-weight: 700; }

  /* ── Export all button ── */
  .export-all-btn {
    width: 100%; padding: 14px; border-radius: 12px;
    background: var(--accent); border: none; color: white;
    font-family: inherit; font-size: 14px; font-weight: 700;
    cursor: pointer; letter-spacing: 0.04em; transition: all 0.15s;
    margin-bottom: 10px;
  }
  .export-all-btn:hover { background: #D85A30; transform: translateY(-2px); }
  .export-all-btn:active { transform: none; }

  /* ── Layer grid ── */
  .layers-panel { }
  .layers-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 16px; }

  .layer-card {
    background: var(--card); border: 1.5px solid #222; border-radius: 14px;
    overflow: hidden; transition: border-color 0.15s, transform 0.15s;
    cursor: pointer;
  }
  .layer-card:hover { border-color: #444; transform: translateY(-3px); }
  .layer-card.visible { border-color: var(--accent); }

  .layer-thumb {
    aspect-ratio: 1; background: repeating-conic-gradient(#1e1e26 0% 25%, #252530 0% 50%) 0 0 / 20px 20px;
    position: relative; overflow: hidden;
  }
  .layer-thumb canvas { width: 100%; height: 100%; display: block; }

  .layer-info { padding: 10px 12px 4px; }
  .layer-name { font-size: 13px; font-weight: 700; color: #f0f0f0; margin-bottom: 3px; }
  .layer-desc { font-size: 11px; color: var(--muted); margin-bottom: 8px; line-height: 1.4; }

  .layer-actions { display: flex; gap: 6px; padding: 0 12px 12px; }
  .btn-vis, .btn-dl {
    flex: 1; padding: 6px 8px; border-radius: 6px; border: 1.5px solid #333;
    background: transparent; color: #888; font-family: inherit;
    font-size: 11px; font-weight: 600; cursor: pointer; transition: all 0.12s;
    letter-spacing: 0.03em;
  }
  .btn-vis:hover { border-color: var(--accent); color: var(--accent); }
  .btn-dl:hover { border-color: #888; color: #f0f0f0; }
  .btn-vis.on { background: rgba(255,107,53,0.12); border-color: var(--accent); color: var(--accent); }

  .progress-bar { height: 3px; background: #222; border-radius: 2px; margin-bottom: 20px; overflow: hidden; }
  .progress-fill { height: 100%; background: var(--accent); width: 0%; transition: width 0.3s; border-radius: 2px; }
  .status-msg { font-size: 12px; color: var(--muted); margin-bottom: 16px; min-height: 18px; }

  .section-title { font-size: 13px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 14px; }

  /* toggle eye icon */
  .eye { font-size: 14px; }
</style>
</head>
<body>

<h1>404BOT Layer Exporter</h1>
<p class="sub">Select a color variation · toggle layers on/off · download individually or all at once as PNGs</p>

<!-- PALETTE SELECTOR -->
<div class="palette-row" id="paletteRow"></div>

<div class="layout">

  <!-- LEFT: Preview + export all -->
  <div class="preview-panel">
    <div class="preview-box"><canvas id="compositeCanvas" width="600" height="600"></canvas></div>
    <div class="preview-label">Composite preview — <span id="activePaletteName">Yellow Genesis</span></div>
    <button class="export-all-btn" onclick="exportAll()">⬇ Export All Layers as PNG</button>
    <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    <div class="status-msg" id="statusMsg">Ready. Select a variation above.</div>
  </div>

  <!-- RIGHT: Layer cards -->
  <div class="layers-panel">
    <div class="section-title">Layers — click to toggle / download</div>
    <div class="layers-grid" id="layersGrid"></div>
  </div>

</div>

<!-- Hidden 600×600 canvas for off-screen rendering -->
<canvas id="offscreen" width="600" height="600" style="display:none"></canvas>

<script>
// ═══════════════════════════════════════════════════════════ PALETTES
const PALETTES = [
  { id:"yellow-genesis", name:"Yellow Genesis",
    visor:"#F4C430", visorGrad:"#E8A000", visorHL:"#FFE87A",
    earInner:"#F4C430", collar:"#7AB648", collarDk:"#5A8F2A",
    armor:"#FFF8E0", armorShade:"#EEE0B0", armorDk:"#D4C080",
    bg:"#C49A6C", bgGrad:"#B08050", cable:"#C8A020", shadowV:"#A07000",
    accent: "#F4C430"
  },
  { id:"cyber-green", name:"Cyber Green",
    visor:"#00D26A", visorGrad:"#00A050", visorHL:"#80FFB4",
    earInner:"#00D26A", collar:"#2255CC", collarDk:"#1133AA",
    armor:"#FFFFFF", armorShade:"#DDE8E0", armorDk:"#B8CCBA",
    bg:"#7A7058", bgGrad:"#5A5040", cable:"#00A050", shadowV:"#006630",
    accent: "#00D26A"
  },
  { id:"purple-void", name:"Purple Void",
    visor:"#9B59D0", visorGrad:"#7030A0", visorHL:"#D4A0FF",
    earInner:"#9B59D0", collar:"#D63080", collarDk:"#A01060",
    armor:"#E8E0F0", armorShade:"#CCC0DC", armorDk:"#A898C4",
    bg:"#2A2A32", bgGrad:"#1A1A22", cable:"#8040C0", shadowV:"#40106A",
    accent: "#9B59D0"
  },
  { id:"cyan-network", name:"Cyan Network",
    visor:"#00C8F0", visorGrad:"#0098C8", visorHL:"#80EEFF",
    earInner:"#00C8F0", collar:"#30A890", collarDk:"#108870",
    armor:"#F0F8F8", armorShade:"#CDE0DF", armorDk:"#A8C8C6",
    bg:"#8A9090", bgGrad:"#6A7070", cable:"#00A8D0", shadowV:"#005880",
    accent: "#00C8F0"
  }
];

// ═══════════════════════════════════════════════════════════ LAYER DEFINITIONS
// Each layer is a function (ctx, palette) => void
// Layers are rendered in ORDER for compositing, but exported individually on transparent bg.

const LAYERS = [
  {
    id: "background",
    name: "Background",
    desc: "Solid muted BG with radial gradient",
    draw(ctx, p) {
      const grad = ctx.createRadialGradient(300, 240, 60, 300, 240, 420);
      grad.addColorStop(0, p.bg);
      grad.addColorStop(1, p.bgGrad);
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 600, 600);
    }
  },
  {
    id: "ears",
    name: "Ears",
    desc: "Cat-like antenna ears with inner accent",
    draw(ctx, p) {
      const sw = 5.5;
      // Ear helper
      const drawEar = (cx) => {
        // Outer
        ctx.beginPath(); ctx.ellipse(cx, 115, 46, 58, 0, 0, Math.PI*2);
        const g = ctx.createRadialGradient(cx-10, 90, 5, cx, 115, 50);
        g.addColorStop(0, p.armor); g.addColorStop(1, p.armorDk);
        ctx.fillStyle = g; ctx.fill();
        ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = sw; ctx.stroke();
        // Inner
        ctx.beginPath(); ctx.ellipse(cx, 115, 28, 36, 0, 0, Math.PI*2);
        const g2 = ctx.createRadialGradient(cx-8, 100, 4, cx, 115, 32);
        g2.addColorStop(0, p.visorHL); g2.addColorStop(1, p.visor);
        ctx.fillStyle = g2; ctx.fill();
        ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 4; ctx.stroke();
      };
      drawEar(174); drawEar(426);
    }
  },
  {
    id: "head",
    name: "Head",
    desc: "White metallic head ellipse with sheen",
    draw(ctx, p) {
      ctx.beginPath(); ctx.ellipse(300, 228, 148, 152, 0, 0, Math.PI*2);
      const g = ctx.createLinearGradient(160, 100, 430, 380);
      g.addColorStop(0, p.armor); g.addColorStop(0.6, p.armorShade); g.addColorStop(1, p.armorDk);
      ctx.fillStyle = g; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 5.5; ctx.stroke();
      // sheen
      ctx.beginPath(); ctx.ellipse(258, 168, 38, 22, 0, 0, Math.PI*2);
      ctx.fillStyle = "rgba(255,255,255,0.18)"; ctx.fill();
    }
  },
  {
    id: "cheek-vents",
    name: "Cheek Vents",
    desc: "3 short black lines on the left cheek",
    draw(ctx, p) {
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 4; ctx.lineCap = "round";
      [[193,272,213,268],[191,285,213,281],[191,298,211,295]].forEach(([x1,y1,x2,y2]) => {
        ctx.beginPath(); ctx.moveTo(x1,y1); ctx.lineTo(x2,y2); ctx.stroke();
      });
    }
  },
  {
    id: "ear-detail",
    name: "Ear Detail",
    desc: "Right cheek mechanical circle detail",
    draw(ctx, p) {
      ctx.beginPath(); ctx.arc(404, 285, 16, 0, Math.PI*2);
      ctx.fillStyle = p.armorShade; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 3; ctx.stroke();
      ctx.beginPath(); ctx.arc(404, 285, 8, 0, Math.PI*2);
      ctx.fillStyle = p.armorDk; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 2.5; ctx.stroke();
      ctx.beginPath(); ctx.arc(404, 285, 3, 0, Math.PI*2);
      ctx.fillStyle = "#0e0e0e"; ctx.fill();
    }
  },
  {
    id: "visor",
    name: "Visor",
    desc: "Oversized colored visor with 404 text",
    draw(ctx, p) {
      ctx.beginPath(); ctx.ellipse(300, 235, 112, 72, 0, 0, Math.PI*2);
      const g = ctx.createLinearGradient(300, 163, 300, 307);
      g.addColorStop(0, p.visorHL+"B0"); g.addColorStop(0.3, p.visor); g.addColorStop(1, p.visorGrad);
      ctx.fillStyle = g; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 5.5; ctx.stroke();
      // gloss
      ctx.save(); ctx.beginPath(); ctx.ellipse(300, 235, 112, 72, 0, 0, Math.PI*2); ctx.clip();
      ctx.beginPath(); ctx.ellipse(280, 209, 52, 18, 0, 0, Math.PI*2);
      ctx.fillStyle = "rgba(255,255,255,0.28)"; ctx.fill();
      // shadow bottom
      ctx.beginPath(); ctx.ellipse(300, 295, 100, 30, 0, 0, Math.PI*2);
      ctx.fillStyle = p.shadowV+"30"; ctx.fill();
      ctx.restore();
      // screw dots
      ctx.beginPath(); ctx.arc(198, 232, 7, 0, Math.PI*2);
      ctx.fillStyle = p.armorDk; ctx.fill(); ctx.strokeStyle="#0e0e0e"; ctx.lineWidth=3; ctx.stroke();
      ctx.beginPath(); ctx.arc(402, 232, 7, 0, Math.PI*2);
      ctx.fillStyle = p.armorDk; ctx.fill(); ctx.stroke();
    }
  },
  {
    id: "visor-text",
    name: "Visor Text",
    desc: '"404" white digital lettering',
    draw(ctx, p) {
      ctx.font = "bold 52px 'Space Grotesk', Arial";
      ctx.textAlign = "center"; ctx.textBaseline = "middle";
      ctx.strokeStyle = "rgba(0,0,0,0.18)"; ctx.lineWidth = 3;
      ctx.strokeText("404", 300, 248);
      ctx.fillStyle = "white"; ctx.fillText("404", 300, 248);
    }
  },
  {
    id: "nose",
    name: "Nose",
    desc: "Small oval nose",
    draw(ctx, p) {
      ctx.beginPath(); ctx.ellipse(300, 317, 10, 7, 0, 0, Math.PI*2);
      ctx.fillStyle = "#0e0e0e"; ctx.fill();
    }
  },
  {
    id: "mouth",
    name: "Mouth",
    desc: "Rectangular rounded smiling mouth",
    draw(ctx, p) {
      ctx.beginPath();
      const g = ctx.createLinearGradient(270, 336, 330, 354);
      g.addColorStop(0, p.collar); g.addColorStop(1, p.collarDk);
      roundRect(ctx, 270, 336, 60, 18, 9);
      ctx.fillStyle = g; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 4; ctx.stroke();
    }
  },
  {
    id: "collar",
    name: "Collar",
    desc: "Thick accent-colored neck collar",
    draw(ctx, p) {
      const g = ctx.createLinearGradient(234, 358, 366, 394);
      g.addColorStop(0, p.collar); g.addColorStop(1, p.collarDk);
      roundRect(ctx, 234, 358, 132, 36, 14);
      ctx.fillStyle = g; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 5.5; ctx.stroke();
      // highlight strip
      roundRect(ctx, 244, 363, 112, 10, 6);
      ctx.fillStyle = "rgba(255,255,255,0.20)"; ctx.fill();
    }
  },
  {
    id: "body",
    name: "Body",
    desc: "Main torso / chest armor shape",
    draw(ctx, p) {
      const g = ctx.createLinearGradient(168, 388, 432, 568);
      g.addColorStop(0, p.armor); g.addColorStop(1, p.armorShade);
      roundRect(ctx, 168, 388, 264, 180, 32);
      ctx.fillStyle = g; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 5.5; ctx.stroke();
      // inner armor plate
      const g2 = ctx.createLinearGradient(196, 410, 404, 540);
      g2.addColorStop(0, p.armor); g2.addColorStop(1, p.armorDk);
      roundRect(ctx, 196, 410, 208, 130, 20);
      ctx.fillStyle = g2; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 4; ctx.stroke();
      // sheen
      roundRect(ctx, 210, 416, 80, 32, 10);
      ctx.fillStyle = "rgba(255,255,255,0.16)"; ctx.fill();
    }
  },
  {
    id: "chest-text",
    name: "Chest Text",
    desc: '"404BOT" label on armor plate',
    draw(ctx, p) {
      ctx.font = "bold 17px 'Space Grotesk', Arial";
      ctx.textAlign = "center"; ctx.textBaseline = "middle";
      ctx.fillStyle = "#0e0e0e"; ctx.fillText("404BOT", 300, 448);
    }
  },
  {
    id: "cable",
    name: "Mechanical Cable",
    desc: "Thin arc cable across torso",
    draw(ctx, p) {
      const drawCable = (lw, color) => {
        ctx.beginPath();
        ctx.moveTo(220, 470); ctx.quadraticCurveTo(260, 440, 300, 468);
        ctx.quadraticCurveTo(340, 496, 380, 472);
        ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = "round"; ctx.stroke();
      };
      drawCable(6.5, "rgba(0,0,0,0.35)");
      drawCable(3.5, p.cable);
    }
  },
  {
    id: "chest-connector",
    name: "Chest Connector",
    desc: "Circular connector hub with nested rings",
    draw(ctx, p) {
      // Ring 1
      ctx.beginPath(); ctx.arc(300, 482, 28, 0, Math.PI*2);
      ctx.fillStyle = p.armorShade; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 4; ctx.stroke();
      // Ring 2 — collar color
      ctx.beginPath(); ctx.arc(300, 482, 16, 0, Math.PI*2);
      ctx.fillStyle = p.collar; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 3; ctx.stroke();
      // Ring 3 — armor dark
      ctx.beginPath(); ctx.arc(300, 482, 8, 0, Math.PI*2);
      ctx.fillStyle = p.armorDk; ctx.fill();
      ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 2; ctx.stroke();
      // Center dot
      ctx.beginPath(); ctx.arc(300, 482, 3.5, 0, Math.PI*2);
      ctx.fillStyle = "#0e0e0e"; ctx.fill();
    }
  },
  {
    id: "arms",
    name: "Arms",
    desc: "Rounded arm panels with shoulder joints",
    draw(ctx, p) {
      const drawArm = (ax) => {
        const flip = ax < 300;
        const g = ctx.createLinearGradient(ax, 400, ax + (flip ? -60 : 60), 510);
        g.addColorStop(0, p.armor); g.addColorStop(1, p.armorDk);
        // Main arm block
        roundRect(ctx, ax, 400, 58, 110, 28);
        ctx.fillStyle = g; ctx.fill();
        ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 5.5; ctx.stroke();
        // Band detail
        const bx = ax;
        roundRect(ctx, bx, 440, 58, 12, 6);
        ctx.fillStyle = p.collar; ctx.fill();
        ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 3; ctx.stroke();
        // Shoulder joint
        const jx = flip ? ax + 50 : ax + 8;
        ctx.beginPath(); ctx.arc(jx, 408, 16, 0, Math.PI*2);
        ctx.fillStyle = p.armorShade; ctx.fill();
        ctx.strokeStyle = "#0e0e0e"; ctx.lineWidth = 3; ctx.stroke();
        ctx.beginPath(); ctx.arc(jx, 408, 8, 0, Math.PI*2);
        ctx.fillStyle = p.armorDk; ctx.fill();
      };
      drawArm(118); // left
      drawArm(424); // right
    }
  },
];

// Utility: roundRect polyfill
function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.quadraticCurveTo(x + w, y, x + w, y + r);
  ctx.lineTo(x + w, y + h - r);
  ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  ctx.lineTo(x + r, y + h);
  ctx.quadraticCurveTo(x, y + h, x, y + h - r);
  ctx.lineTo(x, y + r);
  ctx.quadraticCurveTo(x, y, x + r, y);
  ctx.closePath();
}

// ═══════════════════════════════════════════════════════════ STATE
let activePaletteIdx = 0;
let layerVisible = {};
LAYERS.forEach(l => layerVisible[l.id] = true);

// ═══════════════════════════════════════════════════════════ RENDERING

function drawLayerToCanvas(canvas, layerId, palette, transparent = true) {
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, 600, 600);
  const layer = LAYERS.find(l => l.id === layerId);
  if (layer) layer.draw(ctx, palette);
}

function drawComposite(canvas, palette) {
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, 600, 600);
  // checkerboard bg so transparency is obvious
  ctx.fillStyle = "#14141a"; ctx.fillRect(0, 0, 600, 600);
  LAYERS.forEach(layer => {
    if (layerVisible[layer.id]) layer.draw(ctx, palette);
  });
  // watermark
  ctx.font = "400 11px 'Space Grotesk', Arial";
  ctx.textAlign = "center"; ctx.fillStyle = "rgba(255,255,255,0.25)";
  ctx.fillText("404BOT · HYPERLIQUID · " + palette.name.toUpperCase(), 300, 588);
}

// ═══════════════════════════════════════════════════════════ THUMBNAILS

const thumbCanvases = {};

function renderThumb(layerId) {
  const palette = PALETTES[activePaletteIdx];
  const c = thumbCanvases[layerId];
  if (!c) return;
  drawLayerToCanvas(c, layerId, palette, true);
}

function renderAllThumbs() {
  LAYERS.forEach(l => renderThumb(l.id));
}

function refreshComposite() {
  const palette = PALETTES[activePaletteIdx];
  drawComposite(document.getElementById('compositeCanvas'), palette);
}

// ═══════════════════════════════════════════════════════════ BUILD UI

function buildPaletteButtons() {
  const row = document.getElementById('paletteRow');
  PALETTES.forEach((p, i) => {
    const btn = document.createElement('button');
    btn.className = 'palette-btn' + (i === 0 ? ' active' : '');
    btn.textContent = p.name;
    btn.style.setProperty('--a', p.accent);
    if (i === 0) { btn.style.borderColor = p.accent; btn.style.color = p.accent; }
    btn.onclick = () => {
      document.querySelectorAll('.palette-btn').forEach((b, j) => {
        b.classList.toggle('active', j === i);
        b.style.borderColor = j === i ? PALETTES[j].accent : '#333';
        b.style.color = j === i ? PALETTES[j].accent : '#aaa';
      });
      activePaletteIdx = i;
      document.getElementById('activePaletteName').textContent = p.name;
      renderAllThumbs();
      refreshComposite();
    };
    row.appendChild(btn);
  });
}

function buildLayerCards() {
  const grid = document.getElementById('layersGrid');
  grid.innerHTML = '';
  LAYERS.forEach(layer => {
    const card = document.createElement('div');
    card.className = 'layer-card visible';
    card.id = 'card-' + layer.id;

    const thumb = document.createElement('div');
    thumb.className = 'layer-thumb';

    const c = document.createElement('canvas');
    c.width = 600; c.height = 600;
    thumbCanvases[layer.id] = c;
    thumb.appendChild(c);

    const info = document.createElement('div');
    info.className = 'layer-info';
    info.innerHTML = `<div class="layer-name">${layer.name}</div><div class="layer-desc">${layer.desc}</div>`;

    const actions = document.createElement('div');
    actions.className = 'layer-actions';

    const visBtn = document.createElement('button');
    visBtn.className = 'btn-vis on';
    visBtn.innerHTML = '<span class="eye">👁</span> Show';
    visBtn.onclick = () => toggleLayer(layer.id, visBtn, card);

    const dlBtn = document.createElement('button');
    dlBtn.className = 'btn-dl';
    dlBtn.textContent = '↓ PNG';
    dlBtn.onclick = () => downloadSingleLayer(layer.id);

    actions.appendChild(visBtn); actions.appendChild(dlBtn);
    card.appendChild(thumb); card.appendChild(info); card.appendChild(actions);
    grid.appendChild(card);
  });
}

function toggleLayer(id, btn, card) {
  layerVisible[id] = !layerVisible[id];
  btn.classList.toggle('on', layerVisible[id]);
  btn.innerHTML = `<span class="eye">${layerVisible[id] ? '👁' : '🚫'}</span> ${layerVisible[id] ? 'Show' : 'Hide'}`;
  card.classList.toggle('visible', layerVisible[id]);
  refreshComposite();
}

// ═══════════════════════════════════════════════════════════ EXPORT

function downloadSingleLayer(layerId) {
  const palette = PALETTES[activePaletteIdx];
  const offCtx = document.getElementById('offscreen').getContext('2d');
  offCtx.clearRect(0, 0, 600, 600);
  const layer = LAYERS.find(l => l.id === layerId);
  if (layer) layer.draw(offCtx, palette);
  document.getElementById('offscreen').toBlob(blob => {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = `404bot-${palette.id}-${layerId}.png`; a.click();
    URL.revokeObjectURL(url);
  });
}

async function exportAll() {
  const palette = PALETTES[activePaletteIdx];
  const fill = document.getElementById('progressFill');
  const msg = document.getElementById('statusMsg');

  // Export each layer
  for (let i = 0; i < LAYERS.length; i++) {
    const layer = LAYERS[i];
    msg.textContent = `Exporting: ${layer.name} (${i+1}/${LAYERS.length+1})…`;
    fill.style.width = ((i / (LAYERS.length + 1)) * 100) + '%';

    await new Promise(resolve => {
      const offCtx = document.getElementById('offscreen').getContext('2d');
      offCtx.clearRect(0, 0, 600, 600);
      layer.draw(offCtx, palette);
      document.getElementById('offscreen').toBlob(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `404bot-${palette.id}-${String(i+1).padStart(2,'0')}-${layer.id}.png`;
        a.click();
        URL.revokeObjectURL(url);
        setTimeout(resolve, 120); // small gap between downloads
      });
    });
  }

  // Also export composite
  const offCtx = document.getElementById('offscreen').getContext('2d');
  offCtx.clearRect(0, 0, 600, 600);
  LAYERS.forEach(l => l.draw(offCtx, palette));
  offCtx.font = "400 11px Arial";
  offCtx.textAlign = "center"; offCtx.fillStyle = "rgba(255,255,255,0.25)";
  offCtx.fillText("404BOT · HYPERLIQUID · " + palette.name.toUpperCase(), 300, 588);
  document.getElementById('offscreen').toBlob(blob => {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = `404bot-${palette.id}-COMPOSITE.png`; a.click();
    URL.revokeObjectURL(url);
  });

  fill.style.width = '100%';
  msg.textContent = `✓ All ${LAYERS.length + 1} files exported for "${palette.name}"`;
  setTimeout(() => { fill.style.width = '0%'; msg.textContent = 'Ready.'; }, 3000);
}

// ═══════════════════════════════════════════════════════════ INIT
buildPaletteButtons();
buildLayerCards();
setTimeout(() => {
  renderAllThumbs();
  refreshComposite();
}, 50);
</script>
</body>
</html>
