entity decoder3x8 is
port(
	inp : in std_logic_vector(2 downto 0);
	
	opt : out std_logic_vector(7 downto 0)
);
end decoder3x8;
architecture behavior of decoder3x8 is
	component decoder3x8 is
	port(
		inp : in std_logic_vector(2 downto 0);
		
		opt : out std_logic_vector(7 downto 0)
	);
	end component;


	begin
		process (inp)
			case inp is
				when " 000 " =>
					opt <= " 00000001 " ;
				when " 001 " =>
					opt <= " 00000010 " ;
				when " 010 " =>
					opt <= " 00000100 " ;
				when " 011 " =>
					opt <= " 00001000 " ;
				when " 100 " =>
					opt <= " 00010000 " ;
				when " 101 " =>
					opt <= " 00100000 " ;
				when " 110 " =>
					opt <= " 01000000 " ;
				when " 111 " =>
					opt <= " 10000000 " ;
			end case;
		
		end process;

	end behavior;