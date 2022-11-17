def ogrenci_yazdir():
    isim = input("Öğrencinin isim, soyisim: ")
    vize = float(input("Öğrencinin vize notunu girin: "))
    final = float(input("Öğrencinin final notunu gir: "))
    basari_notu = vize * 0.4 + final * 0.6
    harf_notu = ""
    if basari_notu >= 85:
        harf_notu = "AA"
    elif basari_notu >= 70:
        harf_notu = "BA"
    elif basari_notu >= 60:
        harf_notu = "BB"
    elif basari_notu >= 50:
        harf_notu = "CB"
    elif basari_notu >= 40:
        harf_notu = "CC"
    else:
        harf_notu = "FF"
        
    print("""{} adlı öğrencinin
        Başarı Notu: {}
        Harf Notu: {}
        \n""".format(isim, basari_notu, harf_notu))
    
    with open("notlar.txt", "a") as dosya:
        dosya.writelines("""{} adlı öğrencinin
        Başarı Notu: {}
        Harf Notu: {}
        \n""".format(isim, basari_notu, harf_notu))

kac_ogrenci = int(input("Kaç tane öğrenci yazdıracaksınız? "))
for i in range(kac_ogrenci):
    ogrenci_yazdir()
