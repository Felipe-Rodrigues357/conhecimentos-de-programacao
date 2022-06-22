#include <iostream>
using namespace std;
template<typename T> T soma (T n1, T n2)
{
	return n1+n2;
}
int main(int argc, char *argv[])
{
	cout<<"Soma de Inteiros: "<<soma(10,20)<<endl;
	cout<<"Soma de Reais: "<<soma(1.5,3.5)<<endl;
	return 0;
}
/*Template é possível criar funções, classes
e estruturas genéricas, por exemplo, pode
se formar um template para dois tipos diferentes,
ou seja, não foi preciso fazer uma função para
inteiros e outra função para soma de reais.