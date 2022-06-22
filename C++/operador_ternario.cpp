#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	int num =10;
	/*if(num>10)
		cout<<"Numero maior que 10"<<endl;
	else
		cout<<"Numero menor que 10"<<endl;*/
	num > 10 ? cout<<"Maior" : cout<<"Menor ou Igual";
	return 0;
}
/*
Operador Ternário
<condição>?<operação1>:<operação2> */