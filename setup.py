"""ecoshard setup.py."""
import numpy
from setuptools.extension import Extension
from setuptools import setup

import os
print(os.environ['PATH'])


LONG_DESCRIPTION = '%s\n\n%s' % (
    open('README.rst').read(),
    open('HISTORY.rst').read())

setup(
    name='ecoshard',
    setup_requires=['setuptools_scm'],
    # use_scm_version={'version_scheme': 'post-release',
    #                  'local_scheme': 'node-and-date'},
    install_requires=["requests","gdal","numpy","shapely","psutil","numexpr", "retrying", "scipy", "rtree"],
    description='EcoShard GIS data',
    long_description=LONG_DESCRIPTION,
    maintainer='Rich Sharp',
    maintainer_email='richpsharp@gmail.com',
    url='https://github.com/therealspring/ecoshard',
    packages=[
        'ecoshard',
        'ecoshard.geoprocessing',
        'ecoshard.geoprocessing.routing',
        'ecoshard.taskgraph',
        'ecoshard.fetch_data',
        'ecoshard.geosharding',
        ],
    package_dir={
        'ecoshard': 'src/ecoshard',
        'ecoshard.taskgraph': 'src/taskgraph',
        'ecoshard.fetch_data': 'src/fetch_data',
    },
    zip_safe=False,
    include_package_data=True,
    license='BSD',
    keywords='computing reproduction',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License'
    ],
    ext_modules=[
        Extension(
            name="ecoshard.geoprocessing.routing.routing",
            sources=["src/ecoshard/geoprocessing/routing/routing.pyx"],
            include_dirs=[
                numpy.get_include(),
                'src/ecoshard/geoprocessing/routing'],
            language="c++",
        ),
        Extension(
            "ecoshard.geoprocessing.geoprocessing_core",
            sources=[
                'src/ecoshard/geoprocessing/geoprocessing_core.pyx'],
            include_dirs=[numpy.get_include()],
            language="c++"
        ),
    ]
)
