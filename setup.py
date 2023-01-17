from	setuptools	import	setup

setup(
	name='openFrom',
	version='0.1',
	py_modules=['openFrom'],
	install_requires=[
		'argparse',
		'subprocess'
	],
	entry_points={
		'console_scripts': [
			'openFrom=openFrom:main'
		]
	}
)
