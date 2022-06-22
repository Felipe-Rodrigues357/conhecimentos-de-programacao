#include <iostream>
#include "template_TAD_fila_projeto.h"
using namespace std;

int main(int argc, char *argv[])
{
	Fila<double> f1;
	cout << "Antes de inserir elementos...\n";
	if(f1.vazia())
		cout << "Fila Vazia!!\n";
	else
		cout << "Fila NAO Vazia!!\n";
	try
	{
		double e = f1.remover();
		cout << "Removido o elemento: " << e << endl;
	}
	catch (const char* msg)
	{
		cerr << "Erro: " << msg << endl;
	}
	f1.inserir(5.67);
	f1.inserir(9.23);
	f1.inserir(1.45);
	cout << "\nDepois de inserir elementos...\n";
	if(f1.vazia())
	{
		cout << "Fila vazia!!\n";
	}
	else
	{
		cout << "Fila NAO Vazia!!\n";
	}
	try
	{
		cout << "Elemento da frente: " << f1.frente() << endl;
	}
	catch(const char*msg)
	{
		cerr << "Erro: " << msg << endl;
	}
	try
	{
		cout << "Elemento do final: " << f1.final() << endl;
	}
	catch (const char*msg)
	{
		cerr << "Erro: " << msg << endl;
	}
	try
	{
		double e = f1.remover();
		cout << "Removido o elemento: " << e << endl;
	}
	catch (const char*msg)
	{
		cerr << "Erro: " << msg << endl;
	}
	try
	{
		cout << "Novo elemento da frente: " << f1.frente() << endl;
	}
	catch(const char*msg)
	{
		cerr << "Erro: " << msg << endl;
	}
	Fila<string> f2;
	f2.inserir("C++");
	f2.inserir("Python");
	f2.inserir("Ruby");
	cout << "\n\nFila de Strings...\n";
	try
	{
		cout << "Elemento da frente: " << f2.frente() << endl;
	}
	catch(const char*msg)
	{
		cerr << "Erro: " << msg << endl;
	}
		try
	{
		cout << "Elemento do final: " << f2.final() << endl;
	}
	catch(const char*msg)
	{
		cerr << "Erro: " << msg << endl;
	}
	return 0;
}