#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
	string str = "Felipe";
	cout << "Nome: " << str << endl;
	str.replace(0, 2, "Rodrigues");
	cout << "Nova String: " << str << endl;
	size_t achou=str.find("lipe");
	if(achou != string::npos) //npos da classe string � um membro est�tico constante com o maior valor poss�vel de um elemento do tipo size_t
	{
		cout<<"Achou a Subtring!"<<endl;
	}
	else
	{
		cout<<"Substring nao encontrada!"<<endl;
	}
	string my_str;
	cout<<"Digite seu nome completo: ";
	getline (cin, my_str); // getline pega TUDO que foi escrito, cin s� pegaria o que estava escrito at� o espa�o...
	cout<<"Nome Digitado: "<<my_str<<endl;
	my_str += " Jedi Master";
	cout<<"Nome e Titulo: "<<my_str<<endl;
	return 0;
}
