import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

import bs4 as bs

from business_rules import build_business_rules
from codelists import build_code_lists
from condition import build_conditions
from messagetypes import build_message_types
from rules import build_rules


INITIAL_PATH = Path(os.getcwd())


def extract_docxs_from_zip(zip_path: Path, output_path: Path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_path)


def convert_docx_to_htmls(docx_path: Path, output_path: Path):
    command_and_args = [
        'soffice',
        '--headless',
        '--convert-to', 'html',
        '--outdir', docx_path.parent,
        docx_path,
    ]
    subprocess.run(command_and_args)


def scrape_and_write_markdown(html_path: Path):
    soup = bs.BeautifulSoup(open(html_path).read(), features='html.parser')
    for h1 in soup('h1'):
        for a in h1('a'):
            title = a.text
            a.extract()
            h1.string = title
    with open(html_path.with_suffix('.headers'), 'w') as file:
        file.write(soup.prettify())


def copy_built_files():
    src = INITIAL_PATH / Path('partials')
    dst = INITIAL_PATH / Path('../source/documentation/partials')
    shutil.copytree(src, dst, dirs_exist_ok=True)

    erb_files = [
        'business-rules.html.md.erb',
        'conditions.html.md.erb',
        'messagetypes.html.md.erb',
        'rules.html.md.erb',
        'technical-codelists.html.md.erb',
    ]
    for erb_file in erb_files:
        src = INITIAL_PATH / Path(erb_file)
        dst = INITIAL_PATH / Path(f'../source/documentation/{erb_file}')
        shutil.copyfile(src, dst)


def apply_post_gen_changes_patch():
    # patch file originally generated with:
    # git diff --patch -R ../source/documentation/ > post-gen-changes.patch
    command_and_args = [
        'patch',
        '-p1',
        '-i', INITIAL_PATH / Path('post-gen-changes.patch'),
    ]

    os.chdir(INITIAL_PATH / Path('..'))
    subprocess.run(command_and_args)


def specs_to_markdown():
    with tempfile.TemporaryDirectory() as temp_dir_name:
        output_path = Path(temp_dir_name)

        ddnea_zip_path = INITIAL_PATH / Path(
            '../source/downloads/phase-4.1/Design Document for National Excise Applications (DDNEA) v3.14 for phase 4.1.zip')
        extract_docxs_from_zip(ddnea_zip_path, output_path)

        for docx_path in output_path.rglob("*.docx"):
            convert_docx_to_htmls(docx_path, output_path)

        for html_path in output_path.rglob("*.html"):
            scrape_and_write_markdown(html_path)

        build_message_types()
        build_business_rules()
        build_code_lists()
        build_conditions()
        build_rules()

        copy_built_files()
        apply_post_gen_changes_patch()


if __name__ == "__main__":
    specs_to_markdown()
