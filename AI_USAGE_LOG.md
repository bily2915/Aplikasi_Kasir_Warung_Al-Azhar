# AI Usage Log — Proyek Akhir Algoritma & Pemrograman

## Identitas

| | |
|---|---|
| **Nama** | Randy Ramadhan, Wulan Purnamasari, Bily Nur Sepdiansyah, Ibrahim Hadi Wibisono |
| **NIM** | 0112525012, 0102525702, 0112525002, 0112525003 |
| **Proyek** | Aplikasi Kasir Warung — Sistem POS Berbasis Python |
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Tanggal mulai** | 20 Juni 2026 (Minggu 9 — Proposal) |
| **Tanggal selesai** | 20 Juli 2026 (Minggu 15 — Presentasi) |

---

## Ringkasan Penggunaan AI

| Item | Detail |
|------|--------|
| **AI yang digunakan** | Claude (Anthropic) |
| **Framework** | CRIDE — Context, Request, Iterate, Document, Evaluate |
| **Perkiraan % kode dari AI** | ~40% (docstring, template, review) |
| **Perkiraan % kode sendiri** | ~60% (logika bisnis, algoritma, struktur data, debug) |
| **Jumlah interaksi tercatat** | 8 interaksi |
| **Jenis bantuan** | Dokumentasi, review, debugging hint, format struk |

> **Prinsip utama**: Mahasiswa **menganalisis masalah sendiri terlebih dahulu** sebelum
> berkonsultasi dengan AI. AI **tidak pernah** menulis logika inti program.
> Setiap output AI **selalu direview dan dimodifikasi** sebelum digunakan.

---

## Detail Interaksi

---

### Interaksi 1 — Minggu 9 (Proposal & Analisis)

- **Prompt:**
  > "Bantu saya memahami perbedaan antara Dictionary dan List untuk menyimpan data produk kasir. Mana yang lebih efisien?"

- **Respons AI:**
  Penjelasan perbedaan O(1) lookup pada Dictionary vs O(n) pada List. AI menjelaskan bahwa untuk akses berdasarkan kode produk, Dictionary jauh lebih efisien karena menggunakan hash table.

- **Yang digunakan:**
  Konsep O(1) vs O(n) untuk memutuskan menggunakan `Dict of Dict` sebagai `menu_produk`.

- **Modifikasi:**
  Keputusan desain tetap diambil sendiri setelah memahami penjelasan. Struktur nested dict `{"P001": {"nama": ..., "harga": ..., "stok": ...}}` dirancang sendiri.

- **Pelajaran:**
  Dictionary lebih tepat untuk data yang diakses berdasarkan *key* unik. Pemahaman ini mendasari seluruh desain struktur data proyek.

---

### Interaksi 2 — Minggu 10 (Implementasi — Docstring)

- **Prompt:**
  > "Bantu buat template docstring yang bagus untuk fungsi `tambah_item_ke_keranjang()`. Saya sudah tulis kode-nya, tinggal dokumentasinya."

- **Respons AI:**
  Template docstring dengan format: deskripsi singkat, Bab yang relevan, parameter (Args), nilai kembalian (Returns), dan keterangan Big-O.

- **Yang digunakan:**
  Format template dipakai sebagai standar untuk semua 18 fungsi dalam program.

- **Modifikasi:**
  Setiap docstring diisi dengan konten yang spesifik (bukan hanya placeholder). Contoh nilai konkret dan edge case ditambahkan sendiri.

- **Pelajaran:**
  Docstring yang baik harus menyebutkan: apa yang dilakukan, parameter, return value, dan kompleksitas — semua dalam bahasa yang konsisten.

---

### Interaksi 3 — Minggu 10 (Implementasi — Debugging Format)

- **Prompt:**
  > "Kenapa `format_rupiah(10000)` menghasilkan `'Rp 10,000'` bukan `'Rp 10.000'`? Kode saya: `f'Rp {angka:,'}`"

- **Respons AI:**
  Penjelasan bahwa Python menggunakan koma (`,`) sebagai *thousands separator* secara default. Saran menggunakan `.replace(',', '.')` setelah f-string.

- **Yang digunakan:**
  Solusi `.replace(',', '.')` diimplementasikan secara mandiri setelah memahami penjelasannya.

