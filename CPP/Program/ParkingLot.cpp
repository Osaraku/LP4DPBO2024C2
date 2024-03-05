/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/
#pragma once

#include <iostream>

using namespace std;

class ParkingLot
{
private:
    int kapasitas;
    int jumlahKendaraan;

public:
    // Konstruktor
    ParkingLot(int kapasitas, int jumlahKendaraan)
    {
        this->kapasitas = kapasitas;
        this->jumlahKendaraan = jumlahKendaraan;
    }

    // Setter
    void setKapasitas(int kapasitas)
    {
        this->kapasitas = kapasitas;
    }

    void setJumlahKendaraan(int jumlahKendaraan)
    {
        this->jumlahKendaraan = jumlahKendaraan;
    }

    // Getter
    int getKapasitas()
    {
        return kapasitas;
    }

    int getJumlahKendaraan()
    {
        return jumlahKendaraan;
    }

    // Destruktor
    ~ParkingLot()
    {
    }
};