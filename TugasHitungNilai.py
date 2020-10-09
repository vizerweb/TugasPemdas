# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time;

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('')
print("Program Hitung Mata Kuliah")
print("================================================")
MataKuliah = input("Masukkan Nama Mata Kuliah : ")
maxPertemuan = input("Max Pertemuan : ")
jumlahHadir = input("Masukkan Jumlah Hadir : ")

totalAbsen = int(jumlahHadir) * 100 / int(maxPertemuan)
print("Nilai Absen Yang DiDapatkan Dari Perhitungan Di Atas : ", totalAbsen)

diberiknDosenTugas = input("Masukkan Nilai Tugas Yang Di Berikan Oleh Dosen : ")
diberiknDosenProject = input("Masukkan Nilai Project Yang Di Berikan Oleh Dosen : ")
print("================================================")

totala = totalAbsen*20/100
totalb = int(diberiknDosenTugas)*25/100
totalc = int(diberiknDosenProject)*55/100
print("Konversi Nilai Berdasarkan Persentase Nilai Sesuai Ketentuan..")
print("Nilai Absen (20%) anda Adalah : ",totala)
print("Nilai Absen (25%) anda Adalah : ",totalb)
print("Nilai Absen (55%) anda Adalah : ",totalc)
print("=============== Hasil Akhir ===================")
print("Mata Kuliah : ",MataKuliah)

totalfinal = totalAbsen*20/100+int(diberiknDosenTugas)*25/100+int(diberiknDosenProject)*55/100
print("Anda Mendapatkan Total Nilai : ",totalfinal)

if totalfinal >= 80:
    print("Selamat Anda Mendapatkan Nilai (A)\n"+"Dinyatakan (Lulus)")
elif totalfinal >= 74:
    print("Selamat Anda Mendapatkan Nilai (B)\n"+"Dinyatakan (Lulus)")
elif totalfinal >= 64:
    print("Selamat Anda Mendapatkan Nilai (C)\n"+"Dinyatakan (Lulus)")
elif totalfinal >=40:
    print("Selamat Anda Mendapatkan Nilai (D)\n"+"Dinyatakan (Tidak Lulus)")
elif totalfinal <40:
    print("Selamat Anda Mendapatkan Nilai (E)\n"+"Dinyatakan (Tidak Lulus)")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
