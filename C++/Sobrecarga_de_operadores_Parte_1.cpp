#include <iostream>
using namespace std;

class Complexo
{
public:
	int real, imag;
	Complexo(int real, int imag)
	{
		this->real = real;
		this->imag = imag;
	}
	Complexo operator+ (Complexo& c) // Está redefinindo uma nova tarefa para o operador "+"
	{
		return Complexo(this->real + c.real, this->imag + c.imag);
	}
};
int main(int argc, char *argv[])
{
	Complexo c1(8, 9), c2(25, 66);
	//Complexo c3 = c1 + c2;
	Complexo c3=c1.operator+(c2);
	cout << "Parte Real: " << c3.real << endl;
	cout << "Parte Imaginaria: " << c3.imag << endl;
	return 0;
}