

**UNIVERSITAS AL AZHAR INDONESIA**

Fakultas Ilmu Komputer — Program Studi Teknik Informatika

**LAPORAN TEKNIS PROYEK AKHIR**

Mata Kuliah: Algoritma dan Pemrograman (3 SKS)

| 🏪  APLIKASI KASIR WARUNG Fase 5: Dokumentasi Final |
| :---: |

| Item | Detail |
| :---- | :---- |
| **Nama Mahasiswa 1** | Randy Ramadhan |
| **Nama Mahasiswa 2** | Wulan Purnamasari |
| **Nama Mahasiswa 3** | Bily Nur Sepdiansyah |
| **Nama Mahasiswa 4** | Ibrahim Hadi Wibisono |
| **NIM** | 0112525012, 0102525702, 0112525002, 0112525003 |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Semester** | Genap 2025/2026 |
| **Tanggal Pengumpulan** | 20 Juli 2026 |

# **1\. Pendahuluan**

## **1.1 Latar Belakang Masalah**

Usaha mikro kecil seperti warung kelontong dan warung makan merupakan pilar perekonomian masyarakat Indonesia, namun sebagian besar pengelola masih mengandalkan pencatatan manual yang rawan kesalahan. Ketidakakuratan perhitungan kembalian, kesulitan memantau stok secara real-time, dan tidak adanya riwayat transaksi yang terstruktur menjadi kendala nyata yang dihadapi sehari-hari.

Proyek ini hadir sebagai solusi berbasis Python yang dapat dijalankan di terminal tanpa koneksi internet maupun perangkat khusus, sehingga mudah diadopsi oleh pengelola warung dari berbagai latar belakang teknologi. Sekaligus, proyek ini berfungsi sebagai media pembelajaran untuk mengintegrasikan konsep-konsep algoritma dan pemrograman (Bab 2–13) dalam satu aplikasi yang fungsional.

## **1.2 Tujuan Proyek**

* Membangun aplikasi kasir fungsional berbasis Python CLI yang dapat digunakan secara langsung

* Mengintegrasikan seluruh konsep mata kuliah (Bab 2–13) dalam satu proyek terpadu

* Menerapkan metodologi SDLC sederhana: Analisis → Desain → Implementasi → Testing → Dokumentasi → Presentasi

* Mendokumentasikan penggunaan AI secara transparan sesuai framework CRIDE (Bab 13\)

## **1.3 Ruang Lingkup**

* Aplikasi berbasis CLI (Command Line Interface) — tidak memerlukan GUI

* Menggunakan Python stdlib only — tidak ada pip install

* Data tersimpan dalam memori sesi (in-memory) — tidak ada database atau file I/O

* Mendukung satu operator kasir (single-user)

# **2\. Desain Sistem**

## **2.1 Arsitektur — Top-Down Design (4 Layer)**

Program dirancang menggunakan prinsip Top-Down Design dengan 4 layer yang terpisah jelas tanggung jawabnya:

| Hierarki Fungsi — Top-Down Design Layer 0: main()                  ← Entry point & inisialisasi └── Layer 1: menu\_utama()        ← Router / Controller utama     ├── menu\_kasir()             ← Controller transaksi     │   ├── tambah\_item\_ke\_keranjang()   \[Layer 2: Business Logic\]     │   ├── hapus\_item\_keranjang()     │   ├── hitung\_total()               (iteratif — Bab 4\)     │   ├── hitung\_total\_rekursif()      (rekursif — Bab 11\)     │   ├── proses\_pembayaran()     │   ├── update\_stok()     │   ├── cetak\_struk()        \[Layer 3: Utility / I/O\]     │   └── simpan\_riwayat()     ├── menu\_stok()  → get\_kode\_unik, cari\_produk\_\*, bubble\_sort, sort\_builtin     └── menu\_laporan() → tampilkan\_riwayat, tampilkan\_laporan\_rekursif, bigO |
| :---- |

## **2.2 Pemilihan Struktur Data**

