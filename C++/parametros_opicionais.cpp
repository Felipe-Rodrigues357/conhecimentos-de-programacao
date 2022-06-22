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
/*Parâmetros opicionais é para se não for
passado nenhum parâmetro, é colcado um
default para que não ocorra erros.*/