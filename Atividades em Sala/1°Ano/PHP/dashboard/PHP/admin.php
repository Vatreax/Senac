<?php
    session_start();
    include('verification.php');

    if ($_SESSION['setor'] != 'admin'){
        header('location: ../HTML/index.html');
    }
    
    echo "<a href='../HTML/index.html'>Voltar</a>";

?>
