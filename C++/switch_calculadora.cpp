#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	cout<<"CALCULADORA"<<"\n";
	cout<<"OPERACOES:"<<"\n";
	cout<<"[1] Adicao"<<"\n";
	cout<<"[2] Subtracao"<<"\n";
	cout<<"[3] Multiplicacao"<<"\n";
	cout<<"[4] Divisao"<<"\n";
	cout<<"[5] Fim do programa"<<"\n";
	int num1, num2, op;
	cout<<"Insira o primeiro numero: ";
	cin>>num1;
	cout<<"Insira o segundo numero: ";
	cin>>num2;
	cout<<"Selecione a operacao: ";
	cin>>op;
	switch(op)
	{
	case 1:
		cout<<num1<<"+"<<num2<<"="<<num1+num2;
		break;
	case 2:
		cout<<num1<<"-"<<num2<<"="<<num1-num2;
		break;
	case 3:
		cout<<num1<<"*"<<num2<<"="<<num1*num2;
		break;
	case 4:
		cout<<num1<<"/"<<num2<<"="<<num1/num2;
		break;
	case 5:
		cout<<"PROGRAMA ENCERRADO";
		break;
	default:
		break;
	}
	return 0;
}