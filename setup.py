from setuptools import setup, find_packages

setup(name='mcqgenerator',
    version='0.0.1',
    description='My Application',
    author='Pratyush Kumar Jha',
    author_email='pratyush.snj@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
    )