#include <iostream>
#include <string.h>
using namespace std;
class Estudante
{
private:
protected:
	char* nome;
public:
	Estudante(const char* nome)
	{
		cout << "Construindo objeto..." << nome << endl;
		int tam = strlen(nome) + 1;
		this->nome = new char[tam];
		strcpy(this->nome, nome);
	}
	Estudante (const Estudante&e) // Construtor de C�pia
	{
		cout << "Construindo copia..." << e.nome << endl;
		int tam = strlen(e.nome) + strlen("Copia de ") + 1;
		this->nome = new char[tam]; // Aloca novo bloco de mem�ria para a pilja
		strcpy(this->nome, "Copia de ");
		strcat(this->nome, e.nome);
	}
	~Estudante()
	{
		cout << "Destruindo... " << nome << endl;
		delete[] nome;
		nome = 0;
	}
	const char* getNome()// Fun��o de acesso
	{
		return nome;
	}
};
void foo2(Estudante e)
{

}
void foo()
{
	Estudante estudante("Felipe");
	foo2(estudante);
	cout << "Estudante: " << estudante.getNome() << endl;
}
int main(int argc, char *argv[])
{
	foo();
	return 0;
}
