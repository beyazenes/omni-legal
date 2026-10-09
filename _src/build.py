# -*- coding: utf-8 -*-
import os
# Çıktılar depo köküne yazılır (en/, tr/ …); kaynak dosyalar bu klasörde.
SRC = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(SRC))
import os, re
T = open(os.path.join(SRC, 'template.html'), encoding='utf-8').read()
VERSED = """  <section class="versed" id="versed" aria-labelledby="versed-title">
    <div class="wrap grid">
      <div class="reveal">
        <span class="badge">Coming soon to the App Store</span>
        <div class="versed-head">
          <img src="../img/versed-icon.png" alt="Versed app icon">
          <h2 id="versed-title">Versed</h2>
        </div>
        <p class="tag">A quiet page every morning.</p>
        <p class="body">One Bible verse a day, with a short note on what it meant then and what it might mean on an ordinary day like yours. Read it, draw on the page, stamp it with a photo of your day, and say amen.</p>
        <ul>
          <li>A journal that becomes yours, page by page</li>
          <li>A verse for how you feel today</li>
          <li>No account, no ads, no tracking</li>
        </ul>
      </div>
      <div class="shots reveal" id="versedShots" aria-hidden="true">
        <img class="device shot a" src="../img/versed-notebook.png" alt="" loading="lazy">
        <img class="device shot b" src="../img/versed-page.png" alt="" loading="lazy">
      </div>
    </div>
  </section>"""
