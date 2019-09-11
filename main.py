import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

from pycparser import parse_file, c_ast

from pychelper import PycHelper
from declcheck import DeclCheck


if __name__ == "__main__":

    filename = 'c_files\\year.c'

    Tinfo = PycHelper(filename, 'main')

    ast = parse_file(filename, use_cpp=True,
            cpp_path='gcc',
            cpp_args=['-E', r'-Iutils/fake_ksu'])
    t_ast = [x for x in ast.ext if type(x) is c_ast.FuncDef and x.decl.name == 'main'][0]
    # print(t_ast)
    # print(t_ast.body)
    print(t_ast.body.block_items[0].type)
    ast.show()
