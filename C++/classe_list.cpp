#include <iostream>
#include <list>
using namespace std;
bool par(const int& n)
{
	return(n % 2 == 0);
}
bool comparar_tamanho(const string&s1, const string& s2)
{
	//Se o tamanho da primeira String deve vir antes então retorna true
	if(s1.length() < s2.length())
		return true;
	return false;
}
int main(int argc, char *argv[])
{
	list<int> L1; // Lista de Inteiros Vazia
	list<int> L2(3, 10); // Três Inteiros com o valor 10
	list<int>::iterator it;
	//Inserindo elementos em L1 - push_back e push_front
	L1.push_back(10); // L1:10
	L1.push_front(20); // L1: 20,10
	L1.push_back(30); // L1: 20,10,30
	cout << "Mostrando os elementos de L1: \n";
	for(it = L1.begin(); it != L1.end(); it++)
		cout << *it << endl;
	cout << "\nMostrando os elementos de L2: \n";
	for(it = L2.begin(); it != L2.end(); it++)
		cout << *it << endl;
	//Acessando o primeiro e último elemento de L1 - front e back
	cout << "\nPrimeiro elemento de L1: " << L1.front();
	cout << "\nUltimo elemento de L1: " << L1.back() << endl;
	cout << "\nTamanho de L1: " << L1.size() << " Elementos." << endl;
	//L1: 20,10,30
	//Removendo o primeiro elemento de L1
	L1.pop_front(); // Remove o 20
	//Removendo o último elemento de L1
	L1.pop_back(); // Remove o 30
	cout << "\nNovo L1 ap¢s remo‡Æo do 1§ e £ltimo elementos: " << endl;
	for(it = L1.begin(); it != L1.end(); it++)
		cout << *it << endl;
	//Removendo todos os elementos de L2
	while(!L2.empty())
		L2.pop_front();
	cout << "\nNovo tamanho de L2: " << L2.size() << endl;
	//Atribuindo elementos a L2 - Função assign
	int vet[] = {1, 2, 3, 4};
	L2.assign(vet, vet + 4);
	cout << "\nMostrando os novos elementos de L2:" << endl;
	for(it = L2.begin(); it != L2.end(); it++)
		cout << *it << endl;
	//Inserindo um elemento em L2 - Função insert
	L2.insert(L2.begin(), 100);
	cout << "\nMostrando o nov¡ssimo elemento de L2:" << endl;
	for(it = L2.begin(); it != L2.end(); it++)
		cout << *it << endl;
	it = L2.begin();
	it++; // Aponta para o segundo elemento
	L2.insert(it, 200);
	cout << "\nMostrando o SUPER nov¡ssimo elemento de L2:" << endl;
	for(it = L2.begin(); it != L2.end(); it++)
		cout << *it << endl;
	//Inserindo duas vezes o valor 50 na primeira posição
	L2.insert(L2.begin(), 2, 50);
	cout << "\nMostrando os ULTRAMENTE nov¡ssimos elementos de L2:" << endl;
	for(it = L2.begin(); it != L2.end(); it++)
		cout << *it << endl;
	//Apagando os dois primeiros números
	list<int>::iterator it2 = L2.begin();
	it2++;
	it2++;
	L2.erase(L2.begin(), it2);
	cout << "\nMostrando os ULTRAMENTE nov¡ssimos elementos de L2:" << endl;
	for(it = L2.begin(); it != L2.end(); it++)
		cout << *it << endl;
	//Remover todos os elementos de uma lista - Função Clear
	L2.clear();
	cout << "\nNovo tamanho de L2: " << L2.size() << endl;
	//Função splice, transfere elementos de uma lista para a outra
	list<int>lista1(2, 10), lista2(2, 20);
	it = lista1.begin();
	//Transfere todos os elementos de lista2 para lista1
	lista1.splice(it, lista2);
	cout << "\nElementos da lista1:\n";
	for(it = lista1.begin(); it != lista1.end(); it++)
		cout << *it << endl;
	cout << "\nTamanho de lista2: " << lista2.size() << endl;
	//Remover todos os elementos iguais a um valor
	//Função remove
	lista1.remove(20);
	cout << "\nNovos elementos da lista1:\n";
	for(it = lista1.begin(); it != lista1.end(); it++)
		cout << *it << endl;
	//Remove se ocorrer determinada condição
	//Função remove_if
	int vet2[] = {6, 8, 10, 5, 20, 21, 26, 28, 30, 34, 36, 98, 102};
	list<int>lista3(vet2, vet2 + 13);
	cout << "\nElementos da lista3 antes da remo‡Æo:\n";
	for(it = lista3.begin(); it != lista3.end(); it++)
		cout << *it << " ";
	//Removendo todos os elementos par
	lista3.remove_if(par);
	cout << "\n\nElementos da lista3 depois da remo‡Æo dos pares:\n";
	for(it = lista3.begin(); it != lista3.end(); it++)
		cout << *it << " ";
	cout << "\n";
	//Ordenação de Listas
	int vet3[] = {17, 60, 5, 30, 50};
	list<int> lista4(vet3, vet3 + 5); // Coloca vet3 duas vezes porque o primeiro é o próprio primeiro elemento (fechado) e depois o vet3+5 são os outros elementos, mas abertos, ou seja, precisa ter um número a mais!
	lista4.sort(); // sort sem parâmetro cria a lista crescentemente.
	cout << "\n\nElementos da lista4 Crescente:\n";
	for(it = lista4.begin(); it != lista4.end(); it++)
		cout << *it << " ";
	cout << "\n";
	//Ordenando Strings
	list<string> lista5;
	list<string>::iterator it5;
	lista5.push_back("Python");
	lista5.push_back("C++");
	lista5.push_back("Ruby");
	lista5.push_back("Haskell");
	lista5.sort();
	cout << "\nStrings da lista5 por ordem Alfabetica:\n";
	for(it5 = lista5.begin(); it5 != lista5.end(); it5++)
		cout << *it5 << endl;
	//Ordenando usando critério Próprio
	//Ex: Ordenando por tamanho da String
	lista5.sort(comparar_tamanho);
	cout << "\nStrings da lista5 por ordem de tamanho:\n";
	for(it5 = lista5.begin(); it5 != lista5.end(); it5++)
		cout << *it5 << " - tamanho: " << (*it5).length() << endl;
	return 0;
}
/*Na lista não se pode acessar os elementos
aleatóriamente, acessar diretamente o
elemento, ex: vet[10], vai direto nesse
elemento.*/
