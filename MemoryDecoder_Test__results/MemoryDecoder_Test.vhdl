library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity MemoryAddressDecoder is
port(
	address : in std_logic_vector(2 downto 0);
	
	S : out std_logic_vector(7 downto 0)
);
end MemoryAddressDecoder;
architecture behavior of MemoryAddressDecoder is
	component decoder3x8 is
	port(
		inp : in std_logic_vector(2 downto 0);
		
		opt : out std_logic_vector(7 downto 0)
	);
	end component;

	signal D : std_logic_vector(7 downto 0);


	begin
	decoderinst  : decoder3x8 port map(address ,D );
		S <= D ;

	end behavior;