#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
	vector<int> v(3);
	v[0] = 10;
	v[1] = 20;
	v[2] = 30;
	vector<int>::iterator it;
	cout << "Primeiro Elemento: " << *v.begin() << endl;
	cout << "�ltimo Elemento: " << *(--v.end()) << endl;
	for(it = v.begin(); it != v.end(); it++)
	{
		cout << *it << endl;
	}
	return 0;
}
/*	vector<int>::iterator it = v.begin();
	cout<<*it<<endl; serve para mostrar o
	primeiro elemento o Vetor! Por isso tem
	o begin, igual possui o end e etc...*/
/*	Para usar o v.end precisa decrementar,
	se n�o ele n�o pega o �ltimo elemento
	pois o iterator tem intervalo fechado em
	begin, mas aberto at� o end*/
/*	Para usar acentua��o, clicar com o bot�o
	direito e na parte de "ferramentas",
	"conversion", "Resolve Special Chars"*/
