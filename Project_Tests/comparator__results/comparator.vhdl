library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity comparator_VHDL  is
port(
	A : in std_logic_vector(1 downto 0);
	b : in std_logic_vector(1 downto 0);
	
	A_less_B : out std_logic;
	A_equal_B : out std_logic;
	A_greater_B : out std_logic
);
end comparator_VHDL ;
architecture comparator_structural of comparator_VHDL  is

	signal tmp1 : std_logic;
	signal tmp2 : std_logic;
	signal tmp3 : std_logic;
	signal tmp4 : std_logic;
	signal tmp5 : std_logic;
	signal tmp6 : std_logic;
	signal tmp7 : std_logic;
	signal tmp8 : std_logic;


	begin
		tmp1 <= A ( 1 ) xnor B ( 1 ) ;
		tmp2 <= A ( 0 ) xnor B ( 0 ) ;
		A_equal_B <= tmp1 and tmp2 ;
		tmp3 <= ( ( not A ( 0 ) ) and ( not A ( 1 ) ) ) and B ( 0 ) ;
		tmp4 <= not A ( 1 ) and B ( 1 ) ;
		tmp5 <= not A ( 0 ) and B ( 1 ) and B ( 0 ) ;
		A_less_B <= tmp3 or tmp4 or tmp5 ;
		tmp6 <= not B ( 0 ) and not B ( 1 ) and A ( 0 ) ;
		tmp7 <= not B ( 1 ) and A ( 1 ) ;
		tmp8 <= not B ( 0 ) and A ( 1 ) and A ( 0 ) ;
		A_greater_B <= tmp6 or tmp7 or tmp8 ;

	end comparator_structural;