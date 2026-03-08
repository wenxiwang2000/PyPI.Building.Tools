from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name="wenxi-ai-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "wenxi-ai-tools = wenxi_ai_tools.main:hello",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
    author="Wenxi Wang",
    description="A simple example Python package with a command line entry point.",
    python_requires=">=3.9",
)
