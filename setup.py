
from pip.req import parse_requirements
from setuptools import setup, find_packages

long_description = "Sistema de Gestion de Aforo mediante el uso de Iot"
requirements = parse_requirements('requirements.txt', session=False)
install_requires = [str(r.req) for r in requirements]

setup(
    name             = 'sga_iot_sub',
    description      = 'Sistema de Gestion de Aforo - IOT (Subscriptor)',
    packages         = find_packages(),
    author           = 'sga-iot',
    author_email     = 'sga-iot [at] gmail.com',
    scripts          = ['bin/sga-iot-sub'],
    install_requires = install_requires,
    version          = '0.0.1',
    url              = 'https://github.com/johnmontero/sga-iot-sub',
    license          = "MIT",
    zip_safe         = False,
    keywords         = "sga, iot, subscriptor",
    long_description = long_description,
    classifiers      = [
                        'Development Status :: 4 - Beta',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: MIT License',
                        'Topic :: Software Development :: Build Tools',
                        'Topic :: Software Development :: Libraries',
                        'Topic :: Software Development :: Testing',
                        'Topic :: Utilities',
                        'Operating System :: MacOS :: MacOS X',
                        'Operating System :: Microsoft :: Windows',
                        'Operating System :: POSIX',
                        'Programming Language :: Python :: 2.6',
                        'Programming Language :: Python :: 2.7',
                      ]
)
