library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity deMux1x8 is
port(
	inp : in std_logic;
	s : in std_logic_vector(2 downto 0);
	
	opt0 : out std_logic;
	opt1 : out std_logic;
	opt2 : out std_logic;
	opt3 : out std_logic;
	opt4 : out std_logic;
	opt5 : out std_logic;
	opt6 : out std_logic;
	opt7 : out std_logic
);
end deMux1x8;
architecture behavior of deMux1x8 is



	begin
		process (inp, s)
		begin
			case s is
				when " 000 " =>
						opt0 <= inp ;
						opt1 <= ' 0 ' ;
						opt2 <= ' 0 ' ;
						opt3 <= ' 0 ' ;
						opt4 <= ' 0 ' ;
						opt5 <= ' 0 ' ;
						opt6 <= ' 0 ' ;
						opt7 <= ' 0 ' ;
				when " 001 " =>
						opt0 <= ' 0 ' ;
						opt1 <= inp ;
						opt2 <= ' 0 ' ;
						opt3 <= ' 0 ' ;
						opt4 <= ' 0 ' ;
						opt5 <= ' 0 ' ;
						opt6 <= ' 0 ' ;
						opt7 <= ' 0 ' ;
				when " 010 " =>
						opt0 <= ' 0 ' ;
						opt1 <= ' 0 ' ;
						opt2 <= inp ;
						opt3 <= ' 0 ' ;
						opt4 <= ' 0 ' ;
						opt5 <= ' 0 ' ;
						opt6 <= ' 0 ' ;
						opt7 <= ' 0 ' ;
				when " 011 " =>
						opt0 <= ' 0 ' ;
						opt1 <= ' 0 ' ;
						opt2 <= ' 0 ' ;
						opt3 <= inp ;
						opt4 <= ' 0 ' ;
						opt5 <= ' 0 ' ;
						opt6 <= ' 0 ' ;
						opt7 <= ' 0 ' ;
				when " 100 " =>
						opt0 <= ' 0 ' ;
						opt1 <= ' 0 ' ;
						opt2 <= ' 0 ' ;
						opt3 <= ' 0 ' ;
						opt4 <= inp ;
						opt5 <= ' 0 ' ;
						opt6 <= ' 0 ' ;
						opt7 <= ' 0 ' ;
				when " 101 " =>
						opt0 <= ' 0 ' ;
						opt1 <= ' 0 ' ;
						opt2 <= ' 0 ' ;
						opt3 <= ' 0 ' ;
						opt4 <= ' 0 ' ;
						opt5 <= inp ;
						opt6 <= ' 0 ' ;
						opt7 <= ' 0 ' ;
				when " 110 " =>
						opt0 <= ' 0 ' ;
						opt1 <= ' 0 ' ;
						opt2 <= ' 0 ' ;
						opt3 <= ' 0 ' ;
						opt4 <= ' 0 ' ;
						opt5 <= ' 0 ' ;
						opt6 <= inp ;
						opt7 <= ' 0 ' ;
				when " 111 " =>
						opt0 <= ' 0 ' ;
						opt1 <= ' 0 ' ;
						opt2 <= ' 0 ' ;
						opt3 <= ' 0 ' ;
						opt4 <= ' 0 ' ;
						opt5 <= ' 0 ' ;
						opt6 <= ' 0 ' ;
						opt7 <= inp ;
			end case;
		
		end process;

	end behavior;