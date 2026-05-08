molecules = {
    "CCO": {"mw": 46, "logP": -0.3},
    "CCN": {"mw": 45, "logP": 0.2},
    "CCC": {"mw": 44, "logP": 2.1},
    "COC": {"mw": 46, "logP": 0.5},
    "c1ccccc1": {"mw": 78, "logP": 2.5}
}
def filter_molecules(moolecules, threshold = 0):
    filtered = {}
    for smiles, data in molecules.items():
        if data['logP'] >= threshold:
            filtered[smiles] = data
    return filtered
def rank_molecules (filtered_molecules):
    ranked = sorted(
        filtered_molecules.items(),
        key=lambda item: item[1]['logP'],
        reverse=True
        )
    return ranked
filtered_molecules = filter_molecules(molecules)
ranked_molecules = rank_molecules(filtered_molecules)
print('Filtered Molecules')
for smiles, data in filtered_molecules.items():
    print(smiles, data)
print('Ranked Molecules:')
for smiles, data in ranked_molecules:
    print(smiles,'-', data)
    