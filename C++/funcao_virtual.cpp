#include <iostream>
using namespace std;

class ClasseMae
{
public:
	virtual void showMessage() // Criando um objeto virtual
	{
		cout<<"Ola! Sou a Classe Mae!"<<endl;
	}	
};

class ClasseFilha : public ClasseMae
{
public:
	virtual void showMessage() // N�o � necess�rio colocar tamb�m na classe filha, depois de colocar na classe m�e, mas � utilizado usualmente.
	{
		cout<<"Ola! Sou a Classe Filha!"<<endl;
	}
};

void foo(ClasseMae* p)
{
	p->showMessage();
}
int main(int argc, char *argv[])
{
	ClasseMae mae;
	ClasseFilha filha;
	foo(&mae);
	foo(&filha);
	return 0;
}
/* Por padr�o C++ utiliza a liga��o prematura
se n�o for colocado o "Virtual, apareceria duas vezes
a mensagem da classe m�e... Colocando virtual voc� for�a
uma liga��o tardia, o que resulta na mostra das duas mensagens.*/
//Construtores n�o podem ser declarados virtuais.
//Fun��es virtuais acrescenta em cada objeto um ponteiro adicional oculto.
//Uma classe sem fun��es virtuais, n�o vai ter esse ponteiro.
//Destrutores podem ser declarados virtuais.