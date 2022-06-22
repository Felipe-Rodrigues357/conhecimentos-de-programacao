#include <iostream>
using namespace std;

class Conta
{
public:
	int numero;
	double saldo;
	double depositar(double quantidade);
	double sacar(double quantidade);
	double getSaldo()
	{
		return saldo;
	}
	int getNumero()
	{
		return numero;
	}
};

double Conta::depositar(double quantidade)
{
	if(quantidade > 0)
	{
		saldo += quantidade;
	}
	return saldo;
}
double Conta::sacar (double quantidade)
{
	if(quantidade > 0 && saldo >= quantidade)
	{
		saldo -= quantidade;
	}
	return saldo;
}

void foo(Conta* pc)
{
	pc->depositar(50);
}

Conta* novaConta(int numero) // Nova pilha
{
	Conta* c = new Conta; // "new" serve para criar nova pilha
	c->numero = numero;
	c->saldo = 0.0;
	return c;
}

int main(int argc, char *argv[])
{
	Conta* pc=novaConta(1111);
	cout << "Numero da conta: " << pc->getNumero() << endl;
	cout << "Saldo: R$" << pc->getSaldo() << endl;
	return 0;
}
