import subprocess

subprocess.call(["sed", "-e", "s/\t/ /g", "../public/popular-names.txt"])
