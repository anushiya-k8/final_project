<?php

include("dbconnect.php");
extract($_REQUEST);
$mq=mysqli_query($connect,"select max(id) from signup_data");
$mr=mysqli_fetch_array($mq);
$id=$mr['max(id)']+1;

$ins=mysqli_query($connect,"insert into signup_data(id,bcode,url_data,upi_code,web_url) values($id,'$bc','$mdata','$upi','$wu')");

//https://19hourit.com

if($wu=="gamingzone.in.net")
{
?>

<h5 style="color:#FFFFFF">Registering...</h5>
<?php
}
else
{
?><span style="color:#009900">Registering...</span><?php
}
?>
<script>
//Using setTimeout to execute a function after 5 seconds.
setTimeout(function () {
   //Redirect with JavaScript
   window.parent.location.href= 'https://<?php echo $wu; ?>/store1.php?bc=<?php echo $bc; ?>&upi=<?php echo $upi; ?>&mess=<?php echo $mess; ?>&email=<?php echo $email; ?>';
}, 5000);
</script>


