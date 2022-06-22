package util;

public class CurrencyConverter {
	
	public double conversion;
	public double valueDollars;
	
	public double IOF() {
		return (valueDollars*conversion) * 0.06;
	}
	
	public double total(){
		return (valueDollars*conversion) + IOF();	
	}
	
	public String toString() {
		return "AMOUNT TO BE PAID: R$ " + String.format("%.2f", total());
	}

}
