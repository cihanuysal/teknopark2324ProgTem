#Soru : Kendisine verilen bir miktar sayıdan 
#en büyük olan ile en küçük olanın toplamını 
#döndüren bir fonksiyon yapınız.
def islem(*sayilar):
	eb=sayilar[0]
	ek=sayilar[0]
	for s in sayilar:
		if eb<s: eb=s
		if ek>s: ek=s 
	return eb+ek

x=islem(15,25,7,3,16)
y=islem(15,3,16)
print (x,y)

#ÇIKTI 28 19


