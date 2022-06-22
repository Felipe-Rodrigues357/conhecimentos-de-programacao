#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	const int vet[]={1,2,3};
	const int* p1=&vet[0]; //Ponteiro Array Constante int
	int const* p2=&vet[1]; //Ponteiro Array Constante int
	int* const p3=new int[3]; //Ponteiro Constante para Array int, ou seja, tem que inicializar declarado!
	const char* const p4="Felipe"; //Ponteiro é constante e aponta para characteres constantes! Não podem ser modificados!
	cout<<"*p1 = "<<*p1<<endl;
	cout<<"*p2 = "<<*p2<<endl;
	*p3=1;
	*(p3+1)=2;
	*(p3+2)=3;
	cout<<"p3: "<<endl;
	cout<<*p3<<endl;
	cout<<*(p3+1)<<endl;
	cout<<*(p3+2)<<endl;
	*p3=10;
	cout<<"Valor Modificado p3: "<<*p3<<endl;
	cout<<p4<<endl;
	return 0;
}