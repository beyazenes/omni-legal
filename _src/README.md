# Site kaynakları

GitHub Pages (Jekyll) `_` ile başlayan klasörleri yayınlamaz; bu dosyalar yalnız kaynak.

Depo kökünden çalıştır (çıktılar doğrudan `en/`, `tr/` … altına yazılır):

```
python3 _src/build.py      # en/index.html, tr/index.html   (template.html'den)
python3 _src/casestudy.py  # en/omni/, tr/omni/             (Omni proje hikâyesi)
python3 _src/privacy.py    # en/privacy/, tr/gizlilik/      (site gizliliği)
```

Her derleme CSS/JS adresine `?v=` sürüm damgası basar (önbellek kırıcı) — üçünü de
çalıştır ki tüm sayfalar aynı `site.css` sürümünü istesin.
