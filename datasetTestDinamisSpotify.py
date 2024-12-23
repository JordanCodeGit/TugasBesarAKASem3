import time
import matplotlib.pyplot as plt

# Fungsi untuk membuat dataset dinamis
def generate_dataset(size):
    return [
        {
            "id": i,
            "judul_lagu": f"Lagu {chr(65 + (i % 26))}",
            "artis": f"Artis {chr(65 + (i % 10))}",
            "genre": ["Pop", "Jazz", "Rock", "Hip-Hop", "Classical"][i % 5],
        }
        for i in range(1, size + 1)
    ]

# Fungsi sequential search (Iteratif)
def sequential_search(data, keyword):
    for lagu in data:
        if keyword.lower() in lagu["judul_lagu"].lower():
            return lagu
    return None

# Fungsi sequential search (Rekursif)
def sequential_search_recursive(data, keyword, index=0):
    if index >= len(data):
        return None
    if keyword.lower() in data[index]["judul_lagu"].lower():
        return data[index]
    return sequential_search_recursive(data, keyword, index + 1)

# Fungsi untuk mencari lagu berdasarkan algoritma iteratif dan rekursif
def cari_lagu(data, keyword):
    # Pencarian menggunakan iteratif
    start_time = time.perf_counter()
    hasil_iteratif = sequential_search(data, keyword)
    end_time = time.perf_counter()
    waktu_iteratif = end_time - start_time

    # Pencarian menggunakan rekursif
    start_time = time.perf_counter()
    hasil_rekursif = sequential_search_recursive(data, keyword)
    end_time = time.perf_counter()
    waktu_rekursif = end_time - start_time

    # Tampilkan hasil
    print("\n================ Hasil Pencarian Lagu =================")
    print(f"{'Metode':<15}{'Status':<25}{'Waktu (detik)':<15}")
    print("-" * 55)
    
    if hasil_iteratif:
        print(f"{'Iteratif':<15}{'Lagu ditemukan':<25}{waktu_iteratif:.6f}")
        print(f"{'':<15}{'ID':<10}{hasil_iteratif['id']}")
        print(f"{'':<15}{'Judul':<10}{hasil_iteratif['judul_lagu']}")
        print(f"{'':<15}{'Artis':<10}{hasil_iteratif['artis']}")
        print(f"{'':<15}{'Genre':<10}{hasil_iteratif['genre']}")
        print("")
    else:
        print(f"{'Iteratif':<15}{'Lagu tidak ditemukan':<25}{waktu_iteratif:.6f}")

    if hasil_rekursif:
        print(f"{'Rekursif':<15}{'Lagu ditemukan':<25}{waktu_rekursif:.6f}")
        print(f"{'':<15}{'ID':<10}{hasil_rekursif['id']}")
        print(f"{'':<15}{'Judul':<10}{hasil_rekursif['judul_lagu']}")
        print(f"{'':<15}{'Artis':<10}{hasil_rekursif['artis']}")
        print(f"{'':<15}{'Genre':<10}{hasil_rekursif['genre']}")
    else:
        print(f"{'Rekursif':<15}{'Lagu tidak ditemukan':<25}{waktu_rekursif:.6f}")

    print("-" * 55)
    return waktu_iteratif, waktu_rekursif

# Fungsi utama untuk menjalankan program
def main():
    print("")
    print("-=-=-=-=-= Selamat datang di aplikasi pencarian lagu! =-=-=-=-=-")
    print("Aplikasi ini dirancang untuk analisis studi kasus laporan kami yang berjudul")
    print("'Analisis Kompleksitas Algoritma Sequential Search: Studi Kasus Pencarian Lagu pada Spotify dengan Pendekatan Iteratif dan Rekursif'")
    print("Aplikasi ini dirancang oleh: ")
    print("1. Jordan Angkawijaya (2311102139)")
    print("2. Mahija Danadyaksa Sadtomo (2311102157)")

    iteratif_times = []
    rekursif_times = []
    dataset_sizes = []

    while True:
        try:
            print("")
            size = int(input("Masukkan ukuran dataset (ketik 0 untuk keluar): "))
            if size == 0:
                print("Program berhenti. Thank you for using!!")
                print("")
                break
            if size < 0:
                print("Datasets can't be negative?? Input a positive number pls.")
                continue

            dataset_sizes.append(size)
            data_lagu = generate_dataset(size)
            waktu_iteratif, waktu_rekursif = cari_lagu(data_lagu, "Lagu A")
            iteratif_times.append(waktu_iteratif)
            rekursif_times.append(waktu_rekursif)
        except ValueError:
            print("Inputs should be a number..")

    # Membuat grafik jika ada data yang diinputkan
    if dataset_sizes:
        plt.figure(figsize=(10, 6))
        
        plt.plot(dataset_sizes, iteratif_times, label='Iteratif', marker='o', color='blue', linestyle='-', linewidth=2)
        plt.plot(dataset_sizes, rekursif_times, label='Rekursif', marker='x', color='green', linestyle='--', linewidth=2)

        plt.xlabel('Ukuran Dataset', fontsize=12)
        plt.ylabel('Waktu (detik)', fontsize=12)
        plt.title('Perbandingan Waktu Pencarian Iteratif vs Rekursif', fontsize=14, fontweight='bold')
        plt.suptitle('Dirancang oleh Jordan Angkawijaya & Mahija Danadyaksa Sadtomo', fontsize=10, style='italic')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

if __name__ == "__main__":
    main()
