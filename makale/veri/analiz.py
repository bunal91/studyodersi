# -*- coding: utf-8 -*-
"""
Makaledeki tüm sayısal bulguları yeniden üretir.
Kullanım:  python3 analiz.py
Girdi:     data.py (marka önerileri), deger.py (değer eksenleri),
           kod.py (tasarım öğesi kodlaması)
"""
import collections, statistics, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import DATA
from deger import DEGER
from kod import KOD

AYGIT = {"a":"Sergileme birimi (raf, kaide, vitrin, niş)","m":"Malzeme ve yüzey","i":"Aydınlatma",
 "d":"Dolaşım ve plan kurgusu","g":"Grafik ve anlatı yüzeyi","u":"Üretim görünürlüğü (atölye)",
 "k":"Kişiselleştirme ve etkileşim istasyonu","t":"Dijital ve teknoloji","r":"Renk",
 "o":"Oturma ve dinlenme","s":"Koku, ses ve duyusal donatı",
 "e":"Giriş ve marka eşiği","q":"Satış ve kasa bölgesi"}

# Bitner (1992) servicescape boyutları
BITNER = {"i":"Ortam koşulları","r":"Ortam koşulları","s":"Ortam koşulları",
 "a":"Mekânsal yerleşim ve işlevsellik","d":"Mekânsal yerleşim ve işlevsellik",
 "o":"Mekânsal yerleşim ve işlevsellik","k":"Mekânsal yerleşim ve işlevsellik",
 "t":"Mekânsal yerleşim ve işlevsellik","e":"Mekânsal yerleşim ve işlevsellik",
 "q":"Mekânsal yerleşim ve işlevsellik",
 "m":"İşaretler, simgeler ve eserler","g":"İşaretler, simgeler ve eserler",
 "u":"İşaretler, simgeler ve eserler"}

# Dersin brifindeki sekiz zorunlu alan
PROGRAM = {"e":"Giriş ve marka eşiği","a":"Sergileme alanları","d":"Dolaşım ve mekânsal akış",
 "q":"Satış ve kasa bölgesi","k":"Deneyim ve etkileşim alanları","t":"Deneyim ve etkileşim alanları",
 "u":"Deneyim ve etkileşim alanları","s":"Deneyim ve etkileşim alanları","o":"Deneyim ve etkileşim alanları",
 "m":"Malzeme ve mimari öğeler","i":"Malzeme ve mimari öğeler","r":"Malzeme ve mimari öğeler",
 "g":"Malzeme ve mimari öğeler"}
ZORUNLU = ["Giriş ve marka eşiği","Sergileme alanları","Dolaşım ve mekânsal akış",
 "Satış ve kasa bölgesi","Depolama ve arka alan","Personel alanları",
 "Deneyim ve etkileşim alanları","Malzeme ve mimari öğeler"]

TEMA = {
 "Renk, enerji ve çağdaşlık":["renk","renkli","renk çeşitliliği","dinamik","enerjik","eğlenceli","canlı","keyifli",
   "tatil","trend","feminen","çağdaş","modern","özgür","özgürlük","katman","kontrast","karanlık","tasarım",
   "teknoloji","teknolojik","dijital","bilimsellik","deney","performans","uyum","uzmanlık","yaşam","ışık"],
 "Konfor ve erişilebilirlik":["konfor","konforlu","rahatlık","erişilebilir","erişilebilirlik","ulaşılabilir","ferah",
   "sıcaklık","samimi","samimiyet","sakinlik","güven","aydınlık","işlevsel","fonksiyonel","pratik","kapsamlı"],
 "Zarafet ve lüks":["zarif","zarafet","elegant","sofistike","lüks","seçkinlik","prestij","şık","iddialı","heykelsi",
   "metalik","cüretkâr","güçlü","güç"],
 "Keşif ve hikâye":["keşif","hikâye","sembol","gizem","mitoloji","mitolojik","simya","yolculuk","seyahat","deneme",
   "deneyim","öğrenme","vurgu","arama","ritüel"],
 "Kimlik ve aidiyet":["kimlik","kişisellik","kişiselleştirme","kişisel","aidiyet","bağ","vitrinleşme","sosyalleşme",
   "kültürel","şehirli","fransız","akdeniz nostaljisi","küresel","deniz","denizcilik"],
 "Özgünlük ve tekillik":["özgün","özgünlük","tekillik","özgüven","asilik","alternatif","deneysel","yaratıcı",
   "yaratıcılık","yenilik","esneklik"],
 "Zamansızlık ve kalite":["zamansızlık","zamansız","kalite","miras","nostalji","nostaljik","geleneksel",
   "yaşanmışlık","değer","koleksiyon","koleksiyonculuk","bütünlük"],
 "Doğallık ve sürdürülebilirlik":["doğal","doğallık","doğa","botanik","organik","doğal içerik","saflık","şeffaf"],
 "Zanaat ve el emeği":["zanaat","el yapımı","el işçiliği","özenli","iz","dönüşüm","mozaik","nakış","illüstrasyon"],
 "Duyusallık ve koku":["duyusal","duyusallık","koku","esans","dinleme","dokusal","terapi"],
 "Sadelik ve minimalizm":["sade","sadelik","minimal","minimalist","minimalizm","yalın","düzen","rafine"],
}
DUYU = {"koku","esans","duyusal","duyusallık","dinleme","dokusal","ışık","sıcaklık"}


