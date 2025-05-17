import random

# 1 Data menu makanan (6 item) dan minuman (6 item) beserta harga
food_menu = {
    "Nasi Goreng": 20000,
    "Mie Ayam": 15000,
    "Ayam Geprek": 18000,
    "Sate Ayam": 25000,
    "Bakso": 18000,
    "Rendang": 30000
}

beverage_menu = {
    "Es Teh": 5000,
    "Jus Alpukat": 12000,
    "Es Jeruk": 7000,
    "Kopi": 10000,
    "Susu": 8000,
    "Air Mineral": 4000
}

# 2. Variabel global untuk menyimpan pesanan
food_orders = {}
beverage_orders = {}
# 3. Fungsi untuk menampilkan menu dalam bentuk tabel
def print_menu_box(menu: dict, title: str):
    """
    Menampilkan daftar menu dalam bentuk (tabel) 
    """
    items = list(menu.items())
    
    max_menu_len = max(len(name) for name, _ in items)
    max_price_len = max(len(str(price)) for _, price in items)
    
    # Header kolom
    header_menu = "Menu"
    header_price = "Harga (Rp)"
    max_menu_len = max(max_menu_len, len(header_menu))
    max_price_len = max(max_price_len, len(header_price))
    
    # Kolom nomor
    no_col_width = 4  # lebar kolom untuk "No"
    # Hitung total lebar tabel
    total_width = no_col_width + 3 + max_menu_len + 3 + max_price_len + 3

    # Cetak baris atas tabel
    print("+" + "-" * (total_width - 2) + "+")
    # Cetak judul tabel terpusat
    print("|" + title.center(total_width - 2) + "|")
    print("+" + "-" * (total_width - 2) + "+")
    # Cetak header kolom
    header = f"|{'No'.ljust(no_col_width)} | {header_menu.ljust(max_menu_len)} | {header_price.ljust(max_price_len)} |"
    print(header)
    print("+" + "-" * (total_width - 2) + "+")
    # Cetak tiap baris menu
    for i, (menu_name, price) in enumerate(items, start=1):
        row = f"|{str(i).ljust(no_col_width)} | {menu_name.ljust(max_menu_len)} | {str(price).rjust(max_price_len)} |"
        print(row)
    print("+" + "-" * (total_width - 2) + "+")
