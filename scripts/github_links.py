import git
import re

def get_function_data_from_file(file):
    pattern = r'(?P<name>\b(?:int|void|char|float|double)\s+(\w+)\s*\([^)]*\)\s*{)'
    matches = re.finditer(pattern, file)
    function_info = []
    for match in matches:
        function_name = match.group('name')[:-2]
        start_line = file.count('\n', 0, match.start()) + 1
        function_info.append((function_name, start_line))
    return function_info

def main():
    repo = git.Repo("..")
    default_branch = "main"

    main_branch = repo.commit(default_branch)
    tree = main_branch.tree

    for blob in tree.traverse():
        if blob.type == 'blob':
            if blob.path.split(".")[-1] == "c":
                file = repo.git.show(f"{default_branch}:{blob.path}")
                function_info = get_function_data_from_file(file)
                for i in function_info:
                    print(i)

if __name__ == "__main__":
    main()
