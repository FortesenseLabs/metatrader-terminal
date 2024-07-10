import io
from setuptools import setup, find_packages


def readme():
    with io.open("README.md", encoding="utf-8") as f:
        return f.read()


def requirements(filename):
    with io.open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


setup(
    name="metatrader-sockets",
    version="0.0.1",
    packages=find_packages(),
    url="https://github.com/FortesenseLabs/metatrader-terminal",
    download_url="https://github.com/FortesenseLabs/metatrader-terminal/archive/refs/tags/v0.0.1.tar.gz",
    license="GPL-3.0",
    author="Fortesense Labs",
    author_email="fortesenselabs@gmail.com",
    description="Client SDK of MetaTrader Sockets API",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requirements(filename="requirements.txt"),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",
    keywords=", ".join(
        [
            "metatrader",
            "api",
            "socket-io",
            "mt5",
            "mt4",
            "websockets",
            "mt5-ea",
            "f-api",
            "historical-data",
            "financial-data",
            "stocks",
            "funds",
            "etfs",
            "indices",
            "currency crosses",
            "bonds",
            "commodities",
            "crypto currencies",
            "synthetic instruments",
            "trading",
            "investment",
            "portfolio",
            "backtesting",
            "quantitative analysis",
        ]
    ),
    project_urls={
        "Bug Reports": "https://github.com/FortesenseLabs/metatrader-terminal/issues",
        "Source": "https://github.com/FortesenseLabs/metatrader-terminal",
        "Documentation": "https://github.com/FortesenseLabs/metatrader-terminal/docs",
    },
)
