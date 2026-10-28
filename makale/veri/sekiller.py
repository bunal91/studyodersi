# -*- coding: utf-8 -*-
"""Makalenin şekillerini üretir. Palet: dataviz referans paleti (light)."""
import collections, statistics, sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import DATA
from kod import KOD
from deger import DEGER

OUT = "/home/user/studyodersi/makale/sekil"
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
SERIES = "#2a78d6"                                             # tek seri → tek renk
ORDINAL = ["#86b6ef", "#2a78d6", "#104281"]  # sıralı ölçek (doğrulandı)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "savefig.dpi": 200,
    "axes.edgecolor": AXIS, "text.color": INK,
})

SOM = {1: "Sıfatta kalan", 2: "Öğe adlandıran", 3: "Mekânda yer tutan"}


def solo_of(level, named):
    """ÇÖD kodlarını SOLO düzeylerine eşler (0-4)."""
    if level <= 2:
        return level            # 0→ön yapısal, 1→tek yapılı, 2→çok yapılı
    return 4 if named else 3    # adlandırılmış aygıt → soyutlanmış, diğeri → ilişkisel


def rbar(ax, y, width, color, h=0.52, xmax=None):
    """Tabanda kare, uçta yuvarlatılmış yatay çubuk."""
    r = min(h / 2, width / 2 if width else h / 2)
    if xmax:
        r = min(r, xmax * 0.012)
    b, t, x1 = y - h / 2, y + h / 2, width
    v = [(0, b), (x1 - r, b), (x1 - r + r * .55, b), (x1, y - r * .45), (x1, y),
         (x1, y + r * .45), (x1 - r + r * .55, t), (x1 - r, t), (0, t), (0, b)]
    c = [Path.MOVETO, Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
         Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(v, c), facecolor=color, edgecolor="none", zorder=3))


def hbars(labels, values, fname, title, subtitle, colors=None, note=None,
          suffix="", figh=None, pct_of=None):
    n = len(labels)
    fig, ax = plt.subplots(figsize=(7.2, figh or (0.38 * n + 1.35)))
    vmax = max(values)
    cols = colors or [SERIES] * n
    for i, (v, c) in enumerate(zip(values, cols)):
        rbar(ax, n - 1 - i, v, c, h=0.46, xmax=vmax)
        lab = f"{v}{suffix}" + (f"  (%{100*v/pct_of:.0f})" if pct_of else "")
        ax.text(v + vmax * 0.018, n - 1 - i, lab, va="center", ha="left",
                fontsize=8.5, color=INK2)
    ax.set_yticks(range(n))
    ax.set_yticklabels(labels[::-1], fontsize=9, color=INK)
    ax.set_xlim(0, vmax * 1.30)
    ax.set_ylim(-0.7, n - 0.3)
    ax.set_xticks([])
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(AXIS)
    ax.spines["left"].set_linewidth(0.8)
    ax.tick_params(axis="y", length=0)
    ax.set_title(title, fontsize=10.5, color=INK, loc="left", pad=24, weight="bold")
    ax.annotate(subtitle, xy=(0, 1), xycoords="axes fraction", xytext=(0, 6),
                textcoords="offset points", fontsize=8.5, color=MUTED,
                va="bottom", ha="left")
    fig.tight_layout()
    if note:
        fig.text(ax.get_position().x0, 0.002, note, fontsize=7.5, color=MUTED, va="bottom")
        fig.subplots_adjust(bottom=ax.get_position().y0 + 0.055)
    fig.savefig(f"{OUT}/{fname}", bbox_inches="tight")
    plt.close(fig)
    print("✓", fname)


# ─── Şekil: markayı okuma — değer eksenleri ────────────────────────────────
brands = [x for _, _, bl in DATA for x in bl]
dg = collections.Counter(v for x in brands for v in DEGER[x[0]])
ANA = [(k, v) for k, v in dg.most_common() if v >= 3]
kuyruk = sum(v for k, v in dg.most_common() if v < 3)
ANA.append(("Diğer (4 eksen)", kuyruk))
hbars([k for k, _ in ANA], [v for _, v in ANA], "sekil-deger-eksenleri.png",
      "Öğrencilerin markayı okuduğu değer eksenleri",
      "n = 75 marka · bir marka birden çok eksende okunabilir",
      pct_of=len(brands),
      note="\"Diğer\": doğayla bağ (2), uzmanlık ve danışmanlık (1), belirtilmemiş (2).")

# ─── Şekil: Bitner'ın üç boyutu ───────────────────────────────────────────
BITNER = {"i":"Ortam koşulları","r":"Ortam koşulları","s":"Ortam koşulları",
 "a":"Mekânsal yerleşim ve işlevsellik","d":"Mekânsal yerleşim ve işlevsellik",
 "o":"Mekânsal yerleşim ve işlevsellik","k":"Mekânsal yerleşim ve işlevsellik",
 "t":"Mekânsal yerleşim ve işlevsellik","e":"Mekânsal yerleşim ve işlevsellik",
 "q":"Mekânsal yerleşim ve işlevsellik",
 "m":"İşaretler, simgeler ve eserler","g":"İşaretler, simgeler ve eserler",
 "u":"İşaretler, simgeler ve eserler"}
cb = collections.Counter(); kapsam = collections.Counter()
for s_, m_, n_, a_ in KOD:
    dims = {BITNER[x] for x in a_.split(",") if x}
    for d_ in dims: cb[d_] += 1
    kapsam[len(dims)] += 1
