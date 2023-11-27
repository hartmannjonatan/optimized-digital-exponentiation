library IEEE;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.all;

entity exponentiation is
  	 port(
			KEY: in std_logic_vector(3 downto 0);
        	SW: in std_logic_vector(17 downto 0);
        	LEDR: out std_logic_vector(17 downto 0);
        	HEX0,HEX1,HEX2,HEX3,HEX4,HEX5,HEX6,HEX7	: out std_logic_vector(6 downto 0)
		);
end exponentiation;
  
architecture Structural of exponentiation is
 
 component square is
  	 port(
			x: in STD_LOGIC_VECTOR(3 downto 0);
        	R: out std_logic_vector(7 downto 0)
		);
end component;

component cube is
  	 port(
			x: in STD_LOGIC_VECTOR(3 downto 0);
        	R: out std_logic_vector(12 downto 0)
		);
end component;

component fourth is
  	 port(
			x: in STD_LOGIC_VECTOR(3 downto 0);
        	R: out std_logic_vector(17 downto 0)
		);
end component;

signal x2_out: STD_LOGIC_VECTOR(7 downto 0);
signal x3_out: STD_LOGIC_VECTOR(12 downto 0);
signal x4_out: STD_LOGIC_VECTOR(17 downto 0);

begin
    
    x2: square port map(SW(3 downto 0), x2_out);
    
    x3: cube port map(SW(3 downto 0), x3_out);
    
    x4: fourth port map(SW(3 downto 0), x4_out);
    
    LEDR(17 DOWNTO 0) <= "00000000000000"&SW(3 downto 0) when SW(17 DOWNTO 15) = "001" else
                        "0000000000"&x2_out when SW(17 DOWNTO 15) = "010"else
                        "00000"&x3_out when SW(17 DOWNTO 15) = "011" else
                        x4_out when SW(17 DOWNTO 15) = "100" else
                        "000000000000000001";
  		
end Structural;