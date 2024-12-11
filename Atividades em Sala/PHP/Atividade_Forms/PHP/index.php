<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exibição de Dados</title>
    <link rel="stylesheet" href="../CSS/style.css">
</head>
<body>

    <div class="container">
        <h2 class="title">Dados do Usuário</h2>

        <div class="data-row">
            <div class="label">Nome</div>
            <div class="value"><?php echo ($_POST['nome']); ?></div>
        </div>

        <div class="data-row">
            <div class="label">RG</div>
            <div class="value"><?php echo ($_POST['Rg']); ?></div>
        </div>

        <div class="data-row">
            <div class="label">CPF</div>
            <div class="value"><?php echo ($_POST['CPF']); ?></div>
        </div>

        <div class="data-row">
            <div class="label">Endereço</div>
            <div class="value"><?php echo ($_POST['Endereco']); ?></div>
        </div>

        <div class="data-row">
            <div class="label">Idade</div>
            <div class="value"><?php echo ($_POST['Ano']); ?></div>
        </div>
    </div>

	<div class="container">
		<h2 class="title">Ano</h2>
		<div class="data-row2"><?php echo ($_POST['data']); ?></div>
	</div>

	<div class="container">
		<h2 class="title">Época do Ano Favorita</h2>
		<div class="data-row2"><?php 	$epoca =$_POST["epoca"]; for($i=0; $i<count($epoca);$i++){ echo "$epoca[$i]<br>";}?></div>
	</div>

	

</body>
</html>
