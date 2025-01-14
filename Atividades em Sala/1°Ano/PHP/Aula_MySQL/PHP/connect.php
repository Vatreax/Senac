<?php
    $host= "10.28.2.39";
    $usuario= "suporte";
    $senha= "suporte";
    $bd= "banco139";

    $con = new mysqli($host,$usuario,$senha,$bd);

    if($con -> connect_errno){
        echo "Falha na Conexão: (".$con->connect_errno.")".$con->connect_error;
    } else{
        echo $con->host_info. "\nAtendido";
    }
