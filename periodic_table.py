unique_chemical_compounds = set()

for _ in range(int(input())):
    current_compounds = input().split()
    for compound in current_compounds:
        unique_chemical_compounds.add(compound)

print(*unique_chemical_compounds,sep="\n")