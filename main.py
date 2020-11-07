# DDP LAB-4
# Nama: Raihan Daffa Aziz
# NIM:  0110120020

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini

nama = input("Masukkan nama : ")
total = len(nama)
awal = 0
while awal < total:
    awal = awal + 1
    print(nama[0:awal])

# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini

while True:
  #perulangan terpenuhi
    code = input("Masukkan sebuah teks : ")
    #input sebuah teks
    jumlah = len(code)
    #hitung jumlah teks yang ada di code
    if (jumlah > 8 
    #jika jumlah teks di atas 8 
        and (code.endswith("YYY") 
          or code.endswith("yyy"))
          #dan jika teks diakhiri dengan huruf YYY / yyy
        and (code.startswith('NF') 
          or code.startswith('nf')
          or code.startswith('Nf') 
          or code.startswith('nF'))
          #dan jika teks di mulai dengan NF/nf/Nf/nF
        and not (code.isalpha())
        #dan jika teks tidak berkarakter alphabet semua
        ):
        

          print("Code Teks valid. ")
          break
          #cetak code teks valid dan perogram / perulangan berhenti
    else:
        print("Code Teks tidak valid. ")
        #dan jika salah satu kondisi tidak terpenuhi cetak code teks tidak valid dan perogram akan terus mengulang sampai kondisi terpenuhi
