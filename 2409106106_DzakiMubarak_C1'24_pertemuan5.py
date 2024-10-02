# pertemuan 5

# nama = ["shandy",106,True,3.96]
# matkul = ["APD","APL","WEB","JARKOM",]

# print(matkul)

#nama = ["shandy",106,True,
        #["yuyun",145],3.96,
        #[123,"ALVITO",False,3.66],
        #"rehan"]
#print (nama[4])

#matkul = ["APD",
         # "APL",
         # "WEB",
         # "JARKOM",
         # "BASDAT",
         # "STRUKDAT",
         # "PIT",
         # "KALKULUS",
          #"PROBAS"]

#print(matkul)

#makanan = ["bakso","sate","soto","nasi goreng","mie ayam","ayam goreng","cumi goreng"]
#print("sebelum: ")
#print(makanan)
#makanan.append("nasi goreng")
#print ("sesudah: ")
#makanan.clear()
#print(makanan)
#del makanan[1]
#data = makanan.pop(5)
#print(makanan)
#makanan.insert(2,"nasi goreng")
#makanan[0] = ['ayam','bebek']
#print(makanan)

#minuman 6. 3(dihapus) 6 (air putih) 0(jus tomat)

#minuman = ["susu","jus mangga","jus sirsak","es teler","es teh","es buah"]
#print("sebelum: ")
#print (minuman)
#del minuman[2]
#print("sesudah: ")
#print(minuman)
#minuman[4] = "air putih"
#print(minuman)
#minuman.insert(0,"jus tomat")
#print(minuman)

# makanan = [["bakso","soto","sate","ikan","bebek"],
#            ["teh","kopi","air"]]
# #print (makanan)

# #for i in makanan :
# #     print(i, end=" ")
# for i in makanan :
#     if isinstance(i, list):
#         for j in i :
#           print(j)
#           # print(j, end=" ")
#     else:
#      print(i)

#  akun = []

#  while True:
#      print("Halo! selamat datang di aplikasi catatan")
#      print("silakan pilih 'daftar akun' jika belum buat akun, dab jika sudah miliki akun silakan 'login'")
#      print("1. Daftar akun")
#      print("2. login")
#      print("3. Exit")
#      print("------------------------")
#      opsi = input("pilih opsi")
#      print(" ")
#      if opsi == "1":
#         print("halo pengguna baru! ayo buat akun dulu")
#         username = input("username: ")
#         akuna = False
#         for akun in akuns:
#            if akun[0] == username :
#               akuna = True
#               break
#         if akuna:
#            print("Nama sudah terpakai untuk registrasi silakan coba lagi")
#         else
#            password = input