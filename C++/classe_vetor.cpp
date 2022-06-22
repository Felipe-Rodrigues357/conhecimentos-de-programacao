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

int getIdade (Pessoa pessoas[], const char* nome)
{
	int tam = sizeof(pessoas);
	for(int i = 0; i < tam; i++)
	{
		if(strcmp(nome, pessoas[i].nome) == 0) // função de comparação.
			return pessoas[i].idade;
	}
	return -1;
}

int main(int argc, char *argv[])
{
	Pessoa pessoas[3] =
	{
		{"Anakin", "05871163794", 30},
		{"Felipe", "05871163742", 27},
		{"Joaquim", "05873265556", 26},
	};
	cout << "Nome: " << pessoas[0].nome << endl;
	cout << "CPF: " << pessoas[0].cpf << endl;
	cout << "Idade: " << pessoas[0].idade << endl;
	cout << "--------------------------------" << endl;
	cout << "Nome: " << pessoas[1].nome << endl;
	cout << "CPF: " << pessoas[1].cpf << endl;
	cout << "Idade: " << pessoas[1].idade << endl;
	cout << "--------------------------------" << endl;
	cout << "Nome: " << pessoas[2].nome << endl;
	cout << "CPF: " << pessoas[2].cpf << endl;
	cout << "Idade: " << pessoas[2].idade << endl;
	cout << "--------------------------------" << endl;
	int idade = getIdade(pessoas, "Anakin");
	if(idade!=-1)
	{
		cout<<"Idade do Anakin: "<<idade<<endl;
	}
	else
	{
		cout<<"Pessoa nao encontrada"<<endl;
	}
	return 0;
}
