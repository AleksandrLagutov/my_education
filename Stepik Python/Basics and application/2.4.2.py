import os
import os.path
path = os.path.join('C:')

print(path)
os.chdir("C:\sample")
print(os.getcwd())
print(os.listdir())
print()
list_dirs = []
for current_dir, dirs, files in os.walk("."):
    #print('This dir',current_dir,'Dirs' , dirs,'Files', files)
    for _ in files:
        if '.py' in _:
            list_dirs.append(current_dir[1:])
            print(current_dir[2:])
            break
print(list_dirs)