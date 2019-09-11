from pycparser import parse_file, c_ast


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
    pass

    def collect_defs(self):
        [self.Decls.append(x) for x in self.AST.ext if type(x) is c_ast.Decl]
        [self.Decls.append(x) for x in self.TestedFunc.body.block_items if type(x) is c_ast.Decl]

