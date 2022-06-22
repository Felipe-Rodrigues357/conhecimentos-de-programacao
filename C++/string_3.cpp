#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
	string str = "Felipe";
	cout << "Nome: " << str << endl;
	str.insert(str.size(), " Rodrigues");
	cout << "Nome Completo: " << str << endl;
	str.erase(6, str.size());
	cout << "Primeiro Nome: " << str << endl;
	str.clear();
	if(str.empty())
	{
		cout << "String Deletada"<<endl;
	}
	else
	{
		cout<<"String NAO Deletada!"<<endl;
	}
	cout<<str<<endl;
		 return 0;
}
