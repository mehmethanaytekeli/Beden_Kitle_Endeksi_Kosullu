print("Boy Kilo Endeksi Programı")

boy = float(input("Boyunuz kaç metre:"))
kilo = float(input("Kilonuz:"))

sayı = kilo/boy**2
endeks=round(sayı,2)

print("Endeksiniz:{}".format(endeks))

if 18.5 > endeks :
    print("Zayıfsınız")

elif 18.5 < endeks < 25 :
    print("Normalsiniz")

elif 25 < endeks <30 :
    print("Fazla Kilolusunuz")

elif endeks > 30 :
    print("Obezsiniz")

