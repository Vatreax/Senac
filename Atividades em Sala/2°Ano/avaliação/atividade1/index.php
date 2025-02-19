<?php
    $num1 =$_POST["n1"];
    $num2 =$_POST["n2"];

    $soma = $num1 + $num2;
    $sub = $num1 + $num2;
    $multi = $num1 * $num2;
    $divisa = $num1 / $num2;
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>resultado</title>
</head>
<body>
    <h1>Resultado do Calculo:</h1>
    <p>Numéros - <?php echo"$num1"?> e <?php echo"$num2"?></p>
    <p>Soma = <?php echo"$soma"?></p>
    <p>Subtração = <?php echo"$sub"?></p>
    <p>Multiplicação = <?php echo "$multi"?></p>
    <p>Divisão = <?php echo "$divisa"?></p>
</body>
</html>