package aula13;

import java.util.Scanner;

public class Exer04 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Entre com a primeira nota: ");
		double nota1 = scan.nextInt();
		
		System.out.println("Entre com a segunda nota:");
		double nota2 = scan.nextInt();
		
		System.out.println("Entre com a Terceira nota:");
		double nota3 = scan.nextInt();
		
		System.out.println("Entre com a Quarta nota:");
		double nota4 = scan.nextInt();
		
		double media = (nota1 + nota2 + nota3 + nota4) / 4;
		System.out.println("A media é: " + media);

	}

}
