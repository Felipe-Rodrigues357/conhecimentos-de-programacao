#include <iostream>
using namespace std;
struct Pessoa // Recomendado struct com maiúscula
{
	int idade;
	void setIdade(int idade)
	{
		this->idade=idade;
	}
	int getIdade()
	{
		return this->idade;
	}
};
int main(int argc, char *argv[])
{
	Pessoa p;
	p.setIdade(20); // Boa prática de programação utilizar o método e não acessar diretamente.
	cout<<p.getIdade()<<endl;
	return 0;
}
