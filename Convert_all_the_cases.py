'''
In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.
'''

def change_case(identifier, targetCase):
    if identifier == '':
        return identifier

    if ('-' in identifier) and ('_' in identifier):
       return None

    if '-' in identifier or '_' in identifier:
       for i in identifier:
           if i.isupper():
              return None

    if targetCase != 'snake' and targetCase != 'camel' and targetCase != 'kebab':
        return None

    if targetCase == 'snake':
        identifier = list(identifier)
        for i in identifier:
            if i.isupper():
                identifier[identifier.index(i)] = '_' + i.lower()
            if i == '-':
                identifier[identifier.index(i)] = '_'
        return ''.join(identifier)

    if targetCase == 'camel':
        if '-' in identifier:
            identifier = identifier.split('-')
            for j in range(1, len(identifier)):
                identifier[j] =  identifier[j].title()
            return ''.join(identifier)
        elif '_' in identifier:
            identifier = identifier.split('_')
            for j in range(1, len(identifier)):
                identifier[j] =  identifier[j].title()
            return ''.join(identifier)
        else:
            return identifier


    if targetCase == 'kebab':
        identifier = list(identifier)
        for i in identifier:
            if i == '_':
                identifier[identifier.index(i)] = '-'
            if i.isupper():
                identifier[identifier.index(i)] = '-' + i.lower()
        return ''.join(identifier)
