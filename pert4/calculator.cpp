#include <iostream>
using namespace std;

int main()
{
  cout << "##  program calculator  ##" << endl;
  cout << "=============================" << endl;
  cout << endl;

  int pilihan;
  float num1, num2;

  cout << "1. Penjumlahan"<< endl;
  cout << "2. Pengurangan"<< endl;
  cout << "3. Perkalian"  << endl;
  cout << "4. Pembagian"  << endl;
  cout << endl;

  cout << "Input pilihan operasi: ";
  cin >> pilihan;
  cout << "Angka pertama: ";
  cin >> num1;
  cout << "Angka kedua: ";
  cin >> num2;
  cout << endl;

  switch (pilihan) {
   case 1:
     cout << "Hasil dari " << num1 << " + " << num2 << " = " << num1+num2;
     break;
   case 2:
     cout << "Hasil dari " << num1 << " - " << num2 << " = " << num1-num2;
     break;
   case 3:
     cout << "Hasil dari " << num1 << " * " << num2 << " = " << num1*num2;
     break;
   case 4:
     cout << "Hasil dari " << num1 << " / " << num2 << " = " << num1/num2;
     break;
   default :
     printf("Pilih lah sesuai fitur yang ada");
  }

  cout << endl;
  return 0;
}