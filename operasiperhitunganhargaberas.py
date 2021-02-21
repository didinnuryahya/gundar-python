import numpy as n #Memasukkan numpy dan memberikan nama sebagai n
from scipy import stats #Memasukkan stats dari scipy

class operasiperhitunganhargaberas(): #membuat class yang dinamakan hanum goyang
    def __init__ (self, dsu,dku): #metode class untuk membuat objek dengan parameter pertama self
        self.dsu = dsu #properti pertama dengan sintaks self
        self.dku = dku #properti kedua dengan sintaks self
    def mean_dsu(self): #metode class untuk mengisi atribut mean
        meandesu= np.mean(self.dsu) 
        return meandesu #mengembalikan jumlah data dibagi banyaknya data
    def mean_dku(self): #metode class untuk mengisi atribut mean
        meandeku= np.mean(self.dku) 
        return meandeku #mengembalikan jumlah data dibagi banyaknya data
    def median(self): #metode class untuk mengisi atribut median
        self.dhb.sort() #pengurutan dengan built-in function sort
        if len(self.dhb) % 2 == 0: #jika banyaknya angka berjumlah genap
            hasil = self.dhb[len(self.dhb)//2] + self.dhb[(len(self.dhb)//2-1)]
            return hasil / 2
        else: #jika banyaknya angka berjumlah ganjil
            return self.dhb[(len(self.dhb)//2)+1]
    def modus(self): #metode class untuk mengisi atribut modus
        a = self.dhb #set agar hanya memiliki 1nilai tak duplikat
        moduss=[] #list menyimpan modus
        total = 0 #variabel untuk menyimpan banyak data tertinggi
        for i in a: #mengulang sejumlah banyak nilai anggota 
            jumlah = self.dhb.count(i) #menghitung jumlah nilai dari list
            if(jumlah>1 and jumlah>total): #jika lebih dari 1 dan lebih dari total
                moduss.clear() #menghapus isi list modus
                total = jumlah 
                moduss.append(i) #menambah nilai i ke dalam list moduss
        return moduss #return nilai modus
    def deviasi(self): #metode class untuk mengisi atribut deviasi
        return n.std(self.dhb)
    def k1(self): #metode class untuk mengisi atribut kuartil 1
        return n.quantile(self.dhb,0.25)
    def k2(self): #metode class untuk mengisi atribut kuartil 2
        return n.quantile(self.dhb,0.5)
    def k3(self): #metode class untuk mengisi atribut kuartil 3
        return n.quantile(self.dhb,0.75)
    def kovarian(self): #metode class untuk mengisi atribut kovarian
        return n.array([self.dhb,self.dhk])
    def tampil(self): #metode class untuk mengisi atribut tampil hasil semuanya
        print("===MENGHITUNG HARGA BERAS===")
        print("Data Harga Beras         :", self.dhb)
        print("Data Kunjungan Harian    :",self.dhk)
        print("Mean Harga Beras         : Rp",self.mean())
        print("Median Harga Beras       : Rp",self.median())
        print("Modus Harga Beras        : Rp",self.modus())
        print("Standar Deviansi         :",round(self.deviasi(),2))
        print("Kuartil 1                : Rp",self.k1())
        print("Kuartil 2                : Rp",self.k2())
        print("Kuartil 3                : Rp",self.k3())
        print("Kovarian                 :\n",n.cov(self.kovarian()))
        print("Kovarian                 :\n",n.corrcoef(self.kovarian()))
dsu = [16,22,26,15,8,14,15,17,19,18,18] #list data harga beras
dku = [32,52,72,44,70,44,48,57,62,60] #list harian kunjungan
q = hanumgoyang(dsu,dku) #variabel q untuk memanggil class ojan dan memasukkan dhb dhk kedalam class
q.tampil() #memanggil metode class tampil untuk mengeluarkan outputu