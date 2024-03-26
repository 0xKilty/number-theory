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


def template_to_string(template: str, data: dict) -> str:
    template = Template(template)
    rendered_html = template.render(data)
    return rendered_html


def write_with_template(template: str, data: dict, output: str):
    with open(f'../../templates/{template}', 'r') as base_template_file:
        base_template = base_template_file.read()

    rendered_html = template_to_string(base_template, data)

    with open(f'../../build/number-theory/{output}', 'w') as output_file:
        output_file.write(rendered_html)


def write_with_links(template: str, links: dict) -> str:
    with open(f'../../data/{template}', 'r') as template_file:
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
    repo = git.Repo("../..")
    default_branch = "main"

    main_branch = repo.commit(default_branch)
    tree = main_branch.tree

    res = {}
    for blob in tree.traverse():
        if blob.type == 'blob':
            if (blob.type == 'blob' and 
                blob.path.startswith('python/numbertheory/') and
                blob.path.endswith('.py')):
                file = repo.git.show(f"{default_branch}:{blob.path}")
                get_python_function_data(file, blob.path, res)
    return res

def get_functions_in_page(content, docs):
    soup = BeautifulSoup(content, 'html.parser')
    for h4 in soup.find_all('h4'):
        if cat not in docs:
            docs[cat] = []
        docs[cat].append(h4['id'])

def get_docs_list(docs: dict) -> str:
    list_str = '<ul>'
    for category, functions in docs.items():
        list_str += f'''
            <li>
                <strong><a href="">{category.replace("-", " ").title()}</a></strong>
            </li><ul>
        '''
        for function in functions:
            list_str += f'''
                <li><code>
                    <strong><a href="">{function}</a></strong>
                </code></li>
            '''
        list_str += '</ul>'
    list_str += '</ul>'
    return list_str

if __name__ == "__main__":
    os.chdir('../build')
    clear_dir('.')
    os.makedirs('number-theory')
    os.chdir('./number-theory')
    copy_files('../../assets', '.')

    with open(f'../../data/index.html', 'r') as index_file:
        index_template = index_file.read()
    write_with_template('base.html', {'content': index_template}, 'index.html')

    os.makedirs('contribute')
    with open(f'../../data/contribute.html', 'r') as contribute_file:
        contribute_template = contribute_file.read()
    write_with_template('base.html', {'content': contribute_template}, 'contribute/index.html')

    github_links = get_github_links()
    docs = {}

    for category in os.listdir('../../data/docs'):
        cat = category.split('.')[0]
        os.makedirs(cat)
        content = write_with_links(f'docs/{category}', github_links)
        write_with_template('base.html', {'content': content}, f'{cat}/index.html')
        get_functions_in_page(content, docs)
        

    os.makedirs('examples')
    for example in os.listdir('../../data/examples'):
        example_text = write_with_links(f'examples/{example}', github_links)
        write_with_template('base.html', {'content': example_text}, f'examples/{example}')

    os.makedirs('docs')
    list_str = get_docs_list(docs)
    with open('../../data/docs.html', 'r') as docs_file:
        docs_str = docs_file.read()
    
    docs_content = template_to_string(docs_str, {'list': list_str})
    write_with_template('base.html', {'content': docs_content}, 'docs/index.html')
    