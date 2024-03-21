from jinja2 import Template
import os
import shutil
import git
import re
import ast

def clear_dir(dir_name: str):
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)


def copy_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)
        shutil.copy2(source_path, destination_path)


def write_with_template(template: str, output: str):
    with open('../templates/base.html', 'r') as base_template_file:
        base_template = base_template_file.read()

    with open(f'../templates/{template}.html', 'r') as template_file:
        index_template = template_file.read()

    base_data = {'content': index_template}

    template = Template(base_template)
    rendered_html = template.render(base_data)

    with open(f'../build/{output}.html', 'w') as output_file:
        output_file.write(rendered_html)


def get_c_function_data(file):
    pattern = r'(?P<name>\b(?:int|void|char|float|double)\s+(\w+)\s*\([^)]*\)\s*{)'
    matches = re.finditer(pattern, file)
    function_info = []
    for match in matches:
        function_name = match.group('name')[:-2]
        start_line = file.count('\n', 0, match.start()) + 1
        function_info.append((function_name, start_line))
    return function_info


def get_python_function_data(file):
    functions = []
    tree = ast.parse(file)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            functions.append((node.name, node.lineno))
    return functions


def get_github_links():
    repo = git.Repo("..")
    default_branch = "main"

    main_branch = repo.commit(default_branch)
    tree = main_branch.tree

    for blob in tree.traverse():
        if blob.type == 'blob':
            split_path = blob.path.split('/')
            if split_path[0] == 'python':
                file = repo.git.show(f"{default_branch}:{blob.path}")
                function_info = get_python_function_data(file)
            elif split_path[0] == 'c':
                file = repo.git.show(f"{default_branch}:{blob.path}")
                function_info = get_c_function_data(file)


if __name__ == "__main__":
    os.chdir('../build')
    clear_dir('.')
    copy_files('../assets', '.')
    write_with_template('index', 'index')
    # write the contribute
    # get the github links
    get_github_links()
    # write the categories
    # write the examples
    # write the dir
    

'''
with open('../templates/base.html', 'r') as base_template_file:
    base_template = base_template_file.read()

with open('../templates/index.html', 'r') as template_file:
    index_template = template_file.read()

base_data = {'content': index_template}

template = Template(base_template)

rendered_html = template.render(base_data)

with open('../docs/test.html', 'w') as output_file:
    output_file.write(rendered_html)
'''

