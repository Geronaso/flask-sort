from setuptools import setup

from flask_sort.models import vowel_count

setup(
    name='flask_sort',
    packages=['flask_sort'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

# curl -X POST http://127.0.0.1:5000/vowel_count -H 'Content-Type: application/json' -d '{"words":["batman", "robin", "coringa"]}'

# curl -X POST http://127.0.0.1:5000/sort -H 'Content-Type: application/json' -d '{"words":["batman", "robin", "coringa"],"reverse":"False"}'

# curl -X POST -G 'http://127.0.0.1:5000/sort' -d '{"words":["batman", "robin", "coringa"]}'