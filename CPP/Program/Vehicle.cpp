/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/

#pragma once

#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
private:
    string platNomor;
    string merk;
    int tahunProduksi;
    string warna;

public:
    // Konstruktor
    Vehicle(string platNomor, string merk, int tahunProduksi, string warna)
    {
        this->platNomor = platNomor;
        this->merk = merk;
        this->tahunProduksi = tahunProduksi;
        this->warna = warna;
    }

    // Setter
    void setPlatNomor(string platNomor)
    {
        this->platNomor = platNomor;
    }

    void setMerk(string merk)
    {
        this->merk = merk;
    }

    void setTahunProduksi(int tahunProduksi)
    {
        this->tahunProduksi = tahunProduksi;
    }

    void setWarna(string warna)
    {
        this->warna = warna;
    }

    // Getter
    string getPlatNomor()
    {
        return platNomor;
    }

    string getMerk()
    {
        return merk;
    }

    int getTahunProduksi()
    {
        return tahunProduksi;
    }

    string getWarna()
    {
        return warna;
    }

    // Destruktor
    ~Vehicle()
    {
    }
};