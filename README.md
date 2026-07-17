# 🏪 Kasir Warung — Sistem Point-of-Sale Berbasis Python

**Tugas Akhir Algoritma & Pemrograman — Semester Genap 2025/2026**

---

## 📋 Deskripsi

**Kasir Warung** adalah aplikasi kasir sederhana berbasis CLI (*Command Line Interface*) yang dibangun menggunakan Python murni tanpa library eksternal. Aplikasi ini mensimulasikan sistem kasir warung kelontong dengan fitur input barang, penghitungan total, cetak struk digital, manajemen stok, dan laporan transaksi.

Proyek ini dikembangkan mengikuti tahapan **SDLC Sederhana** (Software Development Life Cycle) dan mengintegrasikan seluruh konsep dari **Bab 2 hingga Bab 13** mata kuliah Algoritma dan Pemrograman.

---

## ✨ Fitur

| No | Fitur | Deskripsi |
|----|-------|-----------|
| 1 | **Proses Transaksi (Kasir)** | Tambah/hapus item, hitung total, proses pembayaran, cetak struk digital ke terminal |
| 2 | **Manajemen Stok Produk** | Tambah produk baru, update harga & stok, demo sorting & searching interaktif |
| 3 | **Laporan Transaksi** | Ringkasan sesi iteratif & rekursif, tampilan tabel analisis Big-O |
| 4 | **Demo Akademik** | Setiap sub-menu berlabel bab yang relevan untuk keperluan presentasi |
| 5 | **Validasi Input** | Semua input divalidasi dengan `try-except` + range check — tidak bisa crash |
| 6 | **Struk Digital** | Format teks berkolom rapi menggunakan `ljust/rjust/center` |

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python **3.8** atau lebih baru
- Tidak memerlukan instalasi library tambahan (`stdlib` only)

### Jalankan Program Utama
```bash
python kasir_warung_v101.py
```

### Jalankan Test Suite (Fase 3)
```bash
python test_kasir_warung.py
# Expected: 48/48 test lulus
```

### Jalankan Test Plan Lengkap (Fase 4)
```bash
python test_fase4.py
# Expected: 68/68 test lulus
```

### Buka Notebook Jupyter
```bash
jupyter notebook kasir_warung.ipynb
```

---

## 🗂️ Struktur File

```
kasir_warung/
├── kasir_warung_v101.py     # ← VERSI FINAL (v1.0.1 — 3 bug fixed)
├── kasir_warung.py          # Versi awal Fase 3 (v1.0.0)
├── test_kasir_warung.py     # Unit test Fase 3 — 48 test cases
├── test_fase4.py            # Test Plan Fase 4 — 68 test cases
├── kasir_warung.ipynb       # Notebook Jupyter per-bab
├── README.md                # Dokumentasi ini
└── AI_USAGE_LOG.md          # Log interaksi dengan AI (Bab 13)
```

---

## 🏗️ Arsitektur — Top-Down Design (4 Layer)

```
main()                          ← Layer 0: Entry Point
└── menu_utama()
    ├── menu_kasir()            ← Layer 1: Controller
    │   ├── tambah_item_ke_keranjang()   ← Layer 2: Business Logic
    │   ├── hapus_item_keranjang()
    │   ├── hitung_total()               (iteratif — Bab 4)
    │   ├── hitung_total_rekursif()      (rekursif — Bab 11)
    │   ├── proses_pembayaran()
    │   ├── update_stok()
    │   ├── cetak_struk()               ← Layer 3: Utility/I/O
    │   └── simpan_riwayat()
    ├── menu_stok()
    │   ├── get_kode_unik()              (Set — Bab 8)
    │   ├── cari_produk_linear()         (O(n) — Bab 9)
    │   ├── cari_produk_binary()         (O(log n) — Bab 9)
    │   ├── bubble_sort_produk()         (O(n²) — Bab 10)
    │   └── sort_produk_builtin()        (O(n log n) — Bab 10)
    └── menu_laporan()
        ├── tampilkan_riwayat()          (iteratif — Bab 4)
        ├── tampilkan_laporan_rekursif() (rekursif — Bab 11)
        └── tampilkan_analisis_bigO()    (Bab 12)
```

---

## 🗄️ Struktur Data

