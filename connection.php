<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST'){

$registration_number = $_POST['reg-num'];
$name = $_POST['full-name'];
$email=$_POST['email'];
$phone=$_POST['number'];
$password = $_POST['password'];
}

$conn = mysql_connect('localhost', 'root', '01AkShAt04#','online_exams');
if($conn->connect_error){
	die('Connection Failed '.connect_error);
}

else{
	$stmt=$conn->prepare("INSERT INTO student ('Registration_number', 'Name', 'Email_Address', 'Phone', 'Password') VALUES (?,?,?,?,?) ");
	$stmt->bind_param("sssii",$registration_number,$name,$email,$phone,$password);
	$stmt->execute();
	echo"Record Inserted Successfully";
	$stmt->close();
	$conn->close();
}
?>

