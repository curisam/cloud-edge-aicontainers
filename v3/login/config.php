<?php
define("DB_SERVER", "localhost");
define("DB_USERNAME", "evc");
define("DB_PASSWORD", "evc");
define("DB_NAME", "evc");

# Connection
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

# Check connection
if (!$link) {
  die("Connection failed: " . mysqli_connect_error());
}
