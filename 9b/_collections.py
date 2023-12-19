# #Soru 2_a: Kullacıdan ad, yas, memleket verileri alarak bir sözlük oluşturan programı yapın.
# # ad=input("Adınız :")
# # yas=input("Yaşınız :")
# # memleket=input("Memleketiniz :")
# # kisi={
# #     "ad"        :ad,
# #     "yas"       :yas,
# #     "memleket"  :memleket
# # }
# #Soru 2_b: Bu giriş işlemiü defa tekrarlanacak ve her sozluk data isminde bir listeye eklenecek
# i=0
# data=list()
# while i<3:
#     ad=input("Adınız :")
#     yas=input("Yaşınız :")
#     memleket=input("Memleketiniz :")
#     kisi={
#         "ad"        :ad,
#         "yas"       :yas,
#         "memleket"  :memleket
#     }
#     data.append(kisi)
#     i+=1
# #Soru 2_c: liste izmirli olanların adını ve yaşını ekrana listeleyen programı yapınız 

# #data[kisi,kisi,kisi]
# countIzmir=0
# for k in data:
#    if k["memleket"]=="izmir":
#        print(k["ad"],k["yas"])
#        countIzmir+=1
# if countIzmir==0 :print("İZMİRLİ YOK")




# #Soru 2_d: 


#WHILE döngüsü

#Yöntem 1
# i=1
# while i<6:
#     print("merhaba")
#     i+=1


#Yöntem 2
# veri="hayır"
# while veri!="evet":
#     veri=input("Çıkmak İstiyoru musun?")

menu="1.KİŞİ EKLE\n2.MEMLETE GÖRE ARA\n3.HEMŞERİ LİSTELE\n4.ÇIKIŞ"
secim="0"
data=list()
while secim!="4":
    print(menu)
    secim=input("SEÇİMİNİZ >>>> ")
    if secim=="1":
        print("_____ KİŞİ EKLEME İŞLEMİ _________")
        ad=input("Adınız :")
        yas=input("Yaşınız :")
        memleket=input("Memleketiniz :")
        kisi={
            "ad"        :ad,
            "yas"       :yas,
            "memleket"  :memleket
        }
        data.append(kisi)

    elif secim=="2":
        print("MEMLEKETE GÖRE KİŞİ LİSTEMELE İŞLEMİ")
        #data[kisi,kisi,kisi,....]
        aranan=input("Aradığınız Vilayeti Girin :")
        sayac=0
        for k in data:
            if k["memleket"]==aranan:
                print(k["ad"],k["yas"])
                sayac+=1
        if sayac==0:print(aranan, " ilinden hiç bir kayıt yok.")
    elif secim=="3":
        print("hemşeri listeme işlemi")
        tekraredeleniller=list()
        #data[
        # k0 bursa    
        # k1 ist
        # k2 izmir
        # k3 ist
        # k4 izmir
        # k5 trabzon
        # ]
        #tekraredenler[
        # 
        # 
        # 
        # ]
        #iller[
        # bursa
        # ist
        # izmir
        # ist
        # izmir
        # trabzon
        # ]
        iller=list()
        for k in data:
            iller.append(k["memleket"])
        i=0    
        while i<len(iller):
            j=i+1
            while j < len(iller):
                if iller[i]==iller[j]:
                    if iller[i] not in tekraredeleniller:
                        tekraredeleniller.append(iller[i])       
                j+=1
            i+=1    
        
        for il in tekraredeleniller:
            print(il, "MEMLEKETİNDEN OLAN HEMŞERİLER")
            for k in data:
                if il==k["memleket"]:
                    print(k["ad"],k["yas"])


    elif secim=="4":
        print("PROGRAMDAN ÇIKILDI")
    else:
        print("HATALI SEÇİM")


