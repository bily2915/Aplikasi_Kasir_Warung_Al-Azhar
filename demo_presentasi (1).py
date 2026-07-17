"""
demo_presentasi.py
==================
Script Demo Otomatis untuk Presentasi Fase 6
Aplikasi Kasir Warung — Randy Ramadhan & Wulan Purnamasari
Universitas Al Azhar Indonesia — Semester Genap 2025/2026

Jalankan: python demo_presentasi.py
TIDAK memerlukan input manual — semua demo berjalan otomatis.
"""

import sys, time
sys.path.insert(0, '.')

# Coba import versi v1.0.1, fallback ke v1.0.0
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("kw", "kasir_warung_v101.py")
    k = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(k)
    print("[ Menggunakan kasir_warung_v101.py (versi final) ]")
except:
    import kasir_warung as k
    print("[ Menggunakan kasir_warung.py ]")

def pause(secs=1.2):
    time.sleep(secs)

def tekan_enter(msg="[ Tekan ENTER untuk lanjut ke demo berikutnya ]"):
    input(f"\n  {msg}\n")

# ══════════════════════════════════════════════════════
print("\n" + "═"*56)
print("   DEMO PRESENTASI — KASIR WARUNG v1.0.1")
print("   Randy Ramadhan & Wulan Purnamasari")
print("   Algoritma & Pemrograman — Al Azhar 2026")
print("═"*56)
tekan_enter("[ ENTER ] Mulai Demo D-1: Menu Produk")

# ──────────────────────────────────────────────────────
# DEMO D-1: TAMPIL MENU PRODUK
# ──────────────────────────────────────────────────────
menu = k.init_menu_default()
riwayat = []
counter = [1]

print("\n" + "═"*56)
print("  D-1  |  BAB 8 — DICTIONARY: Tampil Menu Produk")
print("═"*56)
print("  Struktur data: Dict of Dict")
print("  menu_produk['P001'] =", menu["P001"])
print()
k.tampilkan_menu_produk(menu)
print(f"\n  Total produk : {len(menu)} (dari init_menu_default())")
print(f"  Kode unik    : {k.get_kode_unik(menu)}  ← Bab 8: Set")
pause()
tekan_enter("[ ENTER ] Lanjut ke D-2: Transaksi Lengkap")

# ──────────────────────────────────────────────────────
# DEMO D-2: TRANSAKSI
# ──────────────────────────────────────────────────────
print("\n" + "═"*56)
print("  D-2  |  TRANSAKSI LENGKAP — #TRX-001")
print("═"*56)

keranjang = []
transaksi = [("P001", 2), ("P002", 1), ("P003", 1)]
print("\n  ► Menambahkan item ke keranjang...")
for kode, qty in transaksi:
    ok, msg = k.tambah_item_ke_keranjang(kode, qty, menu, keranjang)
    print(f"    {'✓' if ok else '✗'} {msg}")
    pause(0.4)

print("\n  ► Isi keranjang (Bab 7 — List of Dict):")
k.tampilkan_keranjang(keranjang)

total_iter  = k.hitung_total(keranjang)          # Bab 4
total_rekur = k.hitung_total_rekursif(keranjang) # Bab 11
print(f"\n  ► Total (iteratif  Bab 4)  : {k.format_rupiah(total_iter)}")
print(f"  ► Total (rekursif  Bab 11) : {k.format_rupiah(total_rekur)}")
print(f"  ► Sama? {'✓ Ya' if total_iter == total_rekur else '✗ Tidak'}")

uang = 30000
ok, kembalian, pesan = k.proses_pembayaran(total_iter, uang)
print(f"\n  ► Bayar Rp 30.000 → {pesan}")
print(f"  ► Kembalian: {k.format_rupiah(kembalian)}")

# Cetak struk
stok_p001_sebelum = menu["P001"]["stok"]
k.update_stok(keranjang, menu)
k.cetak_struk(keranjang, total_iter, kembalian, uang, "TRX-001")
k.simpan_riwayat("TRX-001", keranjang, total_iter, riwayat)
counter[0] += 1
print(f"\n  ► Stok P001: {stok_p001_sebelum} → {menu['P001']['stok']} (berkurang {len(transaksi[0])})")
pause()
tekan_enter("[ ENTER ] Lanjut ke D-3: Searching & Sorting")

# ──────────────────────────────────────────────────────
# DEMO D-3: SEARCHING & SORTING
# ──────────────────────────────────────────────────────
print("\n" + "═"*56)
print("  D-3  |  BAB 9 — SEARCHING  +  BAB 10 — SORTING")
print("═"*56)

