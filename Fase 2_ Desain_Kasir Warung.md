

| DOKUMEN DESAIN SISTEM Fase 2 Aplikasi Kasir Warung | Universitas Al Azhar Indonesia  |
| :---- | ----: |

# **1\. Top-Down Design — Dekomposisi Modular**

Prinsip Top-Down Design memecah program dari fungsi paling abstrak (main) ke fungsi konkret. Setiap fungsi memiliki satu tanggung jawab jelas, dapat diuji secara mandiri, dan dapat digunakan ulang di bagian program yang berbeda.

## **1.1 Hierarki Fungsi (Function Hierarchy)**

| LAYER 0 — Main Program main() |
| :---- |
| **LAYER 1 — Menu & Controller** menu\_utama()    •  menu\_kasir()    •  menu\_stok()    •  menu\_laporan() |
| **LAYER 2 — Core Business Logic** tambah\_item\_ke\_keranjang()    •  hapus\_item\_keranjang()    •  hitung\_total()    •  proses\_pembayaran()    •  update\_stok()    •  cari\_produk() |
| **LAYER 3 — Utility & I/O** cetak\_struk()    •  tampilkan\_menu\_produk()    •  simpan\_riwayat()    •  tampilkan\_riwayat()    •  validasi\_input\_angka()    •  format\_rupiah() |

## **1.2 Deskripsi Fungsi per Layer**

**Layer 0 — Entry Point**

**main()**

Fungsi titik masuk program. Menginisialisasi data produk default, memanggil loop menu utama, dan menangani KeyboardInterrupt (Ctrl+C) untuk keluar dengan bersih.

**Layer 1 — Controller Functions**

* menu\_utama()  Menampilkan menu level pertama: Kasir, Manajemen Stok, Laporan, Keluar. Loop hingga user memilih keluar.

* menu\_kasir()  Mengelola alur transaksi: mulai keranjang baru, tambah item, hitung total, proses bayar, cetak struk.

* menu\_stok()  Sub-menu untuk tambah produk baru, update harga, update stok.

* menu\_laporan()  Tampilkan riwayat transaksi dan total pendapatan sesi.

**Layer 2 — Core Business Logic**

* tambah\_item\_ke\_keranjang(kode, qty, menu, keranjang)  Cari produk by kode, validasi stok, tambah/update item di keranjang.

* hapus\_item\_keranjang(kode, keranjang)  Hapus item dari list keranjang berdasarkan kode produk.

* hitung\_total(keranjang)  Iterasi seluruh item, jumlahkan field subtotal, return nilai total.

* proses\_pembayaran(total, uang\_masuk) Validasi uang \>= total, hitung kembalian, return tuple (sukses, kembalian).

* update\_stok(kode, qty\_terjual, menu)  Kurangi stok produk di dictionary menu setelah transaksi konfirmasi.

* cari\_produk(keyword, menu)  Linear search nama/kode produk, return list hasil yang cocok.

**Layer 3 — Utility & I/O Functions**

* cetak\_struk(keranjang, total, kembalian, id\_trx) — Format dan print struk ke stdout.

* tampilkan\_menu\_produk(menu) — Print tabel daftar produk, harga, stok.

* simpan\_riwayat(trx, riwayat) — Append dict transaksi ke list riwayat.

* tampilkan\_riwayat(riwayat) — Print ringkasan semua transaksi sesi.

* validasi\_input\_angka(prompt, min\_val, max\_val) — Input loop dengan try-except, pastikan angka valid dalam range.

* format\_rupiah(angka) — Format integer ke string 'Rp 10.000'.

# **2\. Pemilihan Struktur Data**

Setiap variabel data dirancang dengan pertimbangan operasi dominan yang akan dilakukan: akses cepat by key, urutan iterasi, atau append log.

| Variabel | Tipe | Contoh Nilai | Alasan | Peran |
| :---- | :---- | :---- | :---- | :---- |
| **menu\_produk** | Dict of Dict | {'P001':{'nama':...,'harga':...,'stok':...}} | Akses O(1) by kode | Data produk master |
| **keranjang** | List of Dict | \[{'kode':...,'nama':...,'qty':...,'subtotal':...}\] | Urutan terjaga | Item belanja aktif |
| **riwayat\_transaksi** | List of Dict | \[{'id':...,'waktu':...,'total':...,'items':\[...\]}\] | Append-only log | Log transaksi sesi |
| **counter\_id** | Integer | int \= 1  → '"TRX-001" | Simple increment | ID transaksi unik |

## **2.1 Justifikasi Pemilihan**

* Dictionary untuk menu\_produk: Akses produk berdasarkan kode sering terjadi setiap kali user input kode. Dict memberikan O(1) vs O(n) jika menggunakan list.

* List of Dict untuk keranjang: Urutan item penting untuk tampilan struk. List mempertahankan urutan insert, mudah diiterasi saat cetak.

