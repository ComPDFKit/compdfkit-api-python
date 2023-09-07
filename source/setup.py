from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='compdfkit-api-python',
    version='1.3.2',
    description='Python SDK for compdfkit API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='PDF Technologies, Inc.',
    author_email='support@compdf.com',
    url='https://api.compdf.com/api-reference/overview',
    packages=find_packages(),
    install_requires=['requests', 'requests_toolbelt'],
    license='MIT License',
    python_requires='>=3.8',
)
