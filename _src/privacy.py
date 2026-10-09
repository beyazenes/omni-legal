# -*- coding: utf-8 -*-
import os
# Çıktılar depo köküne yazılır (en/, tr/ …); kaynak dosyalar bu klasörde.
SRC = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(SRC))
# Builds the studio's own (site) privacy pages: /tr/gizlilik/ and /en/privacy/
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
<link rel="canonical" href="https://beyazlabs.com/{path}">
<link rel="alternate" hreflang="en" href="https://beyazlabs.com/en/privacy/">
<link rel="alternate" hreflang="tr" href="https://beyazlabs.com/tr/gizlilik/">
<link rel="icon" href="../../img/omni-icon.png">
<link rel="stylesheet" href="../../site.css?v={ver}">
</head>
<body class="doc-page">
  <nav class="top" aria-label="Main">
    <div class="wrap">
      <a class="brand" href="../">Beyaz <span>Labs</span></a>
      <ul>
        <li><a href="../#contact">{nav_contact}</a></li>
        <li><span class="lang" aria-label="Language">
          <a href="../../en/privacy/" data-l="en" hreflang="en" lang="en" {cur_en}>EN</a>
          <a href="../../tr/gizlilik/" data-l="tr" hreflang="tr" lang="tr" {cur_tr}>TR</a>
        </span></li>
      </ul>
    </div>
  </nav>
  <main class="doc">
    <div class="wrap">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      {body}
      <p class="updated">{updated}</p>
    </div>
  </main>
  <footer>
    <div class="wrap">
      <div class="legal">
        <span>© 2026 Beyaz Labs.</span>
        <span><a href="../">{back}</a></span>
      </div>
    </div>
  </footer>
<script>document.querySelectorAll('.lang a').forEach(a=>a.addEventListener('click',()=>{{try{{localStorage.setItem('lang',a.dataset.l)}}catch(e){{}}}}));</script>
</body>
</html>
'''
def sec(h, p): return '<section><h2>%s</h2>%s</section>' % (h, ''.join('<p>%s</p>' % x for x in p))
TR = dict(lang='tr', path='tr/gizlilik/', cur_tr='aria-current="true"', cur_en='',
  title='Site gizliliği — Beyaz Labs', desc='beyazlabs.com hangi verileri topluyor? Kısaca: neredeyse hiçbirini.',
  nav_contact='İletişim', eyebrow='Gizlilik', h1='Bu site sizi takip etmez.',
  lead='Kısaca: çerez yok, analitik yok, reklam yok. Bu sayfa yalnızca beyazlabs.com sitesini kapsar; uygulamalarımızın kendi gizlilik politikaları vardır.',
  body=''.join([
    sec('Ne toplamıyoruz', ['Çerez kullanmıyoruz. Google Analytics, reklam pikseli ya da başka bir takip aracı yok. Sayfalar dışarıdan yazı tipi, script ya da görsel yüklemez.']),
    sec('Tarayıcınızda kalan tek şey', ['Dil seçiminiz (Türkçe ya da İngilizce) bir sonraki ziyaretinizde hatırlansın diye yalnızca kendi tarayıcınızda saklanır. Bize gönderilmez.']),
    sec('İletişim kutusu', ['“Maili hazırla” bölümüne yazdıklarınız hiçbir sunucuya gönderilmez; yalnızca kendi mail uygulamanızda bir taslak oluşturur. Göndermek size kalmış.',
                        'Bize mail atarsanız adınızı, adresinizi ve mesajınızı yalnızca size yanıt vermek ve teklif hazırlamak için kullanırız; üçüncü kişilerle paylaşmayız. Maillerimiz Cloudflare üzerinden yönlendirilir ve Gmail’de saklanır.']),
    sec('Barındırma', ['Site GitHub Pages üzerinde yayınlanır. GitHub, hizmetin güvenliği için ziyaretçilerin IP adresini kendi sunucu kayıtlarında tutabilir; ayrıntılar <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">GitHub gizlilik bildiriminde</a>.']),
    sec('Haklarınız', ['Bize gönderdiğiniz maillerin silinmesini ya da size ait hangi bilgileri tuttuğumuzu öğrenmek isterseniz <a href="mailto:enes@beyazlabs.com">enes@beyazlabs.com</a> adresine yazmanız yeterli.']),
    sec('Uygulamalarımız', ['Omni Health’in nasıl veri işlediği ayrı bir belgede: <a href="../../privacypolicy.html">Omni Health gizlilik politikası</a>.']),
    sec('Sorumlu', ['Enes Beyaz · Beyaz Labs · <a href="mailto:enes@beyazlabs.com">enes@beyazlabs.com</a>']),
  ]), updated='Son güncelleme: 9 Ekim 2026', back='Ana sayfaya dön')
EN = dict(lang='en', path='en/privacy/', cur_en='aria-current="true"', cur_tr='',
  title='Site privacy — Beyaz Labs', desc='What does beyazlabs.com collect? In short: almost nothing.',
  nav_contact='Contact', eyebrow='Privacy', h1='This site doesn’t track you.',
  lead='In short: no cookies, no analytics, no ads. This page covers beyazlabs.com only; our apps have their own privacy policies.',
  body=''.join([
    sec('What we don’t collect', ['We use no cookies. There is no Google Analytics, ad pixel or other tracking tool. Pages load no fonts, scripts or images from other sites.']),
    sec('The one thing kept in your browser', ['Your language choice (English or Turkish) is stored only in your own browser so it is remembered next time. It is never sent to us.']),
    sec('The contact box', ['What you type into “Write the email” is not sent to any server; it only creates a draft in your own mail app. Sending it is up to you.',
                            'If you email us, we use your name, address and message only to reply and prepare a quote, and we don’t share them with third parties. Our email is routed through Cloudflare and stored in Gmail.']),
    sec('Hosting', ['The site is served by GitHub Pages. GitHub may keep visitors’ IP addresses in its server logs for security; see the <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement">GitHub privacy statement</a>.']),
    sec('Your rights', ['To ask what we hold about you, or to have your emails to us deleted, write to <a href="mailto:enes@beyazlabs.com">enes@beyazlabs.com</a>.']),
    sec('Our apps', ['How Omni Health handles data is covered separately: <a href="../../privacypolicy.html">Omni Health privacy policy</a>.']),
    sec('Who is responsible', ['Enes Beyaz · Beyaz Labs · <a href="mailto:enes@beyazlabs.com">enes@beyazlabs.com</a>']),
  ]), updated='Last updated: 9 October 2026', back='Back to home')
for d in (TR, EN):
    os.makedirs(d['path'], exist_ok=True)
    open(d['path'] + 'index.html', 'w', encoding='utf-8').write(PAGE.format(ver=VER, **d))
    print('ok', d['path'])
