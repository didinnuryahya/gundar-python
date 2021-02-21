def perhitunganpermeter(jarak):
  jarakkm = jarak / 1000
  if jarakkm <= 5:
      biayajarak = jarakkm * 1000
  elif jarakkm > 5 and jarakkm <= 10:
      biayajarak = jarakkm * 900
  elif jarakkm > 10:
      biayajarak = jarakkm * 800
  print("Biaya yang harus dibayar adalah", int(biayajarak))
def perhitunganperkm(jarak):
  if jarak <= 5:
      biayajarak = jarak * 1000
  elif jarak > 5 and jarak <= 10:
      biayajarak = jarak * 900
  elif jarak > 10:
      biayajarak = jarak * 800
  print("Biaya yang harus dibayar adalah", int(biayajarak))

print("Selamat datang di applikasi inventori barang")
print("Category")
print("1. Minuman")
print("2. Makanan")
print("3. Snack")
formatcategory = input("Pilih Category (Eg 1 / Minuman / minuman) ")
if formatcategory == "1" and formatcategory == "Minuman" and formatcategory == "minuman":
    dataminuman = ['coca']
    jarak = float(input("Masukan jarak ojek yang diinginkan   "))
    perhitunganperkm(jarak)
elif formatcategory == "2" and formatcategory == "Makanan" and formatcategory == "makanan":
    jarak = int(input("Masukan jarak ojek yang diinginkan  "))
    perhitunganpermeter(jarak)
elif formatcategory == "3" and formatcategory == "Snack" and formatcategory == "snack":
    jarak = int(input("Masukan jarak ojek yang diinginkan  "))
    perhitunganpermeter(jarak)


 
