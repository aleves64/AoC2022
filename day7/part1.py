import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

def newdir():
    empty_dir = {
        "parent": None,
        "directories": {},
        "files": {},
        "size": 0
    }
    return empty_dir

current_dir = newdir()
root = current_dir
i = 0
while i < len(myinput):
    command = myinput[i]
    command = command.split(" ")
    if command[1] == "cd":
        dirname = command[2]
        if dirname == "..":
            current_dir = current_dir["parent"]
        else:
            if not dirname in current_dir["directories"]:
                new_dir = newdir()
                new_dir["parent"] = current_dir
                current_dir["directories"][dirname] = new_dir 
            current_dir = new_dir
    elif command[1] == "ls":
        while i+1 < len(myinput) and myinput[i+1][0] != '$':
            fileinfo = myinput[i+1].split(" ")
            entry_type = fileinfo[0]
            if entry_type != "dir":
                size = int(fileinfo[0])
                filename = fileinfo[1]
                current_dir["files"][filename] = size
            i += 1
    i += 1

def explore_dirs(directory):
    total = 0
    for subdir in directory["directories"]:
        total += explore_dirs(directory["directories"][subdir])
    for file in directory["files"]:
        total += directory["files"][file]
    directory["size"] = total
    return total

total = 0
def collect_total(directory):
    global total
    if directory["size"] <= 100000:
        total += directory["size"]
    for subdir in directory["directories"]:
        collect_total(directory["directories"][subdir])

explore_dirs(root)
collect_total(root)
print(total)