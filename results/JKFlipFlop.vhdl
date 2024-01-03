entity JKFlipFlop is
port(
	clock : in std_logic;
	j : in std_logic;
	k : in std_logic;
	
	q : out std_logic;
	qb : out std_logic
);
end JKFlipFlop;
architecture behavior of JKFlipFlop is
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
		process (clock)
			if rising_edge ( clock ) then
			if j = ' 0 ' and k = ' 0 ' then
				TMP <= TMP ;
			elsif j = ' 1 ' and k = ' 1 ' then
				TMP <= not TMP ;
			elsif j = ' 0 ' and k = ' 1 ' then
				TMP <= ' 0 ' ;
			else
				TMP <= ' 1 ' ;
			end if;
		
			q <= TMP ;
		
			q <= not TMP ;
		
		end process;

	end behavior;