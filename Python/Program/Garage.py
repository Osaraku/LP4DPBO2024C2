# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

from ParkingLot import ParkingLot
from Car import Car
from Motorcycle import Motorcycle
from Tabel import Tabel

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
        print("List motor di dalam " + self._nama_garasi + " :")
        i = 0
        tab = Tabel() # Instansiasi objek tabel
        arrstr = [[0 for j in range(6)] for i in range(len(self._motorcycles)+1)]

        arrstr[0][0] = "Plat Nomor"
        arrstr[0][1] = "Merk"
        arrstr[0][2] = "Tahun Produksi"
        arrstr[0][3] = "Warna"
        arrstr[0][4] = "Jenis Motor"
        arrstr[0][5] = "Kapasitas Tangki"

        for i, motorcycle in enumerate(self._motorcycles):
            arrstr[i+1][0] = motorcycle.get_plat_nomor()
            arrstr[i+1][1] = motorcycle.get_merk()
            arrstr[i+1][2] = motorcycle.get_tahun_produksi()
            arrstr[i+1][3] = motorcycle.get_warna()
            arrstr[i+1][4] = motorcycle.get_jenis_motor()
            arrstr[i+1][5] = motorcycle.get_kapasitas_tangki()

        tab.buatBaris(6, arrstr)

    # Method untuk menampilkan daftar Car di dalam garasi
    def display_cars(self):
        print("List mobil di dalam " + self._nama_garasi + " :")
        i = 0
        tab = Tabel() # Instansiasi objek tabel
        arrstr = [[0 for j in range(6)] for i in range(len(self._cars)+1)]

        arrstr[0][0] = "Plat Nomor"
        arrstr[0][1] = "Merk"
        arrstr[0][2] = "Tahun Produksi"
        arrstr[0][3] = "Warna"
        arrstr[0][4] = "Jumlah Kursi"
        arrstr[0][5] = "Jumlah Pintu"

        for i, car in enumerate(self._cars):
            arrstr[i+1][0] = car.get_plat_nomor()
            arrstr[i+1][1] = car.get_merk()
            arrstr[i+1][2] = car.get_tahun_produksi()
            arrstr[i+1][3] = car.get_warna()
            arrstr[i+1][4] = car.get_jumlah_kursi()
            arrstr[i+1][5] = car.get_jumlah_pintu()

        tab.buatBaris(6, arrstr)