library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

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

	signal D : std_logic_vector(2 downto 0);
	signal E : std_logic;

	constant seven_segement_pattern : array ( 0 to 9 ) of std_logic_vector(6 downto 0);

	begin
		seven_segement_pattern ( 0 ) <= " 0000001 " ;
		seven_segement_pattern ( 1 ) <= " 343454534 " ;
		seven_segement_pattern ( 2 ) <= " 343454534 " ;
		seven_segement_pattern ( 3 ) <= " 343454534 " ;
		seven_segement_pattern ( 4 ) <= " 343454534 " ;
		seven_segement_pattern ( 5 ) <= " 343454534 " ;
		a <= b + a ;
		b <= b sll 1 srl 2 ;
		a ( 0 ) = " 10 " ;
		a2 <= 2 ;
		if mario = 1 then
				if mario = 2 then
						x <= 2 ;
						if v = 3 then
								x <= 10 ;
						else
								x <= 9 ;
						end if;
				elsif mario = 4 then
						x <= 3 ;
						if v = 3 then
								x <= 10 ;
						else
								x <= 9 ;
						end if;
				else
						x <= 3 ;
						if v = 3 then
								x <= 10 ;
								while i < 4 loop
										mario <= 1 ;
										while i < 4 loop
												mario <= 1 ;
										end loop;
										for i in 1 to 10 loop
												i <= 1 ;
										end loop;
								end loop;
						else
								x <= 9 ;
						end if;
				end if;
		elsif mario = 4 then
				x <= 3 ;
		else
				x <= 1 ;
				if v = 3 then
						x <= 10 ;
				elsif mario = 1 then
						omar <= 3 ;
				else
						x <= 9 ;
				end if;
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
										if v = 3 then
												x <= 10 ;
										else
												x <= 0 ;
										end if;
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
						if v = 3 then
								x <= 10 ;
								if v = 3 then
										x <= 10 ;
								else
										x <= 9 ;
								end if;
						else
								x <= 9 ;
						end if;
				end loop;
				for i in 1 to 10 loop
						i <= 1 ;
						if v = 3 then
								x <= 10 ;
						else
								x <= 9 ;
						end if;
				end loop;
		end loop;
		process (x, y)
			if mario / 2 <= 2 then
					x <= 0 ;
			elsif mario * 2 > 2 then
					x <= 2 ;
					if v = 3 then
							x <= 10 ;
					else
							x <= 9 ;
					end if;
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
					if v = 3 then
							x <= 10 ;
					else
							x <= 9 ;
					end if;
			end loop;
		
			mario <= 5 * 20 xnor 1 ;
		
		end process;

	end behavior;