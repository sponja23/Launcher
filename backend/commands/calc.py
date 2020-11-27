from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                        implicit_multiplication, implicit_application,
                                        rationalize, convert_xor)
from sympy.printing import latex
from ..results import LatexResult
from ..base import command
import re


TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication,
    implicit_application,
    rationalize,
    convert_xor
)

assignment_pattern = re.compile(r"^([a-zA-Z_][a-zA-Z_0-9]*)\s*:=\s*(.+)$")


sympy_dict = {}


@command
def calc(s: str) -> LatexResult:
    global sympy_dict

    if (m := assignment_pattern.match(s)) is not None:
        name = m.group(1)
        value = parse_expr(m.group(2), local_dict=sympy_dict, transformations=TRANSFORMATIONS)
        sympy_dict[name] = value
        return LatexResult(latex(value))
    else:
        return LatexResult(latex(parse_expr(s, local_dict=sympy_dict, transformations=TRANSFORMATIONS)))
