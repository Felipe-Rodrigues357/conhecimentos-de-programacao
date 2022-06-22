#include <iostream>
using namespace std;

int num_global = 12;

void foo()
{
	int num=10;
	cout<<num<<endl;
	cout<<num_global<<endl;
}
int main(int argc, char** argv)
{
	cout<<num_global<<endl;
	foo();
	return 0;
}