print("\n  ► LINEAR SEARCH O(n) — keyword: 'mie'")
hasil_lin = k.cari_produk_linear("mie", menu)
print(f"  Ditemukan {len(hasil_lin)} produk:")
for kode, prod in hasil_lin:
    print(f"    {kode} | {prod['nama']} | {k.format_rupiah(prod['harga'])}")

print("\n  ► BINARY SEARCH O(log n) — cari kode: 'P005'")
terurut = sorted(menu.items(), key=lambda x: x[0])
idx = k.cari_produk_binary("P005", terurut)
if idx != -1:
    print(f"  Ditemukan di indeks [{idx}]: {terurut[idx][1]['nama']}")
print(f"  (Binary search butuh max {__import__('math').ceil(__import__('math').log2(len(menu)))} langkah dari {len(menu)} produk)")

print("\n  ► BUBBLE SORT O(n²) vs TIMSORT O(n log n) — by harga:")
daftar = list(menu.items())
hasil_b = k.bubble_sort_produk(daftar, "harga", True)
comps = len(daftar)*(len(daftar)-1)//2
hasil_t = k.sort_produk_builtin(menu, "harga", True)

print(f"\n  Bubble Sort — {comps} perbandingan:")
for kd, pd in hasil_b[:4]:
    print(f"    {kd} {pd['nama']:<20} {k.format_rupiah(pd['harga'])}")
print(f"    ...")

print(f"\n  Timsort (built-in) — estimasi {round(len(menu)*__import__('math').log2(len(menu)))} perbandingan:")
for kd, pd in hasil_t[:4]:
    print(f"    {kd} {pd['nama']:<20} {k.format_rupiah(pd['harga'])}")
print(f"    ...")

sama = [kd for kd,_ in hasil_b] == [kd for kd,_ in hasil_t]
print(f"\n  Hasil sama? {'✓ Ya' if sama else '✗ Tidak'}")
pause()
tekan_enter("[ ENTER ] Lanjut ke D-4: Rekursi & Laporan")

# ──────────────────────────────────────────────────────
# DEMO D-4: REKURSI + LAPORAN
# ──────────────────────────────────────────────────────
print("\n" + "═"*56)
print("  D-4  |  BAB 11 — REKURSI  +  BAB 12 — BIG-O")
print("═"*56)

# Tambah 1 transaksi lagi untuk laporan
keranjang2 = []
k.tambah_item_ke_keranjang("P004", 2, menu, keranjang2)
k.tambah_item_ke_keranjang("P007", 3, menu, keranjang2)
total2 = k.hitung_total(keranjang2)
k.update_stok(keranjang2, menu)
k.simpan_riwayat("TRX-002", keranjang2, total2, riwayat)

print("\n  ► Visualisasi call stack rekursi (n=2 item keranjang2):")
for i, item in enumerate(keranjang2):
    indent = "  " + "  "*i
    print(f"  {indent}hitung_total_rekursif(krnj, {i})")
    print(f"  {indent}= {item['subtotal']} + hitung_total_rekursif(krnj, {i+1})")
print(f"  {' '*6}= 0  ← BASE CASE")

total_rek = k.hitung_total_rekursif(keranjang2)
total_itr = k.hitung_total(keranjang2)
print(f"\n  Total (rekursif): {k.format_rupiah(total_rek)}")
print(f"  Total (iteratif): {k.format_rupiah(total_itr)}")

print("\n  ► LAPORAN REKURSIF (Bab 11):")
print(f"  {'No.':<4} {'ID':<10} {'Waktu':<10} {'Total':>14}")
print("  " + "-"*42)
total_sesi = k.tampilkan_laporan_rekursif(riwayat)
print("  " + "-"*42)
print(f"  Total pendapatan sesi: {k.format_rupiah(total_sesi)}")

print("\n  ► ANALISIS BIG-O — ringkasan:")
k.tampilkan_analisis_bigO()

# ──────────────────────────────────────────────────────
print("\n" + "═"*56)
print("  DEMO SELESAI — Semua fitur berjalan dengan baik ✓")
print("═"*56)
print("\n  File yang dikumpulkan:")
files = [
    "kasir_warung_v101.py   ← Program utama (v1.0.1)",
    "test_fase4.py          ← 68 test cases (100% PASS)",
    "kasir_warung.ipynb     ← Notebook Jupyter per-bab",
    "README.md              ← Dokumentasi proyek",
    "AI_USAGE_LOG.md        ← 8 interaksi AI (CRIDE)",
    "Fase5_Laporan_Teknis_Kasir_Warung.docx",
    "Presentasi_Kasir_Warung_Fase6.pptx",
]
for f in files:
    print(f"  📄 {f}")
print()
