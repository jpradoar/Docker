<?php

require_once 'dbconfig.php';

$stmt = $db_con->prepare("SELECT * FROM members");
$stmt->execute();



?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title> PHP MYSQL LIST</title>
</head>
<body>
<div align="center">
<h3> PHP MYSQL LIST </h3>
<table cellspacing="0" border="1">
<thead>
<tr>
<th>id</th>
<th>name</th>
<th>address</th>
</tr>
</thead>
<tbody>
<?php
while($row=$stmt->fetch(PDO::FETCH_ASSOC))
{
?>
	<tr>
	<td><?php echo $row['id']; ?></td>
	<td><?php echo $row['name']; ?></td>
	<td><?php echo $row['address']; ?></td>
	</tr>
<?php
	}
	$stmt = null;
?>
</tbody>
</table> 
</div>

</body>
</html>
