from pycparser import parse_file, c_ast
from pychelper2 import PycHelper
from declcheck import DeclCheck


def test_decl_const_empty():
    global t_ast
    global tinfo
    a = DeclCheck(t_ast.body.block_items[0], tinfo)
    a.do_test()
    print(a.Checks[0])
    a.Checks.clear()

def test_decl_const_int():
    global t_ast
    global tinfo
    a = DeclCheck(t_ast.body.block_items[1], tinfo)
    a.do_test()
    print(a.Checks[0])
    a.Checks.clear()


def test_decl_const_float():
    global t_ast
    global tinfo
    a = DeclCheck(t_ast.body.block_items[2], tinfo)
    a.do_test()
    print(a.Checks[0])
    a.Checks.clear()

def test_decl_const_id():
    global t_ast
    global tinfo
    a = DeclCheck(t_ast.body.block_items[3], tinfo)
    a.do_test()
    print(a.Checks[0])
    a.Checks.clear()


# Init
filename = 'c_files\\year.c'
tinfo = PycHelper(filename, 'main')
ast = parse_file(filename, use_cpp=True,
                cpp_path='gcc',
                cpp_args=['-E', r'-Iutils/fake_ksu'])
t_ast = [x for x in ast.ext if type(x) is c_ast.FuncDef and x.decl.name == 'main'][0]

# Tests
test_decl_const_empty()
test_decl_const_int()
test_decl_const_float()
test_decl_const_id()
