Folder structure:
```
├── README.txt
├── features.csv
├── closeness-solvent-dependency.csv
├── closeness-solute-dependency.csv
├── reorganization-energy.csv
├── xyz
│	└── *.xyz
├── example.py
└── ML-GB.pkl

```
# Description:

## This zip file includes three csv file:

features.csv contains the ML model features (charge and SOAP descriptors) for Fig. 8;
closeness-solute-dependency.csv contains the solvent-solute closeness dependent on solvent shown in Fig. 9, including 16 solutes in 5 solvents; 
closeness-solvent-dependency.csv contains MDDF, charge and solvent-solute closeness for the 166 OROP systems solvated in acetonitrile. 
reorganization-energies.csv contains the outer-sphere, inner-sphere and total reorganization energies and the outer-sphere contribution percentages. 

## Solute xyz files
For 166 organic solutes selected from the ROP313 dataset the initial xyz structures are provided.

## Machine learning model
ML-GB.pkl is the Gradient Boost machine learning model that predicts the solvent-solute closeness of solute molecules in MeCN solvent based on the features listed in features.csv

## Python Script
example.py demonstrates how to load the pkl file of the Machine learning model ML-GB.pkl together with the training and test features. 