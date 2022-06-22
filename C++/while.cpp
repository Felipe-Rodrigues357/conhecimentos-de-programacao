#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
	int num=1;
	while(num<=100)
	{
		if(num%2!=0)
		{
			num++;
			continue; // VOLTA PARA O INÍCIO DO LOOP
		}
		cout<<num<<"\n";
		num++;
	}
	return 0; 
}