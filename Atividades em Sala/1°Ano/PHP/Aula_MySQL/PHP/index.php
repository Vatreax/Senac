<?php 

    session_start();
    include("connect.php");

    $nome = mysqli_real_escape_string($con,$_POST['nome']);
    $senha = mysqli_real_escape_string($con,$_POST['senha']);

    if(empty($nome)||empty($senha)){
        header("location: index.html");
    }
    if(empty($nome)||empty($senha)){
        echo "<script> alert('Por Favor, preencha todos os campos.');
        setTimeout(function(){
            window.location.href = './connect.php';},2000);
        </script>";
        exit();
    }
    else{
        echo "Nome: $nome<br>
              Senha: $senha";

    }

    $query = "select * from user where nome = '{$nome}' and senha = '{$senha}'";

    $result = mysqli_query($con,$query);
    $row = mysqli_num_rows($result);

    $retorno = mysqli_fetch_array($result);
    echo "<br>Consulta Realizada: $row";


    if ($row>0){
        $_SESSION['nome'] = $nome;
        $_SESSION['senha'] = $senha;
        $_SESSION['setor'] = $retorno['setor'];
        echo $_SESSION['setor'];

        if ($_SESSION["setor"] == 'admin'){
            header("location:./admin.php");
            exit();
        }

        else if($_SESSION['setor'] == 'user'){
            header("location: ./user.php");
        }
        exit();
    }

