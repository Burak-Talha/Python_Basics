## Tamsayıyı Ondalıklı Sayıya Çevirme
"""Bir tamsayı değeri(integer) ondalıklı sayıya(float) çevirmek için float() fonksiyonunu
kullanabiliriz.Örneklere bakalım."""
print("------------------------------------------------------")
print(type(-8))
print(float(-8))

a = 7
print(float(a))

b = 64
print(float(b))


print("Ondalıklı Sayıyı Tamsayıya Çevirme")

"""Bir ondalıklı sayıyı tamsayıya çevirmek için int() fonksiyonunu kullanabiliriz.Sonuç, ondalıklı sayının tam kısmı
olarak karşımıza çıkacak.Örneklere bakalım."""

print(int(9.54))
print(int(9.99))

c = 6.44
print(int(c))

d = 6
e = 2
print(type(d/e))
print(type((int(d/e))))

### Sayıları Stringlere Çevirme
""" Bir sayıyı string'e çevirmek için str() fonksiyonunu kullanabiliriz.Sayıyı oluşturan tüm rakamlar veya noktalar
birer karaktere dönüşecek."""

f = 30000.0
b = str(f)
print(type(b))
print(len(b))


### Stringleri Tamsayıya Çevirme
"""Bir string'i bir tamsayıya çevirmek istediğimiz zaman int()  fonksiyonunu kullanabiliriz. Ancak biraz dikkatli olmamızda
fayda var. Dönüştürme işlemini yaparken stringin herbir karakterinin bir rakam olduğundan emin olmalıyız. Örneklere 
bakalım."""

g = "7798870030"
h = int(g)
print(h)

### Stringleri Ondalıklı Sayıya Çevirme
"""Bir string'i bir ondalıklı sayıya çevirmek istediğimiz zaman float()  fonksiyonunu kullanabiliriz. Ancak biraz 
dikkatli olmamızda fayda var. Dönüştürme işlemini yaparken stringin ondalıklı sayı formatına uygun olduğundan emin 
olmalıyız. Örneklere bakalım."""

ı =  "734.92908"
print(type(ı))
i = float(ı)
print(i)