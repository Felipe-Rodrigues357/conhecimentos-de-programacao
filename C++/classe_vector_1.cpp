#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
	vector<int> v;
	v.push_back(20); // Insere elementos no vetor
	v.push_back(30);
	v.push_back(40);
	int tam=v.size();
	for(int i = 0; i < tam; i++)
	{
		   cout<<v[i]<<"\n";	
	}
	return 0;
}