package application;

import java.util.Locale;
import java.util.Scanner;

import util.CurrencyConverter;

public class Program {

	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		CurrencyConverter currencyConverter = new CurrencyConverter();
		
		System.out.print("CONVERSION RATE: ");
		currencyConverter.conversion = sc.nextDouble();
		
		System.out.print("DOLLARS: ");
		currencyConverter.valueDollars = sc.nextDouble();
		
		System.out.println(currencyConverter);
		
		sc.close();

	}

}
