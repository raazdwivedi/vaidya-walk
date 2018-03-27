#!/usr/bin/env/python

import os

# os.system('rm pyWrapper/example.py')
# os.system('rm pyWrapper/_*.*')
built = not os.system('python setup.py build')
if built:
    os.system('mv build/*/_*.* pyWrapper/')
    os.system('mv pwalk.py pyWrapper/')
    os.system('cd pyWrapper && python test_pwalk.py')
else:
	print("-------------------------------")
	print("Failed to build extension! Exiting.")
	print("-------------------------------")
