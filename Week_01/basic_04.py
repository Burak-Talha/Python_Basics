print("MERHABA.\nNasılsın?") #\n yeni satıra geçmeye yarar
print("Benim adım:\t\t\t\tBanu") #\t bir tab boşluk bırakarak yazmayı sağlar

#birden fazla değer yazdırmek istiyorsak ',' kullanıyoruz
print("Zeynep", 45 , 'Melisa' , 9.78)

# type()fonksiyonu
j = 78
print(type(j))

#FORMAT
# Formatlama

"""Programlama yaparken bazı yerlerde bir stringin içinde daha önceden tanımlı string,float, int vs. değerleri
yerleştirmek isteyebiliriz. Böyle durumlar için Pythonda format() fonksiyonu bulunmaktadır."""

print("Senin adın {}, senin yaşın {}".format("Erva", 23))

l =  8
m = 24
print("a ve b'nin toplamı {} + {} = {} ' dır.".format(m ,l, l+m ))

variable = "Benim {}".format("Burak")
print(variable)

name = input("ADINIZI GİRİNİZ:")
age = input("Yaşınızı giriniz")
print("Benim adım : {} ,yaşım: {} ".format(name,age))