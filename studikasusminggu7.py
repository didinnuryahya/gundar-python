def perhitunganpermeter(kertasputih, kertasbewarna):
  biayakertasputih = kertasputih * 100
  biayakertaspbewarna = kertasbewarna * 1000
  biayatotal = biayakertasputih + biayakertaspbewarna
  print("Biaya yang harus dibayar adalah", biayatotal)
def perhitunganperkm(kertasputih, kertasbewarna):
  biayakertasputih = kertasputih * 100
  biayakertaspbewarna = kertasbewarna * 1000
  biayasementara = biayakertasputih + biayakertaspbewarna
  biayadiskon = biayasementara * 0.2
  biayatotal = biayasementara - biayadiskon
  print ("Biaya yang harus dibayar adalah", biayatotal)

print("Selamat datang di applikasi perhitungan jarak ojek ")
formatjarak = input("Pilih format jarak  km/meter    ")
kertasputih = int(input("Masukan jumlah print hitam putih   "))
kertasbewarna = int(input("Masukan jumlah print bewarna     "))


if formatjarak == "km":
    perhitunganbiasa(kertasputih, kertasbewarna)
elif mahasiswa == "ya":
    perhitunganmahasiswa(kertasputih, kertasbewarna)

 
