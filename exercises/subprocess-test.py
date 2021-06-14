from subprocess import run

print(
    run(['test', '-e', 'testfile.txt']).returncode == 0
)

print(
    run(['test', '-d', 'testfile.txt']).returncode == 0
)

print(
    run(['test', '-f', 'testfile.txt']).returncode == 0
)