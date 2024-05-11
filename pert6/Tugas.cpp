#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

class Beverage {
private:
    string name;
    double price;

public:
    Beverage(const string& name, double price) : name(name), price(price) {}

    string getName() const {
        return name;
    }

    double getPrice() const {
        return price;
    }
};

class SalesSystem {
private:
    Beverage tea;
    Beverage coffee;

public:
    SalesSystem() : tea("Teh", 3000), coffee("Kopi", 5000) {}

    void displayMenu() const {
        cout << "Menu Minuman:" << endl;
        cout << "1. " << tea.getName() << " - Rp " << tea.getPrice() << endl;
        cout << "2. " << coffee.getName() << " - Rp " << coffee.getPrice() << endl;
    }

    void processOrder(int choice, int quantity) {
        const Beverage& selectedBeverage = (choice == 1) ? tea : coffee;

        if (choice != 1 && choice != 2) {
            cout << "Pilihan tidak valid." << endl;
            return;
        }

        double totalAmount = selectedBeverage.getPrice() * quantity;

        cout << "Anda telah memesan " << quantity << " " << selectedBeverage.getName() << "." << endl;
        cout << "Total harga: Rp " << fixed << setprecision(2) << totalAmount << endl;
        cout << "Terima kasih telah berbelanja!" << endl;
    }
};

int main() {
    SalesSystem sales;

    cout << "Selamat datang di sistem penjualan teh dan kopi!" << endl;
    sales.displayMenu();

    int choice, quantity;
    cout << "Pilih minuman (masukkan nomor): ";
    cin >> choice;

    cout << "Masukkan jumlah yang ingin dibeli: ";
    cin >> quantity;

    sales.processOrder(choice, quantity);

    return 0;
}