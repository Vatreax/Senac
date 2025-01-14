<?php
    if($_SESSION['setor'] != 'admin') {
        echo 'Erro!';
        header('location: ../HTML/index.html');
        exit();
    }

?>