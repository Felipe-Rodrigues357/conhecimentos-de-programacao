#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	int var=10;
	int* pvar; //O "*" cria o ponteiro da vari�vel
	pvar = &var; // L�-se como "Endere�o da Vari�vel var", por isso � preciso colocar o "&"
	cout<<*pvar<<endl;
	return 0;
}