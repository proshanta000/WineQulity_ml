import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "WineQulity_ml"
AUTHOR_USER_NAME = "Proshanta000"
SRC_REPO = "WineMl"
AUTHOR_EMAIL = "proshanta.mithu5@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small python project about wind qulity",
    long_description=long_description,
    long_description_content_type="text/Markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "BUG Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)