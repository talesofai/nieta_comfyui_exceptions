from setuptools import setup, find_packages

setup(
    name="nieta-comfyui-exceptions",
    version="0.0.1",
    packages=find_packages(),
    description="一个用于处理常见异常情况的Python包",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="nieta-zjj",
    author_email="zjj@nieta.art",
    url="https://github.com/talesofai/nieta_comfyui_exceptions",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)