from .commands import filesystem
import jedi

interpreter = jedi.Interpreter("ls(", namespaces=[{"ls": filesystem.ls}])
print(interpreter.get_signatures(1, 3)[0].bracket_start)
