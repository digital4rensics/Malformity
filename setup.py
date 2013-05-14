from setuptools import setup, find_packages

setup(
    name='Malformity',
    author='Keith Gilbert - @digital4rensics',
    version='1.0',
    author_email='Keith@digital4rensics.com',
    description='This project is a collection of transforms and entities to assist in Malware and Malicious Infrastructure research.',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz' ] # list of resources
    },
    install_requires=[
        'canari==0.9',
        'mechanize==0.2.5',
        'BeautifulSoup==3.2.1',
	'requests==1.2.0'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
