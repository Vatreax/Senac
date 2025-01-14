<?php
    include('connect.php');
    include('verification.php');

    $firstname = mysqli_real_escape_string($con,$_POST['firstname']);
    $lastname = mysqli_real_escape_string($con,$_POST['lastname']);
    $sex = mysqli_real_escape_string($con,$_POST['sex']);
    $fone = mysqli_real_escape_string($con,$_POST['fone']);
    $address = mysqli_real_escape_string($con,$_POST['address']);
    $email = mysqli_real_escape_string($con,$_POST['email']);

    $query = "INSERT INTO clientes VALUES
        (null,'{$firstname}','{$lastname}','{$sex}','{$fone}','{$address}','{$email}');";
    $result = mysqli_query($con,$query);

    if ($result == '') {
        echo "<script> alert('Por Favor, preencha todos os campos.');
            setTimeout(function(){
                window.location.href = '../user.html';},2000);</script>";
            exit();
        } else {
            echo "<script language='javascript'>
                window.alert('Cadastro efetuado com sucesso 👍');
                window.location.href='../user.html';
            </script>";
            exit();
        }        
?>