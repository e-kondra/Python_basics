import re

def email_parse(addr):
    RE_GET_PARSER = re.compile(r'(?P<username>^[a-z\_-]*)@(?P<domain>(?<=@)\w*\.\w*)')
    if not RE_GET_PARSER.match(addr):
        raise ValueError(f'Wrong email: {addr}')
    print(*map(lambda x: x.groupdict(), RE_GET_PARSER.finditer(addr)), sep=', ')

email_parse('e-kondra@mail.ru')