| Variabel | Tipe | Contoh Nilai | Justifikasi |
| :---- | :---- | :---- | :---- |
| menu\_produk | Dict of Dict | {'P001':{'nama':...,'harga':3500,'stok':50}} | Akses O(1) by kode produk |
| keranjang | List of Dict | \[{'kode':'P001','qty':2,'subtotal':7000}\] | Urutan insert terjaga, iterasi mudah |
| riwayat | List of Dict | \[{'id':'TRX-001','total':11000,'items':\[...\]}\] | Append-only log O(1) |
| kode\_set | Set | {'P001','P002','P003',...} | Cek duplikat O(1) tanpa iterasi |
| counter\_id | List\[int\] | \[1\] | Mutable container untuk increment dari sub-fungsi |

## **2.3 Desain Algoritma**

Empat kategori algoritma diimplementasikan untuk memenuhi kompetensi Bab 9–11:

| Algoritma | Fungsi | Kompleksitas | Keterangan |
| :---- | :---- | :---- | :---- |
| Linear Search | cari\_produk\_linear() | O(n) | Periksa satu per satu — cocok data kecil (\<100 produk) |
| Binary Search | cari\_produk\_binary() | O(log n) | Bagi dua — prasyarat data terurut by kode |
| Bubble Sort | bubble\_sort\_produk() | O(n²) | Nested loop swap — demo konsep dasar sorting |
| Timsort | sort\_produk\_builtin() | O(n log n) | sorted() Python — production-ready |
| Rekursi | hitung\_total\_rekursif() | O(n)/O(n) | Base case \+ recursive case, demo vs iteratif |
| Rekursi+Akum | tampilkan\_laporan\_rekursif() | O(n)/O(n) | Tail-style dengan parameter akumulasi |

## **2.4 Flowchart Alur Transaksi**

| Flowchart: Satu Siklus Transaksi Kasir START   │   ├─ Inisialisasi: menu\_produk(dict), riwayat(list), counter\_id(list)   │   └─▶ WHILE True (menu\_utama):          │          └─▶ WHILE True (menu\_kasir):                 │                 ├─ \[1\] Input kode & qty                 │     ├─ Dict lookup O(1) → kode ada?                 │     ├─ Validasi stok \>= qty                 │     ├─ Linear search di keranjang → duplikat?                 │     └─ append/update keranjang                 │                 ├─ \[2\] Proses Bayar                 │     ├─ hitung\_total() → akumulasi subtotal O(n)                 │     ├─ Input uang → proses\_pembayaran() O(1)                 │     ├─ update\_stok() → dict mutation O(n)                 │     ├─ cetak\_struk() → string format O(n)                 │     ├─ simpan\_riwayat() → list append O(1)                 │     └─ keranjang.clear() → reset                 │                 └─ \[5\] Batal → clear & break |
| :---- |

# **3\. Implementasi**

## **3.1 Informasi Teknis**

| Bahasa | Python 3.8+ |
| :---- | :---- |
| **Dependensi** | stdlib only (datetime) — tidak perlu pip install |
| **Versi Final** | v1.0.1 (patch 3 bug dari Fase 4\) |
| **Jumlah Fungsi** | 18 fungsi modular |
| **Jumlah Baris Kode** | ±880 baris (termasuk komentar & docstring) |
| **Jumlah Test Case** | 68 (Fase 4\) \+ 48 regression (Fase 3\) \= 116 total |

## **3.2 Highlight Implementasi per Bab**

**Bab 6 — String: Fungsi format\_rupiah & cetak\_struk**

| format\_rupiah() — Bab 6: f-string \+ str.replace() def format\_rupiah(angka: int) \-\> str:     """Konversi int ke string Rupiah. O(1). Bab 6: f-string \+ replace."""     return f"Rp {angka:,}".replace(",", ".")     \# f'Rp {10000:,}' → 'Rp 10,000' → .replace → 'Rp 10.000' |
| :---- |

**Bab 8 — Dictionary/Set: tambah\_item\_ke\_keranjang**

| tambah\_item\_ke\_keranjang() — Dict lookup O(1) \+ Linear Search O(n) if kode not in menu\_produk:            \# Bab 8: O(1) dict lookup     return (False, 'Kode tidak ditemukan.') produk \= menu\_produk\[kode\]             \# Bab 8: dict access if produk\['stok'\] \< qty:               \# Bab 3: validasi     return (False, 'Stok tidak cukup.') for item in keranjang:                 \# Bab 9: linear search     if item\['kode'\] \== kode:           \# cek duplikat         item\['qty'\] \+= qty             \# update qty         item\['subtotal'\] \= item\['qty'\] \* produk\['harga'\]         return (True, 'Updated.') keranjang.append({...})                \# Bab 7: list.append() |
| :---- |

