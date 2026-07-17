"""
test_fase4.py — Fase 4: Testing
Aplikasi Kasir Warung v1.0.1
Randy Ramadhan & Wulan Purnamasari
Universitas Al Azhar Indonesia — 04 Juli 2026
"""
import importlib
import kasir_warung as k
importlib.reload(k)

# ─── Test Runner ────────────────────────────────────────────────
class TestRunner:
    def __init__(self):
        self.results = []
        self.passed = self.failed = 0

    def run(self, no, nama, input_desc, expected, kondisi, actual=""):
        if kondisi:
            self.passed += 1
            actual = actual or expected
            status = "PASS ✓"
        else:
            self.failed += 1
            status = "FAIL ✗"
        self.results.append({"no":no,"nama":nama,"input":input_desc,
                              "expected":expected,"actual":actual,"status":status})
        icon = "  ✓" if kondisi else "  ✗"
        print(f"{icon}  [{no}] {nama}")
        if not kondisi:
            print(f"       Expected : {expected}")
            print(f"       Actual   : {actual}")

    def section(self, title):
        print(f"\n{'─'*60}\n  {title}\n{'─'*60}")

    def report(self):
        total = self.passed + self.failed
        pct   = int(self.passed/total*100) if total else 0
        print("\n" + "="*60)
        print("  RINGKASAN FASE 4 — TEST PLAN")
        print("="*60)
        print(f"  Total  : {total}")
        print(f"  Lulus  : {self.passed} ({pct}%)")
        print(f"  Gagal  : {self.failed}")
        print("="*60)
        if self.failed == 0:
            print("  STATUS : ✓ SEMUA TEST LULUS 🎉")
        else:
            print(f"  STATUS : ✗ {self.failed} GAGAL")
        print("="*60)
        return self.results

tr = TestRunner()

# ════════════════════════════
# BAGIAN 1 — TEST PLAN NORMAL
# ════════════════════════════

tr.section("BAGIAN 1A — Bab 6: format_rupiah()")
cases = [("TC-001","Nilai ribuan",10000,"Rp 10.000"),("TC-002","Nilai ratusan",3500,"Rp 3.500"),
         ("TC-003","Nilai nol",0,"Rp 0"),("TC-004","Nilai jutaan",1500000,"Rp 1.500.000"),
         ("TC-005","Nilai puluhan ribu",75000,"Rp 75.000")]
for no,nm,angka,exp in cases:
    act=k.format_rupiah(angka); tr.run(no,nm,f"angka={angka}",exp,act==exp,act)

tr.section("BAGIAN 1B — Bab 8: init_menu_default() & Dictionary")
menu=k.init_menu_default()
tr.run("TC-006","Jumlah produk = 8","init_menu_default()","8",len(menu)==8,str(len(menu)))
tr.run("TC-007","P001 ada di menu","menu_produk","True","P001" in menu)
tr.run("TC-008","P001 harga=3500","menu['P001']['harga']","3500",menu["P001"]["harga"]==3500,str(menu["P001"]["harga"]))
tr.run("TC-009","P001 stok=50","menu['P001']['stok']","50",menu["P001"]["stok"]==50,str(menu["P001"]["stok"]))
ks=k.get_kode_unik(menu)
tr.run("TC-010","get_kode_unik → set 8 elemen","get_kode_unik(menu)","set, len=8",isinstance(ks,set) and len(ks)==8,str(len(ks)))

