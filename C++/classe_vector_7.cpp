#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
	vector<int> a(2, 20);
	vector<int> b(3, 10);
	a.swap(b);
	for(unsigned int i = 0; i < a.size(); i++)
		cout << a[i] << endl;
	cout<<"FIM DO a!"<<endl;
	for(unsigned int i = 0; i < b.size(); i++)
		cout << b[i] << endl;
	cout<<"\nANTES DO CLEAR!!\n\n";
	cout<<a.size()<<" ELEMENTOS DENTRO DE a"<<endl;
	cout<<b.size()<<" ELEMENTOS DENTRO DE b"<<endl;
	a.clear(); // Limpa TODOS os elementos do vetor.
	b.clear();
	cout<<"\nDEPOIS DO CLEAR!!\n\n";
	cout<<a.size()<<" ELEMENTOS DENTRO DE a DEPOIS DO CLEAR"<<endl;
	cout<<b.size()<<" ELEMENTOS DENTRO DE b DEPOIS DO CLEAR"<<endl;
	return 0;
}