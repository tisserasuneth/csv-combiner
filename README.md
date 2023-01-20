# CSV Combiner - Suneth Tissera
Interviewee : Suneth Tissera   
Company: PMG Digital Agency

## GLP Challenge
A command line program that takes several CSV files as arguments. Each CSV
file (found in the `fixtures` directory of this repo) will have the same
columns. The script outputs a new CSV file to `stdout` that contains the
rows from each of the inputs along with an additional column that has the
filename from which the row came.


## Example
The program is able to handle multiple inputs as required.  
Each csv files is also broken into chunks using the pandas library. This allows for combining even larger .csv files with ease.

```
$ python3 combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv >output.csv
```

Given three input files named `accessories.csv`, `clothing.csv`, and `household_cleaners.csv`

|email_hash|category|
|----------|--------|
|b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6|Satchels|
|c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7|Purses|
|faaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18|Purses|

|email_hash|category|
|----------|--------|
|e8cee956c334047056a8820065cd5c1d2575a3285a2b09ff237752882932eafd|Cardigans|
|8d0eb06f13e26fa3fb1c5f1d7945d544659ad312ebf35f55e0ceb74573468775|Tanks|
|b96c858a8206db09ab13066ee53f24892d2c72b8db7fc0f66db09057e6879d8c|Pants|
|2d945909f4fc18d5f124d1b88e5ee661e1b7e9e9dbcd106a61a40053609b7a93|Blouses|


|email_hash|category|
|----------|--------|
|e088d5dbbca4c61e870dd32e2584623da88870327f060bd0d27465136366f353|Kitchen Cleaner|
|4727745894cc3d99632c89a64067f69327913989cddb9e2de5793d4de12ef4ef|Bathroom Cleaner|
|1ed6083eb9dc193dcd42466b57adce9f581cd70207426a37036a5dda3b3ad55a|Kitchen Cleaner|
|2c3d6ecd8ee8dec11e97c6ca5fb4390ab6b2a48c7f0983f49e80544320878246|Bathroom Cleaner|

### combiner.py outputs:

|email_hash|category|filename|
|----------|--------|--------|
|b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6|Satchels|accessories.csv|
|c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7|Purses|accessories.csv|
|faaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18|Purses|accessories.csv|
|e8cee956c334047056a8820065cd5c1d2575a3285a2b09ff237752882932eafd|Cardigans|clothing.csv|
|8d0eb06f13e26fa3fb1c5f1d7945d544659ad312ebf35f55e0ceb74573468775|Tanks|clothing.csv|
|b96c858a8206db09ab13066ee53f24892d2c72b8db7fc0f66db09057e6879d8c|Pants|clothing.csv|
|2d945909f4fc18d5f124d1b88e5ee661e1b7e9e9dbcd106a61a40053609b7a93|Blouses|clothing.csv|
|e088d5dbbca4c61e870dd32e2584623da88870327f060bd0d27465136366f353|Kitchen Cleaner|household_cleaners.csv|
|4727745894cc3d99632c89a64067f69327913989cddb9e2de5793d4de12ef4ef|Bathroom Cleaner|household_cleaners.csv|
|1ed6083eb9dc193dcd42466b57adce9f581cd70207426a37036a5dda3b3ad55a|Kitchen Cleaner|household_cleaners.csv|
|2c3d6ecd8ee8dec11e97c6ca5fb4390ab6b2a48c7f0983f49e80544320878246|Bathroom Cleaner|household_cleaners.csv|

## Unit Tests

Tests can be conducted using the following command
```
$ python3 -m unittest test_combiner.py
```
### Cases Checked : 

- No Files input
- Valid Files input
- Invalid Files input
- 'filename' Column exitence
- CSV Files Combined Succesfully
