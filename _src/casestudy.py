# -*- coding: utf-8 -*-
# Builds the Omni Health case study: /tr/omni/ and /en/omni/
# Every claim here is something the shipped app actually does — no invented metrics.
import os, time
VER = time.strftime('%Y%m%d%H%M')

PAGE = '''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0709">
<link rel="canonical" href="https://beyazlabs.com/{lang}/omni/">
<link rel="alternate" hreflang="en" href="https://beyazlabs.com/en/omni/">
<link rel="alternate" hreflang="tr" href="https://beyazlabs.com/tr/omni/">
<link rel="icon" href="../../img/omni-icon.png">
<link rel="apple-touch-icon" href="../../img/omni-icon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://beyazlabs.com/img/{shot}omni-today.png">
<link rel="stylesheet" href="../../site.css?v={ver}">
</head>
<body>
  <nav class="top" aria-label="Main">
    <div class="wrap">
      <a class="brand" href="../">Beyaz <span>Labs</span></a>
      <ul>
        <li class="hide-m"><a href="../#services">{nav_services}</a></li>
        <li><a href="../#work">{nav_work}</a></li>
        <li class="hide-m"><a href="../#contact">{nav_contact}</a></li>
        <li><span class="lang" aria-label="Language">
          <a href="../../en/omni/" data-l="en" hreflang="en" lang="en" {cur_en}>EN</a>
          <a href="../../tr/omni/" data-l="tr" hreflang="tr" lang="tr" {cur_tr}>TR</a>
        </span></li>
      </ul>
    </div>
  </nav>

  <header class="hero cs-hero">
    <div class="wrap copy" id="heroCopy">
      <img class="cs-icon" src="../../img/omni-icon.png" alt="{icon_alt}" width="72" height="72">
      <p class="avail"><span class="mark" aria-hidden="true"></span>{kicker}</p>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="cs-cta">
        <a class="badge-link" href="https://apps.apple.com/app/id6775592612" aria-label="{badge_aria}">
          <img src="../../img/app-store-badge.svg" alt="Download on the App Store" width="160" height="53">
        </a>
      </div>
    </div>
    <div class="stage" id="stage" aria-hidden="true">
      <img class="device d1" src="../../img/{shot}omni-rhythm.png" alt="">
      <img class="device d2" src="../../img/{shot}omni-today.png" alt="">
      <img class="device d3" src="../../img/{shot}omni-cook.png" alt="">
    </div>
  </header>

  <section class="cs-stats" aria-label="{stats_label}">
    <div class="wrap">
      <dl>
        {stats}
      </dl>
    </div>
  </section>

  <section class="cs-story">
    <div class="wrap">
      <p class="eyebrow reveal">{story_eyebrow}</p>
      <h2 class="sec-h reveal split">{story_h}</h2>
      <div class="cs-rows">
        {rows}
      </div>
    </div>
  </section>

  <section class="cs-decisions">
    <div class="wrap">
      <p class="eyebrow reveal">{dec_eyebrow}</p>
      <h2 class="sec-h reveal split">{dec_h}</h2>
      <div class="cs-dec">
        {decisions}
      </div>
    </div>
  </section>

  <section class="cs-craft">
    <div class="wrap">
      <p class="eyebrow reveal">{craft_eyebrow}</p>
      <h2 class="sec-h reveal split">{craft_h}</h2>
      <div class="cs-craft-grid">
        <figure class="reveal"><img src="../../img/{shot}omni-rhythm.png" alt="{fig1_alt}" loading="lazy"><figcaption>{fig1}</figcaption></figure>
        <figure class="reveal"><img src="../../img/{shot}omni-recipe.png" alt="{fig2_alt}" loading="lazy"><figcaption>{fig2}</figcaption></figure>
        <figure class="reveal"><img src="../../img/{shot}omni-cook.png" alt="{fig3_alt}" loading="lazy"><figcaption>{fig3}</figcaption></figure>
      </div>
      <ul class="cs-list">
        {craft}
      </ul>
    </div>
  </section>

  <section class="cs-you">
    <div class="wrap">
      <p class="eyebrow reveal">{you_eyebrow}</p>
      <h2 class="sec-h reveal split">{you_h}</h2>
      <div class="cs-cols">
        {you}
      </div>
    </div>
  </section>

  <section class="contact" id="contact">
    <div class="wrap">
      <div class="box reveal">
        <p class="eyebrow">{ct_eyebrow}</p>
        <h2 class="split">{ct_h}</h2>
        <p>{ct_p}</p>
        <div class="actions">
          <a class="btn-light" href="../?svc=phone#contact">{ct_btn} <span aria-hidden="true">→</span></a>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="wrap">
      <div class="legal">
        <span>© 2026 Beyaz Labs. <a href="../../privacypolicy.html">{l_privacy}</a> · <a href="../../support.html">{l_support}</a></span>
        <span><a href="../">{back}</a></span>
      </div>
    </div>
  </footer>
<script src="../../site.js?v={ver}"></script>
</body>
</html>
'''

