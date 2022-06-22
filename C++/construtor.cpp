#include <iostream>
#include <string.h>
using namespace std;

class Pessoa
{
private:

protected:
	char nome[100];
	int idade;
public:
	Pessoa(const char* nome, int idade) // Construtor para utilizar quando o membro for "Protected" ou "Private"
	{
		strcpy(this->nome, nome);
		this->idade = idade;
	}
	char* getNome() // Serve para "buscar" o membro protegido.
	{
		return nome;
	}
	int getIdade()
	{
		return idade;
	}
};

int main(int argc, char *argv[])
{
	Pessoa p("Joao", 30);
	cout << "Nome: " << p.getNome() << endl; // Sempre usar a função membro da classe nessas ocasiões
	cout << "Idade: " << p.getIdade() << endl;
	return 0;
}
