package aula13;

import java.util.Scanner;

public class Exer06 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Entre com o raio do Circulo: ");
		double raio = scan.nextDouble();
		
		double area = Math.PI * Math.pow(raio, 2);
		
		System.out.println("A área do circulo é : " + area);
		
		

	}

}
