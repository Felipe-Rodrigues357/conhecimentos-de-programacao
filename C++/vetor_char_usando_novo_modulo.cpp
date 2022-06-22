#include <iostream>
#include <string.h>
using namespace std;
int main(int argc, char** argv)
{
	char nome[] = "Felipe";
	if(isupper(nome[0])) // isupper fala se é um caracter maísculo ou minúsculo, mostrando 0 para falso e 1 para verdadeiro
	{
		cout<<"Maiuscula"<<endl;
	}
	else
	{
		cout<<"Minuscula"<<endl;	
	}
	return 0;
}
