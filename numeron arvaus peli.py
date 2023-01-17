from random import randint

vastaus=randint(0,100)
peli=False

print("*"*20)
print("tervetuloa pelaamaan")
print("*"*20)

kysymys=input("haluatko pelata? (kyllä/ei: ")
if kysymys=="kyllä":
    peli=True
    print("aloitetaan peli")
    print("arvaa oikea numero")
else:
    print("nähdään pian")

while peli==True:
    arvaus=int(input("syötä arvauksesi: "))
    if arvaus<vastaus:
        print("oikea vastaus suurempi")
    elif arvaus>vastaus:
        print("oikea vastaus on pienempi")
    else:
        print("aarvasit oikein")
        peli=False

