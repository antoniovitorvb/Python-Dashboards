import os

os.getcwd() # get's work directory (WD)

os.listdir() # print list of files of WD

os.listdir('c:\\Users\\vitor\\Desktop\\Asimov') # print list of files from specified directory

actual_dir = os.getcwd()
os.chdir('c:\\Users\\vitor\\Desktop\\Asimov')
os.getcwd()
os.chdir(actual_dir)

os.mkdir('mkdir_test')

os.rename('teste.txt', 'teste2.txt')
os.rename('mkdir_test', 'mkdor_test2')

os.remove('test.csv')
os.rmdir('mkdir_test')

cmd = 'date'
os.system(cmd)

os.path.join(os.getcwd(), 'pasta')
# OU
os.getcwd() + '\\pasta'

os.path.basename(os.getcwd())
# OU
os.getcwd().split('\\')[-1]

lt = os.path.getmtime(actual_dir)
from datetime import datetime as dt
dt.utcfromtimestamp(lt)

os.path.isfile(actual_dir)
os.path.isdir(actual_dir)