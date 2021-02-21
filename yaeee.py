import numpy as npy 
import statistics as sts
class suhu():
    def __init__(self,datasuhu,datalembab):
        self.datasuhu = datasuhu
        self.datalembab = datalembab
    def mean(self,data):
        return npy.mean(data)
    def median(self,data):
        return npy.median(data)
    def modus(self,data):
        return sts.multimode(data)
    def deviasi(self,data):
        return round(npy.std(data),2)
    def k1 (self,data):
        return npy.quantile(data,0.25)
    def k2 (self,data):
        return npy.quantile(data,0.5)
    def k3(self,data):
        return npy.quantile(data,0.75)
    def kovarian(self,dataA,dataB):
        data = npy.array([dataA,dataB])
        return npy.cov(data)
    def korelasi(self, dataA,dataB):
        data = npy.array([dataA,dataB])
        return npy.corrcoef(data)
    def cetak (self):
        print("====Menghitung suhu udara====")
        print("Data suhu udara 10 hari terakhir       :",self.datasuhu)
        print("Data kelembaban udara 10 hari terakhir :",self.datalembab)
        print("Mean                                   :",self.mean(self.datasuhu))
        print("Median                                 :",self.median(self.datasuhu))
        print("modus                                  :",self.modus(self.datasuhu))
        print("Standar Deviasi suhu udara             :",self.deviasi(self.datasuhu))
        print("Kuartil 1                              :",self.k1(self.datasuhu))
        print("Kuartil 2                              :",self.k2(self.datasuhu))
        print("Kuartil 3                              :",self.k3(self.datasuhu))
        print("====Menghitung kelembaban====")
        print("Mean                                   :",self.mean(self.datalembab))
        print("Median                                 :",self.median(self.datalembab))
        print("modus                                  :",self.modus(self.datalembab))
        print("Standar Deviasi suhu udara             :",self.deviasi(self.datalembab))
        print("Kuartil 1                              :",self.k1(self.datalembab))
        print("Kuartil 2                              :",self.k2(self.datalembab))
        print("Kuartil 3                              :",self.k3(self.datalembab))
        print("====Kovarian dan Korelasi====")
        print("Kovarian suhu undara dengan kelembaban : \n",self.kovarian(self.datasuhu,self.datalembab))
        print("Korelasi suhu udara dengan Kelembaban  : \n",self.korelasi(self.datasuhu,self.datalembab))
datasuhu = [33,32,32,32,31,31,32,32,32,32]
datalembab = [60,80,80,80,90,80,80,80,80,80]
a = suhu(datasuhu,datalembab)
a.cetak()