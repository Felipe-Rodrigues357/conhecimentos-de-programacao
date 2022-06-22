#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	char op;
	cout<<"PRESSIONE [Q] PARA SAIR DO SISTEMA: ";
	cin>>op;
	switch(op)
	{
	case 'Q':
		cout<<"PROGRAMA ENCERRADO";
		break;
	case 'q':
		cout<<"PROGRAMA ENCERRADO";
		break;
	default:
		cout<<"COMANDO INEXISTENTE";
		break;
	}
	return 0;
}