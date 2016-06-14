from pdf import create_pdf
from jinja2 import Environment, FileSystemLoader
import os

# dafq is this?
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def html_doc(variables):
    # dafq is that?
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
    return j2_env.get_template('pdf.html.j2').render(
        variables=variables
    )

def create(albumData):
  pdf = create_pdf(html_doc(albumData))
  return pdf
