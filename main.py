import time
import random
import sys
import os

VERSION = "1.5.0"
SYSTEM_NAME = "GHOST SHELL OS"

try:
    if sys.platform == "win32":
        import winsound
        HAS_WINSOUND = True
    else:
        HAS_WINSOUND = False
except ImportError:
    HAS_WINSOUND = False

# ANSI Color Codes
CLR_RESET = "\033[0m"
CLR_GREEN = "\033[92m"
CLR_RED   = "\033[91m"
CLR_CYAN  = "\033[96m"
CLR_BOLD  = "\033[1m"

# --- UTILITAS TERMINAL ---

def clear_screen() -> None:
    """Membersihkan layar terminal."""
    os.system('cls' if sys.platform == 'win32' else 'clear')

def init_terminal() -> None:
    """Mengaktifkan dukungan warna di Windows."""
    if sys.platform == "win32":
        os.system('color')

def play_audio(tipe: str = "ketik") -> None:
    """Memainkan audio sederhana untuk feedback terminal."""
    if HAS_WINSOUND:
        try:
            if tipe == "ketik":
                winsound.Beep(random.randint(700, 900), 10)
            elif tipe == "selesai":
                winsound.Beep(1000, 100)
                winsound.Beep(1200, 150)
        except Exception:
            pass
    elif tipe == "selesai":
        sys.stdout.write("\a") # ASCII Bell
        sys.stdout.flush()

def efek_mesin_tik(teks: str, kecepatan: float = 0.04, suara: bool = True) -> None:
    """Menampilkan teks karakter demi karakter dengan suara."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        if suara and karakter != " ":
            play_audio("ketik")
        time.sleep(kecepatan)
    print()

def tampilkan_garis(panjang: int = 60, karakter: str = "=") -> None:
    """Menampilkan garis pembatas di terminal."""
    print(karakter * panjang)

# --- MODUL SIMULASI ---

def urutan_booting() -> None:
    """Simulasi proses booting sistem OS palsu."""
    tahapan = [
        "Memuat modul kernel tingkat rendah...",
        "Memasang volume file sistem terenkripsi...",
        "Menghubungkan ke jaringan proxy global...",
        "Menyiapkan lapisan firewall virtual...",
        "Memverifikasi integritas Ghost Shell..."
    ]
    for pesan in tahapan:
        efek_mesin_tik(f"[INFO] {pesan}", kecepatan=0.01)
        time.sleep(random.uniform(0.1, 0.3))
    print(f"{CLR_GREEN}Sistem Berhasil Dimuat. Selamat Datang.{CLR_RESET}")

def tampilkan_event_acak() -> None:
    """Menampilkan aktivitas hacker acak untuk efek visual."""
    daftar_event = [
        "Mendekripsi paket data SSH...",
        "Bypass otentikasi biometrik...",
        "Eskalasi hak akses administrator...",
        "Menghapus jejak log akses...",
        "Injeksi payload SQL...",
        "Membuka portal backdoor..."
    ]
    
    selected = random.sample(daftar_event, random.randint(2, 4))
    for event in selected:
        sys.stdout.write(f"[STATUS] {event}")
        sys.stdout.flush()
        for _ in range(3):
            time.sleep(random.uniform(0.1, 0.4))
            sys.stdout.write(".")
            sys.stdout.flush()
            play_audio("ketik")
        print(f" {CLR_GREEN}[BERHASIL]{CLR_RESET}")
        play_audio("selesai")
        time.sleep(0.2)

def bar_progres(label: str, panjang: int = 40) -> None:
    """Progress bar modern dengan animasi di satu baris."""
    print(f"\n{CLR_BOLD}{label}{CLR_RESET}")
    for i in range(101):
        terisi = int(round(panjang * i / 100))
        bar = '█' * terisi + '░' * (panjang - terisi)
        sys.stdout.write(f'\r[{bar}] {i}% ')
        sys.stdout.flush()
        
        if i % 10 == 0:
            play_audio("ketik")
            
        # Variasi kecepatan biar terasa nyata
        if i < 40:
            time.sleep(random.uniform(0.01, 0.04))
        elif i < 85:
            time.sleep(random.uniform(0.03, 0.09))
        else:
            time.sleep(random.uniform(0.1, 0.2))
    print()
    play_audio("selesai")

def hasil_akhir() -> None:
    """Menampilkan hasil acak dari operasi hacking."""
    opsi = [
        {
            "warna": CLR_GREEN,
            "art": "   ACCESS GRANTED   ",
            "msg": "Akses penuh didapatkan. Semua sistem di bawah kendali."
        },
        {
            "warna": CLR_CYAN,
            "art": " TARGET COMPROMISED ",
            "msg": "Data berhasil diekstrak. Target tidak menyadari serangan."
        },
        {
            "warna": CLR_RED,
            "art": "  TRACE DETECTED!   ",
            "msg": "Koneksi terdeteksi oleh admin! Menghancurkan sesi darurat..."
        }
    ]
    
    hasil = random.choice(opsi)
    tampilkan_garis(karakter="-")
    print(f"\n{hasil['warna']}{CLR_BOLD}{hasil['art']}{CLR_RESET}")
    efek_mesin_tik(hasil['msg'], kecepatan=0.04)

# --- ALUR UTAMA ---

def simulasi_hacking(target: str) -> None:
    """Menjalankan skenario hacking lengkap ke target."""
    clear_screen()
    tampilkan_garis()
    efek_mesin_tik(f"MENGINISIALISASI SERANGAN KE: {target}", kecepatan=0.05)
    tampilkan_garis()
    
    time.sleep(0.5)
    tampilkan_event_acak()
    bar_progres("MENGUNDUH BASIS DATA INTI")
    
    tampilkan_event_acak()
    bar_progres("MENEMBUS PROTOKOL ENKRIPSI")
    
    time.sleep(1.0)
    hasil_akhir()
    tampilkan_garis(karakter="-")
    input("\nTekan ENTER untuk kembali ke menu...")

def main() -> None:
    """Entry point utama aplikasi."""
    init_terminal()
    clear_screen()
    
    efek_mesin_tik(f">>> {SYSTEM_NAME} v{VERSION} DIMULAI", kecepatan=0.03)
    tampilkan_garis()
    urutan_booting()
    tampilkan_garis()
    time.sleep(0.5)

    target_saat_ini = "192.168.1.100 [Mainframe Bank]"
    
    while True:
        clear_screen()
        print(f"{CLR_CYAN}--- {SYSTEM_NAME} MENU ---{CLR_RESET}")
        print(f"Target Terkunci: {CLR_RED}{target_saat_ini}{CLR_RESET}")
        print("-" * 30)
        print("1. Jalankan Serangan (Execute Hack)")
        print("2. Ubah Target (Modify Target)")
        print("3. Matikan Terminal (Shutdown)")
        
        pilihan = input("\nGhostShell> ").strip()
        
        if pilihan == "1":
            simulasi_hacking(target_saat_ini)
        elif pilihan == "2":
            efek_mesin_tik("Masukkan Host/IP Baru: ", suara=False)
            baru = input("Target: ").strip()
            target_saat_ini = baru if baru else "Unknown Host"
        elif pilihan == "3":
            efek_mesin_tik("Mematikan semua modul dan menghapus jejak...", kecepatan=0.02)
            print("Terminal ditutup secara aman.")
            break
        else:
            print(f"{CLR_RED}[!] Perintah tidak valid.{CLR_RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSesi diputus paksa.")
        sys.exit()
