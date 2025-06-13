package aula13;
import java.util.Scanner;

public class Exer08 {

	public static void main(String[] args) {
	
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Quanto você ganha por Hora: ");
		double ValorHora = scan.nextDouble();
		System.out.println("Quantas hora voce trabalhou no mês: ");
		double HoraTrabalhada = scan.nextDouble();
		
		double Salario = ValorHora * HoraTrabalhada;
		
		System.out.println("O Valor do Salario: " + Salario);
		 


	}

}
