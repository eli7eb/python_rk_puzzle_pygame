from setuptools import setup

setup(
    name='rk_puzzle_python',
    version='0.1.0',
    packages=['rk_communication', 'player_input'],
    entry_points={
          'console_scripts': [
              'rk_puzzle_python = rk_puzzle_python.__main__:main'
          ]
      },
    url='',
    license='',
    author='elisheva',
    author_email='',
    description=''
)