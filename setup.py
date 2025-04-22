from setuptools import find_packages,setup

setup(
    name = 'email_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'joblib',
        'scikit-learn'
    ],
    include_package_data=True,
)