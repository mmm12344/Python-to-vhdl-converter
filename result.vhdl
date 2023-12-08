entity Mux is
port(
	A : in std_logic;
	
	B : out std_logic
);
end Mux
architecture behavior of Mux is
	signal D : std_logic;
	signal E : std_logic;

	begin
		a <= b + a ;
		b <= b sll 1 ;
		b <= 0 sla 2 ;
		mario <= 30 ** 4 mod 15 sra 40 ;
		if mario = 1 then
			mario <= 1 mod 10 ;
			x <= 4 ;
		elsif mario = 2 then
			m <= 1 sll 2 ;
		else
			mario <= 0 ;
			x <= 3 ;
		end if;
		for i in 1 to 10 loop
			i <= 1 ;
		end loop;
		case i is
			when 3 =>
				mario <= 3 ;
			when 4 =>
				i <= 5 ;
		end case;
		while i < 5 loop
			mario <= 3 ;
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
		
		end process;

	end;