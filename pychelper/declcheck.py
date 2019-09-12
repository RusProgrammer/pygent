from pycparser import c_ast
from testattrs import TestAtrs
# from pychelper2 import PycHelper


class DeclCheck(c_ast.Decl, TestAtrs):

    def __init__(self, declitem, pychlp):
        super().__init__(declitem.name, declitem.quals, declitem.storage,
                         declitem.funcspec, declitem.type, declitem.init,
                         declitem.bitsize, declitem.coord)
        self.PycH = pychlp

    def do_test(self):
        if type(self.type) is c_ast.TypeDecl:
            if self.init is not None:
                if type(self.init) is c_ast.Constant:
                    self.add_check(f'VAR {self.name}, INIT = {self.get_random(self.init.type)}, EV = {self.init.value}')
                    pass
                if type(self.init) is c_ast.ID:
                    ussages = []
                    # self.PycH.search_last_id(self.PycH.TestedFunc.body, self.init, ussages)
                    self.PycH.search_last_id(self.PycH.AST.ext, self, ussages, parent='global')
                    print(123)
                    pass
                if type(self.init) is c_ast.FuncCall:
                    pass
            else:
                dtype = self.get_decl_type()
                self.add_check(f'VAR {self.name}, INIT = {self.get_random(dtype)}, EV = INIT')

    pass

    def get_decl_type(self):
        if type(self.type) is c_ast.TypeDecl:
            return self.type.type.names[0]

