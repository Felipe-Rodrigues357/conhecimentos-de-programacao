#include <iostream>
using namespace std;
struct Pessoa // Recomendado struct com maiúscula
{
	int idade;
	Pessoa (int idade);
	void setIdade(int idade)
	{
		this->idade = idade;
	}
	int getIdade()
	{
		return this->idade;
	}
};
Pessoa::Pessoa (int idade) //Protótipo do Construtor separado da implementação
{
	this->idade = idade;
}
int main(int argc, char *argv[])
{
	Pessoa p(20);
	cout << p.getIdade() << endl;
	return 0;
}