* List of Dict untuk riwayat: Append-only pattern cocok untuk log. Tidak perlu pencarian cepat — cukup tampilkan urutan kronologis.

* Integer counter\_id: Sederhana dan deterministik. Format string 'TRX-001' dihasilkan dari f-string: f'TRX-{counter\_id:03d}'.

# **3\. Desain Algoritma & Pseudocode**

## **3.1 Algoritma Tambah Item ke Keranjang**

| Pseudocode: tambah\_item\_ke\_keranjang(kode, qty, menu, keranjang) FUNCTION tambah\_item\_ke\_keranjang(kode, qty, menu, keranjang):   IF kode NOT IN menu:               // O(1) dict lookup     RETURN error('Kode produk tidak ditemukan')   produk ← menu\[kode\]   IF produk\['stok'\] \< qty:           // validasi stok     RETURN error('Stok tidak mencukupi: ' \+ produk\['stok'\])   // Linear search: apakah kode sudah ada di keranjang?   found ← False   FOR item IN keranjang:             // O(n) search     IF item\['kode'\] \== kode:       item\['qty'\]      ← item\['qty'\] \+ qty       item\['subtotal'\] ← item\['qty'\] \* produk\['harga'\]       found ← True       BREAK   IF NOT found:                      // item baru → append     keranjang.append({       'kode'    : kode,       'nama'    : produk\['nama'\],       'harga'   : produk\['harga'\],       'qty'     : qty,       'subtotal': produk\['harga'\] \* qty     })   RETURN sukses |
| :---- |

## **3.2 Algoritma Hitung Total & Proses Pembayaran**

| Pseudocode: hitung\_total() \+ proses\_pembayaran() FUNCTION hitung\_total(keranjang):   total ← 0   FOR item IN keranjang:             // O(n) akumulasi     total ← total \+ item\['subtotal'\]   RETURN total FUNCTION proses\_pembayaran(total, uang\_masuk):   IF uang\_masuk \< total:             // validasi     RETURN (False, 0, 'Uang kurang')   kembalian ← uang\_masuk \- total   RETURN (True, kembalian, 'OK') |
| :---- |

## **3.3 Algoritma Cetak Struk Digital**

| Pseudocode: cetak\_struk(keranjang, total, kembalian, id\_trx) FUNCTION cetak\_struk(keranjang, total, kembalian, id\_trx):   LEBAR ← 40  // karakter   PRINT '=' \* LEBAR   PRINT 'KASIR WARUNG'.center(LEBAR)   PRINT f'No: {id\_trx}  {datetime.now()}'.center(LEBAR)   PRINT '-' \* LEBAR   FOR item IN keranjang:             // O(n) iterasi     nama\_col  ← item\['nama'\].ljust(20)     qty\_col   ← str(item\['qty'\]).center(4)     harga\_col ← format\_rupiah(item\['subtotal'\]).rjust(12)     PRINT nama\_col \+ qty\_col \+ harga\_col   PRINT '-' \* LEBAR   PRINT 'TOTAL'.ljust(24) \+ format\_rupiah(total).rjust(16)   PRINT 'BAYAR'.ljust(24) \+ format\_rupiah(kembalian+total).rjust(16)   PRINT 'KEMBALI'.ljust(24) \+ format\_rupiah(kembalian).rjust(16)   PRINT '=' \* LEBAR   PRINT 'Terima kasih\!'.center(LEBAR) |
| :---- |

## **3.4 Algoritma Validasi Input**

| Pseudocode: validasi\_input\_angka(prompt, min\_val, max\_val) FUNCTION validasi\_input\_angka(prompt, min\_val=0, max\_val=None):   WHILE True:                        // loop sampai input valid     TRY:       nilai ← int(INPUT(prompt))     // bisa raise ValueError       IF nilai \< min\_val:         PRINT f'Nilai minimal: {min\_val}'         CONTINUE       IF max\_val IS NOT None AND nilai \> max\_val:         PRINT f'Nilai maksimal: {max\_val}'         CONTINUE       RETURN nilai                   // input valid → return     EXCEPT ValueError:       PRINT 'Input harus berupa angka\!'                                      // loop kembali ke WHILE |
| :---- |

# **4\. Ringkasan Algoritma & Kompleksitas**

| Algoritma | Fungsi | Deskripsi | Kompleksitas |
| :---- | :---- | :---- | :---- |
| **Linear Search** | cari\_produk() | Cari item di keranjang sebelum menambah qty | O(n) — n=item keranjang |
| **Akumulasi Sum** | hitung\_total() | Loop seluruh keranjang, jumlahkan subtotal | O(n) — n=item keranjang |
| **String Formatting** | cetak\_struk() | Format teks berkolom menggunakan ljust/rjust | O(n) — n=item di struk |
| **Append Log** | simpan\_riwayat() | Tambah dict transaksi ke list riwayat | O(1) amortized |
| **Input Validation** | validasi\_input\_angka() | try-except \+ conditional untuk setiap input user | O(1) per input |
| **Dict Lookup** | update\_stok() | Kurangi stok langsung via key kode produk | O(1) hash lookup |

