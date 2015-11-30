<?PHP

////////////////////////J06/EX00//////////////////////////// 

class Color{
////////////////////////-------/////////////////////////////
///////////////////////| STATIC |///////////////////////////
////////////////////////-------/////////////////////////////
////ATTRIBUT
	public static $verbose = FALSE;
////METHOD
	public static function doc()
	{
		if (file_exists('Color.doc.txt'))
			print(file_get_contents('Color.doc.txt'));
	}
////////////////////////-------/////////////////////////////
//////////////////////| DYNAMIC |///////////////////////////
////////////////////////-------/////////////////////////////
////ATTRIBUT
	public $red = 0;
	public $green = 0;
	public $blue = 0;
////METHOD
	public function add(Color $rhs)
	{
		$new_col = new Color(array(
			'red' => $this->red + $rhs->red,
			'green' => $this->green + $rhs->green, 
			'blue' => $this->blue + $rhs->blue));
		return ($new_col);
	}

	public function sub(Color $rhs)
	{
		$new_col = new Color(array(
			'red' => $this->red - $rhs->red,
			'green' => $this->green + $rhs->green, 
			'blue' => $this->blue + $rhs->blue));
		return ($new_col);
	}

	public function mult($f)
	{
		$new_col = new Color(array(
			'red' => $this->red * $f,
			'green' => $this->green * $f, 
			'blue' => $this->blue * $f));
		return ($new_col);
	}

	private function _verbose($rhs)
	{	print($this.' '.$str.PHP_EOL);}

////////////////////////////////////////////////////////////
//////////////////PHP_SPECIAL_METHOD////////////////////////
////////////////////////////////////////////////////////////
	public function __construct(array $kwargs)
	{
		if (isset($kwargs['rgb']))
		{
			$rgb = intval($kwargs['rgb']);
			$this->red = ($rgb >> 16) & 0xff;;
			$this->green = ($rgb >> 8) & 0xff;;
			$this->blue = $rgb & 0xff;;
		}
		else if (isset($kwargs['red'], $kwargs['green'], $kwargs['blue']))
		{
			$this->red = intval($kwargs['red']);
			$this->green = intval($kwargs['green']);
			$this->blue = intval($kwargs['blue']);
		}
		if (self::$verbose == TRUE)
			$this->_verbose('constructed');
	}

	public function __destruct()
	{
		if (self::$verbose == TRUE)
			$this->_verbose('destructed');
	}

	public function __toString()
	{
		return sprintf('%s(% 3d, % 3d, % 3d)',
			get_called_class(),
			$this->red,
			$this->green,
			$this->blue);
	}

	public function __get($att)
	{	print('attemtp to access \''.$att.PHP_EOL);}

	public function __set($att, $val) 
	{	print('attemtp to set \''.$att.' attribute to \''.$value.PHP_EOL);}

	public function __call($f, $args)
	{	print('attemtp to call function \''.$f.'with params '.$args.PHP_EOL);}

	public static function __callstatic($att, $val) 
	{	print('attemtp to set \''.$att.' attribute to \''.$value.PHP_EOL);}

	public function __clone()
	{
		if (self::$verbose == TRUE)
			$this->_verbose('cloned');
	}
} 
////////////////////-----------------///////////////////////
///////////////////| COLOR_CLASS_END |//////////////////////
////////////////////-----------------///////////////////////

$var = new Color(array('red'=>100, 'green'=>0, 'blue'=>100));
$var2 = new Color(array('red'=>100, 'green'=>100, 'blue'=>100));

?>
