entity mux4x1 is
port(
	inp0 : in std_logic;
	inp1 : in std_logic;
	inp2 : in std_logic;
	inp3 : in std_logic;
	select : in std_logic_vector(1 downto 0);
	
	opt : out std_logic
);
end mux4x1;
architecture behavior of mux4x1 is
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
		process (inp0,inp1,inp2,inp3,select)
			case select is
				when " 00 " =>
					opt <= inp0 ;
				when " 01 " =>
					opt <= inp1 ;
				when " 10 " =>
					opt <= inp2 ;
				when " 11 " =>
					opt <= inp3 ;
			end case;
		
		end process;

	end behavior;