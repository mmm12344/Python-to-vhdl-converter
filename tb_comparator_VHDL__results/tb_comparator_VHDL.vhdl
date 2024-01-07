library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity tb_comparator_VHDL is
end tb_comparator_VHDL;
architecture behavior of tb_comparator_VHDL is
	component comparator_VHDL is
	port(
		A : in std_logic_vector(1 downto 0);
		b : in std_logic_vector(1 downto 0);
		
		A_less_B : out std_logic;
		A_equal_B : out std_logic;
		A_greater_B : out std_logic
	);
	end component;

	signal A : std_logic;
	signal B : std_logic;
	signal A_less_B : std_logic;
	signal A_equal_B : std_logic;
	signal A_greater_B : std_logic;


	begin
		uut  : comparator_VHDL port map(A ,B ,A_less_B ,A_equal_B ,A_greater_B );
		process
		begin
			for i in 0 to 3 loop
					A <= to_std_logic_vector ( to_unsigned ( i , 2 ) ) ;
					B <= to_std_logic_vector ( to_unsigned ( i + 1 , 2 ) ) ;
					wait for 20 ns;
			end loop;
		
			for i in 0 to 3 loop
					A <= to_std_logic_vector ( to_unsigned ( i + 1 , 2 ) ) ;
					B <= to_std_logic_vector ( to_unsigned ( i , 2 ) ) ;
					wait for 20 ns;
			end loop;
		
			for i in 0 to 3 loop
					A <= to_std_logic_vector ( to_unsigned ( i , 2 ) ) ;
					B <= to_std_logic_vector ( to_unsigned ( i , 2 ) ) ;
					wait for 20 ns;
			end loop;
		
			wait;
		
		end process;

	end behavior;