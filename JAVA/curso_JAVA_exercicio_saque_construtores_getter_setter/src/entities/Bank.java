package entities;

public class Bank {

	private int account;
	private String name;
	private double deposit;
	
	public Bank(int account, String name, double deposit) {
		this.account = account;
		this.name = name;
		this.deposit = deposit;
	}

	
	public Bank(int account, String name) {
		this.account = account;
		this.name = name;
	}


	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}

	public double getDeposit() {
		return deposit;
	}

	public int getAccount() {
		return account;
	}
	
	public void Deposit (double deposit) {
		this.deposit += deposit; 
	}
	
	public void Withdraw (double deposit) {
		this.deposit -= deposit + 5; 
	}
	
	public String toString() {
		return "Account " + account + ", Holder: " + name + ", Balance: $" + String.format("%.2f", deposit);
	}
	
	
	
}