def stats(xs): return ''.join('<div class="reveal"><dt>%s</dt><dd>%s</dd></div>' % x for x in xs)
def rows(xs): return ''.join('<div class="cs-row reveal"><span class="k">%s</span><h3>%s</h3><p>%s</p></div>' % x for x in xs)
def decs(xs): return ''.join('<article class="reveal" style="--c:%s"><span class="tag">%s</span><h3>%s</h3><p>%s</p></article>' % x for x in xs)
def lis(xs): return ''.join('<li class="reveal"><b>%s</b> %s</li>' % x for x in xs)
def cols(xs): return ''.join('<div class="reveal"><h3>%s</h3><p>%s</p></div>' % x for x in xs)

TR = dict(lang='tr', shot='tr/', cur_tr='aria-current="true"', cur_en='',
  title='Omni Health proje hikâyesi — Beyaz Labs',
  desc='Omni Health’i tasarımdan koda, çeviriden App Store’a kadar Beyaz Labs yaptı. Bir uygulamaya nasıl yaklaştığımızın hikâyesi.',
  nav_services='Hizmetler', nav_work='İşlerimiz', nav_contact='İletişim',
  icon_alt='Omni Health uygulama ikonu', kicker='Proje hikâyesi · Omni Health',
  h1='Bir diyetisyen gibi düşünen uygulama.',
  lead='<span>Omni Health’i tasarımdan koda, çeviriden App Store’a kadar baştan sona biz yaptık.</span> <span>Bir uygulamaya nasıl yaklaştığımızı en iyi o anlatır.</span>',
  badge_aria='Omni Health’i App Store’dan indirin',
  stats_label='Kısaca Omni Health',
  stats=stats([('22','dilde yayında'),('6','büyük sürüm, 1.0’dan 1.5’e'),('3','cihaz: iPhone, iPad, Apple Watch'),('0','reklam ya da takip aracı')]),
  story_eyebrow='Hikâye', story_h='Veri değil, <em>bir sonraki adım.</em>',
  rows=rows([
    ('Sorun','Sağlık uygulamaları veri gösterir, karar vermez.','Çoğu beslenme uygulaması günü halkalara, grafiklere ve yüzdelere böler. Veri oradadır ama “şimdi ne yapmalıyım?” sorusunun cevabı yoktur.'),
    ('Yaklaşım','Grafik yerine tek bir cümle.','Omni gününüzü Apple Sağlık’tan okur (su, öğünler, antrenman ve uyku) ve sıradaki en anlamlı adımı tek cümleyle söyler. Bir diyetisyenin yapacağı gibi: önce dinler, sonra önerir.'),
    ('Ürün','22 dilde, App Store’da.','Omni bugün iPhone, iPad ve Apple Watch’ta yayında. 2026 boyunca altı büyük sürümle büyüdü; her sürüm, bir öncekinde öğrendiklerimizle şekillendi.'),
  ]),
  dec_eyebrow='Kararlar', dec_h='İyi ürün, <em>verilen kararlardır.</em>',
  decisions=decs([
    ('#FE2C55','12 sayfa → 2 adım','İlk açılışı kısalttık.','Başlangıç 12 sayfalık bir anketti. Gerekmeyen her soruyu çıkardık; artık iki adımda başlıyorsunuz.'),
    ('#7ACB00','Bilmiyorsa söyler','Tahmin yerine dürüstlük.','Döngü takibi, veriler düzensizken tarih tahmin etmez; hâlâ öğrendiğini açıkça söyler. Yanlış bir tarih, hiç tarih vermemekten kötüdür.'),
    ('#00C7BE','İsteğe bağlı','Yapay zekâ sizin seçiminiz.','Kişisel öneriler yalnızca kullanıcı açarsa çalışır. İstekler App Attest ile korunur, kullanım adil bir haftalık kotayla sınırlanır.'),
    ('#FF9F0A','Reklam yok','Takip de yok.','Uygulamada reklam ya da üçüncü taraf analitik yok. Sağlık verileri cihazda ve Apple Sağlık’ta kalır.'),
  ]),
  craft_eyebrow='Zanaat', craft_h='Görünmeyen işler <em>de dahil.</em>',
  fig1='Ritim: bu hafta, geçen haftayla yan yana.', fig1_alt='Omni Health Ritim ekranı',
  fig2='Günün tarifi, gününüze göre seçilir.', fig2_alt='Omni Health tarif ekranı',
  fig3='Pişirme modu: adım adım, zamanlayıcıyla.', fig3_alt='Omni Health pişirme modu',
  craft=lis([
    ('Apple Sağlık ile iki yönlü senkron.','Su, öğün, antrenman ve uyku; silmeler dahil.'),
    ('Apple Watch uygulaması.','Bileğinizden su ve öğün kaydı.'),
    ('Live Activity zamanlayıcıları.','Pişirirken kilit ekranında geri sayım.'),
    ('Widget’lar ve Siri.','Uygulamayı açmadan kayıt.'),
    ('Kamerayla öğün tarama.','Tabaktaki birden fazla yiyecek ve barkodlar.'),
    ('iPad için ayrı yerleşim.','Büyük ekranda büyük ekran gibi davranır.'),
    ('22 dil.','Uygulama da App Store sayfaları da yerelleştirildi.'),
  ]),
  you_eyebrow='Sizin projeniz', you_h='Aynı özen, <em>sizin uygulamanızda.</em>',
  you=cols([
    ('Kapsamı birlikte daraltırız.','İlk sürüm küçük ve sağlam olur. Gerisi, gerçek kullanıcılardan öğrendiklerimizle gelir.'),
    ('Mağaza sürecini biliyoruz.','App Store incelemesi, ret gerekçeleri, gizlilik etiketleri, sürüm notları… Hepsini yaşadık. Uygulamanızı yayına kadar biz götürürüz.'),
    ('Yayın bitiş değil.','Omni gibi sizin uygulamanız da düzenli güncellemelerle büyür. Yayından sonra da yanınızdayız.'),
  ]),
  ct_eyebrow='Konuşalım', ct_h='Bir uygulama fikriniz mi var?',
  ct_p='Fikrinizi birkaç cümleyle anlatın; nereden başlayabileceğimizi birlikte konuşalım.',
  ct_btn='Fikrimi anlatayım', l_privacy='Omni Gizlilik', l_support='Omni Destek', back='Ana sayfaya dön')

