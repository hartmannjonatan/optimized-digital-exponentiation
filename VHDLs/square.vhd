library IEEE;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.all;

entity square is
  	 port(
			x: in STD_LOGIC_VECTOR(3 downto 0);
        	R: out std_logic_vector(7 downto 0)
		);
end square;
  
architecture Structural of square is
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
 
 signal v1, v2: STD_LOGIC_VECTOR(6 downto 0);

begin

    v1 <=( x(2) and x(3) ) & ( x(1) and x(3) ) & ( x(0) and x(3) ) & ( x(0) and x(2) ) & ( x(0) and x(1) ) & ('0') & ( x(0) );
    v2 <=( x(3) ) & ( x(1) and x(2) ) & ( not(x(1)) and x(2) ) & ('0') & ( x(1) ) & ('0') & ('0');

	
	somador: somadorNbits
			generic map(N => 7)
			port map(v1, v2, R);
  		
end Structural;