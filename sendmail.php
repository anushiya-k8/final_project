<?php

include("dbconnect.php");
extract($_REQUEST);

$mq=mysqli_query($connect,"select max(id) from nin_register");
$mr=mysqli_fetch_array($mq);
$id=$mr['max(id)']+1;
$ins=mysqli_query($connect,"insert into nin_register(id) values($id)");

$q3=mysqli_query($connect,"select * from signup_data where bcode='$bc' && upi_code='$upi' order by id desc");
$r3=mysqli_fetch_array($q3);
$qr2=$r3['url_data'];

$v1=explode("|",$qr2);

if($qr!="")
{
$e1=explode(",",$qr);
	foreach($e1 as $e2)
	{
		echo $e2;
		
		foreach($v1 as $v2)
		{
		$v3=explode("=",$v2);
			if($e2==$v3[0])
			{
			
			mysqli_query($connect,"update nin_register set $e2='$v3[1]' where id=$id");
			}
		}
		
	}
}

////////
include("email.php");
extract($_REQUEST);
		$objEmail	=	new CI_Email();
		//$objEmail->from("iotcloudadmin@iotcloud.co.in", "Info");
		$objEmail->from("iotcloudadmin@iotcloud.co.in", "Info");
		
		$objEmail->to("$email");
		//$objEmail->cc($txt_cc);
		//$objEmail->bcc($txt_bcc);
		$objEmail->subject("Sign Up - Register Confirmation");
		
		
		$objEmail->message("$mess");
		
	
			/*if(file_exists("report.xls"))
			{
				$objEmail->attach("report.xls");
			}*/
			if ($objEmail->send())
			{	
			//echo 'mail sent successfully';
			}
			else
			{	
			//echo 'failed';
			}

?>
<span style="color:#009900">Registered Success, Username and Password sent to Your Mail...</span>



