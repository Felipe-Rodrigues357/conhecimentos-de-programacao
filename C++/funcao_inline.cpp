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
/*Fun��o inline faz a fun��o ser lida mais
r�pido que a fun��o normal. Diminui
a sobrecarga de fun��es. Recomendado para
fun��es pequenas, j� que ocupa muito
espa�o de mem�ria.*/