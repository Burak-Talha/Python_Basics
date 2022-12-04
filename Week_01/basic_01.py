""" Matematikte gördüğümüz tüm tam sayılar pythonda değişken olarak tanımlanır. Paythonda tam sayılara ingilizce tamsayı
anlamına gelen ınteger denir Örneğin : 8 , -65 , 19  , 4459 gibi sayılar integer sayılardır

  Matematikte gördüğmüz sayılardan bir diğeride ondlıklı sayılardır. Ondalıklı sayılarda aynı integer sayılar gibi
  paythonda ki veri tiplerindendir. Ondalıklı sayılara ingilizce float denmektedir.
Örnek olarak : 7.45 , 24.80 ,339.256 float sayı değerleridir."""
# Aritmetik Operatörler

x = 78
y = 6.8
print(type(x))
print(type(y))

""" Şimdi de pythonda basit işlemlere geçelim.
 
 TOPLAMA(+)"""
a = 7
b = 9
print(a+b)

#ÇIKARMA(-)
e = 8.6
d = 5.4
print(e - d)

#ÇARPMA(*)
g = 11
h = 10
ı = g * h
print(ı)

#BÖLME(/)
i = 35
j = 8
print(i / j)

#KALANSIZ BÖLME (//)
k = 45
l = 7
m = k // l
print(type(m))
print(m)

#ÜS ALMA (**)
n = 8
o = 2
# 2 üssü 8
type = o ** n
print(ö)

"""
1. Değişken isimleri bir sayı ile başlayamaz.
2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
3. : '",<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece _ sembolü kullanılabilir)
4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while , not vs.) """