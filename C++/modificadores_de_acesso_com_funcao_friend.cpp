#include <iostream>
#include <string.h>
using namespace std;
//Função "friend" serve para que mesmo não estando dentro da classe, pode acessar os membros protegidos.
class Linguagem
{
	friend void classeAmiga(Linguagem*);
private:
	char nome[100];

protected:
	void displayName()
	{
		cout << "Nome: " << nome << endl;
	}
public:
	void setName (const char* nome)
	{
		strcpy(this->nome, nome);
	}
	void displayName2()
	{
		displayName();
	}
};

class LinguagemAmiga
{
	friend class Linguagem;
};

void classeAmiga(Linguagem* l)
{
	cout << "Classe amiga diz: " << l->nome << endl;
}

int main(int argc, char *argv[])
{
	Linguagem l;
	l.setName("C++");
	l.displayName2();
	classeAmiga(&l);

	return 0;
}
