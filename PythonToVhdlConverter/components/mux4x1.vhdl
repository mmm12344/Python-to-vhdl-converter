entity Mux4x1 is
port(
	inp0 : in std_logic;
	inp1 : in std_logic;
	inp2 : in std_logic;
	inp3 : in std_logic;
	select : in std_logic_vector(1 downto 0);
	
	opt : out std_logic
);
end Mux4x1;
architecture behavior of Mux4x1 is

	begin
		process (inp0,inp1,inp2,inp3,select)
			case select is
				when " 00 " =>
					opt <= inp0 ;
				when " 01 " =>
					opt <= inp1 ;
				when " 10 " =>
					opt <= inp2 ;
				when " 11 " =>
					opt <= inp3 ;
			end case;
		
		end process;

	end behavior;