package aula13;
import java.util.Scanner;

public class Exer13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada de dados
        System.out.print("Quanto você ganha por hora? R$ ");
        double salarioHora = scanner.nextDouble();

        System.out.print("Número de horas trabalhadas no mês: ");
        int horasTrabalhadas = scanner.nextInt();

        // Cálculo do salário bruto
        double salarioBruto = salarioHora * horasTrabalhadas;

        // Cálculo dos descontos
        double ir = salarioBruto * 0.11;     // Imposto de Renda (11%)
        double inss = salarioBruto * 0.08;   // INSS (8%)
        double sindicato = salarioBruto * 0.05; // Sindicato (5%)

        double totalDescontos = ir + inss + sindicato;

        // Cálculo do salário líquido
        double salarioLiquido = salarioBruto - totalDescontos;

        // Exibição dos resultados
        System.out.println("\n+-----------------------------+");
        System.out.printf("+ Salário Bruto : R$ %.2f\n", salarioBruto);
        System.out.printf("- IR (11%%)      : R$ %.2f\n", ir);
        System.out.printf("- INSS (8%%)     : R$ %.2f\n", inss);
        System.out.printf("- Sindicato (5%%): R$ %.2f\n", sindicato);
        System.out.println("+-----------------------------+");
        System.out.printf("= Salário Líquido : R$ %.2f\n", salarioLiquido);
        System.out.println("+-----------------------------+");

        scanner.close();
    }
}
