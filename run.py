#!/usr/bin/python3
from argparse import ArgumentParser
from backend.eval import eval_command
from main import app, window

parse = ArgumentParser()
parse.add_argument("--backend-test", action="store_true")
parse.add_argument("--cli", action="store_true")

args = parse.parse_args()

if args.backend_test:
    import backend.test
elif args.cli:
    while True:
        print(str(eval_command(input("> "))))
else:
    window.show()
    app.exec_()
