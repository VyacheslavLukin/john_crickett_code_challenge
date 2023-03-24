from setuptools import setup

setup(
    name="wc_code_challenge",
    version="0.1",
    py_modules=["ccwc"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        ccwc=ccwc:cli
    """,
)