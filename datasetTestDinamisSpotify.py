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
    print("\n=== Hasil Pencarian ===")
    if hasil_iteratif:
        print(f"Iteratif: Lagu ditemukan: {hasil_iteratif}, Waktu: {waktu_iteratif:.6f} detik")
    else:
        print(f"Iteratif: Lagu tidak ditemukan, Waktu: {waktu_iteratif:.6f} detik")

    if hasil_rekursif:
        print(f"Rekursif: Lagu ditemukan: {hasil_rekursif}, Waktu: {waktu_rekursif:.6f} detik")
    else:
        print(f"Rekursif: Lagu tidak ditemukan, Waktu: {waktu_rekursif:.6f} detik")

    return waktu_iteratif, waktu_rekursif

# Fungsi utama untuk menjalankan program
def main():
    print("Selamat datang di aplikasi pencarian lagu!")

    iteratif_times = []
    rekursif_times = []
    dataset_sizes = []

    while True:
        try:
            size = int(input("Masukkan ukuran dataset (ketik 0 untuk keluar): "))
            if size == 0:
                print("Program berhenti. Terima kasih telah menggunakan aplikasi ini!")
                break
            if size < 0:
                print("Ukuran dataset tidak boleh negatif. Silakan coba lagi.")
                continue

            dataset_sizes.append(size)
            data_lagu = generate_dataset(size)
            waktu_iteratif, waktu_rekursif = cari_lagu(data_lagu, "Lagu A")
            iteratif_times.append(waktu_iteratif)
            rekursif_times.append(waktu_rekursif)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # Membuat grafik jika ada data yang diinputkan
    if dataset_sizes:
        plt.plot(dataset_sizes, iteratif_times, label='Iteratif', marker='o', color='blue', linestyle='-', linewidth=2)
        plt.plot(dataset_sizes, rekursif_times, label='Rekursif', marker='x', color='green', linestyle='--', linewidth=2)

        plt.xlabel('Ukuran Dataset')
        plt.ylabel('Waktu (detik)')
        plt.title('Perbandingan Waktu Pencarian Iteratif vs Rekursif')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    main()