EN = dict(lang='en', shot='', cur_en='aria-current="true"', cur_tr='',
  title='Omni Health case study — Beyaz Labs',
  desc='Beyaz Labs designed, built, translated and shipped Omni Health. The story of how we approach an app.',
  nav_services='Services', nav_work='Work', nav_contact='Contact',
  icon_alt='Omni Health app icon', kicker='Case study · Omni Health',
  h1='An app that thinks like a dietitian.',
  lead='<span>We made Omni Health end to end, from design and code to translation and the App Store.</span> <span>It shows how we approach an app better than anything we could write.</span>',
  badge_aria='Download Omni Health on the App Store',
  stats_label='Omni Health at a glance',
  stats=stats([('22','languages, live'),('6','major releases, 1.0 to 1.5'),('3','devices: iPhone, iPad, Apple Watch'),('0','ads or trackers')]),
  story_eyebrow='The story', story_h='Not more data. <em>The next step.</em>',
  rows=rows([
    ('The problem','Health apps show data. They don’t decide.','Most nutrition apps split the day into rings, charts and percentages. The data is there, but the answer to “what should I do now?” isn’t.'),
    ('The approach','One sentence instead of a chart.','Omni reads your day from Apple Health (water, meals, workouts and sleep) and tells you the one thing worth doing next, in a single sentence. Like a dietitian: listen first, then suggest.'),
    ('The product','Live in 22 languages.','Omni is on iPhone, iPad and Apple Watch today. It grew through six major releases in 2026, each shaped by what we learned from the one before.'),
  ]),
  dec_eyebrow='Decisions', dec_h='Good products are <em>decisions.</em>',
  decisions=decs([
    ('#FE2C55','12 screens → 2 steps','A shorter first launch.','Onboarding used to be a 12-page questionnaire. We cut every question we didn’t need; now you’re in after two steps.'),
    ('#7ACB00','Says when it doesn’t know','Honesty over guesses.','With irregular data, cycle tracking doesn’t predict dates; it says it’s still learning. A wrong date is worse than none.'),
    ('#00C7BE','Opt-in AI','Your call, not ours.','Personal suggestions only run if you turn them on. Requests are protected with App Attest and kept fair with a weekly quota.'),
    ('#FF9F0A','No ads','No tracking either.','No ads and no third-party analytics in the app. Health data stays on the device and in Apple Health.'),
  ]),
  craft_eyebrow='Craft', craft_h='Including the parts <em>you never see.</em>',
  fig1='Rhythm: this week next to last week.', fig1_alt='Omni Health Rhythm screen',
  fig2='A recipe chosen for your day.', fig2_alt='Omni Health recipe screen',
  fig3='Cook mode: step by step, with timers.', fig3_alt='Omni Health cook mode',
  craft=lis([
    ('Two-way Apple Health sync.','Water, meals, workouts and sleep, deletions included.'),
    ('An Apple Watch app.','Log water and meals from your wrist.'),
    ('Live Activity timers.','A countdown on the Lock Screen while you cook.'),
    ('Widgets and Siri.','Log without opening the app.'),
    ('Meal scanning with the camera.','Several foods on one plate, and barcodes.'),
    ('A real iPad layout.','A big screen that behaves like one.'),
    ('22 languages.','The app and its App Store pages are both localised.'),
  ]),
  you_eyebrow='Your project', you_h='The same care, <em>in your app.</em>',
  you=cols([
    ('We narrow the scope together.','The first version is small and solid. The rest comes from what real users teach us.'),
    ('We know the store process.','App Review, rejection reasons, privacy labels, release notes: we’ve been through all of it. We take your app all the way to launch.'),
    ('Launch isn’t the end.','Like Omni, your app grows with regular updates. We stay on after release.'),
  ]),
  ct_eyebrow='Let’s talk', ct_h='Got an idea for an app?',
  ct_p='Tell us about it in a few sentences and we’ll work out where to start, together.',
  ct_btn='Tell us your idea', l_privacy='Omni Privacy', l_support='Omni Support', back='Back to home')

for d in (TR, EN):
    path = d['lang'] + '/omni/'
    os.makedirs(path, exist_ok=True)
    open(path + 'index.html', 'w', encoding='utf-8').write(PAGE.format(ver=VER, **d))
    print('ok', path)
