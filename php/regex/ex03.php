#!/usr/bin/php
<?PHP

if (($str = file_get_contents($argv[1])) == NULL)
	exit(0);

preg_match_all("~<img[^>]+(?<=src)[\s]*=[\s]*\"([^\"]+)~", $str, $fit);

preg_match("~//(.*)~", $argv[1], $dir);
$dir = $dir[1];


if (!mkdir($dir))
{
	print("unable to create ".$dir);
	exit(0);
}


foreach ($fit[1] as $photo_url)
{
	$i = 0;
	$start = 0;
	if ($photo_url[0] == "/")
		$photo_url = $argv[1].$photo_url;
	while ($i < strlen($photo_url))
	{
		if ($photo_url[$i] == "/")
			$start = $i;
		$i++;
	}
	$photo = substr($photo_url, $start + 1, strlen($photo_url) - $start);
	$path = "./".$dir."/".$photo;
	file_put_contents($path, file_get_contents($photo_url));
}

?>
