from pycparser import parse_file, c_ast
from declcheck import DeclCheck


class PycHelper:

    def __init__(self, filepath, funcname):
        self.Decls = []

        # Initialization
        self.FPath = filepath
        self.Fname = funcname
        self.AST = self.get_ast()
        self.TestedFunc = self.get_tested_func()
        self.collect_defs()
        pass

    def get_tested_func(self):
        """Find tested function in abstract syntax tree"""
        t_ast = [x for x in self.AST.ext if type(x) is c_ast.FuncDef and x.decl.name == self.Fname]
        if len(t_ast) < 1:
            raise Exception("Func is not in ast")
        else:
            return t_ast[0]

    def get_ast(self):
        """Get abstract syntax tree from sourcefile"""
        ast = parse_file(self.FPath, use_cpp=True,
                         cpp_path='gcc',
                         cpp_args=['-E', r'-Iutils/fake_ksu'])
        return ast

    def collect_defs(self):
        """Get all definitions"""
        [self.Decls.append(x) for x in self.AST.ext if type(x) is c_ast.Decl]
        [self.Decls.append(x) for x in self.TestedFunc.body.block_items if type(x) is c_ast.Decl]

    def get_decl_by_name(self, declare):
        # TODO
        # What to do, when decls more than 1?
        decls = [x for x in self.Decls if x.name == declare.name]
        if len(decls) > 0:
            return decls[0]
        else:
            raise Exception(f"Declaration for {declare.name} was not found.")

    def search_last_id(self, block, itsearch: DeclCheck, store, parent=''):
        if type(block) is c_ast.Decl:
            if block.name == itsearch.init.name:
                store.append({'type': c_ast.Decl, 'item': block, 'parent': parent})
                return

        if type(block) is c_ast.Assignment:
            if block.lvalue.name == itsearch.init.name:
                store.append({'type': c_ast.Decl, 'item': block, 'parent': parent})
                return

        if type(block) is c_ast.If:
            self.search_last_id(block.iftrue, itsearch, store, 'iftrue')
            self.search_last_id(block.iffalse, itsearch, store, 'iffalse')

        # Recursive search
        if type(block) is c_ast.Compound:
            for item in block.block_items:
                self.search_last_id(item, itsearch, store, parent)

        if type(block) is list:
            for item in block:
                self.search_last_id(item, itsearch, store, parent)

