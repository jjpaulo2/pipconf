CONFIGURATION_FILE_FILTER = [
    ('teste.ini', False),
    ('teste.conf', True),
    ('teste', False),
    ('minha-config.conf', True),
    ('pip.conf', True),
    ('.env', False),
    ('pip.ext', False)
]

GET_CONFIGURATION_FILES = [
    (['teste.ini', 'teste.conf', 'pip.conf'], ['teste.conf', 'pip.conf']),
    (['teste.ini', 'teste', 'pip.env'], []),
    (['pipconf.conf', 'teste.conf', 'pip.conf'], ['pipconf.conf', 'teste.conf', 'pip.conf'])
]

GET_USER_CONFIGURATION_FILES = [
    (['conf1.conf', 'conf2.conf', 'pip.conf'], ['conf1.conf', 'conf2.conf']),
    (['pip.conf'], []),
    (['conf1.conf', 'conf2.conf'], ['conf1.conf', 'conf2.conf'])
]

GET_LOCAL_CONFIGURATION_FILES = [
    ('conf1.conf', 'conf2.conf'),
    ()
]