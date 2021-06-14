from pathlib import Path

print(
    Path('testfile.txt').exists()
)
print(
    Path('im-not-here.txt').exists()
)
print(
    Path('testdirectory').exists()
)


print(
    Path('testfile.txt').is_file()
)

print(
    Path('testdirectory').is_file()
)

print(
    Path('testfile.txt').is_dir()
)
print(
    Path('testdirectory').is_dir()
)