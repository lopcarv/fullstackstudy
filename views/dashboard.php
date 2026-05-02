<?php 
// 1. Caminho correto para o core a partir da pasta views
require_once __DIR__ . '/../core/conexao.php';
include __DIR__ . '/../includes/header.php'; 

// 2. Tentar buscar os dados
try {
    $stmt = $pdo->query("SELECT * FROM produtos ORDER BY id_produto DESC");
    $produtos = $stmt->fetchAll();
} catch (PDOException $e) {
    // Se houver erro de banco, ele será impresso aqui
    echo "<div class='alert alert-danger'>Erro no Banco: " . $e->getMessage() . "</div>";
    $produtos = [];
}
?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h2>📋 Painel de Inventário</h2>
    <a href="cadastro_item.php" class="btn btn-primary">+ Novo Produto</a>
</div>

<div class="card shadow">
    <div class="card-body">
        <table class="table table-hover">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Produto</th>
                    <th>Qtd.</th>
                    <th>Preço (R$)</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <?php if ($produtos): ?>
                    <?php foreach ($produtos as $p): ?>
                    <tr>
                        <td>#<?= $p['id_produto'] ?></td>
                        <td><?= htmlspecialchars($p['nome_produto']) ?></td>
                        <td><?= $p['quantidade'] ?></td>
                        <td>R$ <?= number_format($p['preco_unitario'], 2, ',', '.') ?></td>
                        <td><button class="btn btn-sm btn-info">Ver</button></td>
                    </tr>
                    <?php endforeach; ?>
                <?php else: ?>
                    <tr><td colspan="5" class="text-center">Nenhum item encontrado.</td></tr>
                <?php endif; ?>
            </tbody>
        </table>
    </div>
</div>

<?php include __DIR__ . '/../includes/footer.php'; ?>