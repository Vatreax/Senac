<?php
    echo "Exercício 1<br>";
    $nome = "João";
    $sobreNome = 'Oliveira';
    $nomeCompleto = $nome.$sobreNome;
    echo "<br>Seu nome é $sobreNome, ele Tem ".strlen(string: $nomeCompleto)." caracteres";
    
    $meuNome = 'Rafael Montiel';
    $endereco = 'Casa';
    echo "<hr>";
    echo  "Exercício 2<br>";
    
    echo "<br>Olá, $meuNome. Seu novo endereço: $endereco foi registrado no sistema!";

    echo "<hr>";
    echo "Exercício 3<br>";
    $curso = 'Podôlogia';
    $idade = 20;
    $cidade = 'Campo Grande';
    $estado = 'MS';
    $serie_filme = 'As Branquelas';
    echo "<br>Meu nome é $meuNome, tenho $idade anos, faço o curso de $curso moro na cidade $cidade, $estado. Assisto a série/filme $serie_filme";


?>