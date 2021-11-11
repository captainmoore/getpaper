import sys
import os

currentdir = os.path.dirname(sys.argv[0])
libdir = os.path.join(currentdir, "lib")
sys.path.append(libdir)
os.environ['path'] += ';./lib'