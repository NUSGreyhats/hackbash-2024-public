<?php 
if (!isset($_GET['page'])) {
    $_GET['page'] = 'home.php';
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Tools</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .header {
            background-color: #0073e6;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        .content {
            padding: 20px;
        }
        .tool {
            background-color: #fff;
            margin: 20px 0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .tool h2 {
            color: #333;
        }
        .tool-description {
            color: #666;
        }
    </style>
</head>
<body>

<?php include $_GET['page']; ?>

</body>
</html>
