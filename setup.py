from setuptools import setup
from setuptools import find_packages
from glob import glob
from os.path import basename
from os.path import splitext

setup(
    name="dessin-scale",
    version="1.0.0",
    license="MIT",
    description="指定した画像にデッサンスケールのような枠線を描画した画像を作成するコマンド",
    author="emittam",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=["Pillow"],
    entry_points={
        "console_scripts": [
            "dessin-scale = dessin_scale.main:main",
        ]
    }
)