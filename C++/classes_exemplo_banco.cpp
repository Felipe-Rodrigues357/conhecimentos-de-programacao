#include <iostream>
using namespace std;

class Conta  
{
public:
	int numero;
	double saldo;
	double depositar(double quantidade) // Chamado de Método
	{
		if(quantidade>0)
		{
			saldo+=quantidade;
		}
		return saldo;
	}
	double sacar(double quantidade)
	{
		if(quantidade>0&&saldo>=quantidade)
		{
			saldo-=quantidade;
		}
		return saldo;
	}
};

int main(int argc, char *argv[])
{
	Conta c;
	c.numero=1;
	c.saldo=100.75;
	cout<<"Saldo: R$"<<c.saldo<<endl;
	cout<<"Deposito de R$100,00"<<endl;
	c.depositar(100);
	cout<<"Novo Saldo: R$"<<c.saldo<<endl;
	cout<<"Saque de R$50,00"<<endl;
	c.sacar(50);
	cout<<"Novo Saldo: R$"<<c.saldo<<endl;
	return 0;
}