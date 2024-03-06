from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jenis_motor, kapasitas_tangki):
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        self._jenis_motor = jenis_motor
        self._kapasitas_tangki = kapasitas_tangki

    # Setter untuk atribut jenis_motor
    def set_jenis_motor(self, jenis_motor):
        self._jenis_motor = jenis_motor

    # Getter untuk atribut jenis_motor
    def get_jenis_motor(self):
        return self._jenis_motor

    # Setter untuk atribut kapasitas_tangki
    def set_kapasitas_tangki(self, kapasitas_tangki):
        self._kapasitas_tangki = kapasitas_tangki

    # Getter untuk atribut kapasitas_tangki
    def get_kapasitas_tangki(self):
        return self._kapasitas_tangki