tr.section("BAGIAN 1C — Bab 7+9: tambah_item_ke_keranjang()")
menu=k.init_menu_default(); krnj=[]
ok,_=k.tambah_item_ke_keranjang("P001",2,menu,krnj)
tr.run("TC-011","Tambah item baru sukses","P001,qty=2","sukses=True,len=1",ok and len(krnj)==1,f"ok={ok},len={len(krnj)}")
tr.run("TC-012","Subtotal 3500×2=7000","krnj[0]","7000",krnj[0]["subtotal"]==7000,str(krnj[0]["subtotal"]))
ok,_=k.tambah_item_ke_keranjang("P001",3,menu,krnj)
tr.run("TC-013","Update qty duplikat (2+3=5)","P001 lagi qty=3","qty=5,len=1",ok and krnj[0]["qty"]==5 and len(krnj)==1,f"qty={krnj[0]['qty']}")
tr.run("TC-014","Subtotal terupdate 3500×5=17500","krnj[0]","17500",krnj[0]["subtotal"]==17500,str(krnj[0]["subtotal"]))
ok2,_=k.tambah_item_ke_keranjang("P002",1,menu,krnj)
tr.run("TC-015","Tambah item kedua (P002)","P002,qty=1","len=2",ok2 and len(krnj)==2,f"len={len(krnj)}")

tr.section("BAGIAN 1D — Bab 4+7: hitung_total()")
kj=[{"kode":"P001","nama":"A","harga":3500,"qty":2,"subtotal":7000},
    {"kode":"P002","nama":"B","harga":4000,"qty":1,"subtotal":4000},
    {"kode":"P003","nama":"C","harga":8500,"qty":1,"subtotal":8500}]
tr.run("TC-016","Total 3 item (7000+4000+8500=19500)","keranjang 3 item","19500",k.hitung_total(kj)==19500,str(k.hitung_total(kj)))
tr.run("TC-017","Total keranjang kosong=0","keranjang=[]","0",k.hitung_total([])==0)

tr.section("BAGIAN 1E — Bab 11: hitung_total_rekursif()")
tr.run("TC-018","Rekursif == iteratif (19500)","hitung_total_rekursif(kj)","19500",k.hitung_total_rekursif(kj)==19500,str(k.hitung_total_rekursif(kj)))
tr.run("TC-019","Rekursif kosong=0","[]","0",k.hitung_total_rekursif([])==0)
tr.run("TC-020","Rekursif 1 item=5000","[{subtotal:5000}]","5000",k.hitung_total_rekursif([{"subtotal":5000}])==5000)

tr.section("BAGIAN 1F — Bab 2+3: proses_pembayaran()")
ok,kb,_=k.proses_pembayaran(19500,20000)
tr.run("TC-021","Bayar lebih (20000>19500)","total=19500,uang=20000","sukses,kembalian=500",ok and kb==500,f"ok={ok},kb={kb}")
ok,kb,_=k.proses_pembayaran(19500,19500)
tr.run("TC-022","Bayar pas (uang==total)","total=19500,uang=19500","sukses,kembalian=0",ok and kb==0,f"ok={ok},kb={kb}")
ok,kb,_=k.proses_pembayaran(19500,10000)
tr.run("TC-023","Bayar kurang (10000<19500)","total=19500,uang=10000","gagal",not ok and kb==0,f"ok={ok},kb={kb}")
ok,kb,_=k.proses_pembayaran(0,0)
tr.run("TC-024","Bayar 0 total 0","total=0,uang=0","sukses,kembalian=0",ok and kb==0)

tr.section("BAGIAN 1G — Bab 9: Searching")
menu=k.init_menu_default()
h=k.cari_produk_linear("indomie",menu)
tr.run("TC-025","Linear search nama partial","keyword='indomie'","1 hasil P001",len(h)==1 and h[0][0]=="P001",f"len={len(h)}")
h2=k.cari_produk_linear("P003",menu)
tr.run("TC-026","Linear search kode persis","keyword='P003'","1 hasil P003",len(h2)==1 and h2[0][0]=="P003")
h3=k.cari_produk_linear("kopi",menu)
tr.run("TC-027","Linear partial → Kopi ABC Susu","keyword='kopi'","1 hasil",len(h3)==1)
h4=k.cari_produk_linear("XZYZQQ",menu)
tr.run("TC-028","Linear tidak ditemukan","keyword='XZYZQQ'","0 hasil",len(h4)==0)
terurut=sorted(menu.items(),key=lambda x:x[0])
idx=k.cari_produk_binary("P004",terurut)
tr.run("TC-029","Binary search P004 ditemukan","kode='P004'","idx!=-1",idx!=-1 and terurut[idx][0]=="P004",f"idx={idx}")
tr.run("TC-030","Binary search P001 → idx=0","kode='P001'","0",k.cari_produk_binary("P001",terurut)==0)
tr.run("TC-031","Binary search P008 → idx=7","kode='P008'","7",k.cari_produk_binary("P008",terurut)==7)
tr.run("TC-032","Binary tidak ditemukan → -1","kode='ZZZZ'","-1",k.cari_produk_binary("ZZZZ",terurut)==-1)

