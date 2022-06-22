#include <iostream>
#include <string.h>
using namespace std;

class Pessoa
{
public:
	//Membros da classe:
	char nome[100];
	char cpf[20];
	int idade;
};

int main(int argc, char *argv[])
{
	Pessoa p1; // Instância da classe, chamado de Objeto
	strcpy(p1.nome, "Felipe"); // Exclusivo da <string.h> serve para copiar Strings
	strcpy(p1.cpf, "05871163742");
	p1.idade = 27; // Não se utiliza strcpy porque não é uma String
	cout<<"Nome: "<<p1.nome<<endl;
	cout<<"CPF: "<<p1.cpf<<endl;
	cout<<"Idade: "<<p1.idade<<endl;
	return 0;
}
