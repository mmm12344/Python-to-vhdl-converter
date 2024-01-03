library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

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



	begin
		process (clock)
		begin
			if rising_edge ( clock ) then
					if j = '0' and k = '0' then
							TMP <= TMP ;
					elsif j = '1' and k = '1' then
							TMP <= not TMP ;
					elsif j = '0' and k = '1' then
							TMP <= '0' ;
					else
							TMP <= '1' ;
					end if;
			end if;
		
			q <= TMP ;
		
			q <= not TMP ;
		
		end process;

	end behavior;