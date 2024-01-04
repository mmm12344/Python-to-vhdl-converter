library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity deMux1x4 is
port(
	inp : in std_logic;
	s : in std_logic_vector(1 downto 0);
	
	opt0 : out std_logic;
	opt1 : out std_logic;
	opt2 : out std_logic;
	opt3 : out std_logic
);
end deMux1x4;
architecture behavior of deMux1x4 is



	begin
		process (inp, s)
		begin
			case s is
				when "00" =>
						opt0 <= inp ;
						opt1 <= '0' ;
						opt2 <= '0' ;
						opt3 <= '0' ;
				when "01" =>
						opt0 <= '0' ;
						opt1 <= inp ;
						opt2 <= '0' ;
						opt3 <= '0' ;
				when "10" =>
						opt0 <= '0' ;
						opt1 <= '0' ;
						opt2 <= inp ;
						opt3 <= '0' ;
				when "11" =>
						opt0 <= '0' ;
						opt1 <= '0' ;
						opt2 <= '0' ;
						opt3 <= inp ;
			end case;
		
		end process;

	end behavior;