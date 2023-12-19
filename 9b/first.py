#Örnek : Kullanıcıdan önce kaç veri girişi yapılacağı öğreniliyor. Sonra kullanıcı o kadar kelimeyi bilgisayara
#giriyor. Kelimlerden harf sayısı tek olanları büyük harfle ekrana yazan programı yapınız.

#1 kısım

adet=int(input("Kaç Tane Veri Gireceksin ?"))

#2 KISIM
kelimeler=list()
for i in range(1,adet+1):
    kelimeler.append(input(f"{i} .KELİME : "))

#3 KISIM
for k in kelimeler:
   if  (len(k) % 2 ==1) :
       print(k)
       