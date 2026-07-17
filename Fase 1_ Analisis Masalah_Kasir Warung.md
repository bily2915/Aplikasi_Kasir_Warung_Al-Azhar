

| PROPOSAL PROYEK AKHIR Algoritma dan Pemrograman — Semester Genap 2025/2026 | Universitas Al Azhar Indonesia Fakultas Sains & Teknologi |
| :---- | ----: |

# **Identitas Mahasiswa**

| Nama Mahasiswa 1 | Randy Ramadhan |
| :---- | :---- |
| **Nama Mahasiswa 2** | Wulan Purnamasari |
| **Nama Mahasiswa 3** | Billy Syahputra |
| **Nama Mahasiswa 4** | Ibrahim Hadi |
| **Universitas** | Universitas Al Azhar Indonesia |
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Semester** | Genap 2025/2026 |
| **Tanggal Pengumpulan** | 20 Juni 2026 |

# **1\. Judul Proyek**

**APLIKASI KASIR WARUNG BERBASIS PYTHON**

*Sistem Point-of-Sale Sederhana dengan Manajemen Stok & Cetak Struk Digital*

# **2\. Latar Belakang Masalah**

Usaha mikro kecil seperti warung kelontong dan warung makan merupakan tulang punggung perekonomian masyarakat Indonesia. Namun, sebagian besar pengelola warung masih mengandalkan metode pencatatan manual yang rawan kesalahan, seperti mencatat transaksi di buku atau menghitung kembalian secara perkiraan. Ketidakakuratan ini berdampak langsung pada kerugian finansial dan menurunnya kepercayaan pelanggan.

Ketiadaan sistem pencatatan yang terstruktur menyebabkan pemilik warung kesulitan memantau stok barang secara real-time. Sering kali barang habis tidak diketahui hingga pelanggan memintanya, atau sebaliknya terjadi penumpukan stok yang tidak terjual. Hal ini menghambat pengambilan keputusan bisnis yang efektif, seperti penentuan waktu restok dan identifikasi produk laris.

Dengan mengembangkan Aplikasi Kasir Warung berbasis Python, masalah-masalah tersebut dapat diselesaikan secara sistematis melalui pendekatan algoritmik. Aplikasi ini dirancang sederhana, dapat dijalankan di terminal tanpa memerlukan koneksi internet maupun perangkat khusus, sehingga mudah diadopsi oleh pengelola warung dari berbagai latar belakang teknologi.

# **3\. Tujuan Proyek**

Proyek ini bertujuan untuk:

1. Membangun aplikasi kasir fungsional berbasis Python yang dapat digunakan secara langsung di lingkungan terminal.

2. Mengimplementasikan struktur data Dictionary dan List untuk merepresentasikan data produk, keranjang belanja, dan riwayat transaksi.

3. Menerapkan algoritma pencarian (linear search) untuk menemukan barang berdasarkan nama atau kode produk.

4. Menghasilkan struk transaksi digital yang terformat rapi sebagai output aplikasi.

5. Mendokumentasikan seluruh proses pengembangan sesuai tahapan SDLC sebagai bukti capaian pembelajaran mata kuliah.

# **4\. Fitur yang Akan Dibuat**

| ID | Fitur | Deskripsi |
| :---- | :---- | :---- |
| **F-01** | Manajemen Menu & Stok | Mengelola daftar barang dengan nama, harga, dan stok. Operator dapat menambah, mengubah, dan menghapus item. |
| **F-02** | Input Transaksi Penjualan | Proses pemilihan barang, input kuantitas, dan penghitungan subtotal secara otomatis berbasis struktur data list/dict. |
| **F-03** | Penghitungan Total & Kembalian | Kalkulasi total belanja, penerimaan uang dari pelanggan, dan kembalian secara real-time. |
| **F-04** | Cetak Struk Digital | Mencetak struk transaksi berformat teks ke terminal (stdout) dengan timestamp, rincian item, total, dan kembalian. |
| **F-05** | Riwayat Transaksi | Menyimpan log seluruh transaksi dalam sesi aktif menggunakan struktur list-of-dict untuk pelaporan ringkas. |

# **5\. Rencana Struktur Data**

## **5.1 Data Produk / Menu**

| Representasi: Dictionary of Dictionaries menu \= {     "P001": {"nama": "Indomie Goreng", "harga": 3500, "stok": 50},     "P002": {"nama": "Aqua 600ml",    "harga": 4000, "stok": 30}, } |
| :---- |

Alasan: Dictionary memberikan akses O(1) berdasarkan kode produk, mempercepat proses pencarian item saat transaksi berlangsung.

## **5.2 Keranjang Belanja (Cart)**

| Representasi: List of Dictionaries keranjang \= \[     {"kode": "P001", "nama": "Indomie Goreng", "qty": 2, "subtotal": 7000}, \] |
| :---- |