tr.section("BAGIAN 1H — Bab 10: Sorting")
daftar=list(menu.items())
hbs=k.bubble_sort_produk(daftar,"harga",True)
hl=[p["harga"] for _,p in hbs]
tr.run("TC-033","Bubble sort harga ascending","daftar,harga,True","terurut naik",hl==sorted(hl),str(hl[:3]))
hbd=k.bubble_sort_produk(daftar,"harga",False)
hld=[p["harga"] for _,p in hbd]
tr.run("TC-034","Bubble sort harga descending","daftar,harga,False","terurut turun",hld==sorted(hld,reverse=True))
hbi=k.sort_produk_builtin(menu,"harga",True)
hbil=[p["harga"] for _,p in hbi]
tr.run("TC-035","Timsort harga ascending","harga,True","terurut naik",hbil==sorted(hbil))
hbn=k.sort_produk_builtin(menu,"nama",True)
nl=[p["nama"] for _,p in hbn]
tr.run("TC-036","Timsort nama A-Z","nama,True","terurut A-Z",nl==sorted(nl))
tr.run("TC-037","Bubble & Timsort urutan sama","harga asc","identical",[k_ for k_,_ in hbs]==[k_ for k_,_ in hbi])

tr.section("BAGIAN 1I — Bab 7: hapus & simpan")
kj2=[{"kode":"P003","nama":"Chitato","harga":8500,"qty":1,"subtotal":8500}]
ok,_=k.hapus_item_keranjang("P003",kj2)
tr.run("TC-038","Hapus item → sukses, kosong","kode='P003'","sukses,len=0",ok and len(kj2)==0,f"ok={ok},len={len(kj2)}")
rv=[]
k.simpan_riwayat("TRX-042",kj,19500,rv)
tr.run("TC-039","simpan_riwayat 1 record","id='TRX-042'","len=1",len(rv)==1 and rv[0]["id"]=="TRX-042")
tr.run("TC-040","Record total=19500","riwayat[0]['total']","19500",rv[0]["total"]==19500,str(rv[0]["total"]))

# ════════════════════════════
# BAGIAN 2 — EDGE CASES
# ════════════════════════════

tr.section("BAGIAN 2A — Edge Cases: Batas Stok")
menu=k.init_menu_default(); stok_p001=menu["P001"]["stok"]; krnj_e=[]
ok,_=k.tambah_item_ke_keranjang("P001",stok_p001,menu,krnj_e)
tr.run("TC-041","Tambah qty = stok (batas atas)",f"qty={stok_p001}","sukses",ok,f"ok={ok}")
ok2,msg2=k.tambah_item_ke_keranjang("P001",1,menu,krnj_e)
tr.run("TC-042","Tambah 1 lagi melebihi stok","qty+1 > stok","gagal",not ok2,f"ok={ok2}")
ok3,_=k.tambah_item_ke_keranjang("P001",0,menu,[])
tr.run("TC-043","qty=0 → gagal","qty=0","sukses=False",not ok3)
ok4,_=k.tambah_item_ke_keranjang("P001",-5,menu,[])
tr.run("TC-044","qty negatif → gagal","qty=-5","sukses=False",not ok4)
ok5,_=k.tambah_item_ke_keranjang("p001",1,menu,[])
tr.run("TC-045","Kode lowercase 'p001' tidak ditemukan","kode='p001'","sukses=False",not ok5)

