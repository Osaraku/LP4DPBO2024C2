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

class Motorcycle : public Vehicle
{
private:
    string jenisMotor;
    int kapasitasTangki;

public:
    // Konstruktor
    Motorcycle(string platNomor, string merk, int tahunProduksi, string warna, string jenisMotor, int kapasitasTangki)
        : Vehicle(platNomor, merk, tahunProduksi, warna)
    {
        this->jenisMotor = jenisMotor;
        this->kapasitasTangki = kapasitasTangki;
    }

    // Setter
    void setJenisMotor(string jenisMotor)
    {
        this->jenisMotor = jenisMotor;
    }

    void setKapasitasTangki(int kapasitasTangki)
    {
        this->kapasitasTangki = kapasitasTangki;
    }

    // Getter
    string getJenisMotor()
    {
        return jenisMotor;
    }

    double getKapasitasTangki()
    {
        return kapasitasTangki;
    }

    // Destruktor
    ~Motorcycle()
    {
    }
};