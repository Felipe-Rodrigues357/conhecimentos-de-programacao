#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	int* vet= new int[10];
	cout<<"Digite um numero: ";
	cin>>*(vet);
	cout<<"Voce digitou: "<<vet[0]<<"\n";
	cout<<"Digite outro numero: ";
	cin>>*(vet+1);
	cout<<"Voce digitou: "<<vet[1];
	delete[] vet;// Serve para "limpar" o que foi alocado
	vet=NULL // Boa prática de "limpar" o ponteiro
	return 0;
}