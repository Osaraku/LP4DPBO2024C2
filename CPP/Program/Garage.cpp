/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/
#pragma once

#include <iostream>
#include <string>
#include <vector>
#include "ParkingLot.cpp"
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"

using namespace std;

class Garage : public ParkingLot
{
private:
    string nama;
    int luas;
    vector<Motorcycle *> motorcycles;
    vector<Car *> cars;

public:
    // Konstruktor
    Garage(string nama, int luas, int kapasitas, int jumlahKendaraan)
        : ParkingLot(kapasitas, jumlahKendaraan)
    {
        this->nama = nama;
        this->luas = luas;
    }

    // Setter
    void setNama(string nama)
    {
        this->nama = nama;
    }

    void setLuas(int luas)
    {
        this->luas = luas;
    }

    // Getter
    string getNama()
    {
        return nama;
    }

    int getLuas()
    {
        return luas;
    }

    // Menambahkan Motorcycle ke Garage
    void addMotorcycle(Motorcycle *motorcycle)
    {
        motorcycles.push_back(motorcycle);
    }

    // Menambahkan Car ke Garage
    void addCar(Car *car)
    {
        cars.push_back(car);
    }

    // Menampilkan daftar Motorcycle
    void displayMotorcycles()
    {
        if (motorcycles.empty())
        {
            cout << "Tidak ada Motor di dalam " << nama << endl;
        }
        else
        {
            cout << "Daftar Motor dalam " << nama << endl;
            cout << "-----------------------------" << endl;
            int i = 1;
            for (const auto &motorcycle : motorcycles)
            {
                cout << "Motor ke - " << i << endl;
                cout << "Plat: " << motorcycle->getPlatNomor() << endl;
                cout << "Merk: " << motorcycle->getMerk() << endl;
                cout << "Tahun Produksi: " << motorcycle->getTahunProduksi() << endl;
                cout << "Warna: " << motorcycle->getWarna() << endl;
                cout << "Jenis Motor: " << motorcycle->getJenisMotor() << endl;
                cout << "Kapasitas Tangki: " << motorcycle->getKapasitasTangki() << endl;
                cout << endl;
                i++;
            }
        }
    }

    // Menampilkan daftar Car
    void displayCars()
    {
        if (cars.empty())
        {
            cout << "Tidak ada Mobil di dalam " << nama << endl;
        }
        else
        {
            cout << "Daftar Mobil dalam " << nama << endl;
            cout << "-----------------------------" << endl;
            int i = 1;
            for (const auto &car : cars)
            {
                cout << "Mobil ke - " << i << endl;
                cout << "Plat: " << car->getPlatNomor() << endl;
                cout << "Merk: " << car->getMerk() << endl;
                cout << "Tahun Produksi: " << car->getTahunProduksi() << endl;
                cout << "Warna: " << car->getWarna() << endl;
                cout << "Jumlah Kursi: " << car->getJumlahKursi() << endl;
                cout << "Jumlah Pintu: " << car->getJumlahPintu() << endl;
                cout << endl;
                i++;
            }
        }
    }

    // Destruktor
    ~Garage()
    {
        for (int i = 0; i < motorcycles.size(); i++)
        {
            delete motorcycles[i];
        }
        motorcycles.clear();

        for (int i = 0; i < cars.size(); i++)
        {
            delete cars[i];
        }
        cars.clear();
    }
};
