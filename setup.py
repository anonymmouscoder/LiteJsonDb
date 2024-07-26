"""
░██████╗███████╗████████╗██╗░░░██╗██████╗░░░░██████╗░██╗░░░██╗
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗░░░██╔══██╗╚██╗░██╔╝
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝░░░██████╔╝░╚████╔╝░
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░░░░██╔═══╝░░░╚██╔╝░░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░██╗██║░░░░░░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░
"""
from setuptools import setup, find_packages

long_description = """Documentation is available here:https://github.com/codingtuto/LiteJsonDb/
"""

setup(
    name="LiteJsonDb",
    version="1.0.0",
    author="Coding Team",
    author_email="codingteamgroup@gmail.com",
    license='MIT',
    description='A lightweight JSON-based database system inspired by Firestore (Firebase). It\'s designed for simplicity and ease of use.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/codingtuto/LiteJsonDb/",
    packages=find_packages(exclude=["testing"]),
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Setuptools Plugin",
        "Environment :: Console",
    ],
)
