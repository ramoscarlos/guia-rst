project = 'Guía de reStructuredText'
copyright = '2021, Carlos Alberto Ramos López'
author = 'Carlos Alberto Ramos López'

release = '0.1-alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


latex_elements = {
	'sphinxsetup': '''
		hmargin={0.625in,0.500in},
		vmargin={0.375in,0.750in},
		verbatimwithframe=false
	''',
	'passoptionstopackages': r'''
	\PassOptionsToPackage{
		paperwidth=6in,
		paperheight=9in,
	}{geometry}
	\PassOptionsToPackage{svgnames}{xcolor}
	''',
	'preamble': r'\input{preambulo.tex.txt}',
	'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
	'extrapackages': r'''
		\usepackage{changepage}                     % Para ajustar el margen del código en portada.
		\usepackage{mdframed}                       % Para colocar una caja de color (usada en portada).
		\usepackage{enumitem}                       % Eliminar separación entre elementos de una lista.
		\usepackage{setspace}                       % Permite modificar el espacio entre líneas.
		\usepackage[final]{microtype}               % Mejora la tipografía.
		\usepackage{mathpazo}                       % Cambio de fuente base y matemática.
		\usepackage[ttdefault=true]{AnonymousPro}   % Cambio de fuente de ancho fijo (por una que soporta negritas e itálicas).
		\usepackage{calc}                           % Para poder colocar expresiones calculadas.
		\usepackage{etoolbox}                       % Para colocar contenido antes y después de un entorno ya definido.
		\usepackage[labelformat=empty]{caption}     % Previene que LaTeX coloque el texto "Figura #."
	''',
	'maketitle': r'''
		\input{portada.tex.txt}
		\input{hoja_titulo.tex.txt}
		\input{copyright.tex.txt}
		\input{dedicatoria.tex.txt}
	''',
}

latex_additional_files = [
	'preambulo.tex.txt',
	'portada.tex.txt',
	'hoja_titulo.tex.txt',
	'copyright.tex.txt',
	'dedicatoria.tex.txt',
	# Imágenes
	'img/LeanPub.pdf',
	'img/LeanPub.png',
	'img/LeanPubW.png',
	'img/CC-BY-NC-SA.png'
]