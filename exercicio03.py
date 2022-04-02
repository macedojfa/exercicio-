# DNA to RNA
def dna_to_rna(dnaseq):
    rna = dnaseq.replace("T", "U")
    return rna
dnaseq = input("Digite a sequência de DNA: ").upper()

print(f"A sequência de RNA é: {dna_to_rna(dnaseq)}")

