entity FullAdder is
port(
	a : in std_logic;
	b : in std_logic;
	cin : in std_logic;
	
	sum : out std_logic;
	cout : out std_logic
);
<<<<<<< HEAD
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
=======
end Mux;
architecture behavior of Mux is
	signal D : std_logic_vector(2 downto 0);
	signal E : std_logic;

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
>>>>>>> a40965c7fbb90e18bb87794573fe4ec36c7f4ff9

	end behavior;