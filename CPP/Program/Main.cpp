/*
Saya Muhamad Tio Ariyanto [2201718] mengerjakan soal Latihan Praktikum 4
dalam mata kuliah DPBO untuk keberkahanNya saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin
*/

#include <bits/stdc++.h>
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "ParkingLot.cpp"
#include "Garage.cpp"

int main()
{
    // Membuat objek Garage
    Garage garage1("Garasi-1", 20, 5, 4);
    Garage garage2("Garage 2", 12, 3, 3);

    // Membuat objek Motorcycle
    Motorcycle *motor = new Motorcycle("B 1234 XYZ", "Honda", 2023, "Merah", "Sport", 10);
    Motorcycle *motor2 = new Motorcycle("B 5678 ABC", "Yamaha", 2022, "Biru", "Adventure", 8);
    Motorcycle *motor3 = new Motorcycle("B 9876 QWE", "Suzuki", 2023, "Kuning", "Matic", 9);
    Motorcycle *motor4 = new Motorcycle("B 5432 RTY", "Kawasaki", 2022, "Hijau", "Trail", 7);

    // Membuat objek Car
    Car *mobil = new Car("B 5678 ABC", "Toyota", 2023, "Hitam", 4, 4);
    Car *mobil2 = new Car("B 3456 GHI", "Honda", 2022, "Putih", 4, 5);
    Car *mobil3 = new Car("B 6789 UIO", "Mitsubishi", 2023, "Silver", 4, 5);

    // Menambahkan objek Motorcycle dan Car ke Garage
    garage1.addMotorcycle(motor);
    garage1.addMotorcycle(motor2);

    garage2.addMotorcycle(motor3);
    garage2.addMotorcycle(motor4);

    garage1.addCar(mobil);
    garage1.addCar(mobil2);

    garage2.addCar(mobil3);

    // Menampilkan Garasi Pertama
    cout << "Nama: " << garage1.getNama() << endl;
    cout << "Luas: " << garage1.getLuas() << endl;
    cout << "Kapasitas: " << garage1.getKapasitas() << endl;
    cout << "Jumlah Kendaraan: " << garage1.getJumlahKendaraan() << endl;
    cout << endl;
    garage1.displayMotorcycles();
    cout << endl;
    garage1.displayCars();

    cout << "=============================" << endl;
    cout << endl;

    // Menampilkan Garasi Kedua
    cout << "Nama: " << garage2.getNama() << endl;
    cout << "Luas: " << garage2.getLuas() << endl;
    cout << "Kapasitas: " << garage2.getKapasitas() << endl;
    cout << "Jumlah Kendaraan: " << garage2.getJumlahKendaraan() << endl;
    cout << endl;
    garage2.displayMotorcycles();
    cout << endl;
    garage2.displayCars();

    return 0;
}