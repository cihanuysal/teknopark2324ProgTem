# def kontrol(sayi):
#     if sayi % 2==0 : return "ÇİFT"
#     elif sayi % 2==1 : return "TEK"
#     print("Ne sen sor ne ben söyleyim")

# print(kontrol(0.25))

#Birden Fazla Parametre
#Zorunlu ve isteğe bağlı parametre
#arbitray parametre
#keyword paramater

#Örnek Soru 1:Argument olarak verilen değerlerden
#enküçük sayı ile en büyük sayının  toplamını geriye döndüren 
#islem isimli bir fonksiyon tanımlayın
def islem(*sayilar):
    eb=sayilar[0]
    ek=sayilar[0]
    for x in sayilar:
        if eb<x: eb=x
        if ek>x: ek=x
    return eb+ek

print(islem(6,5,8,15,3,12))


#Örnek Soru 2: topla fonksiyonu çoktan seçmeli

# def etiketYaz(sinif,no,ad,ders="İNGİLİZCE"):
#     print(f"SINIF       : {sinif}")
#     print(f"OKUL NO     : {no}")
#     print(f"İSİM        : {ad}")
#     print(f"DERS ADI    : {ders}")
    


# etiketYaz("9-A", 89,"ZEYNEP AFRA")
# etiketYaz(ad="Saltuk",no=60,sinif="9-A")

# def topla(*sayilar):
#     toplam=0
#     for x in sayilar:
#         toplam+=x
#     return toplam


# print(topla(5,6)) #11
# print(topla(5,6,8,10,15))#44
# print(topla(5,6,8,9,15,6565))#6608

# def etiketYaz2(**degerler):
#     for k in degerler:
#         print(f"{k}       : {degerler[k]}")
#     print("--------------------------------\n")

# etiketYaz2(dolapNo=25,ad="Kitaplık")
# etiketYaz2(adres="Tuzla",aciklama="Kırılacak Eşya")
# etiketYaz2(no=25,isim="Cansu",ders="Hayat Bilgisi")

