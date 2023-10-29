print('kelompok: 6')
print('lalu wilanggeng geni')
print('zainal arifin')
print('salman alfarizi')
print('rian marta wijaya')
print('multazam')
print('khairul azmi')
print('saepul ardi')
def menu():
    print("============== Daftar Barang ===================")
    print("|| Kode ||   Nama Barang   || Harga Satuan    ||")
    print("================================================")
    print("||  A   ||     Telur       ||     Rp.2500     ||")
    print("||  B   ||     Tepung      ||     Rp.9000     ||")
    print("||  C   ||     Minyak      ||    Rp.16000     ||")
    print("||  D   ||     Gula        ||     Rp.8000     ||")
    print("||  E   ||     Garam       ||     Rp.2500     ||")
    print("================================================")

def kasir():
    menu()
    daftar_barang = {
        "A": {"nama": "Telur", "harga": 2500},
        "B": {"nama": "Tepung", "harga": 9000},
        "C": {"nama": "Minyak", "harga": 16000},
        "D": {"nama": "Gula", "harga": 8000},
        "E": {"nama": "Garam", "harga": 2500}
    }

    belanjaan = {}
    total_harga = 0

    while True:
        kode_barang = input("Masukkan kode barang (A/B/C/D/E atau 'selesai' untuk selesai): ").upper()

        if kode_barang == 'SELESAI':
            break

        if kode_barang not in daftar_barang:
            print("Kode barang tidak valid. Masukkan kode yang benar.")
            continue

        jumlah = int(input(f"Masukkan jumlah {daftar_barang[kode_barang]['nama']} yang ingin dibeli: "))
        harga_satuan = daftar_barang[kode_barang]["harga"]
        total_barang = jumlah * harga_satuan

        belanjaan[daftar_barang[kode_barang]["nama"]] = {"jumlah": jumlah, "harga_satuan": harga_satuan, "total_barang": total_barang}
        total_harga += total_barang

    print("\n========================== STRUK BELANJA ================================")
    print("|| Nama Barang   \t||  Quan   \t||   Harga Satuan  \t||    Total     \t||")
    print("=========================================================================")
    for item, data in belanjaan.items():
           print(f"|| {item}         \t||  {data  ['jumlah']}     \t||   Rp. {data      ['harga_satuan']}      \t|| Rp.{data['total_barang']} \t    ||")
    print("=========================================================================")
    print(f"Total Belanja:Rp. {total_harga}")
    uang_pembayaran = int(input("Jumlah uang yang dibayarkan:Rp."))
    kembalian =uang_pembayaran - total_harga
    print(f"Kembalian:Rp.{kembalian}")
    print("||==================================================||")
    print("||      TERIMAKASIH TELAH BELANJA DI TOKO KAMI      ||")
    print("||==================================================||")

kasir()