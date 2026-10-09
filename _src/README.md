# Site kaynakları

GitHub Pages (Jekyll) `_` ile başlayan klasörleri yayınlamaz; bu dosyalar sadece kaynak.

Yeniden üretmek için bu klasörün bir kopyasında, yanında `site.css`, `site.js` ve `img/` ile:

```
python3 build.py      # en/index.html, tr/index.html  (template.html'den)
python3 casestudy.py  # en/omni/, tr/omni/
python3 privacy.py    # en/privacy/, tr/gizlilik/
```

Sonra üretilen dosyaları depo köküne kopyala. Her derleme CSS/JS adresine `?v=` sürüm damgası basar (önbellek kırıcı).
