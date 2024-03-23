from jinja2 import Template
import os
import shutil
import git
import re
import ast
from bs4 import BeautifulSoup

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


def write_with_template(data: dict, output: str):
    with open('../templates/base.html', 'r') as base_template_file:
        base_template = base_template_file.read()

    template = Template(base_template)
    rendered_html = template.render(data)

    with open(f'../build/{output}', 'w') as output_file:
        output_file.write(rendered_html)

def write_with_links(template: str, links: dict) -> str:
    with open(f'../data/{template}', 'r') as template_file:
        read_template = template_file.read()

    template = Template(read_template)
    rendered_html = template.render(links)

    return rendered_html


def get_c_function_data(file):
    pattern = r'(?P<name>\b(?:int|void|char|float|double)\s+(\w+)\s*\([^)]*\)\s*{)'
    matches = re.finditer(pattern, file)
    function_info = []
    for match in matches:
        function_name = match.group('name')[:-2]
        start_line = file.count('\n', 0, match.start()) + 1
        function_info.append((function_name, start_line))
    return function_info


def get_python_function_data(file, path, res):
    tree = ast.parse(file)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            res[node.name] = f'https://github.com/0xKilty/number-theory/blob/main/{path}#L{node.lineno}'


def get_github_links():
    repo = git.Repo("..")
    default_branch = "main"

    main_branch = repo.commit(default_branch)
    tree = main_branch.tree

    res = {}
    for blob in tree.traverse():
        if blob.type == 'blob':
            split_path = blob.path.split('/')
            if split_path[0] == 'python':
                file = repo.git.show(f"{default_branch}:{blob.path}")
                get_python_function_data(file, blob.path, res)
    return res
        

if __name__ == "__main__":
    os.chdir('../build')
    clear_dir('.')
    copy_files('../assets', '.')

    with open(f'../data/index.html', 'r') as index_file:
        index_template = index_file.read()
    write_with_template({'content': index_template}, 'index.html')

    os.makedirs('contribute')
    with open(f'../data/contribute.html', 'r') as contribute_file:
        contribute_template = contribute_file.read()
    write_with_template({'content': contribute_template}, 'contribute/index.html')

    github_links = get_github_links()

    for category in os.listdir('../data/docs'):
        cat = category.split('.')[0]
        print(cat)
        os.makedirs(cat)
        content = write_with_links(f'docs/{category}', github_links)
        write_with_template({'content': content}, f'{cat}/index.html')

    os.makedirs('examples')
    for example in os.listdir('../data/examples'):
        example_text = write_with_links(f'examples/{example}', github_links)
        write_with_template({'content': example_text}, f'examples/{example}')

    os.makedirs('docs')
