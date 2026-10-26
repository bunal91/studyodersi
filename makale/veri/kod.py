# -*- coding: utf-8 -*-
"""
Çalışma Kâğıdı 3, "Anahtar kelime → mekânsal tasarım kararı" sütununun kodlaması.

SOLO = Biggs ve Collis (1982) SOLO taksonomisine göre kodlanan düzey:
  0  ön yapısal      mekânsal içerik yok; ürün/pazarlama ifadesinin tekrarı
  1  tek yapılı      tek bir genel atmosfer sıfatı; çizilemez
  2  çok yapılı      bir ya da birkaç tasarım öğesi sayılır, aralarında ilişki kurulmaz
  3  ilişkisel       öğe mekândaki bir konum, ilişki ya da ölçüyle bağlanır
  4  soyutlanmış     markanın kendi sözlüğünden adlandırılmış, mekânda tekrar eden aygıt

AYGIT = kararın değindiği tasarım aygıtı aileleri (çok etiketli):
  a sergileme birimi · m malzeme ve yüzey · i aydınlatma · d dolaşım ve plan ·
  g grafik ve anlatı yüzeyi · u üretim görünürlüğü · k kişiselleştirme ve etkileşim ·
  t dijital ve teknoloji · r renk · o oturma ve dinlenme · s koku, ses ve duyusal donatı

Satır biçimi: (öğrenci, marka, SOLO, aygıtlar)
"""
KOD = [
("Zehra Meydanaçar","Rouje",2,"m,i"),
("Zehra Meydanaçar","Rivièra Maison",2,"a,g"),
("Zehra Meydanaçar","AGMES",2,"a,m"),
("Sude Elçin","Bliss Atelier",2,"a,m"),
("Sude Elçin","Art Doku Halı",4,"a,g,u,i"),
("Sude Elçin","Yaprak Aybak Design Studio",3,"a,m"),
("Hilal Nur Kahraman","Hereu",4,"u,m,a"),
("Hilal Nur Kahraman","Musto",4,"m,a,k,t"),
("Hilal Nur Kahraman","Tom Dixon",4,"a,i,m"),
("Yasin Bile","Liman Market",4,"t,k,d"),
("Yasin Bile","Hipicon",3,"a,m,i"),
("Yasin Bile","Les Benjamins",3,"i,m,g,t"),
("Ebrar Atalay","Atelier Rebul",2,"a,m,i,s"),
("Ebrar Atalay","Minoa",2,"a,m,i,o"),
("Ebrar Atalay","Yargıcı Home",2,"m,a,o,i"),
("İrem Vural","OPIA Leather",4,"u,k,m"),
("İrem Vural","Pekji",4,"a,d,k"),
("İrem Vural","Desert Lobby",2,"a,g,u"),
("Musa Kaya","Atelier Rebul",2,"a,m,s"),
("Musa Kaya","Mudo Concept",2,"a,m"),
("Musa Kaya","Miniso",2,"a,r"),
("İldem Koca","Montale Paris",4,"d,k,i,s"),
("İldem Koca","Āzlee",4,"a,k"),
("İldem Koca","Philini",4,"m,u,a"),
("Ebrar Dinç","Otrera",2,"a,m"),
("Ebrar Dinç","Chelebi",2,"a,m"),
("Ebrar Dinç","Cademe",3,"k,s,a"),
("Zeynep Berre Kürklü","Kartela",1,"m,r,d"),
("Zeynep Berre Kürklü","Paden Cosmetics",2,"r,a,d"),
("Zeynep Berre Kürklü","Shulebags",4,"a,m,g"),
("Mehmet Yaman","Voyant Apparel Co.",3,"g,a"),
("Mehmet Yaman","Turtile Design",3,"a,m,i"),
("Mehmet Yaman","No:19 Istanbul",3,"m,g,r"),
("Azat Doğru","IKEA",2,"a,s"),
("Azat Doğru","Bath & Body Works",2,"a,i,m"),
("Azat Doğru","Muji",2,"a"),
("Nurgül Karademir","Mise Montrail",2,"m,o"),
("Nurgül Karademir","Labofem",1,"m"),
("Nurgül Karademir","Gordion Coffee",1,"u"),
("Oğuz Kağan Aksoy","Roots Ceramic",2,"m,a,d"),
("Oğuz Kağan Aksoy","Nuwé",2,"a,k,o"),
("Oğuz Kağan Aksoy","Caracal",2,"a,m,g"),
("Eda Yalnız","Grace Brands",2,"m,i,a,o"),
("Eda Yalnız","Zsa Zsa Zsu",3,"r,a,d"),
("Eda Yalnız","Nautica",2,"m,d,a"),
("Buse Sandal","Esra Helvacı Butik",1,"m"),
("Buse Sandal","Be One Jewelry",2,"m,i"),
("Buse Sandal","Selin Shoes",2,"a,o,m"),
("Eda Akşehirlioğlu","Rot&Boa",1,"r,m,d"),
("Eda Akşehirlioğlu","Phytosurgence",1,"k,m"),
("Eda Akşehirlioğlu","Siedres",1,"r,a"),
("Burak Çetincan Horuzoğlu","LunaWear",2,"a,m,d"),
("Burak Çetincan Horuzoğlu","PixelForge",3,"u,t,a"),
("Burak Çetincan Horuzoğlu","Solstice Jewelry",2,"m,i,a"),
("Ezgi Şahin","Sanat Gezgini",2,"a,r,d"),
("Ezgi Şahin","Kadıköy Müzik Market",2,"i,o,m,a"),
("Ezgi Şahin","Mydukkan",3,"a,d,o,s"),
("Esma Sofularlı","Uniqlo",2,"a,d,m"),
("Esma Sofularlı","Oura",2,"t,k,i"),
("Esma Sofularlı","The Purest Solutions",2,"g,a,k"),
("Samet Diribaş","Fibrika Store",2,"u,r,a"),
("Samet Diribaş","Orevo",3,"a,g,i"),
("Samet Diribaş","Carpe",3,"r,i,a"),
("Sude Karman","Kaft",3,"g,a,m,t"),
("Sude Karman","Arma Life",3,"a,m,o"),
("Sude Karman","MAD Parfüm",4,"k,s,t,g"),
("Nehir Yavuz","Kokulab",1,"k,m"),
("Nehir Yavuz","Dilek Optik",1,"d,k"),
("Nehir Yavuz","Only Japan Vinyl",1,"a,o,m"),
("Ceren Sevgen","Half Magic",1,"a,r"),
("Ceren Sevgen","Ofline Jewelry Store",2,"r,m,a"),
("Ceren Sevgen","Liquides Imaginaires",2,"a,m,r"),
("Zeynep Topuz","Abuello.co",1,"i,m,a"),
("Zeynep Topuz","Adellabutik",0,""),
("Zeynep Topuz","Baglovis",0,""),
]
