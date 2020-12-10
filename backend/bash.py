import subprocess


def run_bash(cmd: str) -> str:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, check=True,
                       shell=True, executable="/bin/bash")
    return p.stdout.decode("utf-8").strip()
