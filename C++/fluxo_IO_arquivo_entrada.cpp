//Abrir um arquivo para entrada
//Ler o conte�do desse arquivo
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
	ifstream in("teste.txt"); // Para n�o precisar passar o caminho completo, colocar no mesmo local que o arquivo execut�vel
	string texto;
	char c=in.get();
	texto.push_back(c);
	cout<<"\nMostrando cada Caractere: \n";
	while(in.good()){
		cout<<c;
		c=in.get();
		texto.push_back(c);
	}
	cout<<"\n\nMostrando a String: \n"<<texto<<endl;
	return 0;
}