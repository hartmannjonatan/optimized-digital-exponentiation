library IEEE;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.all;

entity fourth is
  	 port(
			x: in STD_LOGIC_VECTOR(3 downto 0);
        	R: out std_logic_vector(17 downto 0)
		);
end fourth;
  
architecture Structural of fourth is
 component CSA is
 	 generic (n: natural := 12);
  	 port(I0 : in STD_LOGIC_VECTOR((n-1) downto 0);
			I1 : in STD_LOGIC_VECTOR((n-1) downto 0);
			I2 : in STD_LOGIC_VECTOR((n-1) downto 0);
			S : out STD_LOGIC_VECTOR((n-1) downto 0);
			C : out STD_LOGIC_VECTOR(n downto 0));
 end component;
 
 component somadorNbits is
    GENERIC (
        N : INTEGER);
    PORT (
        add1 : IN STD_LOGIC_VECTOR(N - 1 DOWNTO 0);
        add2 : IN STD_LOGIC_VECTOR(N - 1 DOWNTO 0);
        sum : OUT STD_LOGIC_VECTOR(N DOWNTO 0)
    );
 end component;
 
 signal v1, v2, v3, v4: STD_LOGIC_VECTOR(14 downto 0);
 signal csa1_cout, csa1_out, aux_v4: STD_LOGIC_VECTOR(15 DOWNTO 0);
 signal csa2_cout, csa2_out: STD_LOGIC_VECTOR(16 DOWNTO 0);

begin
    v1 <=(( x(1) and x(2) and x(3) )) & (( x(0) and x(1) and x(2) and x(3) )) & (( not(x(1)) and x(2) and x(3) )) & (( x(0) and x(1) and x(3) )) & (( x(0) and x(1) and x(2) )) & (( not(x(0)) and x(2) and x(3) )) & (( not(x(0)) and x(1) and x(2) )) & (( x(0) and not(x(1)) and x(2) ) or ( not(x(0)) and x(1) and x(2) and x(3) )) & (( x(0) and x(1) and not(x(3)) )) & (( x(0) and x(3) )) & (( x(0) and x(1) and x(2) ) or ( x(0) and x(2) )) & (('0')) & (('0')) & (('0')) & (( x(0) ));
    v2 <=(('0')) & (( x(2) and x(3) )) & (( x(1) and x(3) )) & (( x(2) and x(3) )) & (( x(0) and not(x(1)) and x(2) and x(3) )) & (( not(x(0)) and x(1) and x(2) and x(3) ) or ( x(0) and not(x(1)) and x(2) and x(3) )) & (( x(0) and not(x(2)) and x(3) )) & (( x(0) and x(2) ) or ( x(0) and x(3) )) & (( x(1) and x(2) ) or ( x(0) and x(2) )) & (( x(0) and not(x(1)) and x(2) )) & (( x(1) )) & (('0')) & (('0')) & (('0')) & (('0'));
    v3 <=(('0')) & (('0')) & (( x(0) and not(x(1)) and x(2) and x(3) )) & (( x(0) and x(3) )) & (( x(1) and not(x(2)) and x(3) )) & (( x(1) and x(2) ) or ( x(2) and x(3) )) & (( x(1) and not(x(2)) and x(3) )) & (( x(1) and x(2) ) or ( x(0) and x(1) and x(3) )) & (( x(1) and x(2) )) & (( x(1) and x(2) and x(3) ) or ( x(0) and x(2) and x(3) )) & (('0')) & (('0')) & (('0')) & (('0')) & (('0'));
    v4 <=(('0')) & (('0')) & (( x(3) )) & (('0')) & (( x(2) and x(3) )) & (( x(1) and not(x(2)) and x(3) )) & (( x(2) )) & (( x(0) and x(1) and x(2) ) or ( x(0) and x(2) and x(3) )) & (( x(1) and x(2) and x(3) ) or ( x(0) and x(2) and x(3) )) & (( x(1) and x(2) and x(3) ) or ( x(0) and x(2) and x(3) )) & (('0')) & (('0')) & (('0')) & (('0')) & (('0'));
    
    csa1: CSA
			generic map(N => 15)
			port map(v1, v2, v3, csa1_out(14 DOWNTO 0), csa1_cout);
			
	csa1_out(15) <= '0';
	
	aux_v4 <= "0" & v4;
	
    csa2: CSA
			generic map(N => 16)
			port map(csa1_out, csa1_cout, aux_v4, csa2_out(15 DOWNTO 0), csa2_cout);
			
	csa2_out(16) <= '0';
	
	somador: somadorNbits
			generic map(N => 17)
			port map(csa2_out, csa2_cout, R);

end Structural;