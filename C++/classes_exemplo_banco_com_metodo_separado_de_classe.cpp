#include <iostream>
using namespace std;

class Conta
{
public:
	int numero;
	double saldo;
	double depositar(double quantidade); // Necessário declarar a função também dentro da classe.
	double sacar(double quantidade);
};
//"::" é operador de escopo e separa o nome de classe (Conta) e de membro (ex. depositar).
double Conta::depositar(double quantidade) // Utilizando o nome completo da função depositar!
{
	if(quantidade > 0)
	{
		this->saldo += quantidade; // "This->" serve como ponteiro para o objeto da classe atual.
	}
	return this->saldo;
}
double Conta::sacar (double quantidade)
{
	if(quantidade > 0 && saldo >= quantidade)
	{
		saldo -= quantidade;
	}
	return saldo;
}

int main(int argc, char *argv[])
{
	Conta c;
	Conta* pc=&c; // Ponteiro com o endereço de "c".
	pc->numero=1; // Para acessar ou coloca (*pc).numero, entre "()" devido a precedência do "." ser maior que do "*"
	pc->saldo=200; // Operador de seta é mais utilizado que o "(*)".
	cout << "Saldo: R$" << c.saldo << endl;
	cout << "Deposito de R$100,00" << endl;
	c.depositar(100);
	cout << "Novo Saldo: R$" << c.saldo << endl;
	cout << "Saque de R$50,00" << endl;
	c.sacar(50);
	cout << "Novo Saldo: R$" << c.saldo << endl;
	return 0;
}
