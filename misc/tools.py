import os

def mkdir_r(dirname):
    try:
        os.mkdir(dirname)
    except:
        path1, dir1 = os.path.split(dirname)
        mkdir_r(path1)
        mkdir_r(dirname)

    

    
    
