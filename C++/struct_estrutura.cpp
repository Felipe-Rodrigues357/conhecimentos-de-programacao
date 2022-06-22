#include <iostream>
#include <string.h>
using namespace std;
//Estrutura serve para "agrupar" os dados, criar um próprio "tipo" (int, double, etc), isso é bom para poder ter vários tipos diferentes ao mesmo tempo:
typedef	struct pessoa
{
	char nome [100];
	int idade;
	int ano;
	char cpf[20];
} t_pessoa;

int main(int argc, char *argv[])
{
	t_pessoa p;
	// Se colocar somente "p." vão aparecer todas as opções;
	// Se utilizar ponteiro "t_pessoa* p" não pode utilizar o ".", precisa colocar "p->idade" tanto para designar quando para cout..
	strcpy(p.nome, "Felipe"); //O "." serve para acessar a struct!
	p.idade=27;
	cout<<"Nome: "<<p.nome<<endl;
	cout<<"Idade: "<<p.idade<<endl;
	return 0;
}