# Generating Cellular Automata Transitions

Based of the Paper [Non-uniform Non-linear Cellular Automata with Large Cycles and
Their Application in Pseudo-Random Number Generation](https://www.researchgate.net/publication/349348443_Non-uniform_Non-linear_Cellular_Automata_with_Large_Cycles_and_Their_Application_in_Pseudo-Random_Number_Generation)

### gen_ca_all
The program `gen_ca_all.py` generates all possible CA of a given length and writes them to a file in `all_steps/{number-of-steps}`. This output is to form the basis of analysing the patterns to form reversible CAs. The binary formats are written to `all_steps/{number-of-steps}_bin`.

### gen_ca_random
The program `gen_ca_random.py` generates a random non-uniform-reversible CA

Run with sample output

```sh
python3 gen_ca_random.py
0	0	0	0	0	1	0	1			 5
000	000	000	000	001	010	101	010
1	0	1	1	0	1	0	0			 180
010	101	011	110	101	010	100	000
1	0	1	0	0	1	1	0			 166
010	101	010	100	001	011	110	100
1	1	1	1	0	0	0	0			 240
011	111	111	110	100	000	000	000
1	1	0	0	0	0	1	1			 195
011	110	100	000	000	001	011	110
0	1	0	0	0	1	0	0			 68
```

The output is of the format number followed by its 3-neighbourhood in the next line
