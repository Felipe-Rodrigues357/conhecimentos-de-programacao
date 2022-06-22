#include <iostream>
#include <string.h>
using namespace std;
// Public signica que os membros ficam acess�veis a todas as fun��es
// Protected somente para trabalhos internos.
// �nica diferen�a de membros privados e protegidos � a forma pela qual eles reagem a "heran�a" (mais pra frente).
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
	//cout<<l.nome - Dar� erro POIS � protegido/privado, tem que ser acessado atrav�s de m�todo (conforme est� acima).
	return 0;
}
