import os
import shutil
import sys
from argparse import ArgumentParser, SUPPRESS
parser = ArgumentParser()
args = parser.add_argument_group('Options')
args.add_argument("-p", "--python_ver",
                      help="input python ver", type=str, default=None)
                      
arg = parser.parse_args()
py=arg.python_ver 

if os.path.exists("src"):
    shutil.rmtree("src")

src_dir = "linux_src_python%s" % (py)
shutil.copytree(src_dir, "src")