def tags(xs): return ''.join('<li>%s</li>' % x for x in xs)
EN = dict(lang='en', ogl='en_US', shot='', versed=VERSED,
 versed_li='            <li><a href="#versed">Versed</a><span class="soon">SOON</span></li>\n',
 title='Beyaz Labs — Apps & Web Studio',
 desc='Beyaz Labs is an independent studio building mobile apps, websites, online stores and social content — in Turkey and worldwide. Makers of Omni Health.',
 nav_services='Services', nav_work='Work', nav_contact='Contact',
 cur_en='aria-current="true"', cur_tr='',
 hero_eyebrow='Independent design &amp; software studio',
 hero_h1='We build things people <em class="rot" data-words="love to use.|come back to.|trust.">love to use.</em>',
 hero_lead='An independent studio making mobile apps, websites, online stores and social content — calm, fast and built to last.',
 svc_eyebrow='Services', svc_h='Everything you need to <em>show up well online.</em>',
 svc_lead='From a first website to a full mobile app. One studio, one point of contact, in Turkish or English.',
 s1_h='Websites', s1_p='Company and showcase sites that load fast, look great on phones and are easy to keep up to date. We stay on after launch for care and updates.',
 s1_tags=tags(['Corporate','Landing pages','Bilingual','SEO basics','Care &amp; updates']),
 s2_h='Online stores', s2_p='Your own store on İkas or Shopify, independent of marketplaces. Payments, shipping, legal pages and training included.',
 s2_tags=tags(['Setup &amp; design','Payments','Shipping','Product upload','Ongoing care']),
 s3_h='Mobile apps', s3_p='Apps for iPhone, iPad and Android, from first idea to the App Store and Google Play.',
 s3_tags=tags(['iPhone &amp; iPad','Android','Apple Watch','Widgets']),
 s3_proof='Case study: <a href="omni/">Omni Health</a>',
 s4_h='Care & updates', s4_p='Monthly content updates, small changes and checks so your site never goes stale.',
 s4_tags=tags(['Monthly plan','Content edits','Backups']),
 s5_h='Social content', s5_p='Post and Reel designs, captions and a monthly content plan that matches your brand.',
 s5_tags=tags(['Instagram','Reels','Content plan']),
 work_eyebrow='Our work', work_h='We ship our own products, too. <em>Here’s one.</em>',
 work_lead='Omni Health is live on the App Store in 22 languages. We designed and built it end to end.',
 omni_icon_alt='Omni Health app icon', omni_tag='Nutrition and hydration, like a thoughtful dietitian.',
 st1_k='Today', st1_h='One sentence about the one thing that matters.',
 st1_p="Omni reads your day from Apple Health (water, meals, workouts and sleep) and tells you what's worth doing next. No dashboards to decode.",
 st2_k='Cycle-aware nutrition', st2_h='Your nutrition, in sync with your cycle.',
 st2_p="Suggestions adapt to each phase. Cycle data stays in Apple Health and on your device, and Omni won't guess when it can't read your cycle reliably.",
 st3_k='Recipes', st3_h='Recipes that start from your own kitchen.',
 st3_p='Three options shaped by your goals, allergies and the cuisine you grew up with. Log what you ate in one tap.',
 st4_k='Cook Now', st4_h='The timer is already in the step.',
 st4_p='If a step says "five minutes", the timer is one tap away. It keeps time on your Lock Screen and in the Dynamic Island while you cook.',
 badge_aria='Download Omni Health on the App Store',
 l_privacy='Privacy Policy', l_terms='Terms of Use', l_support='Support',
 v_badge='Coming soon to the App Store', v_icon_alt='Versed app icon', v_tag='A quiet page every morning.',
 v_body='One Bible verse a day, with a short note on what it meant then and what it might mean on an ordinary day like yours. Read it, draw on the page, stamp it with a photo of your day, and say amen.',
 v_li1='A journal that becomes yours, page by page', v_li2='A verse for how you feel today', v_li3='No account, no ads, no tracking',
 pr_eyebrow='How we build', pr_h='Small studio. <em>Big on care.</em>', go_aria='ask for a quote', ct_subj_txt='New project',
 pr1_h='One point of contact', pr1_p='The person you brief is the person who designs it and ships it. Your message never waits in a queue.',
 pr2_h='Mobile first', pr2_p='Your customers meet you on a phone, so that’s where we start. Then the laptop, then everything else. All of it fast.',
 pr3_h='Surprises are for birthdays', pr3_p='Scope and price are clear up front. Nobody gets a shock on invoice day.',
 ct_eyebrow='Let’s talk', ct_h='Have a project in mind?',
 ct_p='Fill in the blanks and your email writes itself. We usually reply within 24 hours with ideas and a clear quote.', ct_letter='''Hi Enes, I’m <span class="blank"><input id="fA" data-1p-ignore data-lpignore="true" type="text" autocomplete="off" placeholder="your name" aria-label="your name" spellcheck="false"></span>. We’d like <span class="blank sel" style="--c:#FE2C55"><button type="button" class="pk" id="fSvc" data-value="web" aria-haspopup="listbox" aria-expanded="false" aria-label="Service"><span class="v">a website</span><svg viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button><span class="menu" role="listbox" hidden aria-label="Service"><span role="option" data-v="web" data-c="#FE2C55" aria-selected="true">a website</span><span role="option" data-v="cart" data-c="#FF9F0A" aria-selected="false">an online store</span><span role="option" data-v="phone" data-c="#7ACB00" aria-selected="false">a mobile app</span><span role="option" data-v="care" data-c="#00C7BE" aria-selected="false">care and updates</span><span role="option" data-v="social" data-c="#AF52DE" aria-selected="false">social media content</span><span role="option" data-v="more" data-c="#F7EFF1" aria-selected="false">a few things</span></span></span> for <span class="blank"><input id="fB" data-1p-ignore data-lpignore="true" type="text" autocomplete="off" placeholder="your business" aria-label="your business" spellcheck="false"></span>, and we’d like to start <span class="blank sel"><button type="button" class="pk" id="fWhen" data-value="now" aria-haspopup="listbox" aria-expanded="false" aria-label="When"><span class="v">right away</span><svg viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button><span class="menu" role="listbox" hidden aria-label="When"><span role="option" data-v="now" aria-selected="true">right away</span><span role="option" data-v="month" aria-selected="false">this month</span><span role="option" data-v="months" aria-selected="false">in a few months</span><span role="option" data-v="later" aria-selected="false">whenever suits</span></span></span>.''', ct_send='Write the email', ct_hint='Your mail app opens, so you can edit before sending. Or write directly:', ct_tail='A bit more about it:',
 ct_subject='New%20project', ct_m1_b='One click away,', ct_m1='wherever you are.', ct_m2_b='Turkish or English,', ct_m2='whichever suits you.', ct_m3_b='Quotes are free,', ct_m3='no strings attached.', case_link='Read the case study',
 f_blurb='An independent studio building mobile apps, websites, online stores and social content.',
 f_services='Services', f_apps='Apps', f_soon='SOON', other_href='../tr/', other_l='tr', other_label='Türkçe',
 f_made='Made by Enes Beyaz.', f_omni_support='Omni Support', f_omni_privacy='Omni Privacy', f_site_priv='Site privacy', f_site_priv_href='privacy/', f_tm='Designed in Turkey, works everywhere.')
