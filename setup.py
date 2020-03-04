from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
	name='IsraVoteAI',
	version=__version__,
	packages=find_packages(),
	install_requires=['torch', 'numpy', 'pandas', 'kaggle'],
	entry_points={
		"console_scripts": ["detect_anomalies=IsraVoteAI.main:main"]
	})

