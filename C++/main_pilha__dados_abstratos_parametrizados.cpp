#include <iostream>
#include "pilha__dados_abstratos_parametrizados.h"
using namespace std;
int main(int argc, char *argv[])
{
	Pilha<float> p(100);
	p.empilhar(10.25);
	p.empilhar(11.14);
	p.empilhar(12.05);
	p.desempilhar();
	if(p.vazia())
	cout << "Pilha Vazia: " << p.vazia() << endl;
	cout << "Topo: " << p.getTopo() << endl;
	return 0;
}