TR = dict(lang='tr', ogl='tr_TR', shot='tr/', versed='', versed_li='',
 title='Beyaz Labs — Uygulama ve Web Stüdyosu',
 desc='Beyaz Labs; mobil uygulamalar, web siteleri, e-ticaret mağazaları ve sosyal medya içerikleri üreten bağımsız bir stüdyo. Türkiye geneli ve yurt dışına hizmet. Omni Health’in yapımcısı.',
 nav_services='Hizmetler', nav_work='İşlerimiz', nav_contact='İletişim',
 cur_en='', cur_tr='aria-current="true"',
 hero_eyebrow='Bağımsız tasarım ve yazılım stüdyosu',
 hero_h1='İnsanların <em class="rot" data-words="kullanmayı sevdiği|geri döndüğü|güvendiği">kullanmayı sevdiği</em> işler yapıyoruz.',
 hero_lead='Mobil uygulamalar, web siteleri, e-ticaret mağazaları ve sosyal medya içerikleri üreten bağımsız bir stüdyo. Sade, hızlı ve uzun ömürlü.',
 svc_eyebrow='Hizmetler', svc_h='İnternette iyi görünmek için <em>ihtiyacınız olan her şey.</em>',
 svc_lead='İlk web sitenizden tam bir mobil uygulamaya kadar. Tek stüdyo, tek muhatap; Türkçe ya da İngilizce.',
 s1_h='Web siteleri', s1_p='Hızlı açılan, telefonda kusursuz görünen ve kolayca güncellenebilen kurumsal ve tanıtım siteleri. Yayından sonra da bakım ve güncellemelerde yanınızdayız.',
 s1_tags=tags(['Kurumsal','Tanıtım sayfası','İki dilli','SEO temelleri','Bakım ve güncelleme']),
 s2_h='E-ticaret', s2_p='İkas ya da Shopify üzerinde, pazar yerlerine bağlı kalmadan kendi mağazanız. Ödeme, kargo, yasal sayfalar ve eğitim dahil.',
 s2_tags=tags(['Kurulum ve tasarım','Ödeme','Kargo','Ürün yükleme','Sürekli destek']),
 s3_h='Mobil uygulamalar', s3_p='iPhone, iPad ve Android için uygulamalar; ilk fikirden App Store ve Google Play’e.',
 s3_tags=tags(['iPhone ve iPad','Android','Apple Watch','Widget']),
 s3_proof='Nasıl yaptık: <a href="omni/">Omni Health</a>',
 s4_h='Bakım ve güncelleme', s4_p='Aylık içerik güncellemeleri, küçük değişiklikler ve kontroller; siteniz hiç eskimesin.',
 s4_tags=tags(['Aylık paket','İçerik düzenleme','Yedekleme']),
 s5_h='Sosyal medya içerikleri', s5_p='Markanıza uygun gönderi ve Reels tasarımları, metinler ve aylık içerik planı.',
 s5_tags=tags(['Instagram','Reels','İçerik planı']),
 work_eyebrow='İşlerimiz', work_h='Kendi ürünlerimizi de yapıyoruz. <em>İşte biri.</em>',
 work_lead='Omni Health, 22 dilde App Store’da yayında. Tasarımından koduna, baştan sona biz yaptık.',
 omni_icon_alt='Omni Health uygulama simgesi', omni_tag='Beslenme ve su takibi; düşünceli bir diyetisyen gibi.',
 st1_k='Bugün', st1_h='Önemli olan tek şey, tek cümlede.',
 st1_p='Omni gününüzü Apple Sağlık’tan okur (su, öğünler, antrenman ve uyku) ve sıradaki en anlamlı adımı söyler. Çözülecek grafik yok.',
 st2_k='Döngüne göre beslenme', st2_h='Beslenmeniz, döngünüzle uyumlu.',
 st2_p='Öneriler her evreye göre değişir. Döngü verileri Apple Sağlık’ta ve cihazınızda kalır; Omni, döngünüzü güvenilir okuyamadığında tahmin yürütmez.',
 st3_k='Tarifler', st3_h='Kendi mutfağınızdan başlayan tarifler.',
 st3_p='Hedefinize, alerjilerinize ve büyüdüğünüz mutfağa göre üç seçenek. Yediğinizi tek dokunuşla kaydedin.',
 st4_k='Şimdi Pişir', st4_h='Sayaç zaten adımın içinde.',
 st4_p='Adımda "beş dakika" yazıyorsa sayaç bir dokunuş uzağınızda. Siz pişirirken Kilit Ekranı’nda ve Dynamic Island’da süreyi tutar.',
 badge_aria='Omni Health’i App Store’dan indirin',
 l_privacy='Gizlilik Politikası', l_terms='Kullanım Koşulları', l_support='Destek',
 v_badge='Yakında App Store’da', v_icon_alt='Versed uygulama simgesi', v_tag='Her sabah sessiz bir sayfa.',
 v_body='Her gün bir İncil ayeti ve kısa bir not: o zaman ne anlama geliyordu, bugün sizinki gibi sıradan bir günde ne anlama gelebilir. Okuyun, sayfaya çizin, gününüzün bir fotoğrafını pul gibi yapıştırın ve "amin" deyin.',
 v_li1='Sayfa sayfa sizin olan bir günlük', v_li2='Bugünkü hislerinize göre bir ayet', v_li3='Hesap yok, reklam yok, takip yok',
 pr_eyebrow='Nasıl çalışıyoruz', pr_h='Küçük stüdyo. <em>Büyük özen.</em>', go_aria='teklif iste', ct_subj_txt='Yeni proje',
 pr1_h='Tek muhatap', pr1_p='Projeyi dinleyen, tasarlayan ve teslim eden aynı kişi. Mesajınız bir kuyrukta beklemez.',
 pr2_h='Önce mobil', pr2_p='Müşterileriniz sizi ilk telefonda görür; biz de oradan başlarız. Sonra bilgisayar, sonra gerisi. Hepsi de hızlı.',
 pr3_h='Sürprizler doğum günlerine', pr3_p='Kapsam ve fiyat baştan net. Fatura günü kimse şaşırmaz.',
 ct_eyebrow='Konuşalım', ct_h='Aklınızda bir proje mi var?',
 ct_p='Boşlukları doldurun, mailiniz kendiliğinden yazılsın. Genellikle 24 saat içinde fikirler ve net bir fiyatla döneriz.', ct_letter='''Merhaba Enes, ben <span class="blank"><input id="fA" data-1p-ignore data-lpignore="true" type="text" autocomplete="off" placeholder="adınız" aria-label="adınız" spellcheck="false"></span>. <span class="blank"><input id="fB" data-1p-ignore data-lpignore="true" type="text" autocomplete="off" placeholder="işletmenizin adı" aria-label="işletmenizin adı" spellcheck="false"></span> için <span class="blank sel" style="--c:#FE2C55"><button type="button" class="pk" id="fSvc" data-value="web" aria-haspopup="listbox" aria-expanded="false" aria-label="Hizmet"><span class="v">bir web sitesi</span><svg viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button><span class="menu" role="listbox" hidden aria-label="Hizmet"><span role="option" data-v="web" data-c="#FE2C55" aria-selected="true">bir web sitesi</span><span role="option" data-v="cart" data-c="#FF9F0A" aria-selected="false">bir online mağaza</span><span role="option" data-v="phone" data-c="#7ACB00" aria-selected="false">bir mobil uygulama</span><span role="option" data-v="care" data-c="#00C7BE" aria-selected="false">bakım ve güncelleme</span><span role="option" data-v="social" data-c="#AF52DE" aria-selected="false">sosyal medya içerikleri</span><span role="option" data-v="more" data-c="#F7EFF1" aria-selected="false">birkaç şey</span></span></span> istiyoruz ve <span class="blank sel"><button type="button" class="pk" id="fWhen" data-value="now" aria-haspopup="listbox" aria-expanded="false" aria-label="Ne zaman"><span class="v">hemen</span><svg viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button><span class="menu" role="listbox" hidden aria-label="Ne zaman"><span role="option" data-v="now" aria-selected="true">hemen</span><span role="option" data-v="month" aria-selected="false">bu ay</span><span role="option" data-v="months" aria-selected="false">birkaç ay içinde</span><span role="option" data-v="later" aria-selected="false">acele etmeden</span></span></span> başlamak isteriz.''', ct_send='Maili hazırla', ct_hint='Mail uygulamanız açılır, göndermeden önce düzenleyebilirsiniz. Ya da doğrudan yazın:', ct_tail='Biraz daha detay:',
 ct_subject='Yeni%20proje', ct_m1_b='Bir tık uzağınızdayız,', ct_m1='nerede olursanız olun.', ct_m2_b='Türkçe ya da İngilizce,', ct_m2='hangisi rahatsa.', ct_m3_b='Teklif ücretsiz,', ct_m3='hiçbir bağlayıcılığı yok.', case_link='Omni’nin hikâyesini okuyun',
 f_blurb='Mobil uygulamalar, web siteleri, e-ticaret mağazaları ve sosyal medya içerikleri üreten bağımsız bir stüdyo.',
 f_services='Hizmetler', f_apps='Uygulamalar', f_soon='YAKINDA', other_href='../en/', other_l='en', other_label='English',
 f_made='Enes Beyaz tarafından yapıldı.', f_omni_support='Omni Destek', f_omni_privacy='Omni Gizlilik', f_site_priv='Site gizliliği', f_site_priv_href='gizlilik/', f_tm='Türkiye’de tasarlandı, her yerde çalışır.')
import time
VER = time.strftime('%Y%m%d%H%M')
for d in (EN, TR):
    out = T.replace('{{ver}}', VER)
    for k, v in d.items(): out = out.replace('{{%s}}' % k, v)
    left = re.findall(r'\{\{(\w+)\}\}', out)
    assert not left, (d['lang'], left)
    os.makedirs(d['lang'], exist_ok=True)
    open(d['lang'] + '/index.html', 'w', encoding='utf-8').write(out)
    print('ok', d['lang'])
