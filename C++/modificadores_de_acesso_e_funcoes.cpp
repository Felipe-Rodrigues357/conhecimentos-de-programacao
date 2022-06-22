#include <iostream>
#include <string.h>
using namespace std;
// Public signica que os membros ficam acessíveis a todas as funções
// Protected somente para trabalhos internos.
// Única diferença de membros privados e protegidos é a forma pela qual eles reagem a "herança" (mais pra frente).
class Linguagem
{
private:
	char nome[100];
public:
	void mostrarNome()
	{
		cout<<"Nome: "<<nome<<endl;
	}
	void setNome (const char* nome)
	{
		strcpy(this->nome, nome);
	}
};

int main(int argc, char *argv[])
{
	Linguagem l;
	l.setNome("C++");
	l.mostrarNome();
	//cout<<l.nome - Dará erro POIS é protegido/privado, tem que ser acessado através de método (conforme está acima).
	return 0;
}
