package application;

import java.util.Locale;
import java.util.Scanner;

import entities.Bank;

public class Program {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		double deposit = 0;
		System.out.print("Enter Account Number: ");
		int account = sc.nextInt();
		System.out.print("Enter Account Holder: ");
		sc.nextLine();
		String name = sc.nextLine();
		System.out.print("Is there an Initial Deposit (Y/N): ");
		char answer = sc.next().charAt(0);
		if (answer == 'y') {
			System.out.print("Enter initial Deposit value: ");
			deposit = sc.nextDouble();
		}
				
		Bank bank = new Bank(account, name, deposit);
						
		System.out.println();
		System.out.println("ACCOUNT DATA:");
		System.out.println(bank);
		
		System.out.println();
		System.out.print("Enter a deposit value: ");
		deposit = sc.nextDouble();
		bank.Deposit(deposit);
		System.out.println("Updated Account Data:");
		System.out.println(bank);
		
		System.out.println();
		System.out.print("Enter a withdraw value: ");
		deposit = sc.nextDouble();
		bank.Withdraw(deposit);
		System.out.println("Updated Account Data:");
		System.out.println(bank);
		
		
		sc.close();
		
	}

}
