def generate_python_code(tree):
    if tree[0] == 'program':
        code = ''
        for declaration in tree[1:]:
            code += generate_python_code(declaration) + '\n'
        return code
    elif tree[0] == 'declaration':
        return generate_python_code(tree[1])
    elif tree[0] == 'funDecl':
        return generate_python_code(tree[1])
    elif tree[0] == 'varDecl':
        identifier = tree[2]
        expression = generate_python_code(tree[4]) if len(tree) > 4 else ''
        return f'{identifier} = {expression}'
    elif tree[0] == 'statement':
        return generate_python_code(tree[1])
    elif tree[0] == 'exprStmt':
        return generate_python_code(tree[1]) + ';'
    elif tree[0] == 'forStmt':
        init = generate_python_code(tree[3]) if len(tree) > 3 else ''
        condition = generate_python_code(tree[4]) if len(tree) > 4 else ''
        increment = generate_python_code(tree[5]) if len(tree) > 5 else ''
        statement = generate_python_code(tree[6])
        return f'for {init} {condition} {increment} {statement}'
    elif tree[0] == 'ifStmt':
        condition = generate_python_code(tree[2])
        if_block = generate_python_code(tree[4])
        else_block = generate_python_code(tree[5]) if len(tree) > 5 else ''
        return f'if {condition} {if_block} {else_block}'
    elif tree[0] == 'printStmt':
        expression = generate_python_code(tree[2])
        return f'print({expression})'
    elif tree[0] == 'returnStmt':
        expression = generate_python_code(tree[2]) if len(tree) > 2 else ''
        return f'return {expression}'
    elif tree[0] == 'whileStmt':
        condition = generate_python_code(tree[3])
        block = generate_python_code(tree[4])
        return f'while {condition} {block}'
    elif tree[0] == 'block':
        code = ''
        for declaration in tree[2:]:
            code += generate_python_code(declaration) + '\n'
        return code
    elif tree[0] == 'assignment':
        identifier = generate_python_code(tree[2])
        value = generate_python_code(tree[4])
        return f'{identifier} = {value}'
    elif tree[0] == 'logic_or':
        code = generate_python_code(tree[1])
        for i in range(3, len(tree), 2):
            code += f' or {generate_python_code(tree[i])}'
        return code
    elif tree[0] == 'logic_and':
        code = generate_python_code(tree[1])
        for i in range(3, len(tree), 2):
            code += f' and {generate_python_code(tree[i])}'
        return code
    elif tree[0] == 'equality':
        code = generate_python_code(tree[1])
        for i in range(3, len(tree), 2):
            code += f' {generate_python_code(tree[i])} {generate_python_code(tree[i+1])}'
        return code
    elif tree[0] == 'comparison':
        code = generate_python_code(tree[1])
        for i in range(3, len(tree), 2):
            code += f' {generate_python_code(tree[i])} {generate_python_code(tree[i+1])}'
        return code
    elif tree[0] == 'term':
        code = generate_python_code(tree[1])
        for i in range(3, len(tree), 2):
            code += f' {generate_python_code(tree[i])} {generate_python_code(tree[i+1])}'
        return code
    elif tree[0] == 'factor':
        code = generate_python_code(tree[1])
        for i in range(3, len(tree), 2):
            code += f' {generate_python_code(tree[i])} {generate_python_code(tree[i+1])}'
        return code
    elif tree[0] == 'unary':
        if tree[1] in ['not', '-']:
            return f'{tree[1]} {generate_python_code(tree[2])}'
        else:
            return generate_python_code(tree[1])
    elif tree[0] == 'call':
        primary = generate_python_code(tree[1])
        arguments = generate_python_code(tree[3]) if len(tree) > 3 else ''
        return f'{primary}({arguments})'
    elif tree[0] == 'primary':
        if tree[1] in ['true', 'false', 'nil', 'this']:
            return tree[1]
        elif tree[1].isdigit():
            return tree[1]
        elif tree[1].startswith('"'):
            return tree[1]
        elif tree[1] == 'super':
            return f'super.{generate_python_code(tree[3])}'
        else:
            return tree[1]

import ast        

def initGenerator(tree):
    codeTree = ast.literal_eval(tree)
    with open('codigoGerado.py', 'w') as codefile:
        codefile.write(generate_python_code(tree))
        codefile.close()