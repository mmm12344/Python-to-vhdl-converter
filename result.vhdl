entity Mux8*1 is
port(
	inp0 : in std_logic;
	inp1 : in std_logic;
	inp2 : in std_logic;
	inp3 : in std_logic;
	inp4 : in std_logic;
	inp5 : in std_logic;
	inp6 : in std_logic;
	inp7 : in std_logic;
	select : in std_logic_vector(2 downto 0);
	
	opt : out std_logic
);
end Mux8*1
architecture behavior of Mux is

	begin
<<<<<<< HEAD
		process (inp0,inp1,inp2,inp3,inp4,inp5,inp6,inp7,select)
			case select is
				when " 000 " =>
					opt <= inp 0 ;
				when " 001 " =>
					opt <= inp 1 ;
				when " 010 " =>
					opt <= inp 2 ;
				when " 011 " =>
					opt <= inp 3 ;
				when " 100 " =>
					opt <= inp 4 ;
				when " 101 " =>
					opt <= inp 5 ;
				when " 110 " =>
					opt <= inp 6 ;
				when " 111 " =>
					opt <= inp 7 ;
			end case;
		
=======
		a <= b + a ;
		b <= b sll 1 srl 2 ;
		a ( 0 ) <= " 1 " ;
		a2 <= 2 ;
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
		
>>>>>>> 92956b04298c5476cc809c256ccf4f1a2cf8d872
		end process;

	end;