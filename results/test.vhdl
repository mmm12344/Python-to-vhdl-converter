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
		count <= 0 ;
		demux_output <= " 0000 " ;
		seven_segment_patterns ( 0 ) <= " 0000001 " ;
		seven_segment_patterns ( 1 ) <= " 1001111 " ;
		seven_segment_patterns ( 2 ) <= " 0010010 " ;
		seven_segment_patterns ( 3 ) <= " 0000110 " ;
		seven_segment_patterns ( 4 ) <= " 1001100 " ;
		seven_segment_patterns ( 5 ) <= " 0100100 " ;
		seven_segment_patterns ( 6 ) <= " 0100000 " ;
		seven_segment_patterns ( 7 ) <= " 0001111 " ;
		seven_segment_patterns ( 8 ) <= " 0000000 " ;
		seven_segment_patterns ( 9 ) <= " 0000100 " ;
		process (clk,rst)
			if rst = ' 1 ' then
					count <= 0 ;
			elsif rising_edge ( clk ) then
					if count = 9 then
							count <= 0 ;
					else
							count <= count + 1 ;
					end if;
			else
					0 ;
			end if;
		
		end process;

	end behavior;