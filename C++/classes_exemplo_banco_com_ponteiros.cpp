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

void foo(Conta* pc) // Colocado ponteiro na fun��o para que possa ser acessado o endere�o e n�o a c�pia.
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
	foo(&c); // Utilizou o endere�o de "c" porque se n�o ele utiliza a c�pia do n�mero original, ou seja, 200, � preciso criar um ponteiro para que isso n�o ocorra.
	cout << "Saldo: R$" << pc->getSaldo() << endl;
	return 0;
}
