<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
</head>
<body>
    <h1>Resultado</h1>
<?php
    $anos = $_POST["idade"];
    
    if ($anos > 18) {
        echo "Você é Maior de Idade";
    }
    else{
        echo "Você é Menor de Idade";
    }
?>
</body>
</html>