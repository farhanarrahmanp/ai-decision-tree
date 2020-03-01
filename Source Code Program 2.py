#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:51:45 2019

@author: Farhan
"""

import pandas as pd #Membaca file csv
import math #Perhitungan flooring dan ceiling
import random #Generate angka random
#from sklearn.preprocessing import LabelEncoder #Buat data latih opsi 2
import csv #Buat menulis output file

datalatih = pd.read_csv("data_latih.csv", sep=',',header =None) 
#Membaca file data training
datalatih.columns = ["Suhu","Waktu","Kondisi Langit", "Kelembapan", "Terbang/Tidak"] 
#Penamaan tiap kolom
#print(datalatih)
#Misc. (untuk membentuk data latih opsi 2, namun tidak dipakai untuk kali ini)
#ohe_mda0 = pd.read_csv("data_latih.csv",sep=',',header=None)
#ohe_mda0.columns = ["Suhu","Waktu","Kondisi Langit", "Kelembapan", "Terbang/Tidak"]
#le = LabelEncoder() 
#ohe_mda0['Suhu']= le.fit_transform(ohe_mda0['Suhu']) 
#ohe_mda0['Waktu']= le.fit_transform(ohe_mda0['Waktu']) 
#ohe_mda0['Suhu']= le.fit_transform(ohe_mda0['Suhu']) 
#ohe_mda0['Kondisi Langit']= le.fit_transform(ohe_mda0['Kondisi Langit']) 
#ohe_mda0['Kelembapan']= le.fit_transform(ohe_mda0['Kelembapan']) 
#ohe_mda0['Terbang/Tidak']= le.fit_transform(ohe_mda0['Terbang/Tidak'])
###############################################################################
###############################################################################
"""
Membuat array untuk tiap value dalam kolom 
(Suhu, Waktu, Kondisi Langit, Kelembapan, Terbang/Tidak)
"""
colSuhu = datalatih['Suhu'].values.tolist()
colWaktu = datalatih['Waktu'].values.tolist()
colKondLgt = datalatih['Kondisi Langit'].values.tolist()
colLembap = datalatih['Kelembapan'].values.tolist()
colTerbang = datalatih['Terbang/Tidak'].values.tolist()

for i in range(len(colSuhu)):
    if(colSuhu[i] == 'Rendah'):
        firstVal = colSuhu[i]
    elif(colSuhu[i] == 'Normal'):
        secondVal = colSuhu[i]
    elif(colSuhu[i] == 'Tinggi'):
        thirdVal = colSuhu[i]

arrSuhu = []
arrSuhu.append(firstVal)
arrSuhu.append(secondVal)
arrSuhu.append(thirdVal)
        
for i in range(len(colWaktu)):
    if(colWaktu[i] == 'Pagi'):
        firstVal = colWaktu[i]
    elif(colWaktu[i] == 'Siang'):
        secondVal = colWaktu[i]
    elif(colWaktu[i] == 'Sore'):
        thirdVal = colWaktu[i]
    elif(colWaktu[i] == 'Malam'):
        fourthVal = colWaktu[i]
        
arrWaktu = []
arrWaktu.append(firstVal)
arrWaktu.append(secondVal)
arrWaktu.append(thirdVal)
arrWaktu.append(fourthVal)
        
for i in range(len(colKondLgt)):
    if(colKondLgt[i] == 'Cerah'):
        firstVal = colKondLgt[i]
    elif(colKondLgt[i] == 'Berawan'):
        secondVal = colKondLgt[i]
    elif(colKondLgt[i] == 'Rintik'):
        thirdVal = colKondLgt[i]
    elif(colKondLgt[i] == 'Hujan'):
        fourthVal = colKondLgt[i]
        
arrKondLgt = []
arrKondLgt.append(firstVal)
arrKondLgt.append(secondVal)
arrKondLgt.append(thirdVal)
arrKondLgt.append(fourthVal)

arrLembap = arrSuhu        
#for i in range(len(colLembap)):
#    if(colLembap[i] == 'Rendah'):
#        firstVal = colLembap[i]
#    elif(colLembap[i] == 'Normal'):
#        secondVal = colLembap[i]
#    elif(colLembap[i] == 'Tinggi'):
#        thirdVal = colLembap[i]
#
#arrLembap = []
#arrLembap.append(firstVal)
#arrLembap.append(secondVal)
#arrLembap.append(thirdVal)     
arrTerbang = []
for i in range(len(colTerbang)):
    if(colTerbang[i] == 'Ya'):
        arrTerbang.append(colTerbang[i])
        break
#print(arrSuhu)
#print(arrWaktu)
#print(arrKondLgt)
#print(arrLembap)
#print(arrTerbang)
###############################################################################
###############################################################################
arrDatalatih = datalatih.values #Memasukkan ke dalam array
#print(arrDatalatih)
###############################################################################
###############################################################################
"""
Meng-generate populasi yang dalam 1 populasi berisi beberapa kromosom yang
gene-nya sebanyak 15-bit
"""
def buat_populasi(byk_individu):
    populasi = []
    for i in range(byk_individu):
        kromosom = []
        for j in range(pjg_bit):
            rand = round(random.uniform(0,1))
            kromosom.append(rand)
        populasi.append(kromosom)
    return populasi
#populasi = buat_populasi(byk_individu)
###############################################################################
###############################################################################

###############################################################################
###############################################################################
"""
Memisah kromosom per banyak bit dari setiap aturan
Suhu = 3-bit, Waktu = 4-bit, Kondisi Langit = 4-bit, Kelembapan = 4-bit,
Terbang/Tidak = 1-bit
Aturan: [1 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 1 ]
Kolom:  |Suhu     ||Waktu         ||Langit        ||Lembap    ||Terbang|
"""
def pisah_kromosom(pjg_bit, kromosom):
  return [kromosom[i:i + pjg_bit] for i in range(0, len(kromosom), pjg_bit)]
#print(pisah_kromosom(15,[1,0,1,1,0,0,1,1,1,1,0,0,0,1,1))
###############################################################################
###############################################################################

###############################################################################
###############################################################################
"""
Menemukan kebenaran dari tiap aturan.
Misal pada aturan [1,1,0] apakah benar jawabannya Normal pada array Suhu?
Jawabannya akan menghasilkan nilai True
"""
def cekAturan(arrName, atur, Val):
    i = arrName.index(Val)
#    print(i)
    if(atur[i]==1):
        return True
    else: return False
#print(cekAturan(arrSuhu, [1,1,0],'Normal'))
###############################################################################
###############################################################################

###############################################################################
###############################################################################
"""
Memprediksi aturan dari populasi yang kromosomnya dilakukan cek aturan
dengan nilai dari array tiap kolom data latih apakah Terbang atau Tidak
"""
def prediksi(individu, arrDatalatih):
    aturan = pisah_kromosom(pjg_bit, individu)
    for byk in aturan:
        atSuhu = byk[0:3]
        atWaktu = byk[3:7]
        atKondLgt = byk[7:11]
        atLembap = byk[11:14]
        atTerbang = byk[14]
        if cekAturan(arrSuhu, atSuhu, arrDatalatih[0]) and cekAturan \
        (arrWaktu, atWaktu, arrDatalatih[1]) and cekAturan \
        (arrKondLgt, atKondLgt, arrDatalatih[2]) and \
        cekAturan(arrLembap, atLembap, arrDatalatih[3]):
            if atTerbang == 1:
                return 'Ya'
            else:
                return 'Tidak'
    return '-'
###############################################################################
###############################################################################
#individu = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#print(prediksi(individu, ['Rendah', 'Siang', 'Cerah', 'Rendah']))
#individu = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
#print(prediksi(15,individu, ['Rendah', 'Siang', 'Cerah', 'Rendah']))
###############################################################################
###############################################################################
"""
Menghitung nilai fitness dari kromosom sebuah populasi
Nilai fitness = benar / banyak data dari file data latih
"""
def nilai_fitness(populasi):
    hasil1 = []
    for i in range(byk_individu):
        individu = populasi[i]
        benar = 0
        for j in arrDatalatih:
            hasil2 = prediksi(individu, j)
            if hasil2 == j[4]:
                benar +=1
        hasil1.append({'i':i,'individu' : individu,'score_fitness' : benar / len(arrDatalatih)})
    return hasil1
#pop_fit = nilai_fitness(populasi) # dibuat variabel pop_fit (yang sebelumnya juga) karena variabel akan dipake selanjutnya
#print(pop_fit)
###############################################################################
###############################################################################

###############################################################################
###############################################################################
"""
Melakukan pemilihan orang tua berdasarkan nilai fitness maksimum
"""
def ortu(populasi, score_fitness):
  urutkan_fitness = sorted(score_fitness, key=lambda x: x['score_fitness'], reverse=True) 
  ortu1 = populasi[urutkan_fitness[0]['i']]
  ortu2 = populasi[urutkan_fitness[1]['i']]
  return ortu1, ortu2
###############################################################################
###############################################################################
#ortu = ortu(populasi,pop_fit)
#print(ortu) # bakal di crossover
###############################################################################
###############################################################################
"""
Melakukan pindah silang
"""
def crossover(ortu, p):
  o1, o2 = ortu
  prob = random.uniform(0, 1)
  if prob > p:
    return [o1[:], o2[:]]
  if len(o1) > len(o2):
    o1, o2 = o2, o1
  
  o1_s = [
          random.randint(0, math.floor(len(o1)/2)), 
          random.randint(math.floor(len(o1)/2), len(o1))
        ]
  arrO2 = []
  o1_length = o1_s[1] - o1_s[0]
  o1_gap = int(math.fmod(o1_length,pjg_bit))

  #1
  o2_1 = [o1_s[0], o1_s[0] + o1_length]
  if o2_1 not in arrO2:
    arrO2.append(o2_1)
  #2
  o2_2 = [o1_s[0], o1_s[0] + o1_gap]
  if o2_2 not in arrO2:
    arrO2.append(o2_2)
  #3
  o2_3 = [o1_s[1] - o1_length, o1_s[1]]
  if o2_3 not in arrO2:
    arrO2.append(o2_3)
  #4  
  o2_4 = [o1_s[1] - o1_gap, o1_s[1]]
  if o2_4 not in arrO2:
    arrO2.append(o2_4)

  index_terpilih = round(random.uniform(0, len(arrO2)-1))
  o2_s = arrO2[index_terpilih]
  
  #Anak 1
  kiri = o1[(math.floor(o2_s[0] / pjg_bit) * pjg_bit):o2_s[0]]
  tengah = o2[o2_s[0]:o2_s[1]]
  kanan = o1[o2_s[1]:((math.ceil(o2_s[1] / pjg_bit)) * pjg_bit)]
  anak1 = kiri + tengah + kanan
  #Anak 2
  kiri = o2[0:o2_s[0]]
  tengah = o1[o1_s[0]:o1_s[1]]
  kanan = o2[o2_s[1]:]

  anak2 = kiri + tengah + kanan

  return [anak1, anak2]
#anak = crossover(ortu, 0.8)
#print(ortu)

def mutasi(anak, p):
  for i in range(len(anak[0])):
    prob = random.uniform(0, 1)
    if prob < p:
      if anak[0][i] == 0:
        anak[0][i] = 1
      else:
        anak[0][i] = 0

  for i in range(len(anak[1])):
    prob = random.uniform(0, 1)
    if prob < p:
      if anak[1][i] == 0:
        anak[1][i] = 1
      else:
        anak[1][i] = 0
    
  return anak
#anak = mutasi(anak, 0.2)
#print(anak)
###############################################################################
###############################################################################
"""
Menghasilkan populasi baru berdasarkan nilai fitness
"""
def ganti_generasi(populasi, score_fitness, anak):
  """
  Akan menghasilkan populasi baru dari parameter populasi, berdasarkan fit_res
  """
  urutkan_fitness = sorted(score_fitness, key=lambda x: x['score_fitness'], reverse=True)
  i1 = urutkan_fitness[len(urutkan_fitness)-1]['i']
  i2 = urutkan_fitness[len(urutkan_fitness)-2]['i']
  populasi[i1] = anak[0]
  populasi[i2] = anak[1]
  return populasi
#survive = ganti_generasi(populasi, pop_fit, anak)
#print(survive)
###############################################################################
###############################################################################


###############################################################################
###############################################################################
"""
Main program
"""
pjg_bit = 15
byk_individu = 8
byk_generasi = 4000
populasi = buat_populasi(byk_individu) #Buat populasi
print('Populasi : ')
print(populasi)
print()
kelipatan = 200
for i in range(byk_generasi):
  n_fitness = nilai_fitness(populasi) #Hitung fitness dari populasi
  orangtua = ortu(populasi, n_fitness) #Buat parent
  anak = crossover(orangtua, 0.9) #Lakukan crossover pada parent untuk membuat child, Pc = 0.9
  anak = mutasi(anak, 0.1) #Mutasi pada child, Pm = 0.1
  populasi = ganti_generasi(populasi, n_fitness, anak) #Pergantian generasi

  if int(math.fmod(i,kelipatan)) == 0:
    fitness = nilai_fitness(populasi)
    urutkan_fitness = sorted(fitness, key=lambda x: x['score_fitness'], reverse=True)
    print("Akurasi untuk training set Generasi",i+kelipatan ,"=",urutkan_fitness[0] \
    ['score_fitness']*100,'%')

print()
fitness = nilai_fitness(populasi)
urutkan_fitness = sorted(fitness, key=lambda x: x['score_fitness'], reverse=True)
optimal = urutkan_fitness[0]
kromosom_optimal = populasi[optimal['i']]

datauji = pd.read_csv("data_uji.csv", sep=",",header=None)
datauji.columns = ["Suhu","Waktu","Kondisi Langit", "Kelembapan", "Terbang/Tidak"]
datatest = datauji.values

print('Output prediksi dari file Data Uji : ')
i=0
with open('OUTPUTdata_uji.csv', 'w') as f:
    employee_writer1 = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for d in datatest:
        hasil = prediksi(kromosom_optimal, d)
        print(i+1,datatest[i],hasil)
        i+=1
        employee_writer1.writerow([hasil])
print()
print('OUTPUT file is created')
###############################################################################
###############################################################################
      
