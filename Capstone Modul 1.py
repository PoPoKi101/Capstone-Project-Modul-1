inventory = {
    'A001': {'name': 'Meja', 'quantity': 10, 'price': 200000},
    'B002': {'name': 'Lemari', 'quantity': 20, 'price': 100000},
    'C003': {'name': 'Kursi', 'quantity': 30, 'price': 50000},
}

def display_inventory(inventory):
    print("{:<10} {:<20} {:<10} {:<10}".format('Code', 'Name', 'Quantity', 'Price'))
    for code, item in inventory.items():
        name = item['name']
        quantity = item['quantity']
        price = item['price']
        print("{:<10} {:<20} {:<10} {:<10}".format(code, name, quantity, price))

def add_product_to_inventory(inventory):
    code = input("Masukan Kode Produk: ")
    while code in inventory:
        print("Code produk sudah terdaftar. Silahkan masukan kode produk yang lain.")
        code = input("Masukkan Code Produk: ")
    name = input("Masukkan Nama Produk: ")
    quantity = input("Masukan kuantitas Produk: ")
    while not quantity.isdigit():
        print("Input Anda Tidak Sesuai. Kuantitas Harus Berupa Bilangan Angka positif")
        quantity = input("Masukan kuantitas Produk: ")
    price = input("Masukan Harga Produk: ")
    while not price.isdigit():
        print("Input Anda Tidak Sesuai. Harga Harus Berupa Bilangan Angka positif.")
        price = input("Masukan Harga Produk: ")
    inventory[code] = {'name': name, 'quantity': int(quantity), 'price': int(price)}
    print("Produk Sudah Ditambahkan Kedalam Inventory.")

def update_product(inventory):
    code = input("Masukan Kode Produk Yang Akan di Update: ")
    if code in inventory:
        print("Pilih kolom mana yang akan di update:")
        print("1. Price")
        print("2. Quantity")
        choice = input("Pilihllah Angka (1 or 2): ")
        while choice not in ['1', '2']:
            print("Pilihan Tidak Sesuai.")
            choice = input("Pilihllah Angka (1 or 2): ")
        if choice == '1':
            price = input("Masukkan Harga Yang Baru: ")
            while not price.isdigit():
                print("Input Anda Tidak Sesuai. Harga Harus Berupa Bilangan Angka positif.")
                price = input("Masukkan Harga Yang Baru: ")
            inventory[code]['price'] = (price)
            print("Harga Produk Sudah terupdate.")
        else:
            quantity = input("Masukkan Kuantitas produk yang baru: ")
            while not quantity.isdigit():
                print("Input Anda Tidak Sesuai. Kuantitas Harus Berupa Bilangan Angka positif.")
                quantity = input("Masukkan Kuantitas produk yang baru: ")
            inventory[code]['quantity'] = int(quantity)
            print("Kuantitas sudah terupdate.")
    else:
        print("Kode Produk Tidak Terdaftar Dalam Inventory.")

def remove_product_from_inventory(inventory):
    code = input("Masukan Kode Produk Yang Akan Di Hapus: ")
    if code not in inventory:
        print("Produk Tidak Terdaftar Dalam Inventory.")
    else:
        del inventory[code]
        print("Produk Telah Berhasil Di Hapus.")

def display_product_by_name(inventory, product_name):
    found_product = False
    print("{:<10} {:<20} {:<10} {:<10}".format('Code', 'Name', 'Quantity', 'Price'))
    for code, item in inventory.items():
        if item['name'].lower() == product_name.lower():
            name = item['name']
            quantity = item['quantity']
            price = item['price']
            found_product = True
            print("{:<10} {:<20} {:<10} {:<10}".format(code, name, quantity, price))
    if not found_product:
        print("Produk Tidak Terdaftar Dalam Inventory.")

while True:
    print("\nMenu:")
    print("1. Tampilkan Semua Data Inventory")
    print("2. Cari Produk Berdasarkan Nama")
    print("3. Tambakan Produk kedalam inventory")
    print("4. Update Produk Yang Ada Dalam inventory")
    print("5. Hapus Produk Dalam inventory")
    print("6. Exit")

    choice = input("Masukkan Pilihan Menu: ")

    if choice == '1':
        display_inventory(inventory)
    elif choice == '2':
        product_name = input("Masukan Nama produk: ")
        display_product_by_name(inventory, product_name)
    elif choice == '3':
        add_product_to_inventory(inventory)
    elif choice == '4':
        update_product(inventory)
    elif choice == '5':
        remove_product_from_inventory(inventory)
    elif choice == '6':
        print("Terimakasih, Program Di Hentikan.")
        break
    else:
        print("Pilihan Yang Anda Masukkan Salah. Pilihlah Dari Angka 1 - 6 Berdasarkan Menu.")
