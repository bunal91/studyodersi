# -*- coding: utf-8 -*-
"""
Çalışma Kâğıdı 3, "03 Anahtar kelime → mekânsal tasarım kararı" sütununun kodlaması.

SOMUTLUK — kararın mekânda ne kadar karşılık bulduğu:
  1  sıfatta kalan    anahtar kelime başka bir sıfatla karşılanmış; çizilecek bir şey yok
  2  öğe adlandıran   bir tasarım öğesi adlandırılmış, ama mekândaki yeri söylenmemiş
  3  mekânda yer tutan öğe bir konuma, ilişkiye ya da ölçüye bağlanmış

MARKA_ADI — kararın markanın kendi diliyle adlandırılıp adlandırılmadığı (0/1).
  Yalnızca "mekânda yer tutan" kararlarda görülür.

AYGIT — kararın değindiği tasarım aygıtı aileleri (çok etiketli):
  a sergileme birimi · m malzeme ve yüzey · i aydınlatma · d dolaşım ve plan ·
  g grafik ve anlatı yüzeyi · u üretim görünürlüğü · k kişiselleştirme ve etkileşim ·
  t dijital ve teknoloji · r renk · o oturma ve dinlenme · s koku, ses ve duyusal donatı

Satır biçimi: (öğrenci, marka, somutluk, marka_adi, aygitlar)
"""
KOD = [
("Zehra Meydanaçar","Rouje",2,0,"m,i"),
("Zehra Meydanaçar","Rivièra Maison",2,0,"a,g"),
("Zehra Meydanaçar","AGMES",2,0,"a,m"),
("Sude Elçin","Bliss Atelier",2,0,"a,m"),
("Sude Elçin","Art Doku Halı",3,1,"a,g,u,i"),
("Sude Elçin","Yaprak Aybak Design Studio",3,0,"a,m"),
("Hilal Nur Kahraman","Hereu",3,1,"u,m,a"),
("Hilal Nur Kahraman","Musto",3,1,"m,a,k,t"),
("Hilal Nur Kahraman","Tom Dixon",3,1,"a,i,m"),
("Yasin Bile","Liman Market",3,1,"t,k,d"),
("Yasin Bile","Hipicon",3,0,"a,m,i"),
("Yasin Bile","Les Benjamins",3,0,"i,m,g,t"),
("Ebrar Atalay","Atelier Rebul",2,0,"a,m,i,s"),
("Ebrar Atalay","Minoa",2,0,"a,m,i,o"),
("Ebrar Atalay","Yargıcı Home",2,0,"m,a,o,i"),
("İrem Vural","OPIA Leather",3,1,"u,k,m"),
("İrem Vural","Pekji",3,1,"a,d,k"),
("İrem Vural","Desert Lobby",2,0,"a,g,u"),
("Musa Kaya","Atelier Rebul",2,0,"a,m,s"),
("Musa Kaya","Mudo Concept",2,0,"a,m"),
("Musa Kaya","Miniso",2,0,"a,r"),
("İldem Koca","Montale Paris",3,1,"d,k,i,s"),
("İldem Koca","Āzlee",3,1,"a,k"),
("İldem Koca","Philini",3,1,"m,u,a"),
("Ebrar Dinç","Otrera",2,0,"a,m"),
("Ebrar Dinç","Chelebi",2,0,"a,m"),
("Ebrar Dinç","Cademe",3,0,"k,s,a"),
("Zeynep Berre Kürklü","Kartela",1,0,"m,r,d"),
("Zeynep Berre Kürklü","Paden Cosmetics",2,0,"r,a,d"),
("Zeynep Berre Kürklü","Shulebags",3,1,"a,m,g"),
("Mehmet Yaman","Voyant Apparel Co.",3,0,"g,a"),
("Mehmet Yaman","Turtile Design",3,0,"a,m,i"),
("Mehmet Yaman","No:19 Istanbul",3,0,"m,g,r"),
("Azat Doğru","IKEA",2,0,"a,s"),
("Azat Doğru","Bath & Body Works",2,0,"a,i,m"),
("Azat Doğru","Muji",2,0,"a"),
("Nurgül Karademir","Mise Montrail",2,0,"m,o"),
("Nurgül Karademir","Labofem",1,0,"m"),
("Nurgül Karademir","Gordion Coffee",1,0,"u"),
("Oğuz Kağan Aksoy","Roots Ceramic",2,0,"m,a,d"),
("Oğuz Kağan Aksoy","Nuwé",2,0,"a,k,o"),
("Oğuz Kağan Aksoy","Caracal",2,0,"a,m,g"),
("Eda Yalnız","Grace Brands",2,0,"m,i,a,o"),
("Eda Yalnız","Zsa Zsa Zsu",3,0,"r,a,d"),
("Eda Yalnız","Nautica",2,0,"m,d,a"),
("Buse Sandal","Esra Helvacı Butik",1,0,"m"),
("Buse Sandal","Be One Jewelry",2,0,"m,i"),
("Buse Sandal","Selin Shoes",2,0,"a,o,m"),
("Eda Akşehirlioğlu","Rot&Boa",1,0,"r,m,d"),
("Eda Akşehirlioğlu","Phytosurgence",1,0,"k,m"),
("Eda Akşehirlioğlu","Siedres",1,0,"r,a"),
("Burak Çetincan Horuzoğlu","LunaWear",2,0,"a,m,d"),
("Burak Çetincan Horuzoğlu","PixelForge",3,0,"u,t,a"),
("Burak Çetincan Horuzoğlu","Solstice Jewelry",2,0,"m,i,a"),
("Ezgi Şahin","Sanat Gezgini",2,0,"a,r,d"),
("Ezgi Şahin","Kadıköy Müzik Market",2,0,"i,o,m,a"),
("Ezgi Şahin","Mydukkan",3,0,"a,d,o,s"),
("Esma Sofularlı","Uniqlo",2,0,"a,d,m"),
("Esma Sofularlı","Oura",2,0,"t,k,i"),
("Esma Sofularlı","The Purest Solutions",2,0,"g,a,k"),
("Samet Diribaş","Fibrika Store",2,0,"u,r,a"),
("Samet Diribaş","Orevo",3,0,"a,g,i"),
("Samet Diribaş","Carpe",3,0,"r,i,a"),
("Sude Karman","Kaft",3,0,"g,a,m,t"),
("Sude Karman","Arma Life",3,0,"a,m,o"),
("Sude Karman","MAD Parfüm",3,1,"k,s,t,g"),
("Nehir Yavuz","Kokulab",1,0,"k,m"),
("Nehir Yavuz","Dilek Optik",1,0,"d,k"),
("Nehir Yavuz","Only Japan Vinyl",1,0,"a,o,m"),
("Ceren Sevgen","Half Magic",1,0,"a,r"),
("Ceren Sevgen","Ofline Jewelry Store",2,0,"r,m,a"),
("Ceren Sevgen","Liquides Imaginaires",2,0,"a,m,r"),
("Zeynep Topuz","Abuello.co",1,0,"i,m,a"),
("Zeynep Topuz","Adellabutik",1,0,""),
("Zeynep Topuz","Baglovis",1,0,""),
]
