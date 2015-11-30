#!/usr/bin/php
<?PHP

function ft_strtoupper($array)
{
	print("\n---------------------\n");
	print_r($array);
	print("\n---------------------\n");
	return $array[1].strtoupper($array[2]);
}

function ft_balise($array)
{
	print("\n--------balise-------\n");
	print_r($array);
	print("\n---------------------\n");
	$str = $array;
	$str = preg_replace_callback("~(title=\")([^\"]*)~", ft_strtoupper, $str);
	$str = preg_replace_callback("~(>)([^<]+)~",ft_strtoupper, $str);
	return $str;
}

if ($argc != 2)
	exit(0);

if (!is_file($argv[1]))
{
	print("no file called".$argv[1]."\n");
	exit(0);
}

$str = file_get_contents($argv[1]);

$str = preg_replace_callback("~<a.*</a>~", ft_balise, $str);

print_r($str);

?>