- **Modifikasi:**
  Diimplementasikan sebagai: `f"Rp {angka:,}".replace(",", ".")` — ditulis sendiri.

- **Pelajaran:**
  Python f-string `:,` menggunakan separator bawaan sistem (koma). Untuk format Rupiah Indonesia harus di-replace manual. Ini contoh bahwa memahami *mengapa* lebih penting daripada sekadar copy solusi.

---

### Interaksi 4 — Minggu 11 (Implementasi — Review Binary Search)

- **Prompt:**
  > "Tolong review implementasi binary search saya ini. Sudah benar logikanya? Ada edge case yang terlewat?"
  > *(melampirkan kode `cari_produk_binary()`)*

- **Respons AI:**
  Konfirmasi logika sudah benar. AI menunjukkan bahwa edge case **list kosong** belum ter-handle — jika `daftar_terurut = []`, maka `len() - 1 = -1` dan kondisi `kiri <= kanan` langsung `False`, jadi tidak crash. Namun lebih baik ditambahkan guard eksplisit untuk kejelasan.

- **Yang digunakan:**
  Penambahan guard `if not daftar_terurut: return -1` di awal fungsi.

- **Modifikasi:**
  Guard ditambahkan sendiri. Juga ditambahkan komentar `# edge case: list kosong` agar alasan jelas saat dibaca orang lain.

- **Pelajaran:**
  Defensive programming: selalu pertimbangkan kondisi *empty input* pada fungsi pencarian. Review dari perspektif orang lain membantu menemukan edge case yang terlewat.

---

### Interaksi 5 — Minggu 12 (Progress — Tabel Big-O)

- **Prompt:**
  > "Bantu buat tabel markdown untuk dokumentasi Big-O semua fungsi utama program saya. Berikut daftar fungsinya: ..."

- **Respons AI:**
  Draft tabel markdown dengan kolom: Fungsi, Waktu, Ruang, Keterangan.

- **Yang digunakan:**
  Struktur tabel dipakai sebagai template.

- **Modifikasi:**
  Beberapa nilai Big-O dikoreksi setelah verifikasi manual. Contoh: `simpan_riwayat()` awalnya AI tulis O(1), dikoreksi ke O(n) karena ada `list(keranjang)` yang membuat shallow copy. Keterangan diperinci agar lebih informatif.

- **Pelajaran:**
  Nilai Big-O dari AI tidak selalu 100% tepat — harus diverifikasi dengan menelusuri setiap baris kode secara manual. AI adalah alat bantu, bukan sumber kebenaran mutlak.

---

### Interaksi 6 — Minggu 13 (Finalisasi — Bug Discovery)

- **Prompt:**
  > "Saya menemukan bug: `cari_produk_linear('', menu)` mengembalikan semua 8 produk, padahal harusnya tidak ada yang cocok. Mengapa ini terjadi?"

- **Respons AI:**
  Penjelasan: dalam Python, `'' in 'string apapun'` selalu bernilai `True` karena string kosong adalah substring dari string manapun. Saran: tambahkan guard `if not kw: return hasil` setelah strip.

- **Yang digunakan:**
  Guard `if not kw: return hasil` ditambahkan ke `cari_produk_linear()` sebagai **BUG-003 fix**.

- **Modifikasi:**
  Kode ditulis sendiri. Juga ditambahkan test case TC-047 dan TC-048 di `test_fase4.py` untuk memverifikasi fix.

- **Pelajaran:**
  `'' in any_string` selalu `True` di Python — perilaku Python yang non-intuitif. Selalu test dengan input kosong dan input spasi sebagai bagian dari edge case testing.

---

### Interaksi 7 — Minggu 13 (Finalisasi — Struk Format)

- **Prompt:**
  > "Bagaimana cara membuat tampilan struk kasir yang rapi di terminal dengan kolom yang rata? Nama produk di kiri, qty di tengah, harga di kanan?"

- **Respons AI:**
  Penjelasan metode `str.ljust(n)`, `str.rjust(n)`, dan `str.center(n)`. Contoh: `f"{nama.ljust(20)}{qty:>4}{harga:>12}"`.

- **Yang digunakan:**
  Teknik ljust/rjust diterapkan di fungsi `cetak_struk()` dan `tampilkan_menu_produk()`.

