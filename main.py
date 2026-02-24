import time
import random


def boot_sequence() -> None:
    """
    Menampilkan urutan booting sistem palsu dengan jeda waktu untuk efek dramatis.
    """
    pesan_boot = [
        "Memuat modul kernel...",
        "Memasang volume aman...",
        "Membangun saluran enkripsi...",
        "Memverifikasi integritas sistem...",
        "Menginisialisasi firewall...",
        "Sistem online."
    ]

    for pesan in pesan_boot:
        print(pesan)
        # Memberikan jeda acak antara 0.3 sampai 0.8 detik untuk kesan realistis
        time.sleep(random.uniform(0.3, 0.8))


def main() -> None:
    """
    Titik masuk utama untuk Simulator Hacker Terminal.
    """
    print("Menginisialisasi simulator hacker terminal...")
    print("-" * 40)
    boot_sequence()
    print("-" * 40)
    print("Selamat datang, Hacker. Siap untuk aksi hari ini?")


if __name__ == "__main__":
    main()
