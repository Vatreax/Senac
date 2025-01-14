<?php
    session_start();
    include("index.php");
    include("verification.php");

    if($_SESSION['setor'] != 'admin'){
        header("location: index.php");
        exit();
    }
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabela com DIV</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(130deg, #000000, #851405, #000000);
        }

        .table-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 600px;
            transition: all 0.3s ease;
        }

        .table-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
        }

        .table-header, .table-row {
            display: flex;
            justify-content: space-between;
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }

        .table-header {
            background-color: #c2220d;
            color: white;
            font-size: 16px;
            font-weight: bold;
        }

        .table-row {
            background-color: #f9f9f9;
            font-size: 14px;
            color: #333;
        }

        .table-row:nth-child(even) {
            background-color: #f1f1f1;
        }

        .table-row:hover {
            background-color: #f0a6a6;
            cursor: pointer;
        }

        .table-cell {
            width: 45%;
            padding: 8px;
        }
    </style>
</head>
<body>
    <a href="logout.php" class="sair">Sair</a>
    <div class="table-container">
        <div class="table-header">
            <div class="table-cell">Atributo</div>
            <div class="table-cell">Valor</div>
        </div>
        <div class="table-row">
            <div class="table-cell">Nome</div>
            <div class="table-cell"><?php echo $nome?></div>
        </div>
        <div class="table-row">
            <div class="table-cell">Senha</div>
            <div class="table-cell"><?php echo $senha?></div>
        </div>
    </div>
</body>
</html>
