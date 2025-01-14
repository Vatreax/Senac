<?php
    session_start();
    include("connect.php");
 
    $nome = mysqli_real_escape_string($con,$_POST['nome']);
    $senha = mysqli_real_escape_string($con,$_POST['senha']);
 
    if(empty($nome) || empty($senha)){
        header("location: ../HTML/index.html");
    }

    if(empty($nome) || empty($senha)){
        echo "<script> alert('Por Favor, preencha todos os campos.');
            setTimeout(function(){
            window.location.href = '../HTML/index.html';
            },2000);
            </script>";
        exit();
    } 

    $query = "SELECT * FROM user WHERE nome = '{$nome}' AND senha = '{$senha}'";
    $result = mysqli_query($con, $query);

    $row = mysqli_num_rows($result);
    $retorno = mysqli_fetch_array($result);
    
    if($row>0){
        $_SESSION["nome"] = $nome;
        $_SESSION["setor"] = $retorno['setor'];

        echo "<p>Nome digitado: $nome
              <br>Senha digitada: $senha
              <br>Consulta: $row";
        
        if($_SESSION['setor'] == 'admin') {
            header('location: ../admin.html');
            exit();
        } else if($_SESSION['setor'] == 'user') {
            header('location: ../user.html');
            exit();
        } 
        exit();
    } 
?>

