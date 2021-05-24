def thesaurus_adv(*names):
    names_dict = {}
    for name in names:
        val = names_dict.setdefault(name[name.find(' ') + 1], dict.fromkeys(name[0], [name]))
        n_val = val.setdefault(name[0], [name])
        if name not in n_val:
            n_val.append(name)
    return names_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
