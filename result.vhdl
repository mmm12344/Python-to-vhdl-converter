entity FullAdder is
port(
	a : in std_logic;
	b : in std_logic;
	cin : in std_logic;
	
	sum : out std_logic;
	cout : out std_logic
);
end FullAdder
architecture behavior of FullAdder is
	signal x1 : std_logic;
	signal x2 : std_logic;
	signal x3 : std_logic;

	begin
		x1 <= a xor b ;
		x2 <= a and b ;
		x3 <= x1 and cin ;
		sum <= x1 xor cin ;
		cout <= x2 or x3 ;

	end;