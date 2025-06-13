package aula13;

import java.util.Scanner;

public class Exer09 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Qual a Temperatura em Farenheit: ");
		double TemFar = scan.nextDouble();
		
		double TempCelsio = (5 * ((TemFar - 32)/9));
		
		
		System.out.println("O Valor da Temp em Celscios é: " + TempCelsio);
		
		
	}

}
