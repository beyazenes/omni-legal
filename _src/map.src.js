// Ofis haritası: OSM bina tabanları canvas'ta yükseltilir; ofis pembe yanar, imleçle hafifçe döner.
// Dış istek yok — veri bu dosyanın içinde (window.OFFICE_MAP, officemap.py basar).
(() => {
  const M = window.OFFICE_MAP, cv = document.getElementById('officeMap');
  if (!M || !cv || !cv.getContext) return;
  const pin = document.getElementById('officePin');
  const ctx = cv.getContext('2d');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const R = M.r;

  // Binaları hazırla: noktalar saat yönünün tersine dizilsin ki duvar normalleri dışa baksın
  const B = M.b.map(b => {
    const p = [];
    for (let i = 0; i < b.p.length; i += 2) p.push([b.p[i], b.p[i + 1]]);
    let a = 0;
    for (let i = 0; i < p.length; i++) { const q = p[i], r = p[(i + 1) % p.length]; a += q[0] * r[1] - r[0] * q[1]; }
    if (a < 0) p.reverse();
    const cx = p.reduce((s, q) => s + q[0], 0) / p.length, cy = p.reduce((s, q) => s + q[1], 0) / p.length;
    return { p, h: b.h, o: !!b.o, cx, cy };
  });
  const office = B.find(b => b.o);
  const roads = M.r2.map(r => {
    const p = [];
    for (let i = 0; i < r.p.length; i += 2) p.push([r.p[i] - office.cx, r.p[i + 1] - office.cy]);
    return { p, w: r.w };
  });
  B.forEach(b => { b.p = b.p.map(q => [q[0] - office.cx, q[1] - office.cy]); b.cx -= office.cx; b.cy -= office.cy; });

  const PITCH = 1.0, YAW = -0.42;      // ~57° yukarıdan: binalar arkadaki yollara yatmasın
  let yaw = YAW, pitch = PITCH, ty = YAW, tp = PITCH, W = 0, H = 0, dpr = 1, s = 1, ox = 0, oy = 0;
  let running = false, visible = false, t0 = performance.now();

  const resize = () => {
    const r = cv.getBoundingClientRect();
    dpr = Math.min(devicePixelRatio || 1, 2);
    W = r.width; H = r.height;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    s = Math.min(W, H * 1.25) / (R * 1.55);
    ox = W / 2; oy = H * 0.6;
    draw();
  };

  const proj = (x, y, z, c, sn, cp, sp) => {
    const xr = x * c - y * sn, yr = x * sn + y * c;
    return [ox + xr * s, oy - (yr * sp + z * cp) * s, yr];
  };
  const mix = (a, b, t) => a.map((v, i) => Math.round(v + (b[i] - v) * t));
  const rgb = a => `rgb(${a[0]},${a[1]},${a[2]})`;

  function draw() {
    if (!W) return;
    const c = Math.cos(yaw), sn = Math.sin(yaw), cp = Math.cos(pitch), sp = Math.sin(pitch);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.lineJoin = 'round'; ctx.lineCap = 'round';

    // Yollar: zeminde ince ışık çizgileri
    roads.forEach(r => {
      ctx.beginPath();
      r.p.forEach((q, i) => { const P = proj(q[0], q[1], 0, c, sn, cp, sp); i ? ctx.lineTo(P[0], P[1]) : ctx.moveTo(P[0], P[1]); });
      ctx.strokeStyle = r.w === 2 ? 'rgba(255,255,255,.10)' : 'rgba(255,255,255,.055)';
      ctx.lineWidth = (r.w === 2 ? 7 : 3.5) * s;
      ctx.stroke();
      if (r.w === 2) { ctx.strokeStyle = 'rgba(254,44,85,.35)'; ctx.lineWidth = Math.max(1, .8 * s); ctx.stroke(); }
    });

    // Binalar: uzaktan yakına (ressam algoritması)
    const L = [Math.cos(yaw + 2.2), Math.sin(yaw + 2.2)];   // ışık kameraya göre sabit yönden
    // sıralama anahtarı: kameraya en yakın köşe (merkez uzun binalarda yanıltıyor)
    const order = B.map(b => [b, Math.min(...b.p.map(q => q[0] * sn + q[1] * c))]).sort((a, b) => (a[0].o - b[0].o) || (b[1] - a[1]));   // ofis en yüksek: hep en son çizilir
    for (const [b] of order) {
      const base = b.o ? [254, 44, 85] : [26, 17, 21], top = b.o ? [255, 120, 140] : [40, 28, 33];
      const n = b.p.length;
      if (b.o) { ctx.shadowColor = 'rgba(254,44,85,.65)'; ctx.shadowBlur = 28; }
      for (let i = 0; i < n; i++) {
        const a = b.p[i], d = b.p[(i + 1) % n];
        const nx = d[1] - a[1], ny = -(d[0] - a[0]);           // dış normal
        if (nx * sn + ny * c > 0) continue;                      // kameraya bakmayan duvar
        const ln = Math.hypot(nx, ny) || 1;
        const lit = .5 + .5 * ((nx * L[0] + ny * L[1]) / ln);
        const P1 = proj(a[0], a[1], 0, c, sn, cp, sp), P2 = proj(d[0], d[1], 0, c, sn, cp, sp);
        const P3 = proj(d[0], d[1], b.h, c, sn, cp, sp), P4 = proj(a[0], a[1], b.h, c, sn, cp, sp);
        ctx.beginPath(); ctx.moveTo(P1[0], P1[1]); ctx.lineTo(P2[0], P2[1]); ctx.lineTo(P3[0], P3[1]); ctx.lineTo(P4[0], P4[1]); ctx.closePath();
        ctx.fillStyle = rgb(b.o ? mix([150, 18, 48], base, lit) : mix([14, 9, 11], base, .3 + lit * .9));
        ctx.fill();
        ctx.strokeStyle = b.o ? 'rgba(255,200,210,.35)' : 'rgba(255,255,255,.05)'; ctx.lineWidth = 1; ctx.stroke();
      }
      ctx.beginPath();
      b.p.forEach((q, i) => { const P = proj(q[0], q[1], b.h, c, sn, cp, sp); i ? ctx.lineTo(P[0], P[1]) : ctx.moveTo(P[0], P[1]); });
      ctx.closePath();
      if (b.o) {
        const g = ctx.createLinearGradient(ox - 30 * s, oy, ox + 30 * s, oy);
        g.addColorStop(0, '#FF6A88'); g.addColorStop(1, '#FF9F0A');
        ctx.fillStyle = g;
      } else ctx.fillStyle = rgb(top);
      ctx.fill();
      ctx.strokeStyle = b.o ? 'rgba(255,255,255,.6)' : 'rgba(255,255,255,.12)'; ctx.lineWidth = 1; ctx.stroke();
      ctx.shadowBlur = 0;
    }

    // Kenarlar karanlığa karışsın
    ctx.globalCompositeOperation = 'destination-in';
    const g = ctx.createRadialGradient(ox, oy - 10, 0, ox, oy - 10, Math.max(W, H) * .62);
    g.addColorStop(0, '#000'); g.addColorStop(.55, 'rgba(0,0,0,.9)'); g.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    ctx.globalCompositeOperation = 'source-over';

    // Pin: çatıdan yükselen ince çizgi + HTML etiket
    const bob = reduce ? 0 : Math.sin((performance.now() - t0) / 900) * 1.2;
    const roof = proj(0, 0, office.h, c, sn, cp, sp), head = [roof[0], roof[1] - 58 - bob * 3];   // pin her ekranda binanın üstünde, aynı mesafede
    const lg = ctx.createLinearGradient(0, roof[1], 0, head[1]);
    lg.addColorStop(0, 'rgba(255,255,255,0)'); lg.addColorStop(1, 'rgba(255,255,255,.85)');
    ctx.strokeStyle = lg; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(roof[0], roof[1]); ctx.lineTo(head[0], head[1]); ctx.stroke();
    ctx.fillStyle = 'rgba(255,255,255,.9)'; ctx.beginPath(); ctx.arc(roof[0], roof[1], 2.2, 0, 7); ctx.fill();
    if (pin) pin.style.transform = `translate(${head[0].toFixed(1)}px, ${head[1].toFixed(1)}px)`;
  }

  const tick = () => {
    if (!visible) { running = false; return; }
    const t = performance.now() - t0;
    const iy = ty + Math.sin(t / 6000) * .08;
    yaw += (iy - yaw) * .06; pitch += (tp - pitch) * .06;
    draw();
    requestAnimationFrame(tick);
  };
  const start = () => { if (!running && !reduce) { running = true; requestAnimationFrame(tick); } };

  new ResizeObserver(resize).observe(cv);
  new IntersectionObserver(es => es.forEach(e => { visible = e.isIntersecting; if (visible) start(); })).observe(cv);
  if (!reduce && matchMedia('(hover: hover)').matches) {
    const box = cv.parentElement;
    box.addEventListener('pointermove', e => {
      const r = box.getBoundingClientRect();
      ty = YAW + ((e.clientX - r.left) / r.width - .5) * .7;
      tp = PITCH + ((e.clientY - r.top) / r.height - .5) * -.12;
    });
    box.addEventListener('pointerleave', () => { ty = YAW; tp = PITCH; });
  }
  resize();
})();
