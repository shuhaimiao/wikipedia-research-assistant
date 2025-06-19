from setuptools import setup, find_packages

setup(
    name="wikipedia-research-assistant",
    version="0.1.0",
    description="A MCP server for intelligent Wikipedia research",
    author="Shuhai Miao",
    author_email="shuhai.miao@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "wikipedia>=1.4.0",
        "mcp>=0.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ]
    },
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "wikipedia-assistant=wikipedia_assistant.server:main",
        ],
    },
) 