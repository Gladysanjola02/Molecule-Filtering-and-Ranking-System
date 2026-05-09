Drug Screening Project

This project simulates a simple dru screening pipeline using Python.

It filters, classifies, and ranks molecules based on their properties such as logP and molecular weight.

Concepts Used
- Dictionaries
- Functions
- Loops
- Sorting with lambda

What it does
- Stores molecules using SMILES notation
- Filters molecules based on logP (lipophilicity)
- Ranks molecules from best to worst candidates

THE OUTPUT

Filtered Molecules:

CCN {'mw': 45, 'logP': 0.2}

CCC {'mw': 44, 'logP': 2.1}

COC {'mw': 46, 'logP': 0.5}

c1ccccc1 {'mw': 78, 'logP': 2.5}

Ranked Molecules:

c1ccccc1 - {'mw': 78, 'logP': 2.5}

CCC - {'mw': 44, 'logP': 2.1}

COC - {'mw': 46, 'logP': 0.5}

CCN - {'mw': 45, 'logP': 0.2}
