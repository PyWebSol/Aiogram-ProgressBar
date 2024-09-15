from setuptools import setup, find_packages

setup(
   name="aioprogress",
   author="PyWebSol",
   description="Library for create a progressbar in AioGram.",
   packages=find_packages(),
   include_package_data=True,
   classifiers=[
       "Environment :: Web Environment",
       "Intended Audience :: Developers",
       "Operating System :: OS Independent"
       "Programming Language :: Python",
       "Programming Language :: Python :: 3.10",
       "Topic :: Internet :: WWW/HTTP",
       "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
   ],
   python_requires='>=3.10',
   setup_requires=['aiogram'],
   version_config={
       "dirty_template": "{tag}",
   }
)
