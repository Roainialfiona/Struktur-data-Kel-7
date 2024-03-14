class Node:
    def __init__(self, menu=None, harga=None):
        self.menu = menu
        self.harga = harga
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_menu(self, menu, harga,):
        new_node = Node(menu, harga,)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def tampilkan_pesanan(self):
        current_node = self.head
        if not current_node:
            print("Keranjang pesanan kosong.")
            return
        print("Pesanan:")
        while current_node:
            print(f"- {current_node.menu}: {current_node.harga} rupiah")
            current_node = current_node.next_node
            
    def hitung_total_harga(self):
        total_harga = 0
        current_node = self.head
        while current_node:
            total_harga += current_node.harga
            current_node = current_node.next_node
        return total_harga

# Daftar menu dan harga
menu_harga = {
    "miexue ice cream": 5000,
    "boba shake": 16000,
    "mi sundae": 14000,
    "mi ganas": 11000,
    "creamy manggo boba": 22000
}
# Fungsi untuk menampilkan daftar menu
def tampilkan_daftar_menu():
    print("Daftar Menu:")
    for menu, harga in menu_harga.items():
        print(f"{menu}: {harga} rupiah")
# Fungsi utama
def main():
    keranjang_pesanan = LinkedList()

    while True:
        print("\nMenu Aplikasi:")
        print("1. Tambah pesanan ke keranjang")
        print("2. Tampilkan pesanan yang sudah ditambahkan")
        print("3. Hitung jumlah harga yang dibayarkan")
        print("4. selesai")

        pilihan = input("Masukkan pilihan Anda: ")
        if pilihan == "1":
            tampilkan_daftar_menu()
            menu_pesanan = input("Masukkan nama menu yang ingin dipesan: ").lower()
            if menu_pesanan in menu_harga:
                keranjang_pesanan.tambah_menu(menu_pesanan, menu_harga[menu_pesanan])
                print("Pesanan berhasil ditambahkan ke keranjang.")
            else:
                print("Menu tidak valid. Silakan pilih menu yang tersedia.")
        elif pilihan == "2":
            keranjang_pesanan.tampilkan_pesanan()
        elif pilihan == "3":
            total_harga = keranjang_pesanan.hitung_total_harga()
            print(f"Total biaya yang harus dibayarkan adalah: {total_harga} rupiah")
        elif pilihan == "4":
            print("Terima kasih sudah memesan.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()



