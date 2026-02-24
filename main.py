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


def show_random_events() -> None:
    """
    Menampilkan peristiwa hacking acak untuk memberikan kesan sistem sedang bekerja keras.
    """
    events = [
        "Melewati firewall lapisan 3...",
        "Mendekripsi paket data incoming...",
        "Meningkatkan hak akses (Privilege Escalation)...",
        "Menghapus jejak log sistem...",
        "Mengalihkan rute traffic melalui proxy...",
        "Menembus enkripsi WPA3...",
        "Menginjeksi payload ke buffer...",
        "Sinkronisasi dengan satelit uplink..."
    ]
    
    jumlah_event = random.randint(2, 4)
    selected_events = random.sample(events, jumlah_event)
    
    for event in selected_events:
        sys.stdout.write(f"[STATUS] {event}")
        sys.stdout.flush()
        for _ in range(3):
            time.sleep(random.uniform(0.2, 0.5))
            sys.stdout.write(".")
            sys.stdout.flush()
        print(" [BERHASIL]")
        time.sleep(random.uniform(0.1, 0.4))


def progress_bar(label: str, bar_length: int = 40) -> None:
    """
    Menampilkan progress bar modern yang diperbarui di satu baris.
    """
    sys.stdout.write(f"\n{label}\n")
    for i in range(101):
        filled = int(round(bar_length * i / 100))
        percent = i
        bar = '█' * filled + '░' * (bar_length - filled)
        
        sys.stdout.write(f'\r[{bar}] {percent}% ')
        sys.stdout.flush()
        
        if i < 30:
            time.sleep(random.uniform(0.01, 0.04))
        elif i < 70:
            time.sleep(random.uniform(0.02, 0.08))
        else:
            time.sleep(random.uniform(0.05, 0.15))
            
    print()


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
        type_writer(pesan, speed=0.015)
        time.sleep(random.uniform(0.1, 0.2))


def main() -> None:
    """
    Titik masuk utama untuk Simulator Hacker Terminal.
    """
    type_writer(">>> GHOST SHELL OS v1.0.5 INITIATED", speed=0.03)
    print("=" * 50)
    boot_sequence()
    print("=" * 50)
    
    time.sleep(0.8)
    type_writer("Target Terdeteksi: 10.0.4.129 [Central Datacenter]", speed=0.04)
    
    show_random_events()
    
    progress_bar("MENGEKSTRAKSI SESSION KEYS")
    
    show_random_events()
    show_random_events()
    
    progress_bar("MENGUNDUH CORE DATASET")
    
    print("-" * 50)
    type_writer("OPERASI SELESAI. Semua data berhasil disedot.", speed=0.05)
    type_writer("Memutus koneksi secara aman...", speed=0.04)
    print("Sesi ditutup.")


if __name__ == "__main__":
    main()
