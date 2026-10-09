
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
    if (vs) {
      const r = vs.getBoundingClientRect();
      const v = Math.min(Math.max((innerHeight - r.top) / (innerHeight + r.height), 0), 1);
      vs.style.setProperty('--vp', (v - 0.5).toFixed(3));
    }
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
  // Reserve the height of the tallest word so the phones below never jump.
  if (rot) {
    const h1 = rot.closest('h1');
    const lock = () => {
      const now = rot.textContent; h1.style.minHeight = '';
      let max = 0;
      rot.dataset.words.split('|').forEach(w => { rot.textContent = w; max = Math.max(max, h1.offsetHeight); });
      rot.textContent = now; h1.style.minHeight = max + 'px';
    };
    lock(); addEventListener('resize', lock);
    if (document.fonts) document.fonts.ready.then(lock);
  }
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

(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Headlines: words rise out of an invisible line, one after another.
  const split = (el) => {
    let k = 0;
    const walk = (node) => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            const w = document.createElement('span'); w.className = 'w';
            const i = document.createElement('span'); i.textContent = part; i.style.transitionDelay = (k++ * 0.06) + 's';
            w.appendChild(i); frag.appendChild(w);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1) walk(n);
      });
    };
    walk(el);
  };
  if (!reduce) {
    const heads = document.querySelectorAll('.split');
    heads.forEach(split);
    const ho = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('up'); ho.unobserve(e.target); }
    }), { threshold: 0.3 });
    heads.forEach(h => ho.observe(h));
  }

  // ── "How we build": words light up as you scroll through the section.
  const lit = document.getElementById('lit');
  if (lit) {
    if (!reduce) split(lit);
    const words = [...lit.querySelectorAll('.w')];
    lit.querySelectorAll('.w > span').forEach(s => s.style.transitionDelay = '0s');
    const sec = lit.closest('section');
    // Each word lights when its own line crosses a reading line on screen,
    // sweeping left to right across the line — so the light follows the eye.
    let pos = [];
    const measure = () => {
      const r = lit.getBoundingClientRect();
      pos = words.map(w => { const b = w.getBoundingClientRect(); return b.top - r.top + (b.left - r.left) / r.width * b.height; });
    };
    const paint = () => {
      const top = lit.getBoundingClientRect().top, line = innerHeight * 0.75;
      const end = scrollY + innerHeight >= document.documentElement.scrollHeight - 4;
      words.forEach((w, i) => w.classList.toggle('on', end || top + pos[i] < line));
    };
    if (reduce) words.forEach(w => w.classList.add('on'));
    else {
      const re = () => { measure(); paint(); };
      addEventListener('scroll', paint, { passive: true }); addEventListener('resize', re); re();
      if (document.fonts) document.fonts.ready.then(re);
    }
  }

  // ── Services: a colored bubble with the service icon follows the pointer.
  const list = document.getElementById('svcList'), cur = document.getElementById('svcCursor');
  const icons = {
    web: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="2.5"/><path d="M3 8h18M8 21h8M12 18v3"/></svg>',
    cart: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h2l2.2 10.2a2 2 0 0 0 2 1.6h6.9a2 2 0 0 0 1.9-1.5L21 8H7"/><circle cx="10" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/></svg>',
    phone: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6.5" y="2.5" width="11" height="19" rx="2.8"/><path d="M10.5 5.5h3"/></svg>',
    care: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12a8 8 0 1 1-2.3-5.7M20 4v4h-4"/></svg>',
    social: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".9" fill="currentColor"/></svg>'
  };
  // ── Contact: pick what you need; a service row preselects its chip.
  const pick = document.getElementById('pick'), mail = document.getElementById('mailBtn');
  if (pick && mail) {
    const chips = [...pick.querySelectorAll('button')];
    const sync = () => {
      const sel = chips.filter(c => c.getAttribute('aria-pressed') === 'true').map(c => c.textContent.trim());
      const subj = mail.dataset.subj + (sel.length ? ': ' + sel.join(', ') : '');
      mail.href = 'mailto:enes@beyazlabs.com?subject=' + encodeURIComponent(subj) +
        '&body=' + encodeURIComponent(decodeURIComponent(mail.dataset.body));
    };
    chips.forEach(c => c.addEventListener('click', () => {
      c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); sync();
    }));
    document.querySelectorAll('.svc-list .go').forEach(a => a.addEventListener('click', () => {
      const c = chips.find(c => c.dataset.k === a.dataset.pick);
      if (!c) return;
      c.setAttribute('aria-pressed', 'true'); sync();
      c.classList.remove('flash'); void c.offsetWidth; c.classList.add('flash');
    }));
  }

  if (list && cur && !reduce && matchMedia('(hover: hover) and (min-width: 861px)').matches) {
    let x = 0, y = 0, tx = 0, ty = 0, raf = 0;
    const loop = () => { x += (tx - x) * 0.18; y += (ty - y) * 0.18; cur.style.transform = `translate(${x}px, ${y}px)`; raf = requestAnimationFrame(loop); };
    list.querySelectorAll('.row').forEach(r => {
      r.addEventListener('pointerenter', () => {
        cur.innerHTML = icons[r.dataset.ic] || '';
        cur.style.setProperty('--c', getComputedStyle(r).getPropertyValue('--c'));
        cur.classList.add('on');
      });
    });
    list.addEventListener('pointermove', e => { tx = e.clientX; ty = e.clientY; });
    list.addEventListener('pointerenter', e => { x = tx = e.clientX; y = ty = e.clientY; if (!raf) loop(); });
    list.addEventListener('pointerleave', () => { cur.classList.remove('on'); cancelAnimationFrame(raf); raf = 0; });
  }
})();
