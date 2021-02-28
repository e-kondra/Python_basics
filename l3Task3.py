def thesaurus(*names):
    names_dict = {}
    for name in names:
        val = names_dict.setdefault(name[0], [name])
        if name not in val:
            val.append(name)
    return names_dict


print(thesaurus('Анна', 'Владимир', 'Иван', 'Николай', 'Никита', 'Илья', 'Светлана', 'Вячеслав'))
