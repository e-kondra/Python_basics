from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tk_gens = (tk for tk in zip_longest(tutors, klasses[:len(tutors)], fillvalue=None))

print(type(tk_gens), *tk_gens)
print(type(tk_gens), *tk_gens)
