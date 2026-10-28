# -*- coding: utf-8 -*-
"""
Çalışma Kâğıdı 3, "03 Anahtar kelime → mekânsal tasarım kararı" sütununun kodlaması.

AYGIT — kararın değindiği tasarım öğesi aileleri (çok etiketli):
  a sergileme birimi        m malzeme ve yüzey         i aydınlatma
  d dolaşım ve plan         g grafik ve anlatı yüzeyi  u üretim görünürlüğü
  k kişiselleştirme ve etkileşim istasyonu             t dijital ve teknoloji
  r renk                    o oturma ve dinlenme       s koku, ses ve duyusal donatı
  e giriş ve marka eşiği    q satış ve kasa bölgesi

  e ve q, karar sütununda açıkça geçtiğinde kodlanmıştır; türetilmemiştir.
  Brifin diğer iki zorunlu alanı (depolama ve arka alan, personel alanları)
  hiçbir kararda geçmediği için kod karşılığı yoktur.

MARKA_ADI — kararın markanın kendi diliyle adlandırılıp adlandırılmadığı (0/1).

Satır biçimi: (öğrenci, marka, marka_adi, aygitlar)
"""
KOD = [
("Zehra Meydanaçar","Rouje",0,"m,i"),
("Zehra Meydanaçar","Rivièra Maison",0,"a,g"),
("Zehra Meydanaçar","AGMES",0,"a,m"),
("Sude Elçin","Bliss Atelier",0,"a,m"),
("Sude Elçin","Art Doku Halı",1,"a,g,u,i"),
("Sude Elçin","Yaprak Aybak Design Studio",0,"a,m"),
("Hilal Nur Kahraman","Hereu",1,"u,m,a"),
("Hilal Nur Kahraman","Musto",1,"m,a,k,t"),
("Hilal Nur Kahraman","Tom Dixon",1,"a,i,m"),
("Yasin Bile","Liman Market",1,"t,k,d,e,q"),
("Yasin Bile","Hipicon",0,"a,m,i"),
("Yasin Bile","Les Benjamins",0,"i,m,g,t"),
("Ebrar Atalay","Atelier Rebul",0,"a,m,i,s"),
("Ebrar Atalay","Minoa",0,"a,m,i,o"),
("Ebrar Atalay","Yargıcı Home",0,"m,a,o,i"),
("İrem Vural","OPIA Leather",1,"u,k,m"),
("İrem Vural","Pekji",1,"a,d,k"),
("İrem Vural","Desert Lobby",0,"a,g,u"),
("Musa Kaya","Atelier Rebul",0,"a,m,s"),
("Musa Kaya","Mudo Concept",0,"a,m"),
("Musa Kaya","Miniso",0,"a,r"),
("İldem Koca","Montale Paris",1,"d,k,i,s,e"),
("İldem Koca","Āzlee",1,"a,k"),
("İldem Koca","Philini",1,"m,u,a"),
("Ebrar Dinç","Otrera",0,"a,m"),
("Ebrar Dinç","Chelebi",0,"a,m"),
("Ebrar Dinç","Cademe",0,"k,s,a"),
("Zeynep Berre Kürklü","Kartela",0,"m,r,d"),
("Zeynep Berre Kürklü","Paden Cosmetics",0,"r,a,d"),
("Zeynep Berre Kürklü","Shulebags",1,"a,m,g"),
("Mehmet Yaman","Voyant Apparel Co.",0,"g,a"),
("Mehmet Yaman","Turtile Design",0,"a,m,i"),
("Mehmet Yaman","No:19 Istanbul",0,"m,g,r"),
("Azat Doğru","IKEA",0,"a,s"),
("Azat Doğru","Bath & Body Works",0,"a,i,m"),
("Azat Doğru","Muji",0,"a"),
("Nurgül Karademir","Mise Montrail",0,"m,o"),
("Nurgül Karademir","Labofem",0,"m"),
("Nurgül Karademir","Gordion Coffee",0,"u"),
("Oğuz Kağan Aksoy","Roots Ceramic",0,"m,a,d"),
("Oğuz Kağan Aksoy","Nuwé",0,"a,k,o"),
("Oğuz Kağan Aksoy","Caracal",0,"a,m,g"),
("Eda Yalnız","Grace Brands",0,"m,i,a,o"),
("Eda Yalnız","Zsa Zsa Zsu",0,"r,a,d"),
("Eda Yalnız","Nautica",0,"m,d,a"),
("Buse Sandal","Esra Helvacı Butik",0,"m"),
("Buse Sandal","Be One Jewelry",0,"m,i"),
("Buse Sandal","Selin Shoes",0,"a,o,m"),
("Eda Akşehirlioğlu","Rot&Boa",0,"r,m,d"),
("Eda Akşehirlioğlu","Phytosurgence",0,"k,m"),
("Eda Akşehirlioğlu","Siedres",0,"r,a"),
("Burak Çetincan Horuzoğlu","LunaWear",0,"a,m,d"),
("Burak Çetincan Horuzoğlu","PixelForge",0,"u,t,a"),
("Burak Çetincan Horuzoğlu","Solstice Jewelry",0,"m,i,a"),
("Ezgi Şahin","Sanat Gezgini",0,"a,r,d"),
("Ezgi Şahin","Kadıköy Müzik Market",0,"i,o,m,a"),
("Ezgi Şahin","Mydukkan",0,"a,d,o,s"),
("Esma Sofularlı","Uniqlo",0,"a,d,m"),
("Esma Sofularlı","Oura",0,"t,k,i"),
("Esma Sofularlı","The Purest Solutions",0,"g,a,k"),
("Samet Diribaş","Fibrika Store",0,"u,r,a"),
("Samet Diribaş","Orevo",0,"a,g,i"),
("Samet Diribaş","Carpe",0,"r,i,a"),
("Sude Karman","Kaft",0,"g,a,m,t"),
("Sude Karman","Arma Life",0,"a,m,o"),
("Sude Karman","MAD Parfüm",1,"k,s,t,g"),
("Nehir Yavuz","Kokulab",0,"k,m"),
("Nehir Yavuz","Dilek Optik",0,"d,k"),
("Nehir Yavuz","Only Japan Vinyl",0,"a,o,m"),
("Ceren Sevgen","Half Magic",0,"a,r"),
("Ceren Sevgen","Ofline Jewelry Store",0,"r,m,a"),
("Ceren Sevgen","Liquides Imaginaires",0,"a,m,r"),
("Zeynep Topuz","Abuello.co",0,"i,m,a"),
("Zeynep Topuz","Adellabutik",0,""),
("Zeynep Topuz","Baglovis",0,""),
]
