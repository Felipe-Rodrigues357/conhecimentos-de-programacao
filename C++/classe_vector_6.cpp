#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
	vector<int> v(3);
	v[0]=1;
	v[1]=2;
	v[2]=3;
	cout<<"COMECO DA DEMONSTRACAO DOS ELEMENTOS DO VETOR!!\n";
	cout<<v.back()<<endl;
	cout<<v.front()<<endl;
	cout<<v.at(1)<<endl;
	cout<<"FIM DA DEMONSTRACAO!!\n\n";
	vector<int>::iterator it=v.begin();
	v.insert(it +2, 40);
	cout<<"INSERINDO UM ELEMENTO NO VETOR!\n";
	for(unsigned int i = 0; i < v.size(); i++)
	{
		cout<<v[i]<<endl;
	}
	cout<<"ANTES DO ERASE!!\n\n";
	v.erase(v.begin()+2); // Pode apagar qualquer elemento, só precisa colocar o local do elemento!
	cout<<"DEPOIS DO ERASE!\n";
	for(unsigned int i = 0; i < v.size(); i++)
	{
		cout<<v[i]<<endl;
	}
	return 0;
}