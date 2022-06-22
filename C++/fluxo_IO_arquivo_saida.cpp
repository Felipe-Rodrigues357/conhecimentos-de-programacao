//Abrir um arquivo para saída
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
	ofstream output("saida.txt");
	output<<"Aprendendo C++\n";
	output<<"Testanto saporra\n";
	return 0;
}