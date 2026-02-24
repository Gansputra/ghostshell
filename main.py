import time
import random
import sys


def type_writer(text: str, speed: float = 0.04) -> None:
    """
    Menampilkan teks dengan efek mesin tik (per karakter).
    
    Args:
        text: String yang akan ditampilkan.
        speed: Jeda waktu antar karakter dalam detik.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def boot_sequence() -> None:
    """
    Menampilkan urutan booting sistem palsu dengan efek type writer.
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
        type_writer(pesan, speed=0.03)
        # Memberikan jeda acak antar baris untuk kesan memproses data
        time.sleep(random.uniform(0.2, 0.5))


def main() -> None:
    """
    Titik masuk utama untuk Simulator Hacker Terminal.
    """
    type_writer("Menginisialisasi simulator hacker terminal...", speed=0.05)
    print("-" * 40)
    boot_sequence()
    print("-" * 40)
    time.sleep(0.5)
    type_writer("Selamat datang, Hacker. Siap untuk aksi hari ini?", speed=0.06)


if __name__ == "__main__":
    main()