# 4. Fungsi order_food():
def order_food():
    """
    Menampilkan menu makanan dengan dekorasi kotak, dan menerima input pesanan.
    Pengguna hanya memasukkan nomor untuk memesan.
    Input 0 untuk kembali ke menu utama.
    """
    print("\n=== Pesan Makanan ===")
    print_menu_box(food_menu, "MENU MAKANAN")
    
    food_items = list(food_menu.keys())
    while True:
        try:
            choice = int(input("Masukkan nomor makanan yang ingin dipesan (0 untuk kembali): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka sesuai pilihan.")
            continue
        
        if choice == 0:
            break
        elif 1 <= choice <= len(food_items):
            selected_item = food_items[choice - 1]
            food_orders[selected_item] = food_orders.get(selected_item, 0) + 1
            print(f"Pesanan '{selected_item}' berhasil ditambahkan.")
        else:
            print("Pilihan tidak valid.")
# 5. Fungsi order_beverage():
def order_beverage():
    """
    Menampilkan menu minuman , dan menerima input pesanan.
    Pengguna hanya memasukkan nomor untuk memesan.
    Input 0 untuk kembali ke menu utama.
    """
    print("\n=== Pesan Minuman ===")
    print_menu_box(beverage_menu, "MENU MINUMAN")
    
    beverage_items = list(beverage_menu.keys())
    while True:
        try:
            choice = int(input("Masukkan nomor minuman yang ingin dipesan (0 untuk kembali): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka sesuai pilihan.")
            continue
        
        if choice == 0:
            break
        elif 1 <= choice <= len(beverage_items):
            selected_item = beverage_items[choice - 1]
            beverage_orders[selected_item] = beverage_orders.get(selected_item, 0) + 1
            print(f"Pesanan '{selected_item}' berhasil ditambahkan.")
        else:
            print("Pilihan tidak valid.")
# 6. Fungsi view_cart():
def view_cart():
    """
    Menampilkan ringkasan pesanan (makanan dan minuman) beserta total harga.
    """
    print("\n=== Keranjang Pesanan ===")
    total = 0
    
    if food_orders:
        print("\nMakanan:")
        for item, qty in food_orders.items():
            subtotal = food_menu[item] * qty
            total += subtotal
            print(f"- {item} x{qty} = Rp{subtotal}")
    else:
        print("\nTidak ada pesanan makanan.")
    
    if beverage_orders:
        print("\nMinuman:")
        for item, qty in beverage_orders.items():
            subtotal = beverage_menu[item] * qty
            total += subtotal
            print(f"- {item} x{qty} = Rp{subtotal}")
    else:
        print("\nTidak ada pesanan minuman.")
    
    print(f"\nTotal Harga: Rp{total}")
# 7. Fungsi process_payment():
def process_payment():
    """
    Menampilkan ringkasan pesanan beserta total harga, kemudian meminta
    pengguna memilih metode pembayaran (Cash atau E-money).
    Setelah itu, aplikasi menghasilkan nomor antrian acak dan menampilkan pesan terima kasih.
    Pesanan akan direset setelah pembayaran.
    """
    total = 0
    print("\n=== Ringkasan Pesanan untuk Pembayaran ===")
    if food_orders:
        print("\nMakanan:")
        for item, qty in food_orders.items():
            subtotal = food_menu[item] * qty
            total += subtotal
            print(f"- {item} x{qty} = Rp{subtotal}")
    if beverage_orders:
        print("\nMinuman:")
        for item, qty in beverage_orders.items():
            subtotal = beverage_menu[item] * qty
            total += subtotal
            print(f"- {item} x{qty} = Rp{subtotal}")
    print(f"\nTotal Harga yang harus dibayar: Rp{total}")
    
    # Pilih metode pembayaran
    while True:
        print("\nPilih Metode Pembayaran:")
        print("1. Cash")
        print("2. E-money")
        pay_choice = input("Masukkan pilihan (1/2): ").strip()
        if pay_choice == "1":
            method = "Cash"
            break
        elif pay_choice == "2":
            method = "E-money"
            break
        else:
            print("Pilihan tidak valid. Masukkan 1 atau 2.")
    
    # Generate nomor antrian secara acak
    queue_number = random.randint(1, 100)
    print(f"\nPembayaran dengan {method} berhasil.")
    print(f"Nomor antrian Anda: {queue_number}. Terimakasih telah memesan!")
    
    # Reset pesanan setelah pembayaran
    food_orders.clear()
    beverage_orders.clear()
# 8. Fungsi main():
def main():
    """
    Main loop aplikasi dengan menu awal yang menyediakan opsi:
      1. Pesan Makanan
      2. Pesan Minuman
      3. Lihat Keranjang
      4. Pembayaran
      5. Keluar
    """
    while True:
        print("\n=== Aplikasi Pemesanan ===")
        print("1. Pesan Makanan")
        print("2. Pesan Minuman")
        print("3. Lihat Keranjang")
        print("4. Pembayaran")
        print("5. Keluar")
        option = input("Masukkan pilihan (1-5): ").strip()
        
        if option == "1":
            order_food()
        elif option == "2":
            order_beverage()
        elif option == "3":
            view_cart()
        elif option == "4":
            process_payment()
        elif option == "5":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()


# PENJELASAN (COMMAND) KODE DI ATAS 
# 1. Data menu makanan dan minuman:
#    - Menyimpan 6 item makanan (food_menu) dan 6 item minuman (beverage_menu).
#    - Setiap item memiliki nama (key) dan harga (value).
# 2. Variabel global untuk menyimpan pesanan
#    - Digunakan untuk menyimpan pesanan makanan dan minuman yang dilakukan pengguna.
# 3. Fungsi untuk menampilkan menu dalam bentuk tabel
#    - Menampilkan data menu dalam format tabel dengan kotak.
#    - Menghitung lebar kolom secara dinamis agar tampilan rapi.
# 4. Fungsi order_food():
#    - Menampilkan menu makanan dengan dekorasi kotak.
#    - Menerima input nomor dari pengguna untuk memesan makanan.
#    - Input 0 mengembalikan ke menu utama.
# 5. Fungsi order_beverage():
#    - Menampilkan menu minuman dengan dekorasi kotak.
#    - Menerima input nomor dari pengguna untuk memesan minuman.
#    - Input 0 mengembalikan ke menu utama.
# 6. Fungsi view_cart():
#    - Menampilkan ringkasan pesanan (makanan & minuman) beserta subtotal tiap item.
#    - Menghitung dan menampilkan total harga keseluruhan.
# 7. Fungsi process_payment():
#    - Menampilkan ringkasan pesanan dan total harga.
#    - Meminta input metode pembayaran (Cash atau E-money).
#    - Menghasilkan nomor antrian secara acak dan menampilkan pesan terima kasih.
#    - Mengosongkan keranjang pesanan setelah pembayaran.
# 8. Fungsi main():
#    - Merupakan loop utama aplikasi yang menampilkan menu awal dengan opsi:
#         1. Pesan Makanan
#         2. Pesan Minuman
#         3. Lihat Keranjang
#         4. Pembayaran
#         5. Keluar
#    - Berdasarkan input, fungsi memanggil fungsi terkait.
#
