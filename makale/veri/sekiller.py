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

OUT = "/home/user/studyodersi/makale/sekil"
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
SERIES = "#2a78d6"                                             # tek seri → tek renk
ORDINAL = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # sıralı ölçek (doğrulandı)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "savefig.dpi": 200,
    "axes.edgecolor": AXIS, "text.color": INK,
})

SOLO = ["Ön yapısal", "Tek yapılı", "Çok yapılı", "İlişkisel", "Soyutlanmış"]


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
    ax.set_title(title, fontsize=10.5, color=INK, loc="left", pad=20, weight="bold")
    ax.text(0, 1.028, subtitle, transform=ax.transAxes, fontsize=8.5,
            color=MUTED, va="bottom")
    fig.tight_layout()
    if note:
        fig.text(ax.get_position().x0, 0.002, note, fontsize=7.5, color=MUTED, va="bottom")
        fig.subplots_adjust(bottom=ax.get_position().y0 + 0.055)
    fig.savefig(f"{OUT}/{fname}", bbox_inches="tight")
    plt.close(fig)
    print("✓", fname)


# ─── Şekil: SOLO düzey dağılımı ────────────────────────────────────────────
lv = [l for _, _, l, _ in KOD]
c = collections.Counter(lv)
hbars([f"{SOLO[i]}" for i in range(5)], [c[i] for i in range(5)],
      "sekil-solo-dagilim.png",
      "Marka önerilerinin SOLO düzeyine göre dağılımı",
      f"n = {len(KOD)} marka önerisi · yüzdeler toplam içindeki pay",
      colors=ORDINAL, pct_of=len(KOD),
      note="Düzeyler sıralıdır (ön yapısaldan soyutlanmışa); renk koyulaşması düzey sırasını gösterir.")

# ─── Şekil: öğrencilerin ulaştığı en yüksek düzey ──────────────────────────
per = collections.defaultdict(list)
for s, b, l, a in KOD:
    per[s].append(l)
enyuksek = collections.Counter(max(v) for v in per.values())
baskin = collections.Counter(statistics.mode(v) for v in per.values())
fig, ax = plt.subplots(figsize=(7.2, 3.2))
x = range(5)
w = 0.30
for off, data, lab, col in ((-w/2, enyuksek, "ulaşılan en yüksek düzey", SERIES),
                            (w/2, baskin, "üç önerideki baskın düzey", "#eb6834")):
    ax.bar([i + off for i in x], [data[i] for i in x], width=w - 0.04,
           color=col, edgecolor="none", zorder=3, label=lab)
    for i in x:
        if data[i]:
            ax.text(i + off, data[i] + 0.3, str(data[i]), ha="center",
                    fontsize=8.5, color=INK2)
ax.set_xticks(list(x))
ax.set_xticklabels(SOLO, fontsize=9)
ax.set_ylim(0, max(max(enyuksek.values()), max(baskin.values())) + 2)
ax.set_ylabel("öğrenci sayısı", fontsize=8.5, color=INK2)
ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.legend(frameon=False, fontsize=8.5, loc="upper left", labelcolor=INK2)
ax.set_title("Öğrencilerin SOLO düzeyi profili", fontsize=10.5, loc="left",
             pad=15, weight="bold")
ax.text(0, 1.055, "n = 25 öğrenci · her öğrenci üç marka önerisi getirmiştir",
        transform=ax.transAxes, fontsize=8.5, color=MUTED, va="bottom")
fig.tight_layout()
fig.savefig(f"{OUT}/sekil-ogrenci-profili.png", bbox_inches="tight")
plt.close(fig)
print("✓ sekil-ogrenci-profili.png")

# ─── Şekil: tasarım aygıtı repertuvarı ─────────────────────────────────────
AD = {"a": "Sergileme birimi (raf, kaide, vitrin, niş)", "m": "Malzeme ve yüzey",
      "i": "Aydınlatma", "d": "Dolaşım ve plan kurgusu", "g": "Grafik ve anlatı yüzeyi",
      "u": "Üretim görünürlüğü (atölye)", "k": "Kişiselleştirme ve etkileşim istasyonu",
      "t": "Dijital ve teknoloji", "r": "Renk", "o": "Oturma ve dinlenme",
      "s": "Koku, ses ve duyusal donatı"}
ca = collections.Counter(x for _, _, _, a in KOD for x in a.split(",") if x)
k, v = zip(*ca.most_common())
hbars([AD[i] for i in k], list(v), "sekil-aygit-repertuvari.png",
      "Mekânsal kararların tasarım aygıtı aileleri",
      "n = 75 marka önerisi · bir öneri birden çok aileye girebilir",
      pct_of=len(KOD),
      note="Yüzdeler, ilgili aileye değinen öneri oranıdır; toplamları 100'ü aşar.")

# ─── Şekil: anahtar kelime tematik kümeleri ────────────────────────────────
from analiz import TEMA
kws = [w for _, _, bl in DATA for b in bl for w in b[4]]
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
