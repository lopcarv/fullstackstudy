<?php
//mostrar erros
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// login.php — Autenticação segura com sessões PHP
session_start();

// Se o usuário já estiver logado, redireciona diretamente para a lista de produtos
if (!empty($_SESSION["usuario_id"])) {
    header("Location: produtos.php");
    exit;
}

require_once "config/conexao.php";

$erro = "";

// Processa a requisição quando o formulário é enviado via POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL);
    $senha = $_POST["senha"] ?? "";

    // Validação do Token CSRF para prevenir ataques de falsificação de requisição
    if (empty($_POST["csrf_token"]) || $_POST["csrf_token"] !== ($_SESSION["csrf_token"] ?? "")) {
        $erro = "Requisição inválida. Recarregue a página.";
    } elseif (!$email) {
        $erro = "E-mail inválido.";
    } else {
        // Uso de Prepared Statements para prevenir SQL Injection
        $stmt = getConexao()->prepare(
            "SELECT id, nome, senha FROM usuarios WHERE email = :email AND ativo = 1 LIMIT 1"
        );
        $stmt->execute(["email" => $email]);
        $usuario = $stmt->fetch();

        // Verificação da senha usando password_verify (compara com o hash bcrypt)
        if ($usuario && password_verify($senha, $usuario["senha"])) {
            // Segurança: Regenera o ID da sessão após o login bem-sucedido
            session_regenerate_id(true);
            $_SESSION["usuario_id"]   = $usuario["id"];
            $_SESSION["usuario_nome"] = $usuario["nome"];
            header("Location: produtos.php");
            exit;
        } else {
            // Mensagem genérica para não facilitar ataques de força bruta[cite: 1]
            $erro = "Credenciais inválidas. Tente novamente.";
        }
    }
}

// Geração de novo token CSRF para a sessão atual[cite: 1]
$_SESSION["csrf_token"] = bin2hex(random_bytes(32));
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Login — Inventário</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container d-flex justify-content-center align-items-center min-vh-100">
        <div class="card shadow p-4" style="width:400px">
            <h4 class="text-center mb-4">🔐 Inventário — Login</h4>
            
            <?php if ($erro): ?>
                <div class="alert alert-danger"><?= htmlspecialchars($erro) ?></div>
            <?php endif; ?>

            <form method="POST">
                <!-- Campo oculto com o Token CSRF -->
                <input type="hidden" name="csrf_token" value="<?= $_SESSION["csrf_token"] ?>">
                
                <div class="mb-3">
                    <label>E-mail</label>
                    <input type="email" name="email" class="form-control" required autofocus>
                </div>
                <div class="mb-3">
                    <label>Senha</label>
                    <input type="password" name="senha" class="form-control" required>
                </div>
                <button class="btn btn-primary w-100">Entrar</button>
            </form>
        </div>
    </div>
</body>
</html>