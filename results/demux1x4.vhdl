entity deMux1x4 is
port(
	inp : in std_logic;
	select : in std_logic_vector(1 downto 0);
	
	opt0 : out std_logic;
	opt1 : out std_logic;
	opt2 : out std_logic;
	opt3 : out std_logic
);
end deMux1x4;
architecture behavior of deMux1x4 is
	component mux4x1 is
	port(
		inp0 : in std_logic;
		inp1 : in std_logic;
		inp2 : in std_logic;
		inp3 : in std_logic;
		select : in std_logic_vector(1 downto 0);
		
		opt : out std_logic
	);
	end component;
	component JKFlipFlop is
	port(
		clock : in std_logic;
		j : in std_logic;
		k : in std_logic;
		
		q : out std_logic;
		qb : out std_logic
	);
	end component;
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



	begin
		process (inp, select)
			case select is
				when " 00 " =>
					opt0 <= inp ;
					opt1 <= ' 0 ' ;
					opt2 <= ' 0 ' ;
					opt3 <= ' 0 ' ;
				when " 01 " =>
					opt0 <= ' 0 ' ;
					opt1 <= inp ;
					opt2 <= ' 0 ' ;
					opt3 <= ' 0 ' ;
				when " 10 " =>
					opt0 <= ' 0 ' ;
					opt1 <= ' 0 ' ;
					opt2 <= inp ;
					opt3 <= ' 0 ' ;
				when " 11 " =>
					opt0 <= ' 0 ' ;
					opt1 <= ' 0 ' ;
					opt2 <= ' 0 ' ;
					opt3 <= inp ;
			end case;
		
		end process;

	end behavior;