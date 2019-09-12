from pycparser import c_ast
from testattrs import TestAtrs


class IfCheck(c_ast.If, TestAtrs):

    def __init__(self, ifitem, pychlp):
        super().__init__(ifitem.cond, ifitem.iftrue, ifitem.iffalse, ifitem.coord)

