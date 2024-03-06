from ParkingLot import ParkingLot
from Car import Car
from Motorcycle import Motorcycle

class Garage(ParkingLot):
    def __init__(self, kapasitas, jumlah_kendaraan, nama_garasi, luas_garasi):
        super().__init__(kapasitas, jumlah_kendaraan)
        self._nama_garasi = nama_garasi
        self._luas_garasi = luas_garasi
        self._motorcycles = []
        self._cars = []

    # Setter untuk atribut nama_garasi
    def set_nama_garasi(self, nama_garasi):
        self._nama_garasi = nama_garasi

    # Getter untuk atribut nama_garasi
    def get_nama_garasi(self):
        return self._nama_garasi

    # Setter untuk atribut luas_garasi
    def set_luas_garasi(self, luas_garasi):
        self._luas_garasi = luas_garasi

    # Getter untuk atribut luas_garasi
    def get_luas_garasi(self):
        return self._luas_garasi

    # Method untuk menambahkan objek Motorcycle ke dalam garasi
    def add_motorcycle(self, motorcycle):
        self._motorcycles.append(motorcycle)

    # Method untuk menambahkan objek Car ke dalam garasi
    def add_car(self, car):
        self._cars.append(car)
    
    # Method untuk menampilkan daftar Motorcycle di dalam garasi
    def display_motorcycles(self):
        print("Motorcycles in the garage:")
        for motorcycle in self._motorcycles:
            print(f"License Plate: {motorcycle.get_plat_nomor()}, Brand: {motorcycle.get_merk()}, Year: {motorcycle.get_tahun_produksi()}, Color: {motorcycle.get_warna()}, Jenis Motor: {motorcycle.get_jenis_motor()}, Engine Capacity: {motorcycle.get_kapasitas_tangki()}")

    # Method untuk menampilkan daftar Car di dalam garasi
    def display_cars(self):
        print("Cars in the garage:")
        for car in self._cars:
            print(f"License Plate: {car.get_plat_nomor()}, Brand: {car.get_merk()}, Year: {car.get_tahun_produksi()}, Color: {car.get_warna()}, Number of Seats: {car.get_jumlah_kursi()}, Number of Doors: {car.get_jumlah_pintu()}")
