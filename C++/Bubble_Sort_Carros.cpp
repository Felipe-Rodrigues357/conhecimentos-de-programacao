#include <iostream>
#include <string.h>
#define MAX 10 // Modificar para uma constante, só precisa mudar aqui e não no meio do código
using namespace std;

class Carro
{
public:
	char nome[100];
	char cor[20];
	char placa[20];
	double preco;	
}; 
void ordena (Carro carros[], int tam)//Ordenação utilizando o algoritmo Bubble Sort
{
	Carro aux;
	for(int i = tam; i >=0 ; i--)
	{
		for(int j = 1; j <= i; j++)
		{
			//strcmp(carros[j-1], carros[j].nome); Transformar string em números.
			if(strcmp(carros[j-1].nome, carros[j].nome) == 1) // -1 é quando a string precede a outra e 1 quando a string está adiante. 
			{
				aux=carros[j-1];
				carros[j-1]=carros[j];
				carros[j]=aux;
			}
		}
	}
}
int main(int argc, char *argv[])
{
	Carro carros[MAX];
	int i=0;
	while (true)
	{
		char resp;
		cout<<"Digite o nome do carro: ";
		cin>>carros[i].nome;
		cout<<"Digite o preco: ";
		cin>>carros[i].preco;
		cout<<"Voce deseja continuar? [Y]/[N] ";
		cin>>resp;
		if(resp!='Y')
		{
			break;
		}
		cout<<"=============================="<<endl;
		i++;
	}
	cout<<endl;
	cout<<"Carros inseridos: "<<endl;
	for(int j = 0; j <= i; j++)
	{
		cout<<"Nome do carro: "<<carros[j].nome<<endl;
		cout<<"Preco: R$"<<carros[j].preco<<".000,00"<<endl;
		
	}
	ordena(carros, i);
	cout<<"=========================================="<<endl;
	cout<<"Carros em ordem alfabetica: "<<endl;
	for(int j = 0; j <=i ; j++)
	{
		cout<<"Nome do carro: "<<carros[j].nome<<endl;
		cout<<"Preco: R$"<<carros[j].preco<<".000,00"<<endl;
	}
	
	return 0;
}