# **5\. Desain User Interface (Console-Based)**

Antarmuka dirancang berbasis teks (CLI) menggunakan karakter ASCII. Setiap layar memiliki struktur: header, konten, dan menu pilihan bernomor. Prinsip: minimalis, informatif, dan tidak crash akibat input salah.

## **5.1 Layar Menu Utama**

| Tampilan: menu\_utama() \========================================        KASIR WARUNG — v1.0               \========================================  Selamat datang, Operator\!               \----------------------------------------  \[1\] Proses Transaksi (Kasir)             \[2\] Manajemen Stok Produk                \[3\] Laporan Transaksi Hari Ini           \[4\] Keluar Program                      \----------------------------------------  Pilihan Anda \[1-4\]: \_                   |
| :---- |

## **5.2 Layar Kasir — Transaksi Aktif**

| Tampilan: menu\_kasir() saat keranjang terisi \========================================      TRANSAKSI BARU — \#TRX-003           \========================================  DAFTAR PRODUK TERSEDIA:                   Kode  Nama                Harga  Stok    P001  Indomie Goreng    Rp3.500    48     P002  Aqua 600ml        Rp4.000    29     P003  Chitato 68g       Rp8.500    15   \----------------------------------------  KERANJANG BELANJA:                        Indomie Goreng   x2      Rp  7.000       Aqua 600ml       x1      Rp  4.000       ─────────────────────────────────────     TOTAL                    Rp 11.000     \----------------------------------------  \[1\] Tambah Item    \[3\] Hapus Item         \[2\] Proses Bayar   \[4\] Batal Transaksi    Pilihan \[1-4\]: \_                         |
| :---- |

## **5.3 Layar Struk Digital**

| Output: cetak\_struk() \========================================            KASIR WARUNG                      Jl. Contoh No.1, Jakarta Selatan     \========================================  No      : TRX-003                        Tanggal : 27-06-2026  10:45:23          \----------------------------------------  Item               Qty        Subtotal   \----------------------------------------  Indomie Goreng       2         Rp 7.000   Aqua 600ml           1         Rp 4.000  \----------------------------------------  TOTAL                          Rp11.000   BAYAR                          Rp20.000   KEMBALI                         Rp9.000  \========================================      Terima kasih sudah berbelanja\!           Barang yang dibeli tidak dapat                    dikembalikan.                  \======================================== |
| :---- |

## **5.4 Layar Manajemen Stok**

| Tampilan: menu\_stok() \========================================       MANAJEMEN STOK PRODUK              \========================================  PRODUK SAAT INI:                          Kode  Nama                Harga  Stok    P001  Indomie Goreng    Rp3.500    48     P002  Aqua 600ml        Rp4.000    29     P003  Chitato 68g       Rp8.500    15   \----------------------------------------  \[1\] Tambah Produk Baru                   \[2\] Update Harga Produk                  \[3\] Update Jumlah Stok                   \[4\] Kembali ke Menu Utama                Pilihan \[1-4\]: \_                        |
| :---- |

## **5.5 Layar Laporan Transaksi**

| Tampilan: menu\_laporan() \========================================     LAPORAN TRANSAKSI — SESI INI         \========================================   No.  ID       Waktu      Total         \----------------------------------------    1   TRX-001  10:30:12   Rp  8.500        2   TRX-002  10:38:47   Rp 15.000        3   TRX-003  10:45:23   Rp 11.000     \----------------------------------------   Jumlah Transaksi : 3                     Total Pendapatan : Rp 34.500           \========================================  \[ENTER\] Kembali ke Menu Utama           |
| :---- |

# **6\. Alur Program Utama (Flowchart Tekstual)**

Alur program menggambarkan urutan eksekusi dari awal hingga akhir sesi, mencakup seluruh cabang keputusan utama.

| Alur Program — Top Level START   │   ├─── Inisialisasi menu\_produk (dict default)   ├─── Inisialisasi riwayat\_transaksi \= \[\]   ├─── counter\_id \= 1   │   └─▶ LOOP menu\_utama()          │          ├── \[1\] Kasir ──▶ menu\_kasir()          │      │          │      ├── tambah\_item\_ke\_keranjang()          │      ├── hitung\_total()          │      ├── proses\_pembayaran()          │      ├── update\_stok()          │      ├── cetak\_struk()          │      └── simpan\_riwayat()          │          ├── \[2\] Stok ───▶ menu\_stok()          │      ├── tambah produk baru ke menu          │      └── update harga / stok          │          ├── \[3\] Laporan ▶ menu\_laporan()          │      └── tampilkan\_riwayat()          │          └── \[4\] Keluar                 │                END |
| :---- |

