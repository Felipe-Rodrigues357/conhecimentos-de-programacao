#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
	vector<int> v;
	if(v.empty())
	{
		cout<<"Vetor Vazio!!\n";
	}
	else
	{
		cout<<"Vetor NAO vazio!!\n";
	}
	v.push_back(10);
	if(v.empty())
	{
		cout<<"Vetor Vazio!!\n";
	}
	else
	{
		cout<<"Vetor NAO vazio!!\n";
	}
	return 0;
}