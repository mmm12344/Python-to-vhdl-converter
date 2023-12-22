entity Mux8*1 is
port(
	inp0 : in std_logic;
	inp1 : in std_logic;
	inp2 : in std_logic;
	inp3 : in std_logic;
	inp4 : in std_logic;
	inp5 : in std_logic;
	inp6 : in std_logic;
	inp7 : in std_logic;
	select : in std_logic_vector(2 downto 0);
	
	opt : out std_logic
);
end Mux8*1
architecture behavior of Mux is

	begin
		process (inp0,inp1,inp2,inp3,inp4,inp5,inp6,inp7,select)
			case select is
				when " 000 " =>
					opt <= inp 0 ;
				when " 001 " =>
					opt <= inp 1 ;
				when " 010 " =>
					opt <= inp 2 ;
				when " 011 " =>
					opt <= inp 3 ;
				when " 100 " =>
					opt <= inp 4 ;
				when " 101 " =>
					opt <= inp 5 ;
				when " 110 " =>
					opt <= inp 6 ;
				when " 111 " =>
					opt <= inp 7 ;
			end case;
		
		end process;

	end;