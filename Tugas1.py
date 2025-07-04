print("Tugas System")

print("1. Tarif Parkir")
print("Mobil = 7000/jam")
print("Motor = 5000/jam")

L = int (input("Masukkan Lama Parkir Anda (jam) = "))
J = input("Masukkan Jenis Kendaraan Anda = ")

T1 = 7000 * L
T2 = 5000 * L

if J == "Mobil":
    print(T1, ("Adalah Jumlah Tarif Yang Harus Anda Bayar"))
elif J == "Motor":
    print(T2, ("Adalah Jumlah Tarif Yang Harus Anda Bayar"))
else:
    print("Maaf Kendaraan Anda Tidak Terdeteksi!")
    print("Silahkan Periksa Kembali Kendaraan Anda!")

U = int (input("Masukkan Jumlah Uang = "))

K1 = U - T1
K2 = U - T2

if U >= T1:
    print("Kembalian Anda", K1)
elif U >= T2:
    print("Kembalian Anda", K2)
else:
    print("Maaf Uang Anda Kurang!")

N = input("Masukkan Nama Petugas Parkir = ")
Ig = input("Masukkan Username Instagram Petugas = ")

if J == "Mobil":
    print(("Total tarif yang harus anda bayar"), T1, (", uang anda berikan senilai"), U, ("kembaliannya"), K1, (". Nama petugas parkir"), N, (", IGnya boleh di follow kak"), Ig)
else:
    print(("Total tarif yang harus anda bayar"), T2, (", uang anda berikan senilai"), U, ("kembaliannya"), K2, (". Nama petugas parkir"), N, (", IGnya boleh di follow kak"), Ig)
