# -*- coding: utf-8 -*-
"""
Makaledeki tüm sayısal bulguları yeniden üretir.
Kullanım:  python3 analiz.py
Girdi:     data.py (marka önerileri), deger.py (değer eksenleri),
           kod.py (somutluk ve aygıt kodlaması)
"""
import collections, statistics, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import DATA
from kod import KOD
from deger import DEGER

SOM = {1: "sıfatta kalan", 2: "öğe adlandıran", 3: "mekânda yer tutan"}
AYGIT = {"a":"Sergileme birimi (raf, kaide, vitrin, niş)","m":"Malzeme ve yüzey","i":"Aydınlatma",
 "d":"Dolaşım ve plan kurgusu","g":"Grafik ve anlatı yüzeyi","u":"Üretim görünürlüğü (atölye)",
 "k":"Kişiselleştirme ve etkileşim istasyonu","t":"Dijital ve teknoloji","r":"Renk",
 "o":"Oturma ve dinlenme","s":"Koku, ses ve duyusal donatı"}
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


def b(s): print(f"\n{'='*64}\n{s}\n{'='*64}")


def main():
    brands = [(s, g, x) for s, g, bl in DATA for x in bl]
    kws = [k for _, _, x in brands for k in x[4]]
    ck = collections.Counter(kws)
    meta = {(s, x[0]): x for s, g, bl in DATA for x in bl}

    b("GENEL")
    print(f"teslim {len(DATA)} · marka önerisi {len(brands)} · çeviri hücresi {len(brands)*3}")

    b("MARKA SEÇİMİ")
    for ad, i in (("kategori", 1), ("menşe", 2), ("ölçek", 3)):
        print(f"\n{ad}:")
        for k, v in collections.Counter(x[i] for _, _, x in brands).most_common():
            print(f"  {k:24} {v:3}  %{100*v/len(brands):.1f}")
    kur = [(s, [x[0] for x in bl if x[3] == "kurumsal"]) for s, g, bl in DATA]
    kur = [(s, k) for s, k in kur if k]
    print(f"\nen az bir kurumsal marka öneren: {len(kur)}/{len(DATA)} (%{100*len(kur)/len(DATA):.0f})")
    for s, k in kur: print(f"  {s:28} {len(k)}/3  {', '.join(k)}")

    b("ANAHTAR KELİME HAVUZU")
    hap = sum(1 for v in ck.values() if v == 1)
    print(f"etiket {len(kws)} · tekil {len(set(kws))} · tip/belirti {len(set(kws))/len(kws):.2f}")
    print(f"hapax {hap} → tekillerin %{100*hap/len(set(kws)):.0f}'i · tüm etiketlerin %{100*hap/len(kws):.0f}'i")
    print(f"en sık 10 kelime tüm etiketlerin %{100*sum(v for _, v in ck.most_common(10))/len(kws):.0f}'i")
    print("\ntematik kümeler:")
    for t, w in sorted(TEMA.items(), key=lambda x: -sum(ck[y] for y in set(x[1]))):
        n = sum(ck[y] for y in set(w))
        print(f"  {t:32} {n:3}  %{100*n/len(kws):.1f}")
    print(f"\ndoğrudan duyu göndermeli etiket {sum(ck[d] for d in DUYU)} (%{100*sum(ck[d] for d in DUYU)/len(kws):.1f})")

    b("MARKAYI OKUMA: DEĞER EKSENLERİ")
    dg = collections.Counter(v for _, _, x in brands for v in DEGER[x[0]])
    for k, v in dg.most_common():
        print(f"  {k:36} {v:3}  %{100*v/len(brands):.0f}")
    print(f"  toplam etiket {sum(dg.values())} · marka başına ort. {sum(dg.values())/len(brands):.2f}")

    b("ANAHTAR KELİMEDEN MEKÂNSAL KARARA: SOMUTLUK")
    c = collections.Counter(k[2] for k in KOD)
    for lv in (1, 2, 3):
        print(f"  {SOM[lv]:18} {c[lv]:3}  %{100*c[lv]/len(KOD):5.1f}")
    ad = sum(k[3] for k in KOD)
    print(f"  bunların içinde marka diliyle adlandırılan: {ad} (%{100*ad/len(KOD):.0f})")

    per = collections.defaultdict(list)
    for s_, m, l, n, a in KOD: per[s_].append(l)
    print("\nöğrenci profili (üç öneri):")
    print(f"  en az bir kez 'mekânda yer tutan' karar üreten: "
          f"{sum(1 for v in per.values() if max(v) == 3)}/{len(DATA)}")
    print(f"  üç önerisi de 'sıfatta kalan' ya da 'öğe adlandıran': "
          f"{sum(1 for v in per.values() if max(v) <= 2)}/{len(DATA)}")
    print("  üç öneride baskın:", dict(collections.Counter(
        SOM[statistics.mode(v)] for v in per.values())))

    for ad_, i_ in (("menşe", 2), ("ölçek", 3), ("kategori", 1)):
        agg = collections.defaultdict(list)
        for s_, m, l, n, a in KOD: agg[meta[(s_, m)][i_]].append(l)
        print(f"\n{ad_} × 'mekânda yer tutan' oranı:")
        for k, v in sorted(agg.items(), key=lambda x: -sum(1 for y in x[1] if y == 3)/len(x[1])):
            if len(v) >= 3:
                print(f"  {k:24} n={len(v):2}  %{100*sum(1 for y in v if y == 3)/len(v):.0f}")

    b("TASARIM AYGITI REPERTUVARI")
    ca = collections.Counter(x for _, _, _, _, a in KOD for x in a.split(",") if x)
    for k, v in ca.most_common(): print(f"  {AYGIT[k]:42} {v:3}  %{100*v/len(KOD):.0f}")
    only = sum(1 for *_, a in KOD if a and set(filter(None, a.split(","))) <= {"a", "m"})
    print(f"\nyalnızca sergileme ve/veya malzeme ile sınırlı: {only} (%{100*only/len(KOD):.0f})")
    for kd, ad in (("d", "dolaşım/plan"), ("s", "duyusal donatı")):
        print(f"en az bir kez {ad} kararı üreten öğrenci: "
              f"{len({s_ for s_, m, l, n, a in KOD if kd in a.split(',')})}/{len(DATA)}")
    print("\naygıt çeşitliliği × somutluk:")
    for lv in (1, 2, 3):
        sub = [k for k in KOD if k[2] == lv]
        print(f"  {SOM[lv]:18} öneri başına ort. "
              f"{statistics.mean(len([x for x in k[4].split(',') if x]) for k in sub):.2f} aygıt ailesi")

    b("MARKA DİLİYLE ADLANDIRILAN AYGITLAR")
    nn = [(s_, m) for s_, m, l, n, a in KOD if n]
    print(f"{len(nn)}/{len(KOD)} öneri (%{100*len(nn)/len(KOD):.0f}) · "
          f"{len(set(s_ for s_, _ in nn))}/{len(DATA)} öğrenci")
    for s_, m in nn: print(f"  {s_} — {m}")


if __name__ == "__main__":
    main()
