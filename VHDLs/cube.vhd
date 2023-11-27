library IEEE;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.all;

entity cube is
  	 port(
			x: in STD_LOGIC_VECTOR(3 downto 0);
        	R: out std_logic_vector(12 downto 0)
		);
end cube;
  
architecture Structural of cube is
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
 
 signal v1, v2, v3, csa_out: STD_LOGIC_VECTOR(10 downto 0);
 signal csa_cout, aux: STD_LOGIC_VECTOR(11 DOWNTO 0);

begin
    v1 <=(( x(2) and x(3) )) & (( x(1) and x(2) and x(3) )) & (( not(x(0)) and x(1) and x(3) )) & (( not(x(0)) and x(1) and x(3) )) & (( x(0) and x(1) and x(2) )) & (( x(0) and x(2) )) & (( x(0) and x(1) )) & (( x(0) and x(2) )) & (( x(0) and x(2) )) & (( x(0) and x(1) )) & (( x(0) ));
    v2 <=(('0')) & (( x(3) )) & (( x(0) and x(2) and x(3) )) & (( x(0) and x(3) )) & (( x(2) ) or ( x(0) and x(3) )) & (( not(x(0)) and x(1) and x(3) )) & (( x(0) and x(3) )) & (( x(0) and x(3) )) & (('0')) & (('0')) & (('0'));
    v3 <=(('0')) & (( x(0) and x(1) and x(3) )) & (('0')) & (( x(1) and x(2) ) or ( x(3) and x(2) )) & (( x(1) and x(3) )) & (('0')) & (( x(1) and x(2) ) or ( x(0) and x(2) )) & (( x(1) )) & (('0')) & (('0')) & (('0'));

    csa1: CSA
			generic map(N => 11)
			port map(v1, v2, v3, csa_out, csa_cout);

			
	aux <= '0'&csa_out;
	
	somador: somadorNbits
			generic map(N => 12)
			port map(aux, csa_cout, R);

end Structural;