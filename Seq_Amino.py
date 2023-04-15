''''
Bыполненяя этого кода вы получите графическое представление заданной
аминокислотной последовательности с выделенными участками и подписями аминокислот.

'''

import matplotlib.pyplot as plt
from collections import Counter
from dna_features_viewer import GraphicFeature, GraphicRecord

# Задайте свою последовательность аминокислот
amino_acid_sequence = "AADEFAHIKSNPFRSTVWY"

# Подсчитайте кол-во каждой аминокислоты в последовательности
count_amino_acids = Counter(amino_acid_sequence)

# Вывод
print("Количество аминокислот в последовательности:")
for amino_acid, count in count_amino_acids.items():
    print(f"{amino_acid}: {count}")

record = GraphicRecord(sequence=amino_acid_sequence, features=[
    GraphicFeature(start=5, end=10, strand=+1, color='#ffcccc'),
    GraphicFeature(start=8, end=15, strand=+1, color='#ccccff')
    ])

ax, _ = record.plot(figure_width=5)
record.plot_sequence(ax)

ax.figure.savefig('sequence_and_translation.png', bbox_inches='tight')

# Показать график
plt.show()
