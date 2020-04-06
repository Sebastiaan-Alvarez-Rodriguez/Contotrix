import subprocess

def execute(location, data, repeats):
    subprocess.check_output(['Haut', data, repeats], cwd=location)