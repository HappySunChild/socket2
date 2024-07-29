import setuptools

setup_info = {
	'name': 'socket2',
	'version': '1.0.0',
	'author': 'HappySunChild',
	'description': 'websockets',
	'url': 'https://github.com/HappySunChild',
	'packages': setuptools.find_packages(),
	'python_requires': '>=3.9',
	'install_requires': [
		'websockets>=12.0',
		'python-json>=2.0.9'
	]
}

setuptools.setup(**setup_info)