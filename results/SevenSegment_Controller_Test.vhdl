entity _7segController is
port(
	clk : in std_logic;
	rst : in std_logic;
	number : in std_logic_vector(3 downto 0);
	
	seg : out std_logic_vector(6 downto 0);
	anode : out std_logic_vector(3 downto 0)
);
end _7segController;
architecture behavior of _7segController is
	component deMux1x4 is
	port(
		inp : in std_logic;
		select : in std_logic_vector(1 downto 0);
		
		opt0 : out std_logic;
		opt1 : out std_logic;
		opt2 : out std_logic;
		opt3 : out std_logic
	);
	end component;

	signal count : std_logic_vector(3 downto 0);
	signal D : std_logic_vector(3 downto 0);

	begin
		S <= D ;

	end behavior;