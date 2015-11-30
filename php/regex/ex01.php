#!/usr/bin/php
<?PHP

function ft_get_month($month)
{
	if (preg_match("~anv~",$month))
		return 1;
	if (preg_match("~vrier~",$month))
		return 2;
	if (preg_match("~ars~",$month))
		return 3;
	if (preg_match("~vril~",$month))
		return 4;
	if (preg_match("~ai~",$month))
		return 5;
	if (preg_match("~uin~",$month))
		return 6;
	if (preg_match("~uillet~",$month))
		return 7;
	if (preg_match("~[Aa]o~",$month))
		return 8;
	if (preg_match("~tembr~",$month))
		return 9;
	if (preg_match("~ctobre~",$month))
		return 10;
	if (preg_match("~vembre~",$month))
		return 11;
	if (preg_match("~cembre~",$month))
		return 12;
}

function ft_wf()
{
	print("Wrong Format\n");
	exit(0);
}

$str = $argv[1];

$l_day = "[Ll]undi|[Mm]ardi|[Mm]ercredi|[Jj]eudi|[Vv]endredi|[Ss]amedi|[Dd]imanche";
$l_month = "[Jj]anvier|[Ff][eé]vrier|[Mm]ars|[Aa]vril|[Mm]ai|[Jj]uin|[Jj]uillet|[Aa]o[ûu]t|[Ss]eptembre|[Oo]ctobre|[Nn]ovembre|[Dd][ée]cembre";

$pattern = "~^(".$l_day.") ([0-9]{1,2}) (".$l_month.") ([0-9]{1,4}) ([[0-9]{2}):([[0-9]{2}):([[0-9]{2})$~";
preg_match($pattern, $str, $fit);

if (!$fit[0])
	ft_wf();

$fit[3] = ft_get_month($fit[3]);
date_default_timezone_set("Europe/Prague");
print(mktime($fit[5], $fit[6], $fit[7], $fit[3], $fit[2], $fit[4])."\n");

?>
