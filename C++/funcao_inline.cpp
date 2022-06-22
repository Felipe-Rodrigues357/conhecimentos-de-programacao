#include <iostream>
using namespace std;
inline void foo()
{
	cout<<"Aprendendo C++!";
}
int main(int argc, char *argv[])
{
	foo();
	return 0;
}
/*Função inline faz a função ser lida mais
rápido que a função normal. Diminui
a sobrecarga de funções. Recomendado para
funções pequenas, já que ocupa muito
espaço de memória.*/