try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup = {
          name="PdfSorter",
          version="0.1",
          description="My Project",
          author="KM Chan",
          author_mail="kmchan@kmchan.nl",
          url="https=//github.com/kmchanNL",
          install_requirements="nose",
          packages=find_packages(exclude=('tests*','testing*')),
          scripts=""

}

setup(**config)
