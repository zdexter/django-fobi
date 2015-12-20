# -*- coding: utf-8 -*-
#
# django-fobi documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 14 00:34:43 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../src'))
sys.path.insert(0, os.path.abspath('../examples'))

from nine.versions import DJANGO_LTE_1_7, DJANGO_GTE_1_8, DJANGO_GTE_1_7

if DJANGO_GTE_1_7:
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple.settings_docs')
    django.setup()

try:
    import fobi
    version = fobi.__version__
    project = fobi.__title__
    copyright = fobi.__copyright__
except ImportError as err:
    version = '0.1'
    project = u'django-fobi'
    copyright = u'2014, Artur Barseghyan <artur.barseghyan@gmail.com>'

try:
    from simple import settings_docs as docs_settings
except Exception as e:
    PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))
    gettext = lambda s: s

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    class DocsSettings(object):
        """
        """
        INSTALLED_APPS = (
            # Admin dashboard
            'admin_tools',
            'admin_tools.menu',
            'admin_tools.dashboard',

            # Django core and contrib apps
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.admin',
            'django.contrib.sitemaps',

            # Third party apps used in the project
            #'south', # Database migration app
            #'tinymce', # TinyMCE
            'easy_thumbnails', # Thumbnailer
            'registration', # Auth views and registration app
            'localeurl', # Locale URL

            # *****************************************************************
            # *****************************************************************
            # **************************** Fobi core **************************
            # *****************************************************************
            # *****************************************************************
            'fobi',

            # *****************************************************************
            # *****************************************************************
            # ************************* Fobi form elements ********************
            # *****************************************************************
            # *****************************************************************

            # *****************************************************************
            # **************************** Form fields ************************
            # *****************************************************************
            #'fobi.contrib.plugins.form_elements.fields.birthday',
            'fobi.contrib.plugins.form_elements.fields.boolean',
            'fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple',
            'fobi.contrib.plugins.form_elements.fields.date',
            'fobi.contrib.plugins.form_elements.fields.date_drop_down',
            'fobi.contrib.plugins.form_elements.fields.datetime',
            'fobi.contrib.plugins.form_elements.fields.decimal',
            'fobi.contrib.plugins.form_elements.fields.email',
            'fobi.contrib.plugins.form_elements.fields.file',
            'fobi.contrib.plugins.form_elements.fields.float',
            'fobi.contrib.plugins.form_elements.fields.hidden',
            #'fobi.contrib.plugins.form_elements.fields.hidden_model_object',
            'fobi.contrib.plugins.form_elements.fields.input',
            'fobi.contrib.plugins.form_elements.fields.integer',
            'fobi.contrib.plugins.form_elements.fields.ip_address',
            'fobi.contrib.plugins.form_elements.fields.null_boolean',
            'fobi.contrib.plugins.form_elements.fields.password',
            'fobi.contrib.plugins.form_elements.fields.radio',
            'fobi.contrib.plugins.form_elements.fields.regex',
            'fobi.contrib.plugins.form_elements.fields.select',
            'fobi.contrib.plugins.form_elements.fields.select_model_object',
            'fobi.contrib.plugins.form_elements.fields.select_multiple',
            'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
            'fobi.contrib.plugins.form_elements.fields.slug',
            'fobi.contrib.plugins.form_elements.fields.text',
            'fobi.contrib.plugins.form_elements.fields.textarea',
            'fobi.contrib.plugins.form_elements.fields.time',
            'fobi.contrib.plugins.form_elements.fields.url',

            # *****************************************************************
            # ************************ Security elements **********************
            # *****************************************************************
            'fobi.contrib.plugins.form_elements.security.honeypot',

            # *****************************************************************
            # ************************* Testing elements **********************
            # *****************************************************************
            'fobi.contrib.plugins.form_elements.test.dummy',

            # *****************************************************************
            # ************************* Content elements **********************
            # *****************************************************************
            'fobi.contrib.plugins.form_elements.content.content_image',
            'fobi.contrib.plugins.form_elements.content.content_text',
            'fobi.contrib.plugins.form_elements.content.content_video',

            # *****************************************************************
            # *****************************************************************
            # ************************* Fobi form handlers ********************
            # *****************************************************************
            # *****************************************************************
            'fobi.contrib.plugins.form_handlers.db_store',
            'fobi.contrib.plugins.form_handlers.http_repost',
            'fobi.contrib.plugins.form_handlers.mail',

            # *****************************************************************
            # *****************************************************************
            # ************************** Fobi themes **************************
            # *****************************************************************
            # *****************************************************************

            # *****************************************************************
            # ************************ Bootstrap 3 theme **********************
            # *****************************************************************
            'fobi.contrib.themes.bootstrap3', # Bootstrap 3 theme
            # DateTime widget
            'fobi.contrib.themes.bootstrap3.widgets.form_elements.datetime_bootstrap3_widget',
            'fobi.contrib.themes.bootstrap3.widgets.form_elements.date_bootstrap3_widget',

            # *****************************************************************
            # ************************ Foundation 5 theme *********************
            # *****************************************************************
            'fobi.contrib.themes.foundation5', # Foundation 5 theme
            'fobi.contrib.themes.foundation5.widgets.form_handlers.db_store_foundation5_widget',

            # *****************************************************************
            # **************************** Simple theme ***********************
            # *****************************************************************
            'fobi.contrib.themes.simple', # Simple theme
        )

        if DJANGO_LTE_1_7:
            INSTALLED_APPS.append('south')

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': PROJECT_DIR('../db/example.db'),
            }
        }
        MEDIA_ROOT = PROJECT_DIR(os.path.join('..', 'media'))
        MEDIA_URL = '/media/'
        MIDDLEWARE_CLASSES = (
            'django.contrib.sessions.middleware.SessionMiddleware',
            'localeurl.middleware.LocaleURLMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            # Uncomment the next line for simple clickjacking protection:
            # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
        )
        ROOT_URLCONF = 'urls'
        SECRET_KEY = '97818c*w97Zi8a-m^1coRRrmurMI6+q5_kyn*)s@(*_Pk6q423'
        SITE_ID = 1
        STATICFILES_DIRS = (
            PROJECT_DIR(os.path.join('..', 'media', 'static')),
        )
        STATICFILES_FINDERS = (
            'django.contrib.staticfiles.finders.FileSystemFinder',
            'django.contrib.staticfiles.finders.AppDirectoriesFinder',
            #'django.contrib.staticfiles.finders.DefaultStorageFinder',
        )
        STATIC_URL = '/static/'
        STATIC_ROOT = PROJECT_DIR(os.path.join('..', 'static'))

        if DJANGO_GTE_1_8:
            TEMPLATES = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    #'APP_DIRS': True,
                    'DIRS': [PROJECT_DIR('templates'),],
                    'OPTIONS': {
                        'context_processors': [
                            "django.contrib.auth.context_processors.auth",
                            "django.core.context_processors.debug",
                            "django.core.context_processors.i18n",
                            "django.core.context_processors.media",
                            "django.core.context_processors.static",
                            "django.core.context_processors.tz",
                            "django.contrib.messages.context_processors.messages",
                            "django.core.context_processors.request",
                            "fobi.context_processors.theme", # Important!
                            "fobi.context_processors.dynamic_values", # Optional
                        ],
                        'loaders': [
                            'django.template.loaders.filesystem.Loader',
                            'django.template.loaders.app_directories.Loader',
                            'django.template.loaders.eggs.Loader',
                            'admin_tools.template_loaders.Loader',
                        ],
                        'debug': False,
                    }
                },
            ]
        else:
            TEMPLATE_CONTEXT_PROCESSORS = (
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.core.context_processors.request",
                "fobi.context_processors.theme", # Important!
                "fobi.context_processors.dynamic_values", # Optional
            )
            TEMPLATE_DIRS = (
                PROJECT_DIR('templates'),
            )
            TEMPLATE_LOADERS = (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            )
            TEMPLATE_DEBUG = False
    # END class ExampleSettings()

    docs_settings = DocsSettings()

