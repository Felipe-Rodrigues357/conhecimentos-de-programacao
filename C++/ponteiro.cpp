#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	int var=10;
	int* pvar; //O "*" cria o ponteiro da variável
	pvar = &var; // Lê-se como "Endereço da Variável var", por isso é preciso colocar o "&"
	cout<<*pvar<<endl;
	return 0;
}