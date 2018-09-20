import os

proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
print("proj path: {}".format(proj_path))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("base dir: {}".format(BASE_DIR))
