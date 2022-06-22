#include <iostream>
#include <string.h>
using namespace std;
void inverte(char nome[])
{
	int tam;
	for(tam=0;nome[tam];tam++);
	{
		for(int i = tam - 1; i >= 0; i--)
		{
			cout << nome[i];
		}
	}
}
int main(int argc, char** argv)
	{
		char nome[]="Felipe";
		cout<<"Seu nome invertido eh ";
		inverte(nome);
		return 0;
	}
