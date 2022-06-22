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
	virtual void showMessage() // Não é necessário colocar também na classe filha, depois de colocar na classe mãe, mas é utilizado usualmente.
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
/* Por padrão C++ utiliza a ligação prematura
se não for colocado o "Virtual, apareceria duas vezes
a mensagem da classe mãe... Colocando virtual você força
uma ligação tardia, o que resulta na mostra das duas mensagens.*/
//Construtores não podem ser declarados virtuais.
//Funções virtuais acrescenta em cada objeto um ponteiro adicional oculto.
//Uma classe sem funções virtuais, não vai ter esse ponteiro.
//Destrutores podem ser declarados virtuais.