tr.section("BAGIAN 2B — Edge Cases: Search & Sort")
tr.run("TC-046","Binary search list kosong → -1","[]","-1",k.cari_produk_binary("P001",[])==-1)
menu=k.init_menu_default()
h0=k.cari_produk_linear("",menu)
tr.run("TC-047","Linear keyword kosong → [] (FIX v1.0.1)","keyword=''","0 hasil",len(h0)==0,f"len={len(h0)}")
hs=k.cari_produk_linear("   ",menu)
tr.run("TC-048","Linear keyword spasi → [] (strip)","keyword='   '","0 hasil",len(hs)==0)
try:
    ri=k.sort_produk_builtin(menu,"tidak_ada")
    tr.run("TC-049","Sort kunci invalid → fallback (FIX v1.0.1)","kunci='tidak_ada'","no KeyError",len(ri)==len(menu))
except KeyError:
    tr.run("TC-049","Sort kunci invalid → fallback (FIX v1.0.1)","kunci='tidak_ada'","no KeyError",False,"KeyError!")
try:
    gk=[{"kode":"GHOST","nama":"X","harga":0,"qty":1,"subtotal":0}]
    k.update_stok(gk,k.init_menu_default())
    tr.run("TC-050","update_stok kode ghost → skip (FIX v1.0.1)","kode='GHOST'","no KeyError",True)
except KeyError:
    tr.run("TC-050","update_stok kode ghost → skip (FIX v1.0.1)","kode='GHOST'","no KeyError",False,"KeyError!")

tr.section("BAGIAN 2C — Edge Cases: Rekursi")
tr.run("TC-051","Rekursi 1 item=99999","[{subtotal:99999}]","99999",k.hitung_total_rekursif([{"subtotal":99999}])==99999)
kb200=[{"subtotal":100}]*200
tr.run("TC-052","Rekursi 200 item (depth aman)","200×100","20000",k.hitung_total_rekursif(kb200)==20000)
rv2=[]
for i in range(5): k.simpan_riwayat(f"TRX-{i+1:03d}",kj,19500,rv2)
tl=k.tampilkan_laporan_rekursif(rv2)
tr.run("TC-053","Laporan rekursif 5×19500=97500","5 trx","97500",tl==97500,str(tl))

tr.section("BAGIAN 2D — Edge Cases: Dict Mutation & Misc")
mu=k.init_menu_default(); s_p002=mu["P002"]["stok"]
ku=[{"kode":"P002","nama":"Aqua","harga":4000,"qty":3,"subtotal":12000},
    {"kode":"P004","nama":"Teh","harga":5000,"qty":5,"subtotal":25000}]
k.update_stok(ku,mu)
tr.run("TC-054","Stok P002 berkurang 3","P002 qty=3",f"{s_p002-3}",mu["P002"]["stok"]==s_p002-3,str(mu["P002"]["stok"]))
tr.run("TC-055","Stok P004 berkurang 5","P004 qty=5","35",mu["P004"]["stok"]==35,str(mu["P004"]["stok"]))
ok_h,_=k.hapus_item_keranjang("XXXX",kj)
tr.run("TC-056","Hapus kode tidak ada → gagal","kode='XXXX'","False",not ok_h)
ok_h2,_=k.hapus_item_keranjang("P001",[])
tr.run("TC-057","Hapus dari keranjang kosong → gagal","keranjang=[]","False",not ok_h2)
try:
    neg=k.format_rupiah(-5000)
    tr.run("TC-058","format_rupiah negatif tidak crash","angka=-5000","tidak raise",True,f"hasil='{neg}'")
except Exception as e:
    tr.run("TC-058","format_rupiah negatif tidak crash","angka=-5000","tidak raise",False,str(e))

# ════════════════════════════
# BAGIAN 3 — DEBUGGING LOG
# ════════════════════════════

