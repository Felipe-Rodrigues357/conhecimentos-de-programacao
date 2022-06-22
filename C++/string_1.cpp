#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
	string str1;
	string str2;
	cout<<"Primeiro nome: ";
	cin>>str1;
	cout<<"String: "<<str1<<endl;
	cout<<"Tamanho: "<<str1.length()<<endl;
	cout<<str1.at(2)<<endl;
	cout<<"Sobrenome: ";
	cin>>str2;
	cout<<"String: "<<str2<<endl;
	cout<<"Tamanho: "<<str2.length()<<endl;
	cout<<str2.at(2)<<endl;
	cout<<"Nome Completo: "<<str1<<" "<<str2;
	return 0;
}