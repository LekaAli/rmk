<?php
require("class.phpmailer.php");
require_once('class.smtp.php');
$errorMSG = "";

// NAME
if (empty($_POST["name"])) {
    $errorMSG = "Name is required ";
} else {
    $name = $_POST["name"];
}

// EMAIL
if (empty($_POST["email"])) {
    $errorMSG .= "Email is required ";
} else {
    $email = $_POST["email"];
}

// MESSAGE
if (empty($_POST["message"])) {
    $errorMSG .= "Message is required ";
} else {
    $message = $_POST["message"];
}


// prepare email body text
$MsgContent = "";
$MsgContent .= "Name: ";
$MsgContent .= $name;
$MsgContent .= "<br> \n";
$MsgContent .= "Email: ";
$MsgContent .= $email;
$MsgContent .= "<br> \n";
$MsgContent .= "Message: ";
$MsgContent .= $message;
$MsgContent .= "<br> \n";

$mail = new PHPMailer();
$mail->IsSMTP();
//$mail->SMTPDebug = 1; 
$mail->SMTPAuth = true;
$mail->SMTPSecure = 'ssl'; 
$mail->Host = "mail.limeheritage.co.za"; 
$mail->Port = 465; 
$mail->IsHTML(true);
$mail->SetLanguage("tr", "phpmailer/language");
$mail->CharSet  ="utf-8";
$mail->Username = "_mainaccount@limeheritage.co.za"; 
$mail->Password = "@#Lim2252$%"; 
$mail->SetFrom("support@eheritage.gov.za", "Limpopo eHeritage"); 
$mail->AddAddress("serotoke@gmail.com"); 
$mail->Subject = "Subject"; 
$mail->Body = $MsgContent ; 

$success = $mail->Send();


if ($success && $errorMSG == ""){
   echo "success";
}else{
    if($errorMSG == ""){
        echo "Something went wrong :(";
    } else {
        echo $errorMSG . "<br> Mailer Error: " . $mail->ErrorInfo;
    }
}

?>
