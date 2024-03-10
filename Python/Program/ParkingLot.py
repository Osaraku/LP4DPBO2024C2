# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

class ParkingLot:
    def __init__(self, kapasitas, jumlah_kendaraan):
        self._kapasitas = kapasitas
        self._jumlah_kendaraan = jumlah_kendaraan

    # Setter untuk atribut kapasitas
    def set_kapasitas(self, kapasitas):
        self._kapasitas = kapasitas

    # Getter untuk atribut kapasitas
    def get_kapasitas(self):
        return self._kapasitas

    # Setter untuk atribut jumlah_kendaraan
    def set_jumlah_kendaraan(self, jumlah_kendaraan):
        self._jumlah_kendaraan = jumlah_kendaraan

    # Getter untuk atribut jumlah_kendaraan
    def get_jumlah_kendaraan(self):
        return self._jumlah_kendaraan