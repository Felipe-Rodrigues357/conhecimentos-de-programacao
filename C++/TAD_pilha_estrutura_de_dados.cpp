//Implementa��o do TAD Pilha (Stack)
#include <iostream>
using namespace std;

class Pilha
{
private:
	int*vet;
	int max_tam;
	int topo;
public:
	Pilha() // Construtor
	{
		vet = new int[100]; // Alocando 100 novos inteiros.
		max_tam = 99;
		topo = -1;
	}
	~Pilha()
	{
		delete[] vet;
	}
	void empilhar(int e)
	{
		if(topo == max_tam)
		{
			cout << "Pilha Cheia!" << endl;
		}
		else
		{
			vet[++topo] = e;
		}
	}
	void desempilhar()
	{
		if(topo == -1)
		{
			cout << "Pilha vazia!" << endl;
		}
		else
		{
			topo--;
		}
	}
	int getTopo()
	{
		if(topo != -1)
		{
			return vet[topo];
		}
		return -1;
	}
	int vazia()
	{
		return(topo == -1);
	}
};
int main(int argc, char *argv[])
{
	Pilha p;
	p.empilhar(25);
	p.empilhar(33);
	p.empilhar(29);
	p.desempilhar();
	cout << "Pilha Vazia: " << p.vazia() << endl;
	cout << "Topo: " << p.getTopo() << endl;
	return 0;
}
