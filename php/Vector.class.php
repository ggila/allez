<?PHP

require_once 'Color.class.php';

class Vector{

// static

public static $verbose = FALSE;

// dynamic

	private	$_x;
	private	$_y;
	private	$_z;
	private	$_w = 0.0;

	private function _verbose($str) {
		print($this.' '.$str.PHP_EOL);
	}

// getter

	public function getX() { return $this->_x; }
	public function getY() { return $this->_y; }
	public function getZ() { return $this->_z; }
	public function getW() { return $this->_w; }

// php special method

	public function __construct(array $kwargs) {
	//coordinate
		if (!isset($kwargs['dest'])
			exit('Error in Vector constructor : Vertex dest is  missing'.PHP_EOL);
		$this->_x(double)$kwargs['x']);
		$this->_y(double)$kwargs['y']);
		$this->_z(double)$kwargs['z']);
	//systeme de coordonnees homogenes
		if (isset($kwargs['w']))
			$this->_w = (double)$kwargs['w'];
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
