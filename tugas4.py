data=[]
while(True):
    nama=input("Masukan nama : ")
    nim=input("Masukan nim : ")
    NilaiTugas=int(input("Masukan Nilai Tugas : "))
    NilaiUTS=int(input("Masukan Nilai UTS : "))
    NilaiUAS=int(input("Masukan Nilai UAS : "))
    Akhir=int((30 * Tugas / 100) + (35 * UTS / 100) + (35 * UAS / 100)
    data.append([nama, nim, NilaiTugas, NilaiUTS, NilaiUAS, Akhir])
    ulangi=input("Tambah data (y/t)? ")
    if ulangi.lower() == "t":
        break;

print("\nDaftar Nama\n")
print("=============================================================")
print("|   NAMA   |   NIM   |  NILAI TUGAS | NILAI UTS | NILAI UAS |   AKHIR   |")
print("=============================================================")
for x in data:
    print("| {0:8s} | {1:7s} | {2:12s} | {3:9s} | {4:9s} | {5:9s}|" .format(x[0], x[1], x[2], x[3], x[4], X[5]))
print("=============================================================")