print("\n" + "="*60)
print("  BAGIAN 3 — DEBUGGING LOG (Identifikasi & Fix)")
print("="*60)
bugs=[
    {"id":"BUG-001","fungsi":"update_stok()","baris":"~560",
     "masalah":"KeyError saat keranjang berisi kode tidak di menu",
     "reproduce":"update_stok([{'kode':'GHOST'}], menu) → KeyError",
     "fix":"Guard: if kode not in menu_produk: continue",
     "verify":"TC-050 PASS + 48 regression PASS","status":"FIXED v1.0.1 ✓"},
    {"id":"BUG-002","fungsi":"sort_produk_builtin()","baris":"~590",
     "masalah":"KeyError jika kunci bukan 'harga'/'nama'/'stok'",
     "reproduce":"sort_produk_builtin(menu,'tidak_ada') → KeyError",
     "fix":"KUNCI_VALID set + fallback ke 'nama'",
     "verify":"TC-049 PASS + 48 regression PASS","status":"FIXED v1.0.1 ✓"},
    {"id":"BUG-003","fungsi":"cari_produk_linear()","baris":"~440",
     "masalah":"Keyword kosong '' mengembalikan semua produk (karena '' in str selalu True)",
     "reproduce":"cari_produk_linear('',menu) → 8 hasil (harusnya 0)",
     "fix":"Guard: if not kw: return hasil",
     "verify":"TC-047 TC-048 PASS + 48 regression PASS","status":"FIXED v1.0.1 ✓"},
]
for b in bugs:
    print(f"\n  {b['id']} | {b['fungsi']} | baris {b['baris']}")
    print(f"  Masalah  : {b['masalah']}")
    print(f"  Reproduce: {b['reproduce']}")
    print(f"  Fix      : {b['fix']}")
    print(f"  Verify   : {b['verify']}")
    print(f"  Status   : {b['status']}")

# ════════════════════════════
# BAGIAN 4 — REGRESSION
# ════════════════════════════

tr.section("BAGIAN 4 — Regression (Fase 3 tidak rusak)")
menu=k.init_menu_default()
checks=[
    ("TC-R01","format_rupiah(10000)=='Rp 10.000'",k.format_rupiah(10000)=="Rp 10.000"),
    ("TC-R02","init_menu 8 produk",len(k.init_menu_default())==8),
    ("TC-R03","tambah item baru sukses",k.tambah_item_ke_keranjang("P001",1,k.init_menu_default(),[])[0]),
    ("TC-R04","hitung_total iteratif",k.hitung_total([{"subtotal":5000},{"subtotal":3000}])==8000),
    ("TC-R05","hitung_total rekursif==iter",k.hitung_total_rekursif([{"subtotal":5000},{"subtotal":3000}])==8000),
    ("TC-R06","proses_pembayaran sukses",k.proses_pembayaran(10000,15000)[0]),
    ("TC-R07","binary search found",k.cari_produk_binary("P003",sorted(menu.items(),key=lambda x:x[0]))!=-1),
    ("TC-R08","bubble sort ascending",(lambda h:h==sorted(h))([p["harga"] for _,p in k.bubble_sort_produk(list(menu.items()),"harga",True)])),
    ("TC-R09","timsort ascending",(lambda r:[p["harga"] for _,p in r]==sorted([p["harga"] for _,p in r]))(k.sort_produk_builtin(menu,"harga",True))),
    ("TC-R10","get_kode_unik returns set",isinstance(k.get_kode_unik(menu),set)),
]
for no,nm,cond in checks:
    tr.run(no,nm,"regression","True",cond)

# ════════════════════════════
# LAPORAN AKHIR
# ════════════════════════════

results=tr.report()
print("\n  TABEL TEST PLAN RINGKAS:")
print(f"  {'No':<8} {'Test Case':<38} Status")
print("  "+"─"*56)
for r in results:
    ic="✓" if "PASS" in r["status"] else "✗"
    print(f"  {r['no']:<8} {r['nama'][:36]:<38} {ic}")
