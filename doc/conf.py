# -*- coding: utf-8 -*-
#
# just_mospec documentation build configuration file

import sys
import os
from importlib import import_module

sys.path.insert(0, os.path.abspath('../py'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'astropy': ('https://docs.astropy.org/en/stable/', None),
    'h5py': ('https://docs.h5py.org/en/latest/', None)
    }

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'just_mospec'
copyright = u'2026, Gu Yizhou'

__import__(project)
package = sys.modules[project]

version = package.__version__.split('-', 1)[0]
release = package.__version__

exclude_patterns = ['_build']
add_function_parentheses = True
pygments_style = 'sphinx'
keep_warnings = True
napoleon_include_private_with_doc = True

autodoc_mock_imports = []
for missing in ('numpy', 'scipy', 'astropy', 'desisim'):
    try:
        foo = import_module(missing)
    except ImportError:
        autodoc_mock_imports.append(missing)

html_theme = 'sphinx_rtd_theme'
html_last_updated_fmt = '%b %d, %Y'
htmlhelp_basename = 'just_mospecdoc'
