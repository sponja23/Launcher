import subprocess
import os
from typing import List


def file_autocomplete(path: str) -> List[str]:
    p = subprocess.run(f"compgen -f {path}", stdout=subprocess.PIPE,
                       check=True, shell=True, executable="/bin/bash")
    results = p.stdout.decode("utf-8").split('\n')
    if "" in results:
        results.remove("")
    results = [s + "/" if os.path.isdir(s) else s for s in results]  # Add / to end of dirs
    return results


def directory_autocomplete(path: str) -> List[str]:
    p = subprocess.run(f"compgen -d {path}", stdout=subprocess.PIPE,
                       check=True, shell=True, executable="/bin/bash")
    results = p.stdout.decode("utf-8").split('\n')
    if "" in results:
        results.remove("")
    results = [s + "/" for s in results]
    return results
