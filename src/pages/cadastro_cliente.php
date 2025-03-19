<?php 
    include('../config/funcoes.php');
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php get_css(['cadastro_cliente', 'base', 'style']) ?>
    
    <title>Eao Quadrado</title>
</head>
<body>
    <header class="header">
    <?php get_header() ?>
    </header>

    <main>
        <div class="roadmap">Home / Cadastro de Cliente</div>
        <div class="register_client">
            <h2>Cadastro de Cliente</h2>
            <div class="form-container">
                <img src="../assets/img/foto_cliente.png" alt="foto do cliente" class="client-image">
                
                <form class="form">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="nome">Nome</label>
                            <input type="text" id="nome" name="nome" placeholder="John" required>
                        </div>
                        <div class="form-group">
                            <label for="sobrenome">Sobrenome</label>
                            <input type="text" id="sobrenome" name="sobrenome" placeholder="Doe" required>
                        </div>
                    </div>
    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="nascimento">Data de Nascimento</label>
                            <input type="date" id="nascimento" name="nascimento" required>
                        </div>
                        <div class="form-group">
                            <label for="cpf">CPF</label>
                            <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required>
                        </div>
                    </div>
    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="email">E-mail</label>
                            <input type="email" id="email" name="email" placeholder="johndoe@gmail.com" required>
                        </div>
                        <div class="form-group">
                            <label for="telefone">Número de Telefone</label>
                            <input type="text" id="telefone" name="telefone" placeholder="(67) 99999-9999" required>
                        </div>
                    </div>
    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="cep">CEP</label>
                            <input type="text" id="cep" name="cep" placeholder="7900000" required>
                        </div>
                        <div class="form-group">
                            <label for="endereco">Endereço</label>
                            <input type="text" id="endereco" name="endereco" placeholder="R.Clovis" required>
                        </div>
                    </div>
    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="bairro">Bairro</label>
                            <input type="text" id="bairro" name="bairro" placeholder="Pioneiro" required>
                        </div>
                        <div class="form-group">
                            <label for="complemento">Complemento (opcional)</label>
                            <input type="text" id="complemento" name="complemento">
                        </div>
                    </div>
    
                    <div class="password-group">
                        <div class="form-group">
                            <label for="senha">Senha</label>
                            <input type="password" id="senha" name="senha" placeholder="*********" required>
                        </div>
                        <div class="form-group">
                            <label for="confirmar-senha">Confirmar Senha</label>
                            <input type="password" id="confirmar-senha" name="confirmar-senha" placeholder="*********" required>
                        </div>
                    </div>
    
                    <div class="terms-container">
                        <div class="checkbox-container">
                            <input type="checkbox" id="termos" name="termos" required>
                            <label for="termos">Li e concordo com os <a href="#">Termos de Uso</a></label>
                        </div>
                        <div class="checkbox-container">
                            <input type="checkbox" id="politicas" name="politicas" required>
                            <label for="politicas">Li e concordo com as <a href="#">Políticas da Empresa</a></label>
                        </div>
                    </div>
    
                    <div class="buttons-container">
                        <button type="reset" class="button-cancel">Cancelar</button>
                        <button type="submit" class="button-confirm">Registrar</button>
                    </div>
                </form>
            </div>
        </div>
    </main>
    

    <footer>
    <?php get_footer() ?>
    </footer>
</body>
<script src="assets/js/script.js"></script>
</html>