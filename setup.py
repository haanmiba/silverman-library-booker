from setuptools import setup, find_packages

setup(
    name="SilvermanLibraryStudyRoomBooker",
    version='1.0.0',
    description='Room booker for UB Silverman Library.',
    long_description="Command-line interface for booking study rooms in the University at Buffalo Silverman Library.",
    url='https://github.com/haanmiba/silverman-library-booker',
    keywords='cli webscrape webcrawl',
    author='haanmiba',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'silverman-booker = commands:main'
        ]
    }
)