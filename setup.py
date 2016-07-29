from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='pansharpening',
      version='0.1.0',
      description=u"Pansharpening",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Sean Gillies",
      author_email='sean@mapbox.com',
      url='https://github.com/mapbox/pansharpen',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'rasterio',
          'rio-mucho',
      ],
      extras_require={
          'test': ['pytest', 'hypothesis', 'pytest-cov','codecov'],
      },
      entry_points="""
      [console_scripts]
      pansharpen=pansharpen.scripts.pan_cli:cli
      """
      )
