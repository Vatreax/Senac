<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="atividade3.css">
</head>
<body>
    <?php 
    for ($i=0; $i<101;$i++){
        if($i % 5 == 0 && $i % 3 == 0){
            echo "<br><h3>$i - A</h3>";

        } elseif($i % 5 == 0){
            echo "<br><h4>$i - B</h4>";

        } elseif($i % 3 == 0){
            echo "<br><h5>$i - AB</h5>";
        } else{
            echo "<br><p>$i</p>";
        }
             
    }
?>
</body>
</html>

