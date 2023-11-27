LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY somadorNbits IS
    GENERIC (
        N : INTEGER := 8);
    PORT (
        add1 : IN STD_LOGIC_VECTOR(N - 1 DOWNTO 0);
        add2 : IN STD_LOGIC_VECTOR(N - 1 DOWNTO 0);
        sum : OUT STD_LOGIC_VECTOR(N DOWNTO 0)
    );
END somadorNbits;

ARCHITECTURE rtl OF somadorNbits IS
BEGIN
    sum <= std_logic_vector(resize(unsigned(add1), N + 1) + resize(unsigned(add2), N + 1));
END rtl;