from Garage import Garage
from Car import Car
from Motorcycle import Motorcycle

# Membuat objek Garage
garasi = Garage(50, 10, "Garasi A", 100)

# Membuat objek Motorcycle
motorcycle1 = Motorcycle("M 1234 AB", "Honda", 2022, "Hitam", "Sport", 150)
motorcycle2 = Motorcycle("M 5678 CD", "Yamaha", 2023, "Biru", "Adventure", 200)

# Membuat objek Car
car1 = Car("B 1234 CD", "Toyota", 2022, "Merah", 5, 4)
car2 = Car("B 5678 EF", "Honda", 2023, "Putih", 4, 2)

# Menambahkan objek Motorcycle dan Car ke dalam garasi
garasi.add_motorcycle(motorcycle1)
garasi.add_motorcycle(motorcycle2)
garasi.add_car(car1)
garasi.add_car(car2)

# Menampilkan informasi tentang garasi
print("Garage Information:")
print("Nama Garasi:", garasi.get_nama_garasi())
print("Luas Garasi:", garasi.get_luas_garasi())
print("Kapasitas:", garasi.get_kapasitas())
print("Jumlah Kendaraan:", garasi.get_jumlah_kendaraan())
print()

# Menampilkan daftar Motorcycle dan Car di dalam garasi
garasi.display_motorcycles()
print()
garasi.display_cars()