Alasan: List mempertahankan urutan item yang diinput, memudahkan iterasi saat mencetak struk.

## **5.3 Riwayat Transaksi**

| Representasi: List of Dictionaries (append-only log) riwayat \= \[     {"id": "TRX-001", "waktu": "2026-06-20 10:30", "total": 11500, "items": \[...\]}, \] |
| :---- |

Alasan: Append-only list menjamin integritas log transaksi dan memudahkan pelaporan ringkasan penjualan per sesi.

# **6\. Rencana Algoritma**

## **6.1 Linear Search — Pencarian Produk**

Digunakan untuk mencari item di keranjang berdasarkan kode produk sebelum menambah kuantitas (menghindari duplikasi baris). Kompleksitas: O(n) di mana n \= jumlah item di keranjang.

## **6.2 Iterasi & Akumulasi — Kalkulasi Total**

Loop iteratif melalui seluruh item di keranjang untuk menjumlahkan subtotal. Setiap subtotal \= harga x qty, dan total \= sum(subtotal semua item). Kompleksitas: O(n).

## **6.3 String Formatting — Cetak Struk**

Algoritma pemformatan teks menggunakan f-string dan ljust/rjust Python untuk menghasilkan struk berkolom rapi di terminal. Tidak bergantung pada library eksternal.

## **6.4 Validasi Input — Error Handling**

Setiap input pengguna divalidasi menggunakan try-except dan conditional check (kode produk ada?, stok cukup?, jumlah uang cukup?). Bertujuan mencegah crash dan memberikan pesan error yang informatif.

# **7\. Rencana Penggunaan AI**

Tim akan memanfaatkan bantuan AI secara transparan dan bertanggung jawab pada bagian-bagian berikut:

| AI Usage Log — Rencana Bagian yang AKAN dibantu AI: Pembuatan docstring dan komentar kode (dokumentasi teknis) Saran perbaikan algoritma setelah konsep awal selesai ditulis sendiri Pengecekan logika edge case (stok habis, input negatif, dll.) Template format struk digital agar terlihat profesional Bagian yang TIDAK dibantu AI (dikerjakan mandiri): Penulisan kode inti (core logic) seluruh fitur Desain struktur data dan pemilihan algoritma Sesi testing & debugging Presentasi dan penjelasan lisan |
| :---- |

# **8\. Timeline Proyek**

| Minggu | Tanggal | Fase | Deliverable |
| :---- | :---- | :---- | :---- |
| Minggu 9 | 20 Juni 2026 | **Proposal** | Problem statement, fitur, & rencana struktur data |
| Minggu 10-11 | 27 Juni 2026 | **Implementasi** | Pengembangan kode inti (Core Features) |
| Minggu 12 | 04 Juli 2026 | **Progress** | Demo kemajuan & feedback awal |
| Minggu 13-14 | 11 Juli 2026 | **Finalisasi** | Penyempurnaan kode, testing, & dokumentasi |
| Minggu 15 | 18 Juli 2026 | **Presentasi** | Demo final & pengumpulan berkas |

# **9\. Requirements Analysis**

## **9.1 Functional Requirements (FR)**

Sistem harus mampu melakukan hal-hal berikut:

* FR-01: Menampilkan daftar seluruh produk beserta harga dan stok tersisa.

* FR-02: Menerima input kode produk dan kuantitas dari operator kasir.

* FR-03: Memvalidasi ketersediaan stok sebelum menambahkan item ke keranjang.

* FR-04: Menghitung total harga seluruh item dalam keranjang secara otomatis.

* FR-05: Menerima input uang pembayaran dan menghitung kembalian.

* FR-06: Mencetak struk transaksi ke terminal dengan format yang terstandarisasi.

* FR-07: Memperbarui stok secara otomatis setelah transaksi selesai.

* FR-08: Menyimpan dan menampilkan riwayat transaksi dalam satu sesi.

## **9.2 Non-Functional Requirements (NFR)**

Sistem harus memenuhi standar kualitas berikut:

* NFR-01 Usability: Antarmuka berbasis teks (CLI) intuitif dengan menu bernomor.

* NFR-02 Reliability: Aplikasi tidak boleh crash akibat input pengguna yang tidak valid.

* NFR-03 Portability: Dapat dijalankan di Python 3.x tanpa instalasi library pihak ketiga.

* NFR-04 Maintainability: Kode diorganisir dalam fungsi-fungsi terpisah dengan docstring lengkap.

* NFR-05 Performance: Respons setiap operasi \< 1 detik untuk dataset produk \< 100 item.

Jakarta, 20 Juni 2026

| Mahasiswa 1 Randy Ramadhan | Mahasiswa 2 Wulan Purnamasari  |
| :---: | :---: |

| Mahasiswa 3 Billy Syahputra | Mahasiswa 4 Ibrahim Hadi   |
| :---: | :---: |

