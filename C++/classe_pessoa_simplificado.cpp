#include <iostream>
#include <string.h>
using namespace std;

class Pessoa
{
public:
	char nome[100];
	char cpf[20];
	int idade;
};

int main(int argc, char *argv[])
{
	Pessoa p1={"Felipe","05871163742", 27};
	cout<<"Nome: "<<p1.nome<<endl;
	cout<<"CPF: "<<p1.cpf<<endl;
	cout<<"Idade: "<<p1.idade<<endl;
	return 0;
}