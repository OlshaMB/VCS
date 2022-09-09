from argparse import ArgumentParser
import os,platform,shutil,glob
from typing import Dict, Literal
def copyGlob(src:Literal,dst):
    for file in glob.glob(src):
        print(file,dst)
        if os.path.isfile(file):
            shutil.copy(file, dst)
        else:
            shutil.copytree(file, dst, dirs_exist_ok=True)
def copy(copyStructure:Dict[str,str],prefix="./dist/"):
    for currentPath in copyStructure.keys():
        if "*" in currentPath:
            copyGlob(currentPath, os.path.join(prefix,copyStructure[currentPath]))
            continue
        if os.path.isfile(currentPath):
            shutil.copy(currentPath, os.path.join(prefix,copyStructure[currentPath]))
        else:
            shutil.copytree(currentPath, os.path.join(prefix,copyStructure[currentPath]),dirs_exist_ok=True)
def createDirIfNotExists(path:str):
    if not os.path.exists(path):
        os.mkdir(path)
bundleDirs=[]
parser = ArgumentParser()
'''parser.add_argument("-m","--mode", choices=["min", "dev", "all"], default="all")
parser.add_argument("-t","--target", choices=["macos-raw", "linux-raw", "windown-default"]) # TODO: add macos-brew, linux-ubuntu, linux-debian'''
parser.add_argument("-o", "--output", default="dist")
args = parser.parse_args()
bundleDirs.append(os.path.join(".",args.output))
for dirName in bundleDirs:
    createDirIfNotExists(dirName)
    copy({
        "./requirements.txt":"requirements.txt",
        "./pyproject.toml":"pyproject.toml",
        "./LICENSE":"LICENSE",
        "./docs":"docs",
        r"./src/": ""
    },dirName)