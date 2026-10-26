# -*- coding: utf-8 -*-
"""
Makaledeki tüm sayısal bulguları yeniden üretir.
Kullanım:  python3 analiz.py
Girdi:     data.py (marka önerileri), kod.py (ÇÖD ve aygıt kodlaması)
"""
import collections, statistics, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import DATA
from kod import KOD

AYGIT = {"a":"sergileme birimi (raf/kaide/vitrin/niş)","m":"malzeme ve yüzey","i":"aydınlatma",
 "d":"dolaşım ve plan kurgusu","g":"grafik / anlatı yüzeyi","u":"üretim görünürlüğü (atölye)",
 "k":"kişiselleştirme / etkileşim istasyonu","t":"dijital ve teknoloji","r":"renk",
 "o":"oturma ve dinlenme","s":"koku / ses / duyusal donatı"}

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


def baslik(s): print(f"\n{'='*66}\n{s}\n{'='*66}")


def main():
    brands = [(s, g, b) for s, g, bl in DATA for b in bl]
    kws = [k for _, _, b in brands for k in b[4]]
    c_kw = collections.Counter(kws)

    baslik("GENEL")
    print(f"teslim: {len(DATA)}   marka önerisi: {len(brands)}   çeviri hücresi: {len(brands)*3}")

    baslik("4.2  MARKA SEÇİMİ")
    for alan, idx in (("kategori", 1), ("menşe", 2), ("ölçek", 3)):
        print(f"\n{alan}:")
        for k, v in collections.Counter(b[idx] for _, _, b in brands).most_common():
            print(f"  {k:24} {v:3}  %{100*v/len(brands):.1f}")
    kur = [(s, [b[0] for b in bl if b[3] == "kurumsal"]) for s, g, bl in DATA]
    kur = [(s, k) for s, k in kur if k]
    print(f"\nen az bir kurumsal marka öneren: {len(kur)}/{len(DATA)} öğrenci (%{100*len(kur)/len(DATA):.0f})")
    for s, k in kur: print(f"  {s:28} {len(k)}/3  {', '.join(k)}")

    baslik("4.3  ANAHTAR KELİME HAVUZU")
    hapax = sum(1 for v in c_kw.values() if v == 1)
    print(f"toplam etiket {len(kws)} · tekil {len(set(kws))} · tip/belirti {len(set(kws))/len(kws):.2f}")
    print(f"hapax {hapax} → tekillerin %{100*hapax/len(set(kws)):.0f}'i, tüm etiketlerin %{100*hapax/len(kws):.0f}'i")
    print(f"en sık 10 kelime tüm etiketlerin %{100*sum(v for _, v in c_kw.most_common(10))/len(kws):.0f}'ini karşılıyor")
    print("\ntematik kümeler:")
    for t, w in sorted(TEMA.items(), key=lambda x: -sum(c_kw[y] for y in set(x[1]))):
        n = sum(c_kw[y] for y in set(w))
        print(f"  {t:32} {n:3}  %{100*n/len(kws):.1f}")
    print(f"\ndoğrudan duyu göndermeli etiket: {sum(c_kw[d] for d in DUYU)}  (%{100*sum(c_kw[d] for d in DUYU)/len(kws):.1f})")

    baslik("4.4  ÇEVİRİ ÖZGÜLLÜĞÜ DÜZEYİ (ÇÖD)")
    c = collections.Counter(k[2] for k in KOD)
    kum = 0
    for lv in range(4):
        kum += 100*c[lv]/len(KOD)
        print(f"  Düzey {lv}: {c[lv]:3}  %{100*c[lv]/len(KOD):5.1f}   kümülatif %{kum:.1f}")
    print(f"  ortalama ÇÖD {statistics.mean(k[2] for k in KOD):.2f} · işlemsel (≥2) %{100*(c[2]+c[3])/len(KOD):.1f}")

    per = collections.defaultdict(list)
    for s, b, l, a, n in KOD: per[s].append(l)
    rows = sorted(((statistics.mean(v), s) for s, v in per.items()), reverse=True)
    print("\nöğrenci ortalamaları:")
    for m, s in rows: print(f"  {m:.2f}  {s}")
    ms = [m for m, _ in rows]
    print(f"  min {min(ms):.2f} · medyan {statistics.median(ms):.2f} · max {max(ms):.2f}")

    meta = {(s, b[0]): b for s, g, bl in DATA for b in bl}
    for alan, idx in (("menşe", 2), ("ölçek", 3), ("kategori", 1)):
        agg = collections.defaultdict(list)
        for s, b, l, a, n in KOD: agg[meta[(s, b)][idx]].append(l)
        print(f"\n{alan} × ort. ÇÖD:")
        for k, v in sorted(agg.items(), key=lambda x: -statistics.mean(x[1])):
            if len(v) >= 3: print(f"  {k:24} n={len(v):2}  {statistics.mean(v):.2f}")

    baslik("4.5  TASARIM AYGITI REPERTUVARI")
    ca = collections.Counter(x for s, b, l, a, n in KOD for x in a.split(",") if x)
    for k, v in ca.most_common(): print(f"  {AYGIT[k]:42} {v:3}  %{100*v/len(KOD):.0f}")
    only = sum(1 for s, b, l, a, n in KOD if a and set(filter(None, a.split(","))) <= {"a", "m"})
    print(f"\nyalnızca sergileme ve/veya malzeme ile sınırlı: {only} (%{100*only/len(KOD):.0f})")
    for kod_, ad in (("d", "dolaşım/plan"), ("s", "duyusal donatı")):
        ogr = len({s for s, b, l, a, n in KOD if kod_ in a.split(",")})
        print(f"en az bir kez {ad} kararı üreten öğrenci: {ogr}/{len(DATA)}")
    print("\naygıt çeşitliliği × ÇÖD:")
    for lv in range(4):
        sub = [k for k in KOD if k[2] == lv]
        if sub:
            print(f"  Düzey {lv}: öneri başına ort. "
                  f"{statistics.mean(len([x for x in k[3].split(',') if x]) for k in sub):.2f} aygıt ailesi")

    baslik("4.6  ADLANDIRILMIŞ MEKÂNSAL AYGIT")
    nn = [(s, b) for s, b, l, a, n in KOD if n]
    print(f"{len(nn)}/{len(KOD)} öneri (%{100*len(nn)/len(KOD):.0f}) · {len(set(s for s, _ in nn))}/{len(DATA)} öğrenci")
    print(f"bu önerilerin ÇÖD ortalaması: {statistics.mean(l for _, _, l, _, n in KOD if n):.2f}")
    for s, b in nn: print(f"  {s} — {b}")


if __name__ == "__main__":
    main()
