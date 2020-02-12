import os
#Gets the current directory
cwd = os.getcwd()
for i in os.listdir(cwd):
    if('vgcore.' in i ):
        os.system('rm '+i)
