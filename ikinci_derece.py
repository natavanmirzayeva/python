a = input("x karesinin katsayisini giriniz: ")
b = input("xin katsayisini giriniz: ")
c = input("sabit terimi girin: ")
delta = b*b-4*a*c
if delta < 0:
    print "reel kok yok"
if delta == 0:
    kok = -b/2*a
    print kok
if delta > 0:
    kok1 = -b+(delta)**1.0/2
    kok2 = -b-(delta)**1.0/2
    print kok1,kok2
