<?php
    include("connect.php");

    $query = "select * from produtos";
    $result = mysqli_query($con, $query);
    
    // $retorno = mysqli_fetch_array($result);

//    foreach ($retorno as $value){
//     echo "$key: $value <br>";
//    }

    // echo "<br>";
    // echo $retorno["id"];
    // echo "<br>";
    // echo $retorno["nome"];
    // echo "<br>";
    // echo $retorno["descricao"];
    // echo "<br>";
    // echo $retorno["preco"];




?>
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="../CSS/table.css">
        <link rel="stylesheet" href="../CSS/admin.css">
    </head>
    <body>
    <div class="dashboard">
        <!-- Menu Lateral -->
        <div class="sidebar">
            <div class="sidebar-header">
                <h2>Admin</h2>
            </div>
            <ul class="sidebar-menu">
                <li><a href="../admin.html">Dashboard</a></li>
                <li><a href="#">Usuários</a></li>
                <li><a href="#">Relatórios</a></li>
                <li><a href="#">Configurações</a></li>
                <li><a href="./index.html">Logout</a></li>
            </ul>
        </div>
        <table border=1>
            <thead>
                <tr>
                <th>id</th>
                <th>nome</th>
                <th>descricao</th>
                <th>valor</th>
<?php while($retorno = mysqli_fetch_array($result)){ ?>
            <tbody>
                <tr>
                    <td><?php echo $retorno["id"];?></td>
                    <td><?php echo $retorno["nome"];?></td>
                    <td><?php echo $retorno["descricao"];?></td>
                    <td><?php echo $retorno["preco"];?></td>
                </tr>
        <?php }
        ?>
            </tbody>
            </table>
        </thead>  
    </body>
    </html>