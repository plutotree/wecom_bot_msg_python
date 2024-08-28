from setuptools import setup, find_packages

setup(
    name='wecom_bot_msg',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    author='plutotree',
    author_email='plutotreetree@gmail.com',
    description='A simple API wrapper for WeCom (Worker Wechat) group bot to send msg.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/plutotree/wecom_bot_msg_python',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
