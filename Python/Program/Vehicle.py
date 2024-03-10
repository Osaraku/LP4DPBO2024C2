# Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
# dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
# seperti yang telah dispesifikasikan. Aamiin

class Vehicle:
    def __init__(self, plat_nomor, merk, tahun_produksi, warna):
        self._plat_nomor = plat_nomor
        self._merk = merk
        self._tahun_produksi = tahun_produksi
        self._warna = warna

    # Setter untuk atribut plat_nomor
    def set_plat_nomor(self, plat_nomor):
        self._plat_nomor = plat_nomor

    # Getter untuk atribut plat_nomor
    def get_plat_nomor(self):
        return self._plat_nomor

    # Setter untuk atribut merk
    def set_merk(self, merk):
        self._merk = merk

    # Getter untuk atribut merk
    def get_merk(self):
        return self._merk

    # Setter untuk atribut tahun_produksi
    def set_tahun_produksi(self, tahun_produksi):
        self._tahun_produksi = tahun_produksi

    # Getter untuk atribut tahun_produksi
    def get_tahun_produksi(self):
        return self._tahun_produksi

    # Setter untuk atribut warna
    def set_warna(self, warna):
        self._warna = warna

    # Getter untuk atribut warna
    def get_warna(self):
        return self._warna