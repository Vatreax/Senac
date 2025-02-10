<?php
        echo "Exercício 1<br>";
        $nota1 = 10;
        $nota2 = 5;
        $notaMaxima = ($nota1 + $nota2) / 2;
        echo "As notas $nota1 e $nota2, dão a média de $notaMaxima ";

        echo "<hr>";

        echo "Exercício 2<br>";
        $preco = 100;
        $desconto = 10;
        $total =  100 - ($preco * $desconto) / 100;
        echo "O produto custa $preco, com um desconto de $desconto%, o valor cai para $total";

        echo "<hr>";

        echo "Exercício 3<br>";
        $idade1 = 18;
        $idade2 = 19;
        $idade3 = 19;
        $idade4 = 16;
        $idade5 = 18;

        $media = ($idade1 + $idade2 + $idade3 + $idade4 + $idade5) / 5;
        echo "A média de idade dos meus colegas é, $media"
?>