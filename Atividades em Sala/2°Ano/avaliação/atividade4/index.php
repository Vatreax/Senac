<?php 
    function emQuadrado(){
    $altura = $_POST["n1"];
    $largura = $_POST["n2"];

    $area = $altura * $largura;   
    
    echo "<h1>Dados do Quadrado:</h1>";
    echo "<p>Largura =  $largura </p>";
    echo "<p>Altura =   $altura</p>";
    echo "<p>Área=  $area </p>";
    echo "<h4>O Quadrado/Retângulo:</h2><br>";
    echo '<div style="height: '.$altura.'px; width: '.$largura.'px; border: 2px black solid;"></div>';
    }
?>


    


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php emQuadrado() ?>
</body>
</html>