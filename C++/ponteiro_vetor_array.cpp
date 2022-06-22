#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	int array[]={1,2,3,4,5};
	int* parray=&array[4];
	int** pparray=&parray;
	cout<<**pparray;
	return 0;
}