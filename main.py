import time
import random
import sys
import os

try:
    if sys.platform == "win32":
        import winsound
        HAS_WINSOUND = True
    else:
        HAS_WINSOUND = False
except ImportError:
    HAS_WINSOUND = False


def play_sound(sound_type: str = "type") -> None:
    """
    Memainkan suara terminal sederhana.
    """
    if HAS_WINSOUND:
        try:
            if sound_type == "type":
                winsound.Beep(random.randint(600, 800), 10)
            elif sound_type == "complete":
                winsound.Beep(1000, 100)
                winsound.Beep(1200, 150)
        except Exception:
            pass
    else:
        if sound_type == "complete":
            sys.stdout.write("\a")
            sys.stdout.flush()


def type_writer(text: str, speed: float = 0.04, sound: bool = True) -> None:
    """
    Menampilkan teks dengan efek mesin tik dan suara.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if sound and char != " ":
            play_sound("type")
        time.sleep(speed)
    print()


def show_random_events() -> None:
    """
    Menampilkan peristiwa hacking acak.
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
            time.sleep(random.uniform(0.1, 0.3))
            sys.stdout.write(".")
            sys.stdout.flush()
            play_sound("type")
        print(" [BERHASIL]")
        play_sound("complete")
        time.sleep(random.uniform(0.1, 0.2))


def progress_bar(label: str, bar_length: int = 40) -> None:
    """
    Menampilkan progress bar modern.
    """
    sys.stdout.write(f"\n{label}\n")
    for i in range(101):
        filled = int(round(bar_length * i / 100))
        percent = i
        bar = '█' * filled + '░' * (bar_length - filled)
        
        sys.stdout.write(f'\r[{bar}] {percent}% ')
        sys.stdout.flush()
        
        if i % 10 == 0:
            play_sound("type")
            
        if i < 30:
            time.sleep(random.uniform(0.01, 0.03))
        elif i < 70:
            time.sleep(random.uniform(0.02, 0.06))
        else:
            time.sleep(random.uniform(0.04, 0.1))
            
    print()
    play_sound("complete")


def display_outcome() -> None:
    """
    Menampilkan hasil akhir hacking secara acak.
    """
    outcomes = [
        {
            "color": "\033[92m", # Hijau
            "text": """
   _   ___ ___ ___ ___ ___    ___ ___   _   _  _ _____ ___ ___ 
  /_\ / __/ __| __/ __/ __|  / __| _ \ /_\ | \| |_   _| __|   \\
 / _ \ (_| (__| _|\__ \__ \ | (_ |   // _ \| .` | | | | _|| |) |
/_/ \_\___\___|___|___/___/  \___|_|_/_/ \_\_|\_| |_| |___|___/ 
            """,
            "message": "AKSES DIBERIKAN: Kendali penuh sistem diperoleh."
        },
        {
            "color": "\033[96m", # Cyan
            "text": """
 _____ _   ___ ___ ___ _____    ___ ___  __  __ ___ ___  ___  __  __ ___ ___ ___ ___ 
|_   _/_\ | _ \ __| __|_   _|  / __/ _ \|  \/  | _ \ _ \/ _ \|  \/  |_ _/ __| __|   \\
  | |/ _ \|   / _|| _|  | |   | (_| (_) | |\/| |  _/   / (_) | |\/| || | (__| _|| |) |
  |_/_/ \_\_|_|___|___| |_|    \___\___/|_|  |_|_| |_|_\\___/|_|  |_|___\___|___|___/ 
            """,
            "message": "TARGET KOMPROMIS: Data berhasil diekstraksi ke server pusat."
        },
        {
            "color": "\033[91m", # Merah
            "text": """
 _____ ___   _   ___ ___   ___  ___ _____ ___ ___ _____ ___ ___  
|_   _| _ \ /_\ / __| __| |   \| __|_   _| __/ __|_   _| __|   \\ 
  | | |   // _ \ (__| _|  | |) | _|  | | | _| (__  | | | _|| |) |
  |_| |_|_/_/ \_\___\___| |___/|___| |_| |___\___| |_| |___|___/ 
            """,
            "message": "JEJAK TERDETEKSI: Mematikan koneksi darurat... Evakuasi data gagal!"
        }
    ]
    
    res = random.choice(outcomes)
    print(f"\n{res['color']}{res['text']}\033[0m")
    play_sound("complete")
    type_writer(res['message'], speed=0.04)


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
        type_writer(pesan, speed=0.01)
        time.sleep(random.uniform(0.05, 0.15))


def run_hacking_simulation(target: str) -> None:
    """
    Menjalankan simulasi hacking terhadap target tertentu.
    """
    print("\n" + "=" * 60)
    type_writer(f"Menginisialisasi serangan ke: {target}", speed=0.04)
    print("=" * 60)
    
    time.sleep(0.5)
    show_random_events()
    progress_bar("MENJEBOL PERTAHANAN KERNEL")
    
    show_random_events()
    progress_bar("MENGUNDUH REGISTRI RAHASIA")
    
    print("-" * 60)
    type_writer("Proses selesai. Menganalisis hasil akhir...", speed=0.05)
    time.sleep(1.0)
    
    display_outcome()
    print("-" * 60)
    time.sleep(1.0)


def main() -> None:
    """
    Titik masuk utama untuk Simulator Hacker Terminal dengan menu interaktif.
    """
    if sys.platform == "win32":
        os.system('color')

    # Pembersihan layar awal
    os.system('cls' if sys.platform == 'win32' else 'clear')

    type_writer(">>> GHOST SHELL OS v1.3.0 INITIATED", speed=0.03)
    print("=" * 60)
    boot_sequence()
    print("=" * 60)
    time.sleep(0.5)

    target_saat_ini = "10.0.4.129 [Central Datacenter]"
    
    while True:
        print(f"\n[SISTEM SIAP] - Target Saat Ini: {target_saat_ini}")
        print("1. Mulai Peretasan (Start Hack)")
        print("2. Ganti Target (Change Target)")
        print("3. Keluar (Exit)")
        
        pilihan = input("\nGhostShell> ").strip()
        
        if pilihan == "1":
            run_hacking_simulation(target_saat_ini)
        elif pilihan == "2":
            type_writer("Masukkan alamat target baru: ", speed=0.03, sound=True)
            target_saat_ini = input("Target: ").strip()
            if not target_saat_ini:
                target_saat_ini = "Unknown Host"
            type_writer(f"Target diubah menjadi: {target_saat_ini}", speed=0.03)
        elif pilihan == "3":
            type_writer("Memutuskan koneksi secara aman...", speed=0.03)
            print("Sesi ditutup. Sampai jumpa, Hacker.")
            break
        else:
            print("[ERROR] Perintah tidak dikenal. Silakan pilih 1-3.")


if __name__ == "__main__":
    main()
