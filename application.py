#!/usr/bin/env python
from application import application

# Elastic Beanstalk initialization
# application.secret_key = 'cC1YCIWOj9GgWspgNEo2'

if __name__ == '__main__':
    application.run(debug=True)