**Bab 9 — Binary Search O(log n)**

| cari\_produk\_binary() — Divide & Conquer def cari\_produk\_binary(kode\_target, daftar\_terurut):     if not daftar\_terurut: return \-1   \# edge case guard (Fase 4 fix)     kiri, kanan \= 0, len(daftar\_terurut) \- 1     while kiri \<= kanan:               \# Bab 4: while         tengah \= (kiri \+ kanan) // 2         kode\_tengah \= daftar\_terurut\[tengah\]\[0\]         if kode\_tengah \== kode\_target: return tengah  \# found         elif kode\_tengah \< kode\_target: kiri \= tengah \+ 1         else: kanan \= tengah \- 1     return \-1 |
| :---- |

**Bab 11 — Rekursi: hitung\_total\_rekursif**

| hitung\_total\_rekursif() — Base Case \+ Recursive Case def hitung\_total\_rekursif(keranjang, indeks=0):     \# BASE CASE: tidak ada item tersisa     if indeks \>= len(keranjang):         return 0     \# RECURSIVE CASE: subtotal\[i\] \+ total sisa item     return keranjang\[indeks\]\['subtotal'\] \\          \+ hitung\_total\_rekursif(keranjang, indeks \+ 1\)     \# Depth n, O(n) waktu, O(n) ruang (call stack) |
| :---- |

# **4\. Testing & Hasil Pengujian**

## **4.1 Strategi Testing**

Testing dilakukan dalam dua fase dengan pendekatan unit test manual (tanpa framework eksternal). Setiap fungsi diuji secara terpisah (isolated unit testing) sebelum diintegrasikan.

| Fase | File | Test Cases | Cakupan |
| :---- | :---- | :---- | :---- |
| Fase 3 | test\_kasir\_warung.py | 48 | Normal cases — verifikasi logika bisnis dasar |
| Fase 4 | test\_fase4.py | 68 | Edge cases \+ Error handling \+ Bug hunting \+ Regression |
| Total | — | 116 | Semua test case dijalankan setelah setiap perubahan kode |

## **4.2 Hasil Test Plan — Fase 4 (68 Test Cases)**

| Suite | Modul/Fungsi | Hasil | Rate |
| :---- | :---- | :---- | :---- |
| TS-01 Bab 6 | format\_rupiah() | 6 / 6 | ✓ 100% |
| TS-02 Bab 7+8 | Dictionary & Set | 12 / 12 | ✓ 100% |
| TS-03 Bab 7+8+9 | tambah\_item\_ke\_keranjang | 14 / 14 | ✓ 100% |
| TS-04 Bab 7+9 | hapus\_item\_keranjang | 6 / 6 | ✓ 100% |
| TS-05 Bab 4+11 | hitung\_total (iter \+ rekursif) | 9 / 9 | ✓ 100% |
| TS-06 Bab 2+3 | proses\_pembayaran | 7 / 7 | ✓ 100% |
| TS-07 Bab 8 | update\_stok | 4 / 4 | ✓ 100% |
| TS-08 Bab 9 | Linear & Binary Search | 15 / 15 | ✓ 100% |
| TS-09 Bab 10 | Bubble Sort & Timsort | 8 / 8 | ✓ 100% |
| TS-10 Bab 11 | Rekursi (laporan) | 5 / 5 | ✓ 100% |
| TS-11 Bab 7+8 | simpan\_riwayat | 5 / 5 | ✓ 100% |
| TS-12 Debug | Bug Hunt & Fix (3 bugs) | 4 / 4 | ✓ 100% |
| Regression | Semua fungsi Fase 3 | 10 / 10 | ✓ 100% |

| ✓  TOTAL: 68/68 TEST LULUS — PASS RATE 100% Diverifikasi dengan: python test\_fase4.py |
| :---: |

## **4.3 Bug yang Ditemukan & Diperbaiki (Fase 4 → v1.0.1)**

| ID | Fungsi | Masalah | Fix v1.0.1 |
| :---- | :---- | :---- | :---- |
| BUG-001 | update\_stok() | KeyError saat kode produk tidak ada di menu | if kode not in menu\_produk: continue |
| BUG-002 | sort\_produk\_builtin() | KeyError jika kunci field tidak valid | KUNCI\_VALID set \+ fallback ke 'nama' |
| BUG-003 | cari\_produk\_linear() | Keyword '' mengembalikan semua produk | if not kw: return hasil (guard) |

# **5\. Dokumentasi Kode**

## **5.1 Standar Docstring**

Setiap fungsi dalam kasir\_warung\_v101.py dilengkapi docstring dengan format standar: deskripsi singkat, referensi bab mata kuliah, parameter (Args), nilai kembalian (Returns), keterangan Big-O, dan catatan patch jika ada.

| Template Docstring Standar def nama\_fungsi(param1: tipe, param2: tipe) \-\> tipe\_return:     """     Deskripsi singkat fungsi — apa yang dilakukan.          Bab X — NamaKonsep: penjelasan konsep yang diimplementasikan.     Big-O: O(...) — alasan kompleksitas.     PATCH vX.X.X — BUG-XXX: deskripsi fix (jika ada).          Args:         param1: deskripsi parameter pertama         param2: deskripsi parameter kedua          Returns:         Tipe dan penjelasan nilai kembalian     """ |
| :---- |

## **5.2 Contoh Docstring Fungsi Utama**

| Docstring tambah\_item\_ke\_keranjang() def tambah\_item\_ke\_keranjang(kode: str, qty: int,                               menu\_produk: dict, keranjang: list) \-\> tuple:     """     Tambah item ke keranjang belanja atau update qty jika sudah ada.          Bab 8 — Dictionary: lookup O(1) by kode produk.     Bab 7 — List: linear search untuk cek duplikat \+ append.     Bab 9 — Searching: linear search sebelum append (hindari duplikat).     Bab 3 — Seleksi: validasi kode ada, qty \> 0, stok cukup.     Big-O: O(n) — n \= jumlah item saat ini di keranjang.          Args:         kode: kode produk uppercase, mis. "P001"         qty: jumlah item yang ingin ditambahkan (harus \> 0\)         menu\_produk: dict produk master (diakses read-only)         keranjang: list keranjang aktif (dimodifikasi in-place)          Returns:         tuple (sukses: bool, pesan: str)     """ |
| :---- |

# **6\. AI Usage Log — Bab 13 (CRIDE Framework)**

## **6.1 Ringkasan Penggunaan AI**

| AI yang digunakan | Claude (Anthropic) |
| :---- | :---- |
| **Framework** | CRIDE — Context, Request, Iterate, Document, Evaluate |
| **% kode dari AI** | \~15% (docstring template, review, penjelasan konsep) |
| **% kode sendiri** | \~85% (semua logika bisnis, algoritma, struktur data) |
| **Jumlah interaksi** | 8 interaksi terdokumentasi (Minggu 9–14) |

## **6.2 Tabel Interaksi AI**

| \# | Waktu | Topik | Output & Keputusan |
| :---- | :---- | :---- | :---- |
| 1 | Minggu 9 | Dict vs List efficiency? | Memilih Dict untuk menu\_produk (O(1) lookup) |
| 2 | Minggu 10 | Template docstring fungsi | Standar docstring untuk 18 fungsi |
| 3 | Minggu 10 | Bug format\_rupiah → 'Rp 10,000' | f-string :, \+ .replace(',','.') |
| 4 | Minggu 11 | Review binary search | Guard if not daftar\_terurut → \-1 |
| 5 | Minggu 12 | Draft tabel Big-O | Diverifikasi manual, 3 nilai dikoreksi |
| 6 | Minggu 13 | BUG-003: '' in str → True | Guard if not kw: return \[\] |
| 7 | Minggu 13 | Teknik ljust/rjust cetak struk | f'{nama.ljust(20)}{qty:\>4}' |
| 8 | Minggu 14 | Outline README profesional | Struktur README \+ konten ditulis sendiri |

## **6.3 Batas yang Ditetapkan**

| ✗  TIDAK meminta AI menulis fungsi logika bisnis dari nol ✗  TIDAK copy-paste kode AI tanpa memahaminya ✗  TIDAK menggunakan AI untuk menjawab quiz/ujian ✓  AI boleh menjelaskan konsep yang belum dipahami ✓  AI boleh mereview kode yang sudah ditulis mahasiswa ✓  AI boleh membantu format & dokumentasi |
| :---- |

# **7\. Kesimpulan & Refleksi**

## **7.1 Capaian Proyek**

Proyek Aplikasi Kasir Warung berhasil diselesaikan sesuai target SDLC dengan seluruh 12 bab konsep terintegrasi dalam satu program yang fungsional. Aplikasi dapat dijalankan langsung di terminal Python tanpa dependensi eksternal, dan seluruh 116 test case (68 Fase 4 \+ 48 regression) lulus dengan pass rate 100%.

| Fase | Status | Capaian | Tanggal |
| :---- | :---- | :---- | :---- |
| Analisis (Fase 1\) | ✓ Selesai | Proposal, problem statement, 5 FR \+ 5 NFR | 20 Juni 2026 |
| Desain (Fase 2\) | ✓ Selesai | Top-Down Design, struktur data, pseudocode | 27 Juni 2026 |
| Implementasi (Fase 3\) | ✓ Selesai | 18 fungsi, v1.0.0, 48 test cases | 27 Juni 2026 |
| Testing (Fase 4\) | ✓ Selesai | 68 test, 3 bug fixed, v1.0.1 | 04 Juli 2026 |
| Dokumentasi (Fase 5\) | ✓ Selesai | README, AI Log, Laporan Teknis | 20 Juli 2026 |

## **7.2 Pembelajaran dari Setiap Bab**

* Bab 2–5 (Dasar): Type hints Python memaksa berpikir tentang tipe data di awal — mencegah banyak bug sejak penulisan kode.

* Bab 6 (String): f-string sangat powerful untuk UI teks; ljust/rjust adalah solusi elegan untuk tabel di terminal tanpa library.

* Bab 7–8 (List/Dict/Set): Pilihan struktur data menentukan efisiensi. Dict untuk lookup, List untuk urutan, Set untuk cek keanggotaan.

* Bab 9 (Searching): Binary search O(log n) jauh lebih cepat dari linear O(n), tapi butuh data terurut. Trade-off ini nyata dalam praktik.

* Bab 10 (Sorting): Bubble sort O(n²) berguna untuk memahami konsep, tapi Timsort O(n log n) yang dipakai production. Keduanya punya tempat masing-masing.

* Bab 11 (Rekursi): Rekursi lebih elegan secara kode, tapi O(n) ruang karena call stack. Iteratif lebih efisien memori untuk kasus yang sama.

* Bab 12 (Big-O): Menganalisis kompleksitas kode sendiri mengajarkan intuisi tentang mana bagian yang bisa jadi bottleneck jika data bertumbuh.

* Bab 13 (AI Partner): AI paling berguna bukan sebagai generator kode, melainkan sebagai 'reviewer' dan 'explainer'. Urutan yang tepat: coba sendiri dulu, baru tanya AI.

## **7.3 Tantangan & Solusi**

| Tantangan | Solusi |
| :---- | :---- |
| counter\_id tidak bisa di-increment dari sub-fungsi | Dikemas dalam list\[int\] agar mutable: \[1\] |
| format\_rupiah() menghasilkan 'Rp 10,000' (salah) | f-string :, \+ .replace(',','.') |
| Binary search belum handle list kosong | Guard if not daftar\_terurut: return \-1 |
| Keyword '' mengembalikan semua produk | Guard if not kw: return \[\] di linear search |
| Struk tidak rata kolom di berbagai panjang nama | Kombinasi \[:22\] truncate \+ ljust(22) |

## **7.4 Refleksi Pengembangan**

Proyek ini membuktikan bahwa konsep-konsep algoritmik yang dipelajari secara terpisah di kelas memiliki koneksi yang erat dalam aplikasi nyata. Dictionary digunakan bersama Linear Search; Sorting dibutuhkan sebelum Binary Search bisa bekerja; Rekursi adalah cara pandang alternatif dari iterasi. Membangun aplikasi dari nol memberi pemahaman yang jauh lebih dalam dibandingkan hanya mengerjakan soal latihan.

Penggunaan framework CRIDE untuk berinteraksi dengan AI juga mengajarkan bahwa AI adalah alat yang sangat powerful, tapi hanya jika pemakainya sudah memiliki pemahaman dasar yang kuat. AI tidak bisa menggantikan proses berpikir — ia hanya bisa mempercepat seseorang yang sudah tahu arah yang ingin dituju.

Jakarta, 20 Juli 2026

