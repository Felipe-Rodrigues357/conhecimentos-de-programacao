#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
	ifstream in("teste.txt");
	char c;
	while(true)
	{
		in >> c;
		if(in.fail()) // Testa de REALMENTE tem um caractere para ser lido.
		{
			break;
		}
		cout << c;
	}
	return 0;
}
