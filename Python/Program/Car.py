# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jumlah_kursi, jumlah_pintu):
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        self._jumlah_kursi = jumlah_kursi
        self._jumlah_pintu = jumlah_pintu

    # Setter untuk atribut jumlah_kursi
    def set_jumlah_kursi(self, jumlah_kursi):
        self._jumlah_kursi = jumlah_kursi

    # Getter untuk atribut jumlah_kursi
    def get_jumlah_kursi(self):
        return self._jumlah_kursi

    # Setter untuk atribut jumlah_pintu
    def set_jumlah_pintu(self, jumlah_pintu):
        self._jumlah_pintu = jumlah_pintu

    # Getter untuk atribut jumlah_pintu
    def get_jumlah_pintu(self):
        return self._jumlah_pintu