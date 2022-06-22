#include <iostream>
using namespace std;
class Pai1
{
public:
	void foo()
	{
		cout << "Sou o Pai1" << endl;
	}
};
class Pai2
{
public:
	void foo()
	{
		cout << "Sou o Pai2" << endl;
	}
};
class Filha : public Pai1, public Pai2
{

};
int main(int argc, char *argv[])
{
	Filha f;
	f.Pai1::foo();
	f.Pai2::foo();
	return 0;
}