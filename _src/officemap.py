# Ofis haritası: _src/office.osm (OpenStreetMap, ODbL) → map.js (veri + çizici)
# Depo kökünden: python3 _src/officemap.py
# Veri bir kez indirildi:
#   curl "https://api.openstreetmap.org/api/0.6/map?bbox=37.3680,37.0650,37.3762,37.0708" -o _src/office.osm
import json, math, os, xml.etree.ElementTree as ET

SRC = os.path.dirname(os.path.abspath(__file__))
OFFICE = (37.06791069162132, 37.37205390962871)   # Google profilindeki pin
OFFICE_WAY = '353786413'                          # Yüncüler İş Merkezi (pin bu bloğun köşesinde)
OFFICE_LEVELS = 5
RADIUS = 190                                      # m, sahneye giren çevre
FLOOR = 3.2                                       # m, kat yüksekliği

root = ET.parse(os.path.join(SRC, 'office.osm')).getroot()
nodes = {n.get('id'): (float(n.get('lat')), float(n.get('lon'))) for n in root.iter('node')}
kx = 111320 * math.cos(math.radians(OFFICE[0])); ky = 110540

def xy(ll):  # metre; x doğu, y kuzey
    return ((ll[1] - OFFICE[1]) * kx, (ll[0] - OFFICE[0]) * ky)

def guess_levels(wid):
    # OSM'de çoğu binanın kat bilgisi yok: kimliğe bağlı sabit bir tahmin (her derlemede aynı)
    h = (int(wid) * 2654435761) % 1000 / 1000
    return 3 + int(h * h * 7)   # 3–9 kat, alçaklar daha sık

buildings, roads = [], []
for w in root.iter('way'):
    t = {x.get('k'): x.get('v') for x in w.iter('tag')}
    pts = [xy(nodes[nd.get('ref')]) for nd in w.iter('nd') if nd.get('ref') in nodes]
    if len(pts) < 2: continue
    if 'building' in t:
        if pts[0] == pts[-1]: pts = pts[:-1]
        cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
        if math.hypot(cx, cy) > RADIUS: continue
        office = w.get('id') == OFFICE_WAY
        lv = OFFICE_LEVELS if office else int(t.get('building:levels') or guess_levels(w.get('id')))
        b = {'p': [round(v, 1) for p in pts for v in p], 'h': round(lv * FLOOR, 1)}
        if office: b['o'] = 1
        buildings.append(b)
    elif 'highway' in t and t['highway'] not in ('footway', 'steps', 'path', 'cycleway', 'pedestrian', 'service'):
        if min(math.hypot(*p) for p in pts) > RADIUS * 1.15: continue
        major = t['highway'] in ('motorway', 'trunk', 'primary', 'secondary')
        roads.append({'p': [round(v, 1) for p in pts for v in p], 'w': 2 if major else 1})

assert any(b.get('o') for b in buildings), 'ofis binası bulunamadı'
data = json.dumps({'r': RADIUS, 'b': buildings, 'r2': roads}, separators=(',', ':'))
js = open(os.path.join(SRC, 'map.src.js'), encoding='utf-8').read()
open('map.js', 'w', encoding='utf-8').write(
    '// Üretildi: _src/officemap.py — elle düzenleme. Harita verisi © OpenStreetMap katkıda bulunanlar (ODbL)\n'
    'window.OFFICE_MAP=' + data + ';\n' + js)
print('ok map.js', len(buildings), 'bina', len(roads), 'yol', round(os.path.getsize('map.js') / 1024), 'KB')