k, v = zip(*cb.most_common())
hbars(list(k), list(v), "sekil-bitner.png",
      "Kararların servicescape boyutlarına dağılımı",
      "n = 75 marka önerisi · bir öneri birden çok boyuta değinebilir",
      pct_of=len(KOD),
      note="Boyutlar Bitner (1992). Önerilerin yalnızca %28'i üç boyutu birden kurmaktadır.")

# ─── Şekil: brifin zorunlu alanlarıyla örtüşme ────────────────────────────
PROGRAM = {"e":"Giriş ve marka eşiği","a":"Sergileme alanları","d":"Dolaşım ve mekânsal akış",
 "q":"Satış ve kasa bölgesi","k":"Deneyim ve etkileşim alanları","t":"Deneyim ve etkileşim alanları",
 "u":"Deneyim ve etkileşim alanları","s":"Deneyim ve etkileşim alanları","o":"Deneyim ve etkileşim alanları",
 "m":"Malzeme ve mimari öğeler","i":"Malzeme ve mimari öğeler","r":"Malzeme ve mimari öğeler",
 "g":"Malzeme ve mimari öğeler"}
ZORUNLU = ["Malzeme ve mimari öğeler","Sergileme alanları","Deneyim ve etkileşim alanları",
 "Dolaşım ve mekânsal akış","Giriş ve marka eşiği","Satış ve kasa bölgesi",
 "Depolama ve arka alan","Personel alanları"]
cp = collections.Counter()
for s_, m_, n_, a_ in KOD:
    for z in {PROGRAM[x] for x in a_.split(",") if x}: cp[z] += 1
hbars(ZORUNLU, [cp.get(z, 0) for z in ZORUNLU], "sekil-program-kapsami.png",
      "Kararların brifin zorunlu alanlarıyla örtüşmesi",
      "n = 75 marka önerisi · dersin brifi sekiz alanın çözülmesini istemektedir",
      pct_of=len(KOD),
      note="Son dört alan, kararların neredeyse tamamında boş kalmaktadır.")

# ─── Şekil: tasarım aygıtı repertuvarı ─────────────────────────────────────
AD = {"a": "Sergileme birimi (raf, kaide, vitrin, niş)", "m": "Malzeme ve yüzey",
      "i": "Aydınlatma", "d": "Dolaşım ve plan kurgusu", "g": "Grafik ve anlatı yüzeyi",
      "u": "Üretim görünürlüğü (atölye)", "k": "Kişiselleştirme ve etkileşim istasyonu",
      "t": "Dijital ve teknoloji", "r": "Renk", "o": "Oturma ve dinlenme",
      "s": "Koku, ses ve duyusal donatı", "e": "Giriş ve marka eşiği",
      "q": "Satış ve kasa bölgesi"}
ca = collections.Counter(x for *_, a in KOD for x in a.split(",") if x)
k, v = zip(*ca.most_common())
hbars([AD[i] for i in k], list(v), "sekil-aygit-repertuvari.png",
      "Mekânsal kararların tasarım aygıtı aileleri",
      "n = 75 marka önerisi · bir öneri birden çok aileye girebilir",
      pct_of=len(KOD),
      note="Yüzdeler, ilgili aileye değinen öneri oranıdır; toplamları 100'ü aşar.")

# ─── Şekil: anahtar kelime tematik kümeleri ────────────────────────────────
from analiz import TEMA
kws = [w for x in brands for w in x[4]]
ck = collections.Counter(kws)
tema = sorted(((sum(ck[y] for y in set(ws)), t) for t, ws in TEMA.items()), reverse=True)
hbars([t for _, t in tema], [n for n, _ in tema], "sekil-anahtar-kelime-temalari.png",
      "Anahtar kelimelerin tematik kümelere dağılımı",
      f"n = {len(kws)} anahtar kelime etiketi (146 tekil kelime)",
      pct_of=len(kws),
      note="Kümeler, kelime havuzundan tümevarımla türetilmiştir.")

# ─── Şekil: ürün kategorisi ────────────────────────────────────────────────
KAT = {"giyim": "Giyim", "ev-yasam": "Ev ve yaşam ürünleri",
       "taki-mucevher": "Takı ve mücevher", "parfum-koku": "Parfüm ve koku",
       "aksesuar-deri": "Aksesuar ve deri", "kozmetik-bakim": "Kozmetik ve bakım",
       "kitap-plak-kirtasiye": "Kitap, plak, kırtasiye", "teknoloji-obje": "Teknoloji ve obje",
       "denizcilik": "Denizcilik", "sanat-obje": "Sanat objesi"}
cc = collections.Counter(b[1] for _, _, bl in DATA for b in bl)
ana = [(KAT[k2], n) for k2, n in cc.most_common() if k2 in KAT]
diger = sum(n for k2, n in cc.items() if k2 not in KAT)
ana.append(("Diğer (6 kategori)", diger))
hbars([a for a, _ in ana], [n for _, n in ana], "sekil-urun-kategorisi.png",
      "Önerilen markaların ürün kategorisi dağılımı",
      "n = 75 marka önerisi · 16 kategori", pct_of=75,
      note="\"Diğer\": botanik, kahve, seramik, ayakkabı, müzik enstrümanı, gözlük (her biri 1).")
