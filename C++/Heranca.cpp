#include <iostream>
#include <string.h>
using namespace std;

class Animal // Classe mãe (classe base)
{
protected:
	char* nome;
public:
	Animal (const char* nome)
	{
		cout<<"Construindo Animal..."<<endl;
		this->nome=new char [strlen(nome)+1];
		strcpy(this->nome, nome);
	}
	~Animal()
	{
		delete[] nome;
		nome=0;
	}
	const char* getNome()
	{
		return nome;
	}
};
class Cachorro: public Animal // Classe filha (herda características de Animal)/ Colocar "Public: ..." faz com que herde a outra classe
{
protected:
	int idade;
public:
	Cachorro(const char* nome) : Animal(nome)
	{
		cout<<"Construindo cachorro..."<<endl;
		idade=0;
	}
	int getIdade()
	{
		return idade;
	}
	void setIdade(int idade)
	{
		this->idade=idade;
	}
};
int main(int argc, char *argv[])
{
	Cachorro c("Yankee");
	c.setIdade(5);
	cout<<"Nome: "<<c.getNome()<<endl; // Manipulado pela classe Animal e não Cachorro...
	cout<<"Idade: "<<c.getIdade()<<endl;
	return 0;
}
// Ao executar será visto que aparecerá antes o "Construindo Animal", pois o construtor da classe base é chamado antes de qualquer base da classe atual.