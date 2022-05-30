from Student import Student

def showMenu():
    #try: Hataları denetler.
    try:
        print("ULUDAĞ ÜNİVERSİTESİ ÖĞRENCİ TANIMA SİSTEMİNE HOŞGELDİNİZ")
        print("\n","#"*5, "Seçim Yapın", "#"*5)
        print("1) Öğrenci ekle")
        print("2) Öğrenci bul")
        print("3) Öğrenci sil")
        print("4) Öğrenci bilgilerini güncelle")
        print("5) Tüm öğrencileri görüntüle")
secim = input("Seçim yap: ")
        if secim == "q" or secim == "exit": #yukarıda gösterilen sayılar yerine 'q' ya da 'exit' girilirse sistemden çıkmasını sağlar 
            exit(0)

        secim = int(secim)

        if secim == 1:              # shell'e 1 girildiği zaman eklenilmek istenen öğrenci hakkında sorular sorar.
            ad = input("Adı: ")
            soyad = input("Soyad: ")
            sehir = input("Yaşadığı şehir: ")
            okul = input("Bölümü: ")
            dogum = int(input("Doğum yılı: "))
            mail = input("Mail adresi: ")
            tel = input("Telefon numarası: ")
            egitim = []
            while True:
                egt = input("Aldığı dersler: ")
                if egt == "":
                    break
                egitim.append(egt)
                #Aldığı dersler sorusunu sonlandırmak için kutucuğu boş bırakıp enter tuşuna basmak gerekiyor.
            ogrenci = {"dogum_tarihi": dogum, "egitim": egitim, "okul": okul, "soyadi": soyad,
                       "sehir": sehir, "tel": tel, "adi": ad, "mail": mail}


            std = Student()
            std.addStudent(ogrenci)   
            print("#"*5,"Öğrenci Eklendi", "#"*5) #Bilgileri girilen öğrencinin kayıt edilmesini sağlar
            showMenu()  #İşlemler bittikten sonra giriş menüsüne geri dönülmesini sağlar

elif secim == 2:
            ad = input("Aradığınız öğrencinin adı: ")
            soyad = input("Aradığınız öğrencinin soyadı: ")

            std = Student()
            std.viewStudent(ad,soyad) #adı ve soyadı girilen öğrencinin tüm bilgilerinin gösterilmesini sağlar
            showMenu()            
elif secim == 3:
            ad = input("Silinecek öğrencinin adı: ")
            soyad = input("Silinecek öğrencinin soyadı: ")

            std = Student()
            std.deleteStudent(ad,soyad)
            print("#"*5,"Öğrenci silindi", "#"*5)
            showMenu()
        elif secim == 4:
            print("\nGüncellenecek öğrencinin bilgilerini girin.")

            ad = input("Adı: ")
            soyad = input("Soyad: ")

            sehir = input("\nYaşadığın şehir: ")
            okul = input("Okulun: ")
            dogum = int(input("Doğum yılı: "))
            mail = input("Mail adresi: ")
            tel = input("Telefon numarası: ")
            egitim = []
