cuaca = "mendung"

if cuaca == "mendung":
    print ("diam di rumah")
else:
    print ("hsri ini mendung")



Umur = int(input("masukkan umur anda:"))
if Umur > 0:
    if Umur <= 10:
        print ("Umur Anda termasuk kategori anak-anak")
    elif Umur <= 18:
        print( "Umur Anda termasuk kategori remaja")
    elif Umur <= 35:
        print("Umur Anda termasuk kategori dewasa")
    elif Umur <= 65:
        print("Umur Anda termasuk kategori paruh baya")
else:
    print("Umur Anda termasuk kategori Tua")



nim = int(input("masukkan nim: "))

if nim >= 1 and nim <= 50 :
    if nim >= 1 and nim <= 25:
        print ("kelas A'1")
    else:
        print ("kelas A'2")
elif nim >= 51 and nim <= 100:
    if nim >= 51 and nim<= 75:
        print ("kelas B'1")
    else:
        print ("kelas B'2")
elif nim >= 101 and nim <= 121:
    if nim >= 101 and nim <= 110:
        print ("kelas C'1")
    else:
        print ("kelas C'2")      
else :
    print("Anda bukan Mahasiswa informatika 24")


nim = int(input("masukkan nim: "))
hasil = "kelas A" if nim >= 1 and nim <= 50 else "kelas B" if nim >= 51 and nim <= 100 else "kelas C" if nim >= 101 and nim <= 121 else "mahasiswa siluman"
print (hasil)