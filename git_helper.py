import subprocess
import os

def run_git(args):
    try:
        result = subprocess.run(['git'] + args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

print("Git Log:")
print(run_git(['log', '--oneline', '-n', '5']))
print("\nGit Status:")
print(run_git(['status']))
print("\nTracked files:")
print(run_git(['ls-files']))
