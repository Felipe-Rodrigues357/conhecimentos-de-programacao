#include <iostream>
using namespace std;
int quad (int num){
	return num*num;
}
int main(int argc, char *argv[])
{
	int num=10;
	cout<<"Quadrado de " <<num<<": "<<quad(num)<<endl;
	return 0;
}
/*Par�metros opicionais � para se n�o for
passado nenhum par�metro, � colcado um
default para que n�o ocorra erros.*/