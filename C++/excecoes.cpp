/*Exce��es servem para fun��es relatarem
erros e que eles sejam retratados*/
#include <iostream>
using namespace std;
double div(double n1, double n2)
{
	if(n2 == 0)
		throw "Divisao por zero!\n";
	else
		cout<<n1/n2;
	return n1/n2;
}
int fat(int n)
{
	if(n < 0)
		throw "Numero Negativo!";
	if(n == 0 || n == 1)
		return 1;
	return n * fat(n - 1);
}
int main(int argc, char *argv[])
{
	int n, neg, div1, div2;
	cout << "Escolha um numero para saber o fatorial: ";
	cin >> n;
	cout << "Escolha um numero negativo: ";
	cin >> neg;
	cout << "Escolha o primeiro numero da Divisao: ";
	cin >> div1;
	cout << "Escolha o segundo numero da Divisao: ";
	cin >> div2;
	try // Tenta executar o bloco de c�digo!
	{
		cout << "Fatorial de " << n << ": " << fat(n) << endl;
		cout << "Fatorial de " << neg << ": " << fat(neg) << endl;
		cout << div1 << "/" << div2 << "=" << div(div1,div2) << endl;
	}
	catch(const char*e) // Serve para capturar os erros!
	{
		cerr << "Erro: " << e << endl; // Objeto que indica erro
	}
	catch(...) // Para "pegar" qualquer erro, que n�o seja um erro definido!
	{
		cerr << "Erro Inesperado!" << endl;
	}
	return 0;
}
/*try catch throw s�o as palavras
reservadas para exce��o*/
