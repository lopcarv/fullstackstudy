<?php
// 1. Incluir a conexão com o banco
require_once 'conexao.php';

// 2. Verificar se os dados foram enviados via POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    
    // 3. Captura e Sanitização Básica (Foco em Segurança)
    $nome  = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_SPECIAL_CHARS);
    $qtd   = filter_input(INPUT_POST, 'qtd', FILTER_VALIDATE_INT);
    $preco = filter_input(INPUT_POST, 'preco', FILTER_VALIDATE_FLOAT);

    // 4. Validação Simples
    if ($nome && $qtd !== false && $preco !== false) {
        try {
            // 5. Preparar a Query (Prevenção contra SQL Injection)
            $sql = "INSERT INTO produtos (nome_produto, quantidade, preco_unitario) 
                    VALUES (:nome, :qtd, :preco)";
            
            $stmt = $pdo->prepare($sql);
            
            // 6. Vincular os parâmetros
            $stmt->bindParam(':nome', $nome);
            $stmt->bindParam(':qtd', $qtd);
            $stmt->bindParam(':preco', $preco);
            
            // 7. Executar
            if ($stmt->execute()) {
                // Sucesso: Redireciona para o dashboard com mensagem
                header("Location: ../views/dashboard.php?status=sucesso");
                exit;
            }
        } catch (PDOException $e) {
            // Erro técnico (Logar internamente, não exibir ao usuário)
            die("Erro ao salvar no banco de dados: " . $e->getMessage());
        }
    } else {
        // Dados inválidos
        header("Location: ../views/cadastro_item.php?status=erro_validacao");
        exit;
    }
} else {
    // Acesso direto não permitido
    header("Location: ../views/cadastro_item.php");
    exit;
}