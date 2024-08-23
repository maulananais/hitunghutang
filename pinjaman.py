from datetime import datetime, timedelta

# Fungsi untuk menghitung cicilan bulanan
def hitung_cicilan_bulanan(pokok_hutang, jumlah_bulan, bunga_tahunan, bunga_per_hari, hari_terlambat):
    bunga_per_bulan = bunga_tahunan / 12 / 100
    cicilan_pokok_bulanan = pokok_hutang / jumlah_bulan
    bunga_bulanan = pokok_hutang * bunga_per_bulan
    cicilan_bulanan = cicilan_pokok_bulanan + bunga_bulanan

    # Menghitung denda keterlambatan jika ada
    if hari_terlambat > 0:
        denda = pokok_hutang * bunga_per_hari * hari_terlambat / 100
    else:
        denda = 0
    
    cicilan_total = cicilan_bulanan + denda
    return cicilan_total, denda

# Fungsi untuk menghitung tanggal lunas hutang
def hitung_tanggal_lunas(tanggal_mulai, jumlah_bulan):
    tanggal_mulai_obj = datetime.strptime(tanggal_mulai, "%d-%m-%Y")
    tanggal_lunas = tanggal_mulai_obj + timedelta(days=(jumlah_bulan * 30))  # Mengasumsikan 30 hari per bulan
    return tanggal_lunas.strftime("%d-%m-%Y")

# Input dari pengguna
pokok_hutang = float(input("Masukkan pokok hutang (misalnya, 10000000): "))
jumlah_bulan = int(input("Masukkan jangka waktu hutang dalam bulan (misalnya, 60): "))
bunga_tahunan = float(input("Masukkan bunga tahunan dalam persen (misalnya, 12): "))
tanggal_mulai = input("Masukkan tanggal mulai hutang (dd-mm-yyyy): ")
keterlambatan = input("Apakah ada keterlambatan pembayaran? (y/n): ")

if keterlambatan.lower() == 'y':
    bunga_per_hari = float(input("Masukkan bunga keterlambatan per hari dalam persen (misalnya, 0.05): "))
    hari_terlambat = int(input("Masukkan jumlah hari keterlambatan: "))
else:
    bunga_per_hari = 0
    hari_terlambat = 0

# Menghitung cicilan bulanan
cicilan_bulanan, denda = hitung_cicilan_bulanan(pokok_hutang, jumlah_bulan, bunga_tahunan, bunga_per_hari, hari_terlambat)

# Menghitung tanggal lunas
tanggal_lunas = hitung_tanggal_lunas(tanggal_mulai, jumlah_bulan)

# Menghitung total hutang yang harus dibayar
total_hutang = cicilan_bulanan * jumlah_bulan

# Menampilkan hasil
print(f"Tanggal Lunas Hutang: {tanggal_lunas}")
print(f"Cicilan bulanan yang harus dibayar: Rp{cicilan_bulanan:,.2f}")
if denda > 0:
    print(f"Denda keterlambatan: Rp{denda:,.2f}")
print(f"Total hutang yang harus dibayar selama {jumlah_bulan} bulan: Rp{total_hutang:,.2f}")
