#!/usr/local/bin/php
<?php  
$a = exec('python getr.py');
echo "This page has been viewed ";
echo $a; 
echo " times! <br> <br>";
exec('python incr.py');


$user_agent = $_SERVER['HTTP_USER_AGENT']; 

if (preg_match('/MSIE/i', $user_agent)) { 
	exec('python ie.py');
}

else if (preg_match('/Firefox/i', $user_agent)) { 
	exec('python firefox.py');
}

else if (preg_match('/Chrome/i', $user_agent)) { 
	exec('python chrome.py');
}

else if (preg_match('/Safari/i', $user_agent)) { 
	exec('python safari.py');
}

include("ie.txt"); 
echo " Visitors are explorers of the internet. <br>";
include("firefox.txt"); 
echo " Visitors are into foxes and fire. <br>";
include("chrome.txt"); 
echo " Visitors are chromed out. <br>";
include("safari.txt"); 
echo " Visitors are on safari. \n";
?>

