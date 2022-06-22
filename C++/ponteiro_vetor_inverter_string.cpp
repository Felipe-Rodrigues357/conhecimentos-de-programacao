#include <iostream>
#include <string.h>
using namespace std;
int main(int argc, char** argv)
{
	char nome[100];
	int tam;
	char* pfim;
	char* p;
	char* pini;
	cout<<"Digite seu nome: ";
	cin>>nome;
	tam=strlen(nome);
	pfim=&nome[tam];
	pini=&nome[0];
	p=&nome[tam-1];
	while(true)
	{
		cout<<*p;
		if(p==pini)
		{
			break;
		}
		p--;
	}
	cout<<endl;
	return 0;
}