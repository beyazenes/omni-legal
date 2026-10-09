
(() => {
  document.documentElement.classList.add('js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Reveal on scroll — content is visible by default; only hidden once JS runs.
  const io = new IntersectionObserver((es) => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.top < innerHeight) el.classList.add('in'); else io.observe(el);
  });

  // Hero phones fold flat as you scroll.
  const stage = document.getElementById('stage');
  const hero = document.querySelector('.hero');
  const vs = document.getElementById('versedShots');
  let ticking = false;
  const onScroll = () => {
    ticking = false;
    if (reduce) return;
    const p = Math.min(Math.max(scrollY / (innerHeight * 0.8), 0), 1);
    hero.style.setProperty('--p', p.toFixed(3));
    stage.style.setProperty('--lift', (p * 120).toFixed(1));
    const r = vs.getBoundingClientRect();
    const v = Math.min(Math.max((innerHeight - r.top) / (innerHeight + r.height), 0), 1);
    vs.style.setProperty('--vp', (v - 0.5).toFixed(3));
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // Omni story: the active step is read from scroll position on every frame,
  // so scrolling down and back up always lands on the same screen.
  const stack = document.getElementById('pinScreen');
  const shots = [...stack.querySelectorAll('.scr img')];
  const halo = document.getElementById('halo');
  const steps = [...document.querySelectorAll('.step')];
  let cur = 0;
  const pick = () => {
    const mobile = matchMedia('(max-width: 860px)').matches;
    const line = innerHeight * (mobile ? 0.78 : 0.55);
    let i = 0;
    steps.forEach((s, k) => { if (s.getBoundingClientRect().top < line) i = k; });
    if (i === cur) return;
    stack.classList.toggle('rev', i < cur);
    shots.forEach((im, k) => { im.classList.toggle('was', k === cur); im.classList.toggle('on', k === i); });
    steps.forEach((s, k) => s.classList.toggle('on', k === i));
    halo.style.setProperty('--halo', steps[i].dataset.halo);
    cur = i;
  };
  // Doğrudan (rAF'siz): dört dikdörtgen okumak ucuz ve iOS Safari'nin
  // momentum kaydırmasında bile ekran yazıyla aynı anda değişiyor.
  addEventListener('scroll', pick, { passive: true });
  addEventListener('resize', pick);
  pick();
})();

document.querySelectorAll('.lang a').forEach(a => a.addEventListener('click', () => {
  try { localStorage.setItem('lang', a.dataset.l); } catch (e) {}
}));
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Rotating headline word
  const rot = document.querySelector('.hero h1 .rot');
  if (rot && !reduce) {
    const words = rot.dataset.words.split('|'); let i = 0;
    setInterval(() => {
      rot.classList.add('out');
      setTimeout(() => {
        i = (i + 1) % words.length; rot.textContent = words[i];
        rot.classList.remove('out'); rot.classList.add('pre');
        void rot.offsetWidth; rot.classList.remove('pre');
      }, 450);
    }, 2800);
  }
  if (reduce || !matchMedia('(hover: hover)').matches) return;
  // Hero glow follows pointer
  const hero = document.querySelector('.hero');
  hero.addEventListener('pointermove', e => {
    const r = hero.getBoundingClientRect();
    hero.style.setProperty('--gx', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%');
    hero.style.setProperty('--gy', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%');
  });
  // Card spotlight + tilt
  document.querySelectorAll('.svc .c').forEach(c => {
    c.addEventListener('pointermove', e => {
      const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      c.style.setProperty('--mx', (x * 100) + '%'); c.style.setProperty('--my', (y * 100) + '%');
      c.style.setProperty('--ry', ((x - .5) * 6).toFixed(2) + 'deg'); c.style.setProperty('--rx', ((.5 - y) * 6).toFixed(2) + 'deg');
    });
    c.addEventListener('pointerleave', () => { c.style.setProperty('--rx', '0deg'); c.style.setProperty('--ry', '0deg'); });
  });
})();
