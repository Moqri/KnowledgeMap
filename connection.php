<?php
  $dbhost="127.0.0.1";
  $dbuser="root";
  $dbpass="12345";
  
  $db="kmap";
  
  $conn=mysql_connect($dbhost,$dbuser,$dbpass);
  mysql_select_db($db)
?>
