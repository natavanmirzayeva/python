sayi1 = input("birinci sayiyi giriniz: ")
sayi2 = input("ikinci sayiyi giriniz: ")
sayi3 = input("ucuncu sayiyi giriniz: ")
enkucuksayi = sayi1
if sayi2 < enkucuksayi:
    enkucuksayi = sayi2
if sayi3 < enkucuksayi:
    enkucuksayi = sayi3
print enkucuksayi
else:
    print "uc sayi birbirine esittir"
