import pycodestyle
import os

def check_pep8(files):
    style = pycodestyle.StyleGuide()
    result = style.check_files([files])
    return result.total_errors

if __name__ == "__main__":
    os.chdir('../python')
    for file in os.listdir('.'):
        check_pep8(file)
        print(" ")