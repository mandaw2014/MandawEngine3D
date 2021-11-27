from distutils.core import setup

setup(name='Mandaw3D',
      version='b0.0.1',
      description='A 3D Python GameEngine Made With RaylibPy',
      author='mandaw2014',
      keywords="python 3d game development",
      author_email='mandawbuisness@gmail.com',
      url='https://github.com/mandaw2014/MandawEngine3D',
      packages=['mandaw3d'],
      package_dir={'mandaw3d': 'mandaw3d'},
      install_requires=["raylibpy"]
      )