| Variabel | Tipe | Contoh | Alasan |
|----------|------|--------|--------|
| `menu_produk` | `Dict of Dict` | `{"P001": {"nama":"...", "harga":3500, "stok":50}}` | Akses O(1) by kode produk |
| `keranjang` | `List of Dict` | `[{"kode":"P001", "qty":2, "subtotal":7000}]` | Urutan insert terjaga |
| `riwayat` | `List of Dict` | `[{"id":"TRX-001", "total":11000, "items":[...]}]` | Append-only log O(1) |
| `kode_set` | `Set` | `{"P001","P002",...}` | Cek duplikat O(1) |
| `counter_id` | `List[int]` | `[1]` | Mutable container agar bisa dimodifikasi dari fungsi |

---

## ⚙️ Algoritma yang Digunakan

| Bab | Algoritma | Fungsi | Kompleksitas |
|-----|-----------|--------|-------------|
| Bab 9 | Linear Search | `cari_produk_linear()` | O(n) |
| Bab 9 | Binary Search | `cari_produk_binary()` | O(log n) |
| Bab 10 | Bubble Sort | `bubble_sort_produk()` | O(n²) |
| Bab 10 | Timsort (built-in) | `sort_produk_builtin()` | O(n log n) |
| Bab 11 | Rekursi | `hitung_total_rekursif()` | O(n) waktu, O(n) ruang |
| Bab 11 | Rekursi + Akumulasi | `tampilkan_laporan_rekursif()` | O(n) waktu, O(n) ruang |
| Bab 4 | Iterasi + Akumulasi | `hitung_total()` | O(n) waktu, O(1) ruang |

---

## 📚 Konsep yang Diintegrasikan

| Bab | Konsep | Lokasi di Kode |
|-----|--------|----------------|
| Bab 2 | Variabel & Tipe Data | Semua variabel, type hints |
| Bab 3 | Seleksi (if/elif/else) | Routing menu, validasi bisnis |
| Bab 4 | Perulangan (for/while) | Loop menu, iterasi keranjang |
| Bab 5 | Fungsi | 18 fungsi modular Top-Down |
| Bab 6 | String | `cetak_struk`, `format_rupiah` |
| Bab 7 | List/Tuple | Keranjang, riwayat, return tuple |
| Bab 8 | Dictionary/Set | `menu_produk`, `get_kode_unik` |
| Bab 9 | Searching | `cari_produk_linear/binary` |
| Bab 10 | Sorting | `bubble_sort`, `sort_builtin` |
| Bab 11 | Rekursi | `hitung_total_rekursif` |
| Bab 12 | Big-O | Komentar + `tampilkan_analisis_bigO` |
| Bab 13 | AI Partner | CRIDE Framework, AI_USAGE_LOG.md |

---

## 🧪 Hasil Testing

| Fase | File | Test Cases | Hasil |
|------|------|-----------|-------|
| Fase 3 | `test_kasir_warung.py` | 48 | ✅ 100% PASS |
| Fase 4 | `test_fase4.py` | 68 | ✅ 100% PASS |
| Bug Fixed | v1.0.1 | 3 bugs | ✅ Semua verified |

---

## 🔄 Changelog

### v1.0.1 — 04 Juli 2026 (Fase 4 Patch)
- **FIX BUG-001**: `update_stok()` — guard kode ghost (`if kode not in menu: continue`)
- **FIX BUG-002**: `sort_produk_builtin()` — validasi `KUNCI_VALID` + fallback ke `'nama'`
- **FIX BUG-003**: `cari_produk_linear()` — guard keyword kosong (`if not kw: return []`)

### v1.0.0 — 27 Juni 2026 (Fase 3 Initial)
- Rilis pertama — semua fitur dasar lengkap

---

## 👤 Identitas

| | |
|---|---|
| **Nama** | Randy Ramadhan, Wulan Purnamasari, Bily Nur Sepdiansyah, Ibrahim Hadi Wibisono |
| **NIM** | 0112525012, 0102525702, 0112525002, 0112525003 |
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Universitas** | Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |

---

*_Bertumbuh, Berproses, dan Bernilai Bersama dalam Menyelesaikan Tugas Akhir Algoritma & Pemrograman_*
