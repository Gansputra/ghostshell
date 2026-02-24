import time
import random
import sys


def type_writer(text: str, speed: float = 0.04) -> None:
    """
    Menampilkan teks dengan efek mesin tik (per karakter).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def progress_bar(label: str, bar_length: int = 40) -> None:
    """
    Menampilkan progress bar modern yang diperbarui di satu baris.
    """
    sys.stdout.write(f"{label}\n")
    for i in range(101):
        filled = int(round(bar_length * i / 100))
        percent = i
        bar = '█' * filled + '░' * (bar_length - filled)
        
        # Format tampilan: [██████░░░░] 60%
        sys.stdout.write(f'\r[{bar}] {percent}% ')
        sys.stdout.flush()
        
        # Jeda acak: lebih lambat di akhir untuk efek dramatis
        if i < 30:
            time.sleep(random.uniform(0.01, 0.05))
        elif i < 70:
            time.sleep(random.uniform(0.02, 0.1))
        elif i < 90:
            time.sleep(random.uniform(0.05, 0.2))
        else:
            time.sleep(random.uniform(0.1, 0.4))
            
    print("\n")


def boot_sequence() -> None:
    """
    Menampilkan urutan booting sistem palsu.
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
        type_writer(pesan, speed=0.02)
        time.sleep(random.uniform(0.1, 0.3))


def main() -> None:
    """
    Titik masuk utama untuk Simulator Hacker Terminal.
    """
    type_writer(">>> GHOST SHELL OS v1.0.0 INITIATED", speed=0.04)
    print("-" * 50)
    boot_sequence()
    print("-" * 50)
    
    time.sleep(1)
    type_writer("Target: 192.168.1.104 (Mainframe Bank Pusat)", speed=0.05)
    type_writer("Status: Penetrasi dilakukan...", speed=0.05)
    
    # Menjalankan progress bar palsu
    progress_bar("Membuka enkripsi lapisan SSL/TLS...")
    progress_bar("Mengekstrak database administratif...")
    
    type_writer("AKSES DIBERIKAN. Selamat datang di sistem inti.", speed=0.06)
    print("\nTerminal ditutup. Sesi berakhir.")


if __name__ == "__main__":
    main()
