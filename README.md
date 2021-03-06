IMFP-calc

# Calculation of the inelatic mean free path (IMFP) of electrons in a solid
You can calculate the IMFP of electrons for a range of kinetic energies with this script. 
The calculation is based on the TPP2M formula by Tanuma Powell and Penn [1]. 

## Prerequisites
Python >= 3.7 </br>
Packages: </br>

```Python
pandas
```

```Python
numpy
```

```Python
dataclass
```

```Python
os
```

```Python
matplotlib
```

## How to use the script
Execute the **main.py** script.</br>
On Windows: Double click the **IMFP.bat** file to start the execution.</br>

The program will ask you for an input of which element you want to plot
in the console. You can input all elements/compunds in the table within the **data** folder. Enter 
the kinetic energy range of the calculation. The plotted IMFP and probing depth (estimated 3* IMFP) 
will open. The corresponding data (in .csv file) and plot (.png) will be stored in the results folder 
that is created upon the first execution. The dataset provides you with the parameters that were used for the calculation.

## How to add a new material or change properties

You can add properties of the materials you are interested in into the dataset in the **data** folder. 
You can simply add your own material to the table in the **data** folder or change existing entries in the table.</br>
If you are unsure on the number of valence electrons to use for your own compound, refer to the handbook of the NIST Standard Reference Database 71.
It contains a list of recommended values for the number of valence electrons for the TPP2M formula. You can access it [here](https://www.nist.gov/system/files/documents/srd/SRD71UsersGuideV1-2.pdf) (page 32).

## References
[1] S. Tanuma, C. J. Powell, D. R. Penn: Surf. Interf. Anal.,Vol. 21, 165 (1994)</br>