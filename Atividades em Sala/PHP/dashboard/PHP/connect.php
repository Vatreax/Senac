<?php
    // Connect Banco de Dados
    $host = "10.28.2.39";
    $usuario = "suporte";
    $senha = "suporte";
    $db = "banco139";

    $con = new mysqli($host, $usuario, $senha, $db);

    if ($con->connect_errno){
        echo "Falha na Conexão:(".$con->connect_errno.")".$con->connect_errno;
    } // else {
    //     echo "<p>Sucesso na Conexão: ".$con->host_info."";
    // }
?>