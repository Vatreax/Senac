<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forms Recebido</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container-recebidos">
        <fieldset>
            <legend>Dados Pessoais</legend>
            <h1>Nome:</h1>
            <p><?php echo ($_POST["nome"]); ?></p>

            <h1>Sexo:</h1>
            <p><?php echo ($_POST["sexo"]); ?></p>

            <h1>Dada de Nascimento:</h1>
            <p><?php echo ($_POST["data"]) ?></p>

            <h1>Idade:</h1>
            <p><?php echo ($_POST["idade"]); ?></p>

            <h1>Sexo:</h1>
            <p><?php echo ($_POST["sexo"]); ?></p>
        </fieldset>

        <fieldset>
            <legend>Login</legend>
            <h1></h1>
    
        </fieldset>

        <fieldset>
            <legend>Dados Complementares</legend>
            <h1>CPF:</h1>
            <p><?php echo ($_POST["cpf"]); ?></p>

            <h1>RG:</h1>
            <p><?php echo ($_POST["rg"]); ?></p>

            <h1>Cidade:</h1>
            <p><?php echo ($_POST["cidade"]); ?></p>

            <h1>Estado:</h1>
            <p><?php echo ($_POST["estado"]); ?></p>

            <h1>Celular:</h1>
            <p><?php echo ($_POST["celular"]) ?></p>
        </fieldset>
    </div>
</body>
</html>