def b(s): print(f"\n{'='*62}\n{s}\n{'='*62}")


def main():
    brands = [(s, g, x) for s, g, bl in DATA for x in bl]
    kws = [k for _, _, x in brands for k in x[4]]
    ck = collections.Counter(kws)
    N = len(KOD)

    b("GENEL")
    print(f"teslim {len(DATA)} · marka önerisi {N} · anahtar kelime eşleşmesi {N*3}")

    b("1. MARKA SEÇİMİ")
    for ad, i in (("kategori", 1), ("menşe", 2), ("ölçek", 3)):
        print(f"\n{ad}:")
        for k, v in collections.Counter(x[i] for _, _, x in brands).most_common():
            print(f"  {k:24} {v:3}  %{100*v/N:.1f}")
    kur = [(s, [x[0] for x in bl if x[3] == "kurumsal"]) for s, g, bl in DATA]
    kur = [(s, k) for s, k in kur if k]
    print(f"\nen az bir kurumsal marka öneren: {len(kur)}/{len(DATA)} (%{100*len(kur)/len(DATA):.0f})")

    b("2. MARKAYI OKUMA: DEĞER EKSENLERİ")
    dg = collections.Counter(v for _, _, x in brands for v in DEGER[x[0]])
    for k, v in dg.most_common():
        print(f"  {k:36} {v:3}  %{100*v/N:.0f}")
    print(f"  toplam etiket {sum(dg.values())} · marka başına ort. {sum(dg.values())/N:.2f}")

    b("3. ANAHTAR KELİMELER")
    print(f"etiket {len(kws)} · tekil {len(set(kws))} · yalnızca bir kez geçen {sum(1 for v in ck.values() if v == 1)}")
    print(f"en sık 10 kelime tüm etiketlerin %{100*sum(v for _, v in ck.most_common(10))/len(kws):.0f}'i")
    print("\ntematik kümeler:")
    for t, w in sorted(TEMA.items(), key=lambda x: -sum(ck[y] for y in set(x[1]))):
        n = sum(ck[y] for y in set(w))
        print(f"  {t:32} {n:3}  %{100*n/len(kws):.1f}")
    print(f"\ndoğrudan duyu göndermeli etiket {sum(ck[d] for d in DUYU)} (%{100*sum(ck[d] for d in DUYU)/len(kws):.1f})")

    b("4. KARARLARIN TASARIM ÖĞELERİNE DAĞILIMI")
    ca = collections.Counter(x for *_, a in KOD for x in a.split(",") if x)
    for k, v in ca.most_common(): print(f"  {AYGIT[k]:42} {v:3}  %{100*v/N:.0f}")
    only = sum(1 for *_, a in KOD if a and set(filter(None, a.split(","))) <= {"a", "m"})
    print(f"\nyalnızca sergileme ve/veya malzeme ile sınırlı: {only} (%{100*only/N:.0f})")
    for kd, ad in (("d", "dolaşım"), ("s", "duyusal donatı")):
        print(f"en az bir kez {ad} kararı üreten öğrenci: "
              f"{len({s for s, m, n, a in KOD if kd in a.split(',')})}/{len(DATA)}")

    b("5. BITNER'IN ÜÇ BOYUTU")
    cb = collections.Counter(); kapsam = collections.Counter(); per = collections.defaultdict(set)
    for s, m, n, a in KOD:
        dims = {BITNER[x] for x in a.split(",") if x}
        for d in dims: cb[d] += 1
        kapsam[len(dims)] += 1
        per[s] |= dims
    for k, v in cb.most_common(): print(f"  {k:36} {v:3}  %{100*v/N:.0f} öneride")
    print("\nöneri başına kaç boyut:")
    for n_ in sorted(kapsam): print(f"  {n_} boyut: {kapsam[n_]:3}  %{100*kapsam[n_]/N:.0f}")
    print(f"öğrenci düzeyinde üç boyuta da değinen: {sum(1 for v in per.values() if len(v) == 3)}/{len(DATA)}")

    b("6. BRİFİN SEKİZ ZORUNLU ALANIYLA ÖRTÜŞME")
    cp = collections.Counter()
    for s, m, n, a in KOD:
        for z in {PROGRAM[x] for x in a.split(",") if x}: cp[z] += 1
    for z in ZORUNLU:
        print(f"  {z:32} {cp.get(z, 0):3}  %{100*cp.get(z, 0)/N:3.0f}")
    print(f"\n  değinilen alan sayısı: {len([z for z in ZORUNLU if cp.get(z, 0)])}/8")

    b("7. MARKANIN DİLİYLE ADLANDIRILAN BİRİMLER")
    nn = [(s, m) for s, m, n, a in KOD if n]
    print(f"{len(nn)}/{N} öneri (%{100*len(nn)/N:.0f}) · {len(set(s for s, _ in nn))}/{len(DATA)} öğrenci")
    for s, m in nn: print(f"  {s} — {m}")
    print("\nbu önerilerin ortalama tasarım öğesi sayısı: "
          f"{statistics.mean(len([x for x in a.split(',') if x]) for s, m, n, a in KOD if n):.2f}")
    print("diğer önerilerde: "
          f"{statistics.mean(len([x for x in a.split(',') if x]) for s, m, n, a in KOD if not n):.2f}")


if __name__ == "__main__":
    main()
