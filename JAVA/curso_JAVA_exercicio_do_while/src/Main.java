import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double c, f; 
		char resp; 
		c = 0;
		f = 0;
		do {
			System.out.print("Digite a Temperatura em Celcius: ");
			c = sc.nextDouble();
			f = (9*c)/5 + 32;
			System.out.printf("Temperatura em Fahrenheit: %.1f%n", f);
			System.out.print("Deseja Repetir (s/n)? ");
			resp = sc.next().charAt(0);
		} while(resp != 'n');
		System.out.println("FIM DO PROGRAMA!");
		sc.close();
	}

}
