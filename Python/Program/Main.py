# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

from Garage import Garage
from Car import Car
from Motorcycle import Motorcycle

# Membuat objek Garage
garasi = Garage(50, 4, "Garasi A", 35)
garasi2 = Garage(12, 3, "Garasi B", 20);

# Membuat objek Motorcycle
motorcycle1 = Motorcycle("M 1234 AB", "Honda", 2022, "Hitam", "Sport", 4)
motorcycle2 = Motorcycle("M 5678 CD", "Yamaha", 2023, "Biru", "Adventure", 5)
motorcycle3 = Motorcycle("D 9876 QWE", "Suzuki", 2023, "Kuning", "Matic", 9)
motorcycle4 = Motorcycle("D 5432 RTY", "Kawasaki", 2022, "Hijau", "Trail", 7)


# Membuat objek Car
car1 = Car("B 1234 CD", "Toyota", 2022, "Merah", 5, 4)
car2 = Car("B 5678 EF", "Honda", 2023, "Putih", 4, 6)
car3 = Car("Z 3456 GHI", "Nissan", 2022, "Biru", 4, 2)
car4 = Car("Z 6789 UIO", "Mitsubishi", 2023, "Silver", 4, 5)

# Menambahkan objek Motorcycle dan Car ke dalam garasi
garasi.add_motorcycle(motorcycle1)
garasi.add_motorcycle(motorcycle2)
garasi.add_car(car1)
garasi.add_car(car2)

garasi2.add_motorcycle(motorcycle3)
garasi2.add_motorcycle(motorcycle4)
garasi2.add_car(car3)
garasi2.add_car(car4)

# Menampilkan informasi tentang garasi pertama
print("Informasi Garasi ke-1")
print("---------------------")
print("Nama Garasi:", garasi.get_nama_garasi())
print("Luas Garasi:", garasi.get_luas_garasi())
print("Kapasitas:", garasi.get_kapasitas())
print("Jumlah Kendaraan:", garasi.get_jumlah_kendaraan())
print()

# Menampilkan daftar Motorcycle dan Car di dalam garasi
garasi.display_motorcycles()
print()
garasi.display_cars()

print()
print()
print("=====================")

# Menampilkan informasi tentang garasi pertama
print("Informasi Garasi ke-2")
print("---------------------")
print("Nama Garasi:", garasi2.get_nama_garasi())
print("Luas Garasi:", garasi2.get_luas_garasi())
print("Kapasitas:", garasi2.get_kapasitas())
print("Jumlah Kendaraan:", garasi2.get_jumlah_kendaraan())
print()

# Menampilkan daftar Motorcycle dan Car di dalam garasi
garasi2.display_motorcycles()
print()
garasi2.display_cars()