#include <iostream>
#include <string.h>
using namespace std;

class Pessoa
{
private:

protected:
	char nome[100];
	int idade;
	int* parentes;
	double* filhos;
public:
	Pessoa(const char* nome, int idade) 
	{
		strcpy(this->nome, nome);
		this->idade = idade;
		parentes= new int[100];
		filhos=new double[100];
		cout<<"Entrou no Construtor: "<<nome<<endl;
	}
	char* getNome()
	{
		return nome;
	}
	int getIdade()
	{
		return idade;
	}
	~Pessoa() // Destrutor vem com o "~" antes dele.
	{
		cout<<"Entrou no Destrutor: "<<nome<<endl;
		delete[] parentes; // Muito importante usar o delete e retornar a memória para a pilha
		delete[] filhos;
	} 
};

int main(int argc, char *argv[])
{
	Pessoa pessoas[3]={{"joao", 30}, {"maria", 20},{"pedro", 40}};
	//cout << "Nome: " << p.getNome() << endl; 
	//cout << "Idade: " << p.getIdade() << endl;
	return 0;
}
