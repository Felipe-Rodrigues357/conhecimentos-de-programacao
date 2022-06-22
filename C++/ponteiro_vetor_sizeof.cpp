#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	int*vet= new int[10];
	int aux[4];
	aux[0]=10;
	aux[1]=20;
	aux[2]=30;
	aux[3]=40;
	for(int i = 0; i < sizeof(aux)/sizeof(int); i++)//colocando "sizeof" você pode mudar o tamanho de um vetor sem precisar mudar no for, é o vetor divido pelo tipo
	{
		cout<<aux[i]<<"\n";
	}
	return 0;
}