/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/
#pragma once

#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle
{
private:
    int jumlahKursi;
    int jumlahPintu;

public:
    // Konstruktor
    Car(string platNomor, string merk, int tahunProduksi, string warna, int jumlahKursi, int jumlahPintu)
        : Vehicle(platNomor, merk, tahunProduksi, warna)
    {
        this->jumlahKursi = jumlahKursi;
        this->jumlahPintu = jumlahPintu;
    }

    // Setter
    void setJumlahKursi(int jumlahKursi)
    {
        this->jumlahKursi = jumlahKursi;
    }

    void setJumlahPintu(int jumlahPintu)
    {
        this->jumlahPintu = jumlahPintu;
    }

    // Getter
    int getJumlahKursi()
    {
        return jumlahKursi;
    }

    int getJumlahPintu()
    {
        return jumlahPintu;
    }

    // Destruktor
    ~Car()
    {
    }
};