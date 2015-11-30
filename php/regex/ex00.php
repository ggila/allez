#!/usr/bin/php
<?PHP

if ($argc > 1)
{
	$str = trim($argv[1]);
	print(preg_replace('~ {2,}|\t+~', ' ', $str)."\n");
}

?>
