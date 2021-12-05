daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {"Hadeyal":"085883648213", "Nurfadilah":"085787653467"}

print("="*50)
print("   Nama          | Nomor Telepon ")
print("="*50)
print(" # Hadeyal       | ", kontak["Hadeyal"])
print(" # Nurfadilah    | ", kontak["Nurfadilah"])
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Kontak Hadeyal
print("Menampilkan kontak Hadeyal")
print("="*50)
print(" # Hadeyal       | ", kontak["Hadeyal"])
print("-"*50)
print()
print()
print("="*50)

# Menampikan Kontak Dengan Nama Aldi
print("Menambahkan kontak dengan Nama Aldi")
print("dengan nomor Telepon 085746372718")
kontak["Aldi"]="085746372718"
print("="*50)
print(" # Aldi          | ", kontak["Aldi"])
print("-"*50)
print()
print()
print("="*50)

# Mengubah Nomor Nurfadilah Dengan Nomor Baru
print("Mengubah Nomor Nurfadilah dengan Nomor 085781793926")
print("="*50)
print(" # Nurfadilah    | ", kontak["Nurfadilah"])
print("="*50)
print()
print()
print("="*50)

# Menampilkan Semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Semua Nomor
print("Menampilkan Semua Nomor dalam Kontak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Semua Daftar Kontak
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)

# Menghapus salah satu Kontak
print("Hapus Kontak Aldi")
print("="*50)
kontak.pop("Aldi")
print(kontak.items())
print("-"*50)
print()
print()
