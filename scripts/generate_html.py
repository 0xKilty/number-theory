from jinja2 import Template

with open('../templates/base.html', 'r') as base_template_file:
    base_template = base_template_file.read()

with open('../templates/index.html', 'r') as index_template_file:
    index_template = index_template_file.read()

base_data = {
    'content': index_template
}

template = Template(base_template)

rendered_html = template.render(base_data)

with open('../docs/test.html', 'w') as output_file:
    output_file.write(rendered_html)