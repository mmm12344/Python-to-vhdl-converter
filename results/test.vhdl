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
		s : in std_logic_vector(1 downto 0);
		
		opt : out std_logic
	);
	end component;
	component deMux1x4 is
	port(
		inp : in std_logic;
		s : in std_logic_vector(1 downto 0);
		
		opt0 : out std_logic;
		opt1 : out std_logic;
		opt2 : out std_logic;
		opt3 : out std_logic
	);
	end component;
	component JKFlipFlop is
	port(
		clock : in std_logic;
		j : in std_logic;
		k : in std_logic;
		
		q : out std_logic;
		qb : out std_logic
	);
	end component;

	signal D : std_logic_vector(2 downto 0);
	signal E : std_logic;

	constant seven_segement_pattern : array ( 0 to 9 ) of std_logic_vector(6 downto 0);

	begin
		count <= 0 ;
		demux_output <= "0000" ;
		seven_segment_patterns ( 0 ) <= "0000001" ;
		seven_segment_patterns ( 1 ) <= "1001111" ;
		seven_segment_patterns ( 2 ) <= "0010010" ;
		seven_segment_patterns ( 3 ) <= "0000110" ;
		seven_segment_patterns ( 4 ) <= "1001100" ;
		seven_segment_patterns ( 5 ) <= "0100100" ;
		seven_segment_patterns ( 6 ) <= "0100000" ;
		seven_segment_patterns ( 7 ) <= "0001111" ;
		seven_segment_patterns ( 8 ) <= "0000000" ;
		seven_segment_patterns ( 9 ) <= "0000100" ;
		m <=	"1000" when ( a ) = "00" else
			"0100" when ( a ) = "01" else
		process (clock)
		begin
			qmario <= TMP ;
		
			qkdjfksjf <= not TMP ;
		
			if j = '0' and k = '0' then
					TMP <= TMP ;
			elsif j = '1' and k = '1' then
					TMP <= not TMP ;
			elsif j = '0' and k = '1' then
					TMP <= '0' ;
			else
					TMP <= '1' ;
			end if;
		
			qmario <= TMP ;
		
			qkdjfksjf <= not TMP ;
		
			mario <= 9 ;
		
			a <= 3 ;
		
			case ( a ) is
				when "00" =>
						m <= "1000" ;
				when "01" =>
						m <= "0100" ;
						case ( a ) is
							when "00" =>
									m <= "1000" ;
									case ( a ) is
										when "00" =>
												m <= "1000" ;
										when "01" =>
												m <= "0100" ;
									end case;
							when "01" =>
									m <= "0100" ;
						end case;
				when "10" =>
						m <= "0010" ;
				when "11" =>
						m <= "0001" ;
			end case;
		
		end process;
		m <=	"1000" when ( a ) = "00" else
			"0100" when ( a ) = "01" else
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
					case ( a ) is
						when "00" =>
								m <= "1000" ;
						when "01" =>
								m <= "0100" ;
					end case;
			end if;
		
			q <= TMP ;
		
			q <= not TMP ;
		
			case ( a ) is
				when "01" =>
						if mario = 2 then
								x <= 0 ;
						end if;
			end case;
		
		end process;
	c1  : mux4x1 port map(mario, m , ar);
	end behavior;