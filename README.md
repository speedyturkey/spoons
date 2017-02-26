*README*

This is the README for the SpoonsOnline application.

Setup Instructions

For now, we need to use both Anaconda and virtualenv. The environment on AWS by default will
be a standard Python 3.4 install, so our Conda build probably won't work and we'll need to use virtualenv for production. However, it is easier to use Conda for development. Current solution to this is to keep dependencies for both up-to-date (environment.yml for Conda and requirements.txt for virtualenv).


To use Anaconda
1. Install Anaconda, a free distribution of Python.
2. Clone this repository.
3. Execute the following:
  `conda env create -f environment.yml`
  `source activate spoons`


To use virtualenv, run the following commands:
`pip install virtualenv`
`virtualenv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

`deactivate` will exit the virtual environment.

For more information on setting up a virtual environment using Anaconda, see: http://stiglerdiet.com/blog/2015/Nov/24/my-python-environment-workflow-with-conda/

For more information on virtualenv, see:
http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref
