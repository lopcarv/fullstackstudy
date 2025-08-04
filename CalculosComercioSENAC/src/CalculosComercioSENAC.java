import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.text.DecimalFormat;

public class CalculosComercioSENAC extends JFrame {
    private JTextField custoField, margemLucroField, receitaTotalField, lucroField;
    private JTextField precoVendaField, custoVariavelField, custosFixosField;
    private JTextField precoOriginalField, descontoField;
    private JTextArea resultadoArea;

    public CalculosComercioSENAC() {
        setTitle("CalComSENAC - Cálculos Comerciais | Desenvolvido por Luis Carvalho - SENAC NEP Capanema");
        setSize(800, 600);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel topo = new JPanel(new BorderLayout());
        JLabel logo = new JLabel(new ImageIcon("senac_logo.png"));
        topo.add(logo, BorderLayout.WEST);
        JLabel titulo = new JLabel("CalComSENAC - Calculadora Comercial | SENAC NEP Capanema", JLabel.CENTER);
        titulo.setFont(new Font("Arial", Font.BOLD, 22));
        topo.add(titulo, BorderLayout.CENTER);
        add(topo, BorderLayout.NORTH);

        JPanel painel = new JPanel();
        painel.setLayout(new GridLayout(12, 2, 8, 8));
        painel.setBackground(Color.WHITE);

        custoField = new JTextField();
        margemLucroField = new JTextField();
        receitaTotalField = new JTextField();
        lucroField = new JTextField();
        precoVendaField = new JTextField();
        custoVariavelField = new JTextField();
        custosFixosField = new JTextField();
        precoOriginalField = new JTextField();
        descontoField = new JTextField();

        painel.add(new JLabel("Custo:")); painel.add(custoField);
        painel.add(new JLabel("Margem de Lucro (%):")); painel.add(margemLucroField);
        painel.add(new JLabel("Receita Total:")); painel.add(receitaTotalField);
        painel.add(new JLabel("Lucro:")); painel.add(lucroField);
        painel.add(new JLabel("Preço de Venda:")); painel.add(precoVendaField);
        painel.add(new JLabel("Custo Variável:")); painel.add(custoVariavelField);
        painel.add(new JLabel("Custos Fixos:")); painel.add(custosFixosField);
        painel.add(new JLabel("Preço Original:")); painel.add(precoOriginalField);
        painel.add(new JLabel("Desconto (%):")); painel.add(descontoField);

        JButton calcularBtn = new JButton("Calcular Tudo");
        painel.add(calcularBtn);

        resultadoArea = new JTextArea();
        resultadoArea.setEditable(false);
        JScrollPane scroll = new JScrollPane(resultadoArea);

        add(painel, BorderLayout.CENTER);
        add(scroll, BorderLayout.SOUTH);

        JPanel rodape = new JPanel();
        rodape.add(new JLabel("Desenvolvido por Luis Carvalho | SENAC NEP Capanema"));
        add(rodape, BorderLayout.PAGE_END);

        JMenuBar menu = new JMenuBar();
        JMenu sobre = new JMenu("Sobre");
        JMenuItem info = new JMenuItem("Informações do Projeto");
        info.addActionListener(e -> JOptionPane.showMessageDialog(this,
                "Calculadora Comercial para SENAC - NEP Capanema\nAutor: Luis Carvalho\nRealiza os principais cálculos de comércio."));
        sobre.add(info);
        menu.add(sobre);
        setJMenuBar(menu);

        calcularBtn.addActionListener(e -> calcularTudo());
    }

    private void calcularTudo() {
        DecimalFormat df = new DecimalFormat("0.00");
        resultadoArea.setText("");

        try {
            double custo = Double.parseDouble(custoField.getText());
            double margem = Double.parseDouble(margemLucroField.getText()) / 100;
            double receita = Double.parseDouble(receitaTotalField.getText());
            double lucro = Double.parseDouble(lucroField.getText());
            double precoVenda = Double.parseDouble(precoVendaField.getText());
            double custoVariavel = Double.parseDouble(custoVariavelField.getText());
            double custosFixos = Double.parseDouble(custosFixosField.getText());
            double precoOriginal = Double.parseDouble(precoOriginalField.getText());
            double desconto = Double.parseDouble(descontoField.getText()) / 100;

            double precoVendaCalc = custo + (custo * margem);
            double margemLucroCalc = (lucro / receita) * 100;
            double markup = precoVenda / custo;
            double pontoEquilibrio = custosFixos / (precoVenda - custoVariavel);
            double precoComDesconto = precoOriginal - (precoOriginal * desconto);

            resultadoArea.append("📊 Resultados:\n");
            resultadoArea.append("Preço de Venda = " + df.format(precoVendaCalc) + "\n");
            resultadoArea.append("Margem de Lucro (%) = " + df.format(margemLucroCalc) + "%\n");
            resultadoArea.append("Markup = " + df.format(markup) + "\n");
            resultadoArea.append("Ponto de Equilíbrio = " + df.format(pontoEquilibrio) + " unidades\n");
            resultadoArea.append("Preço com Desconto = " + df.format(precoComDesconto) + "\n");

        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Preencha corretamente todos os campos com números válidos.");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new CalculosComercioSENAC().setVisible(true));
    }
}
