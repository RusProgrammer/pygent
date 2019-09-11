from random import randrange, uniform
from pycparser import c_ast
from testattrs import TestAtrs


class DeclCheck(c_ast.Decl, TestAtrs):

    def __init__(self, declitem):
        super().__init__(declitem.name, declitem.quals, declitem.storage,
                         declitem.funcspec, declitem.type, declitem.init,
                         declitem.bitsize, declitem.coord)

    def check_const(self):
        if self.init.type == 'int':
            self.add_check(f'VAR {self.name}, INIT = {str(randrange(10000))}, EV = {self.init.value}')
        if self.init.type == 'double' or self.init.type == 'float':
            self.add_check(f'VAR {self.name}, INIT = {str(uniform(0.0, 100000.9))}, EV = {self.init.value}')
        if self.init.type == 'string':
            self.add_check(f'VAR {self.name}, INIT = NULL, EV = {self.init.value}')

    def do_test(self):
        if type(self.type) is c_ast.TypeDecl:
            if type(self.type) is c_ast.Constant:
                self.check_const()
                pass
            if type(self.type) is c_ast.ID:
                pass
            if type(self.type) is c_ast.FuncCall:
                pass
    pass
