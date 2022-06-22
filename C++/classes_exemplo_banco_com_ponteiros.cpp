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

void foo(Conta* pc) // Colocado ponteiro na função para que possa ser acessado o endereço e não a cópia.
{
	pc->depositar(50);
}

Conta* novaConta(int numero){
	Conta* c=new Conta;
	c->numero=numero;
	c->saldo=0.0;
	return c;
}

int main(int argc, char *argv[])
{
	Conta c;
	Conta* pc = &c;
	pc->numero = 1;
	pc->saldo = 200;
	foo(&c); // Utilizou o endereço de "c" porque se não ele utiliza a cópia do número original, ou seja, 200, é preciso criar um ponteiro para que isso não ocorra.
	cout << "Saldo: R$" << pc->getSaldo() << endl;
	return 0;
}
