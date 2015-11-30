<?PHP

////////////////////////J06/EX01//////////////////////////// 

require_once 'Color.class.php';

class Vertex{
////////////////////////-------/////////////////////////////
///////////////////////| STATIC |///////////////////////////
////////////////////////-------/////////////////////////////
////ATTRIBUT
	public static $verbose = FALSE;
////METHOD
	public static function doc()
	{
		if (file_exists('Vertex.doc.txt'))
			print(file_get_contents('Vertex.doc.txt'));
	}
////////////////////////-------/////////////////////////////
//////////////////////| DYNAMIC |///////////////////////////
////////////////////////-------/////////////////////////////
////ATTRIBUT
	private	$_x;
	private	$_y;
	private	$_z;
	private	$_w = 1.0;
	private	$_color;
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

	private function _verbose($str)
	{	print($this.' '.$str.PHP_EOL);}

////////////////////////////////////////////////////////////
//////////////////PHP_SPECIAL_METHOD////////////////////////
////////////////////////////////////////////////////////////
	public function __construct(array $kwargs)
	{
		if (!isset($kwargs['x']) || !isset($kwargs['y']) || !isset($kwargs['z']))
			exit('Error in Vertex constructor : coordinate missing'.PHP_EOL);
		$this->_x = (double)$kwargs['x'];
		$this->_y = (double)$kwargs['y'];
		$this->_z = (double)$kwargs['z'];
		if (isset($kwargs['w']))
			$this->_w = (double)$kwargs['w'];
		if (isset($kwargs['color']))
			$this->_color = clone $kwargs['color'];
		else
			$this->_color = new Color(array('rgb' => 0xffffff));
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
		$str =  sprintf('%s(%.2f, %.2f, %.2f ; %.2f'
			, get_called_class()
			, $this->_x
			, $this->_y
			, $this->_z
			, $this->_w);
		if (self::$verbose == TRUE)
			$str .= $this->_color;
		$str .= ')';
		return $str;
	}

	public function __get($att)
	{	print('attemtp to access \''.$att.PHP_EOL);}

	public function __set($att, $val) 
	{	print('attemtp to set \''.$att.' attribute to \''.$value.PHP_EOL);}

	public function __call($f, $args)
	{	print('attemtp to call function \''.$f.'with params '.$args.PHP_EOL);}

	public static function __callstatic($att, $val) 
	{	print('attemtp to set \''.$att.' attribute to \''.$value.PHP_EOL);}
/*
	public function __clone()
	{	print('_clone called'.PHP_EOL);}
 */} 
////////////////////-----------------///////////////////////
///////////////////| COLOR_CLASS_END |//////////////////////
////////////////////-----------------///////////////////////

?>
