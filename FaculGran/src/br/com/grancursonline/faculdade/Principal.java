
package br.com.grancursonline.faculdade;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args){

        int a, b, resposta;
        String nome = "";
        double percentual;

        Scanner in = new Scanner(System.in);

        System.out.print("Digite o primeiro numero: ");
        a = in.nextInt();

        System.out.print("Digite o segundo numero: ");
        b = in.nextInt();

        System.out.print("Digite o seu nome: ");
        nome = in.next();

        System.out.print("Digite um numero percentual: ");
        percentual = in.nextDouble();

        resposta = a + b;

        System.out.println("A soma dos dois numeros eh: " + resposta);
        System.out.println("Quem escreveu foi: " + nome);
    }
}
