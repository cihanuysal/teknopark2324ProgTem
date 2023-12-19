# #Örnek : Kullanıcıdan önce kaç veri girişi yapılacağı öğreniliyor. 
# #Sonra kullanıcı o kadar kelimeyi bilgisayara
# #giriyor. 
# #Kelimlerden harf sayısı tek olanları büyük harfle ekrana yazan programı yapınız.


# #1. kısım
adet=int(input("Kaç Kelime Gireceksin ? : "))

data=list()
for e in range(1,adet+1):
    data.append(input(f"{adet}. Kelime : "))
 
for k in data:
   if len(k) % 2==1: print(str(k).upper())
