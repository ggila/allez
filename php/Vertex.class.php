<?PHP

require_once 'Color.class.php';

class Vertex{

// static

public static $verbose = FALSE;

// dynamic

private	$_x;
	private	$_y;
	private	$_z;
	private	$_w = 1.0;
	private	$_color;

	private function _verbose($str)
	{	print($this.' '.$str.PHP_EOL);}

// getter, setter

	public function getX() { return $this->_x; }
	public function getY() { return $this->_y; }
	public function getZ() { return $this->_z; }
	public function getW() { return $this->_w; }
	public function getColor() { return $this->_color; }

	public function setX($v) { return $this->_x = $v; }
	public function setY($v) { return $this->_y = $v; }
	public function setZ($v) { return $this->_z = $v; }
	public function setW($v) { return $this->_w = $v; }
	public function setColor(Color $v) { return $this->_color = $v; }

// php special method

	public function __construct(array $kwargs){

		if (!isset($kwargs['x']) || !isset($kwargs['y']) || !isset($kwargs['z']))
			exit('Error in Vertex constructor : coordinate missing'.PHP_EOL);
		$this->setX((double)$kwargs['x']);
		$this->setY((double)$kwargs['y']);
		$this->setZ((double)$kwargs['z']);

		if (isset($kwargs['w']))
			$this->_w = (double)$kwargs['w'];
		$this->_color = isset($kwargs['color']) ? clone $kwargs['color'] :
						new Color(array('rgb' => 0xffffff));
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
		$str =  sprintf('%s(%.2f, %.2f, %.2f, %.2f'
			, get_called_class()
			, $this->_x
			, $this->_y
			, $this->_z
			, $this->_w);
		if (self::$verbose == TRUE)
			$str .= ', '.$this->_color;
		$str .= ')';
		return $str;
	}
}

?>
