entity Mux is
port(
	A : in std_logic;
	C : in integer range 0 to 9;
	F : in integer;
	
	B : out std_logic
);
end Mux;
architecture behavior of Mux is
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

	signal D : std_logic_vector(2 downto 0);
	signal E : std_logic;

	constant mario : array ( 0 to 9 ) of std_logic_vector(9 downto 0);

	begin
		a <= b + a ;
		b <= b sll 1 srl 2 ;
		a ( 0 ) = " 10 " ;
		a2 <= 2 ;
		if mario = 1 then
			x <= 0 ;
		elsif mario = 2 then
			x <= 2 ;
		else
			x <= 1 ;
		end if;
		A <= not c ;
		A <= 1 ;
		rising_edge ( mario ) ;
		a_1 <= 0 ;
		mario <= 30 ** 4 mod 15 sra 40 ;
		for i in 1 to 10 loop
				i <= 1 ;
				while i < 4 loop
						mario <= 1 ;
						while i < 4 loop
								mario <= 1 ;
						end loop;
						for i in 1 to 10 loop
								i <= 1 ;
						end loop;
				end loop;
				for i in 1 to 10 loop
						i <= 1 ;
						while i < 4 loop
								mario <= 1 ;
								for i in 1 to 10 loop
										i <= 1 ;
								end loop;
						end loop;
				end loop;
				i <= 5 ;
		end loop;
		case i is
			when 3 =>
				mario <= 3 ;
			when 4 =>
				i <= 5 ;
		end case;
		while i < 5 loop
				mario <= 3 ;
				while mario = 3 loop
						i <= 5 ;
						while i < 4 loop
								mario <= 1 ;
						end loop;
						for i in 1 to 10 loop
								i <= 1 ;
						end loop;
				end loop;
				while i < 4 loop
						mario <= 1 ;
				end loop;
				for i in 1 to 10 loop
						i <= 1 ;
				end loop;
		end loop;
		process (x, y)
			if mario / 2 <= 2 then
				x <= 0 ;
			elsif mario * 2 > 2 then
				x <= 2 ;
			else
				y <= 0 ;
			end if;
		
			case mario is
				when 3 =>
					i <= 3 ;
				when 4 =>
					mario <= 5 ;
			end case;
		
			while mario < 5 loop
					i <= 4 ;
			end loop;
		
			mario <= 5 * 20 xnor 1 ;
		
		end process;

	end behavior;