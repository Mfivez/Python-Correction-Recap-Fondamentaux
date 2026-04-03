# 1 Listes

prenoms = ["Michel", "Ethienne", "Stéphane"];

print(prenoms[0])
print(prenoms[-1])

prenoms.append('Jean')
prenoms[1] = 'Carl'

# 2 Tuples

point_2d = (5, 6);

x = point_2d[0]
y = point_2d[1]

print(x)
print(y)

# 3 Sets

fruits = {'banane', 'poire', 'pêche', 'poire'};

fruits.add('kiwi')
fruits.discard('banane')
print(fruits)

# 4 Dictionnaire

etudiant = {
    "nom": "a",
    "age": 2,
    "ville": "b"
}

print(etudiant['nom'])
etudiant['age'] = 12
etudiant['note'] = 3