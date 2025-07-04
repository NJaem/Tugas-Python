print("Tugas Sistem")

print("2. Hotel Coconut")
print("HOTEL COCONUT")
print("Pilihan Kamar: ")
print("1. Frontend = Rp150.000/hari")
print("2. Backend = Rp200.000/hari")
print("3. System = Rp250.000/hari")

Frontend = 150000
Backend = 200000
System = 250000

NP = input ("Masukkan Nama Pengunjung = ")
JK = input ("Masukkan Jenis Kamar = ")
H = int (input("Berapa Hari Akan Menginap? (angka) = "))
O = int (input ("Masukkan Jumlah Pengunjung = "))

if JK == "Frontend":
    B = H * Frontend

if JK == "Backend":
    B = H * Backend

if JK == "System":
    B = H * System

else:
    print("Kamar Tidak Tersedia")

HR = input ("Hari Check-In, (Senin-Minggu) = ")
Ci = float (input("Masukkan Jam Check-In (00.00 - 23.00) = "))
Co = float (input("Masukkan Jam Check-Out (00.00 - 23.00)) = "))

print("Metode Pembayaran:")
print("1. Cash")
print("2. Qris")
print("3. Kredit")

MP = input ("Masukkan Metode Pembayaran = ")

if O > 3:
    B += 100000 * H

if HR == "Jumat":
    B -= (B * 0.10)

if Co > Ci:
    B += (150000 * (Co - Ci))

if MP == "Cash":
    if B > 50000:
        B -= (B * 0.10)

if MP == "Qris":
    if B > 50000:
        B -= (B * 0.15)

elif MP == "Kredit":
    if B > 50000:
        B -= (B * 0.5)

else:
    print("Metode Pembayaran Tidak Terbaca")

print(f"Total Pembayaran: Rp{B:,.2f}")

U = float(input("Masukkan Jumlah Uang Anda: "))

if U >= B:
    K = U - B

print("====== Struk Pembayaran ======")
print("Nama Pelanggan : " ,NP)
print("Jenis Kamar : " ,JK)
print("Lama Menginap : " ,H)
print("Jumlah Pengunjung : " ,O)
print("Jam Check-In : " ,Ci)
print("Jam Check-Out : " ,Co)
print("Metode Pembayaran : " ,MP)
print(f"Total Pembayaran : {B:,.2f}")
print(f"Uang : {U:,.2f}")
print(f"Kembalian : {K:,.2f}")