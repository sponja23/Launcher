#!/usr/bin/python3
from backend.eval import eval_command
from argparse import ArgumentParser

parse = ArgumentParser()
parse.add_argument("--backend-test", action="store_true")

args = parse.parse_args()

if args.backend_test:
    import backend.test
else:
    while True:
        print(str(eval_command(input("> "))))
