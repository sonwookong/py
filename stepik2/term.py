n = int(input())
glb = {'global': {'parent': None, 'variables': set()}}
ot=set()

def _add(_nam, _arg):
    glb[_nam]['variables'].add(_arg)


def _create(_nam,_arg):
    glb[_nam] = {'parent': _arg, 'variables': set()}


def _get(_nam, _arg):
    if _arg in glb[_nam]['variables']:
        ot.add(_nam)
    elif glb[_nam]['parent'] is not None:
        _get(glb[_nam]['parent'], _arg)
    else:
        ot.add('None')

for i in range(n):
    com, nam, arg = input().split()
    if com == 'add':
        _add(nam, arg)
    elif com == 'create':
        _create(nam, arg)
    elif com == 'get':
        _get(nam, arg)
    else:
        ot.add('Unknown command')
print(*ot, sep='\n')