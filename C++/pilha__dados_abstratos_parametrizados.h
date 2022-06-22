#include <iostream> /* FUNÇÕES TEMPLATE TEM
QUE SER NO ARQUIVO CABEÇALHO (.h)*/
using namespace std;
template <class Type>
class Pilha
{
private:
	Type*vet;
	int max_tam;
	int topo;
public:
	Pilha(int tam)
	{
		vet = new Type[tam];
		max_tam = tam - 1;
		topo = -1;
	}
	~Pilha()
	{
		delete[] vet;
	}
	void empilhar(Type e)
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
	Type getTopo()
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
