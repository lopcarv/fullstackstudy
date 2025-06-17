package aula13;


import java.util.Scanner;
public class Exer12 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Qual a sua altura? ");
		double a = scan.nextDouble();
		
		double pesoIdeal = (72.7  * a) -58;
		
		
		System.out.println(" Seu peso ideal deve ser " + pesoIdeal );
		

	}

}

