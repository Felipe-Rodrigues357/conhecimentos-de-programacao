#include <iostream>
using namespace std;
struct Pessoa // Recomendado struct com mai�scula
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
	p.setIdade(20); // Boa pr�tica de programa��o utilizar o m�todo e n�o acessar diretamente.
	cout<<p.getIdade()<<endl;
	return 0;
}
