# -*- coding: utf-8 -*-
# Çalışma Kâğıdı 3 "Marka Araştırması" veri seti — 25 teslim x 3 marka önerisi
# alan: (ogrenci, grup, [ (marka, kategori, mensei, anahtar_kelimeler[]) x3 ])
# kategori: giyim, aksesuar-deri, taki-mucevher, parfum-koku, kozmetik-bakim,
#           ev-yasam, seramik, kitap-plak-kirtasiye, muzik-enstruman, sanat-obje,
#           teknoloji-obje, gozluk, denizcilik, kahve, botanik, ayakkabi
# mensei: TR, YD (yurtdisi)
# olcek: nis (bagimsiz/kucuk), kurumsal (yerlesik zincir/global)

DATA = [
("Zehra Meydanaçar","G2",[
  ("Rouje","giyim","YD","nis",["zahmetsiz","fransız","nostaljik"]),
  ("Rivièra Maison","ev-yasam","YD","nis",["rafine","küresel","samimi"]),
  ("AGMES","taki-mucevher","YD","nis",["minimalist","heykelsi","el yapımı"])]),
("Sude Elçin","G2",[
  ("Bliss Atelier","giyim","TR","nis",["iddialı","elegant","sofistike"]),
  ("Art Doku Halı","ev-yasam","TR","nis",["zanaat","kültürel","özenli"]),
  ("Yaprak Aybak Design Studio","ev-yasam","TR","nis",["koleksiyonculuk","zamansızlık","kontrast"])]),
("Hilal Nur Kahraman","G4",[
  ("Hereu","aksesuar-deri","YD","nis",["zanaat","akdeniz nostaljisi","sade şıklık"]),
  ("Musto","denizcilik","YD","kurumsal",["performans","miras","denizcilik"]),
  ("Tom Dixon","ev-yasam","YD","kurumsal",["metalik","heykelsi","cüretkâr"])]),
("Yasin Bile","G3",[
  ("Liman Market","denizcilik","TR","nis",["pratik","kapsamlı","dijital"]),
  ("Hipicon","sanat-obje","TR","nis",["özgün","modern","yaratıcı"]),
  ("Les Benjamins","giyim","TR","kurumsal",["dinamik","çağdaş","kültürel"])]),
("Ebrar Atalay","G4",[
  ("Atelier Rebul","parfum-koku","TR","kurumsal",["zarafet","nostalji","duyusallık"]),
  ("Minoa","kitap-plak-kirtasiye","TR","nis",["keşif","sakinlik","sosyalleşme"]),
  ("Yargıcı Home","ev-yasam","TR","kurumsal",["doğallık","zamansızlık","konfor"])]),
("İrem Vural","G5",[
  ("OPIA Leather","aksesuar-deri","TR","nis",["zanaat","kişiselleştirme","zamansızlık"]),
  ("Pekji","parfum-koku","TR","nis",["sanat","keşif","kimlik"]),
  ("Desert Lobby","taki-mucevher","TR","nis",["hikâye","sembol","el işçiliği"])]),
("Musa Kaya","G1",[
  ("Atelier Rebul","parfum-koku","TR","kurumsal",["zarif","geleneksel","duyusal"]),
  ("Mudo Concept","ev-yasam","TR","kurumsal",["modern","doğal","yaşam"]),
  ("Miniso","ev-yasam","YD","kurumsal",["eğlenceli","renkli","erişilebilir"])]),
("İldem Koca","G5",[
  ("Montale Paris","parfum-koku","YD","nis",["yolculuk","keşif","gizem"]),
  ("Āzlee","taki-mucevher","YD","nis",["miras","tekillik","bağ"]),
  ("Philini","aksesuar-deri","YD","nis",["iz","zanaat","dönüşüm"])]),
("Ebrar Dinç","G3",[
  ("Otrera","aksesuar-deri","TR","nis",["el işçiliği","doğallık","özgünlük"]),
  ("Chelebi","taki-mucevher","TR","nis",["zarafet","doğallık","değer"]),
  ("Cademe","ev-yasam","TR","nis",["kişiselleştirme","koku","yaratıcılık"])]),
("Zeynep Berre Kürklü","G5",[
  ("Kartela","giyim","TR","nis",["zamansızlık","kalite","rahatlık"]),
  ("Paden Cosmetics","kozmetik-bakim","TR","nis",["renk çeşitliliği","kişisellik","erişilebilirlik"]),
  ("Shulebags","aksesuar-deri","TR","nis",["vitrinleşme","kimlik","aidiyet"])]),
("Mehmet Yaman","G2",[
  ("Voyant Apparel Co.","giyim","TR","nis",["özgünlük","tasarım","nakış"]),
  ("Turtile Design","ev-yasam","TR","nis",["el işçiliği","mozaik","ışık"]),
  ("No:19 Istanbul","taki-mucevher","TR","nis",["doğallık","seyahat","zamansızlık"])]),
("Azat Doğru","G5",[
  ("IKEA","ev-yasam","YD","kurumsal",["fonksiyonel","sade","erişilebilir"]),
  ("Bath & Body Works","parfum-koku","YD","kurumsal",["duyusal","canlı","keyifli"]),
  ("Muji","ev-yasam","YD","kurumsal",["minimal","doğal","işlevsel"])]),
("Nurgül Karademir","G5",[
  ("Mise Montrail","giyim","TR","nis",["konforlu","özgün","doğal"]),
  ("Labofem","botanik","TR","nis",["botanik","terapi","estetik"]),
  ("Gordion Coffee","kahve","TR","nis",["zanaat","ritüel","keşif"])]),
("Oğuz Kağan Aksoy","G5",[
  ("Roots Ceramic","seramik","TR","nis",["doğal","özgün","dokusal"]),
  ("Nuwé","taki-mucevher","TR","nis",["zarif","özgün","kişisel"]),
  ("Caracal","kozmetik-bakim","TR","nis",["güven","doğal","şeffaf"])]),
("Eda Yalnız","G4",[
  ("Grace Brands","ev-yasam","TR","kurumsal",["zarafet","seçkinlik","yaşam"]),
  ("Zsa Zsa Zsu","ev-yasam","TR","nis",["renk","özgürlük","katman"]),
  ("Nautica","giyim","YD","kurumsal",["deniz","özgürlük","keşif"])]),
("Buse Sandal","G5",[
  ("Esra Helvacı Butik","giyim","TR","nis",["zarif","sade","şık"]),
  ("Be One Jewelry","taki-mucevher","TR","nis",["lüks","sıcaklık","aydınlık"]),
  ("Selin Shoes","ayakkabi","TR","nis",["güçlü","konforlu","zamansız"])]),
("Eda Akşehirlioğlu","G1",[
  ("Rot&Boa","giyim","TR","nis",["enerjik","tatil","ferah"]),
  ("Phytosurgence","kozmetik-bakim","YD","nis",["deney","doğa","doğal içerik"]),
  ("Siedres","giyim","TR","nis",["renkli","deneysel","özgün"])]),
("Burak Çetincan Horuzoğlu","G3",[
  ("LunaWear","giyim","TR","nis",["minimalizm","doğallık","konfor"]),
  ("PixelForge","teknoloji-obje","TR","nis",["teknoloji","esneklik","yenilik"]),
  ("Solstice Jewelry","taki-mucevher","TR","nis",["zarafet","güven","doğallık"])]),
("Ezgi Şahin","G5",[
  ("Sanat Gezgini","sanat-obje","TR","nis",["vurgu","erişilebilirlik","bütünlük"]),
  ("Kadıköy Müzik Market","kitap-plak-kirtasiye","TR","nis",["samimiyet","yaşanmışlık","dinleme"]),
  ("Mydukkan","muzik-enstruman","TR","nis",["vurgu","deneme","öğrenme"])]),
("Esma Sofularlı","G3",[
  ("Uniqlo","giyim","YD","kurumsal",["sadelik","düzen","konfor"]),
  ("Oura","teknoloji-obje","YD","nis",["teknoloji","kişisellik","sakinlik"]),
  ("The Purest Solutions","kozmetik-bakim","TR","nis",["saflık","bilimsellik","keşif"])]),
("Samet Diribaş","G2",[
  ("Fibrika Store","teknoloji-obje","TR","nis",["teknolojik","eğlenceli","özgün"]),
  ("Orevo","taki-mucevher","TR","nis",["heykelsi","mitolojik","güçlü"]),
  ("Carpe","giyim","TR","nis",["alternatif","karanlık","özgür"])]),
("Sude Karman","G4",[
  ("Kaft","giyim","TR","nis",["illüstrasyon","sanat","özgünlük"]),
  ("Arma Life","giyim","TR","nis",["dinamik","şehirli","konfor"]),
  ("MAD Parfüm","parfum-koku","TR","nis",["esans","koku","duyusallık"])]),
("Nehir Yavuz","G2",[
  ("Kokulab","parfum-koku","TR","nis",["kişisellik","doğal","deneyim"]),
  ("Dilek Optik","gozluk","TR","nis",["güven","uyum","uzmanlık"]),
  ("Only Japan Vinyl","kitap-plak-kirtasiye","TR","nis",["koleksiyon","keşif","nostalji"])]),
("Ceren Sevgen","G1",[
  ("Half Magic","kozmetik-bakim","YD","nis",["özgüven","güç","sanat"]),
  ("Ofline Jewelry Store","taki-mucevher","TR","nis",["tutku","gizem","asilik"]),
  ("Liquides Imaginaires","parfum-koku","YD","nis",["mitoloji","simya","zarafet"])]),
("Zeynep Topuz","G5",[
  ("Abuello.co","giyim","TR","nis",["modern","zarif","özgün"]),
  ("Adellabutik","giyim","TR","nis",["feminen","zarif","trend"]),
  ("Baglovis","aksesuar-deri","TR","nis",["modern","fonksiyonel","ulaşılabilir"])]),
]
