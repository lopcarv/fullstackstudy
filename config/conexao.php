<?php
/**
 * ARQUIVO: config/conexao.php
 * OBJETIVO: Gerenciar a conexão com o BD usando PDO.
 * CURSO: Técnico em Informática / Desenvolvimento de Sistemas
 */

// Configurações do Banco de Dados (Ambiente Local)
define('DB_HOST', 'localhost');
define('DB_NAME', 'sistema_inventario'); // Nome do banco que você criou no PHPMyAdmin
define('DB_USER', 'root');               // Usuário padrão do XAMPP
define('DB_PASS', '');                   // Senha padrão do XAMPP (vazia)

/**
 * Função para retornar a instância da conexão.
 * Implementa o padrão de garantir uma única conexão por execução.
 */
function getConexao() {
    try {
        // DSN (Data Source Name)
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        
        $opcoes = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,    // Lança exceções em caso de erro
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Retorna dados como array associativo
            PDO::ATTR_EMULATE_PREPARES => false,            // Usa prepared statements reais
        ];

        return new PDO($dsn, DB_USER, DB_PASS, $opcoes);

    } catch (PDOException $e) {
        // Em produção, nunca mostre o erro detalhado ($e->getMessage()) ao usuário.
        // Aqui, como estamos em ambiente de ensino, vamos exibir para facilitar o debug.
        die("ERRO TÉCNICO: Não foi possível conectar ao banco de dados. <br> Detalhes: " . $e->getMessage());
    }
}