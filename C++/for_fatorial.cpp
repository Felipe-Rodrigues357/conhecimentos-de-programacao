#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	int num, fat=1;
	cout<<"Digite o numero desejado: ";
	cin>>num;
	for(int i = 1; i <num ; i++)
	{
		fat=fat*(i+1);
	}
	cout<<"FATORIAL DE "<<num<<" = "<<fat;
	return 0;
}