- **Modifikasi:**
  Lebar kolom (`20`, `4`, `12`) ditentukan sendiri berdasarkan eksperimen. Penambahan `[:22]` untuk truncate nama yang terlalu panjang — ide sendiri.

- **Pelajaran:**
  String alignment di Python sangat berguna untuk UI berbasis teks. Teknik ini juga berlaku untuk format laporan dan tabel data.

---

### Interaksi 8 — Minggu 14 (Dokumentasi — README)

- **Prompt:**
  > "Bantu saya membuat outline README yang profesional untuk proyek Python ini. Apa saja bagian yang sebaiknya ada?"

- **Respons AI:**
  Saran outline: Deskripsi, Fitur, Cara Menjalankan, Struktur File, Arsitektur, Struktur Data, Algoritma, Hasil Testing, Changelog, Identitas.

- **Yang digunakan:**
  Struktur outline sebagai panduan. Semua konten ditulis sendiri.

- **Modifikasi:**
  Ditambahkan bagian "Demo Akademik" dan tabel "Konsep yang Diintegrasikan" yang relevan untuk konteks tugas akhir kuliah — tidak ada di saran AI.

- **Pelajaran:**
  README yang baik harus menjawab pertanyaan: *apa*, *mengapa*, *bagaimana menjalankan*, dan *siapa pembuatnya*. Untuk konteks akademik, tambahkan juga pemetaan ke konsep yang dipelajari.

---

## Refleksi

### Apa yang Berhasil dengan Framework CRIDE

**C — Context (Konteks yang jelas)**: Setiap kali bertanya ke AI, selalu disertakan kode yang sudah ditulis sendiri dan deskripsi masalah spesifik. Hasilnya: jawaban AI jauh lebih relevan dan tepat sasaran dibanding bertanya secara umum.

**R — Request (Permintaan spesifik)**: Tidak pernah meminta AI untuk "buatkan program kasir". Permintaan selalu spesifik: "review fungsi ini", "jelaskan mengapa ini terjadi", "bantu format docstring". Hasilnya: kontrol penuh pada logika program tetap di tangan mahasiswa.

**I — Iterate (Revisi bertahap)**: Jawaban AI jarang langsung dipakai mentah. Selalu ada proses baca → pahami → modifikasi. Contoh terbaik: tabel Big-O dari AI dikoreksi 3 nilai setelah verifikasi manual.

**D — Document (Dokumentasi)**: Setiap interaksi dicatat di log ini. Proses ini memaksa refleksi: "apa yang saya pelajari dari interaksi ini?" — lebih berharga daripada output AI-nya sendiri.

**E — Evaluate (Evaluasi kritis)**: AI pernah salah (nilai Big-O `simpan_riwayat`, saran edge case binary search yang sebenarnya sudah handled). Kemampuan mengevaluasi output AI sama pentingnya dengan kemampuan menggunakan AI.

### Batasan yang Ditetapkan Sendiri

- ❌ **Tidak** meminta AI menulis fungsi logika bisnis dari nol
- ❌ **Tidak** copy-paste kode AI tanpa memahaminya
- ❌ **Tidak** menggunakan AI untuk menjawab soal latihan atau quiz
- ✅ AI boleh menjelaskan konsep yang belum dipahami
- ✅ AI boleh mereview kode yang sudah ditulis
- ✅ AI boleh membantu format/dokumentasi

### Pelajaran Terpenting

> *"AI adalah seperti senior developer yang bisa ditanya kapan saja — tapi tanggung jawab kode tetap ada di tangan kita. Jika kita tidak bisa menjelaskan setiap baris kode kepada dosen, berarti kita belum benar-benar memahaminya."*

Penggunaan AI paling bermanfaat bukan saat kita tidak tahu cara mengerjakan sesuatu, melainkan saat kita **sudah punya draft** dan ingin perspektif tambahan. Urutan yang tepat: **Coba sendiri → Stuck → Tanya AI → Pahami → Modifikasi → Implementasi**.

---

*Dokumen ini merupakan bukti transparansi penggunaan AI sesuai kebijakan akademik.*
*Randy Ramadhan, Wulan Purnamasari, Bily Nur Sepdiansyah, Ibrahim Hadi Wibisono — Universitas Al Azhar Indonesia — 2026*
