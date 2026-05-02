<?php include '../includes/header.php'; ?>

<div class="card shadow-sm">
    <div class="card-header bg-primary text-white">
        <h4 class="mb-0">Cadastrar Novo Item</h4>
    </div>
    <div class="card-body">
        <form action="../core/processar_produto.php" method="POST">
            <div class="mb-3">
                <label class="form-label">Nome do Produto</label>
                <input type="text" name="nome" class="form-control" required placeholder="Ex: Teclado Mecânico">
            </div>
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label class="form-label">Quantidade</label>
                    <input type="number" name="qtd" class="form-control" min="0" value="0">
                </div>
                <div class="col-md-6 mb-3">
                    <label class="form-label">Preço Unitário (R$)</label>
                    <input type="number" step="0.01" name="preco" class="form-control" required>
                </div>
            </div>
            <button type="submit" class="btn btn-success w-100">Salvar no Inventário</button>
        </form>
    </div>
</div>

<?php include '../includes/footer.php'; ?>