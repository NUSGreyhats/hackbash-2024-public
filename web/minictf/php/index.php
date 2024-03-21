<?php error_reporting(0); ?>
<?php 
    if (!isset($_GET['page'])) {
        header('Location: /?page=zeyu');
        die();
    }
?>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>About Me</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
	<div class="lazarus-pit">
        <h1>About <?php echo ucwords($_GET['page']); ?></h1>
        <list>
            <a href="?page=zeyu">About Zeyu</a>
            <a href="?page=devesh">About Devesh</a>
            <a href="?page=php">About PHP</a>
            <a href="?page=flag">About Flag</a>
        </list>
        <p>
            <?php include "/var/www/html/".$_GET['page'] ?>
        </p>
    </div>

</body>
</html>