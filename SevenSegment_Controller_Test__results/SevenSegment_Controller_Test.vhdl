library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity _7segController is
port(
	clk : in std_logic;
	rst : in std_logic;
	number : in std_logic_vector(3 downto 0);
	
	seg : out std_logic_vector(6 downto 0);
	anode : out std_logic_vector(3 downto 0)
);
end _7segController;
architecture behavior of _7segController is
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

	signal count : integer range 0 to 9;
	signal demux_output : std_logic_vector(3 downto 0);

	constant seven_segment_patterns : array ( 0 to 9 ) of std_logic_vector(6 downto 0);

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
	deMux_inst  : deMux1x4 port map('1' ,count ,demux_output ( 0 ) ,demux_output ( 1 ) ,demux_output ( 2 ) ,demux_output ( 3 ) );
		process ( clk , rst )
		begin
			if rst = '1' then
					count <= 0 ;
			elsif rising_edge ( clk ) then
					if count = 9 then
							count <= 0 ;
					else
							count <= count + 1 ;
					end if;
			end if;
		
		end process;
		seg <= seven_segment_patterns ( count ) ;
		anode <= demux_output ;

	end behavior;