from Bio.Seq import Seq
from collections import Counter

# Задайте свою последовательность аминокислот
aminо_acid_sequence = "AADEFAHIKSNPFRSTVWY"

# Создайте объект Seq
seq_obj = Seq(aminо_acid_sequence)

# Подсчитайте кол-во каждой аминокислоты в последовательности
count_amino_acids = Counter(seq_obj)

# Вывoд
print("Количество аминокислот в последовательности:")
for amino_acid, count in count_amino_acids.items():
    print(f"{amino_acid}: {count}")