# -- Django configuration ------------------------------------------------------
from django.conf import settings

if not settings.configured:
    INSTALLED_APPS = list(docs_settings.INSTALLED_APPS)

    INSTALLED_APPS.append('mptt')
    INSTALLED_APPS.append('cms')
    INSTALLED_APPS.append('fobi.contrib.apps.djangocms_integration')
    INSTALLED_APPS.append('feincms')
    INSTALLED_APPS.append('fobi.contrib.apps.feincms_integration')
    INSTALLED_APPS.append('captcha')
    INSTALLED_APPS.append('fobi.contrib.plugins.form_elements.security.captcha')

    if 'foo' in INSTALLED_APPS:
        INSTALLED_APPS.remove('foo')

    django_configuration = {
        'DATABASES': docs_settings.DATABASES,
        'INSTALLED_APPS': INSTALLED_APPS,
        'MEDIA_ROOT': docs_settings.MEDIA_ROOT,
        'MEDIA_URL': docs_settings.MEDIA_URL,
        'MIDDLEWARE_CLASSES': docs_settings.MIDDLEWARE_CLASSES,
        'ROOT_URLCONF': docs_settings.ROOT_URLCONF,
        'SECRET_KEY': docs_settings.SECRET_KEY,
        'SITE_ID': docs_settings.SITE_ID,
        'STATICFILES_DIRS': docs_settings.STATICFILES_DIRS,
        'STATICFILES_FINDERS': docs_settings.STATICFILES_FINDERS,
        'STATIC_URL': docs_settings.STATIC_URL,
        'STATIC_ROOT': docs_settings.STATIC_ROOT,
    }

    if DJANGO_GTE_1_8:
        django_configuration.update({
            'TEMPLATES': docs_settings.TEMPLATES
        })
    else:
        django_configuration.update({
            'TEMPLATE_CONTEXT_PROCESSORS': docs_settings.TEMPLATE_CONTEXT_PROCESSORS,
            'TEMPLATE_DIRS': docs_settings.TEMPLATE_DIRS,
            'TEMPLATE_LOADERS': docs_settings.TEMPLATE_LOADERS,
        })

    settings.configure(**django_configuration)

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
#project = u'django-fobi'
#copyright = u'2014, Artur Barseghyan <artur.barseghyan@gmail.com>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = '0.1'
# The full version, including alpha/beta/rc tags.
#release = '0.1'
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'django-fobidoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'django-fobi.tex', u'django-fobi Documentation',
   u'Artur Barseghyan \\textless{}artur.barseghyan@gmail.com\\textgreater{}', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'django-fobi', u'django-fobi Documentation',
     [u'Artur Barseghyan <artur.barseghyan@gmail.com>'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'django-fobi', u'django-fobi Documentation',
   u'Artur Barseghyan <artur.barseghyan@gmail.com>', 'django-fobi', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'django-fobi'
epub_author = u'Artur Barseghyan <artur.barseghyan@gmail.com>'
epub_publisher = u'Artur Barseghyan <artur.barseghyan@gmail.com>'
epub_copyright = u'2014, Artur Barseghyan <artur.barseghyan@gmail.com>'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True
