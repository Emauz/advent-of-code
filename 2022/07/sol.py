#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"

BYTES_AVAILABLE = 70000000
BYTES_REQUIRED = 30000000

class Inode():
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent

        # locals
        self.size = size
        if(self.parent is not None):
            self.parent.add_size(size)
        self.files = {} # name -> inode mapping
        self.dirs = {} # name -> inode mapping
        self.dirs['..'] = parent

    def __repr__(self):
        ret = ''
        ret += f"Inode: {self.name}\n"
        ret += f"size: {self.size}\n"
        ret += f"files:\n"
        for name in self.files.keys():
            ret += f"\t{name}\n"
        ret += f"dirs:\n"
        for name in self.dirs.keys():
            ret += f"\t{name}\n"
        return ret

    # adds bytes to this inode's reported size on disk, propagates to parents
    def add_size(self, size):
        self.size += size
        if(self.parent is not None):
            self.parent.add_size(size)


with open(filename) as f:
    input_lines = f.readlines()

def construct_tree(cwd):
    while(len(input_lines) > 0):
        # grab next available command
        cmd = input_lines.pop(0)
        cmd = cmd.split()
        if(cmd[0] == '$'):
            # we're dealing with a command
            if(cmd[1] == 'cd'):
                target_inode = cwd.dirs[cmd[2]]
                construct_tree(target_inode)
            elif(cmd[1] == 'ls'):
                continue
        elif(cmd[0] == 'dir'):
            name = cmd[1]
            node = Inode(name, cwd)
            cwd.dirs[name] = node
        else:
            # this is a file command
            size = int(cmd[0])
            name = cmd[1]
            node = Inode(name, cwd, size)
            cwd.files[name] = node

def part1(tree):
    sum = 0
    if(tree.size <= 100000):
        sum += tree.size
    for subdir in tree.dirs.keys():
        if(subdir != '..'): # avoid looping
            sum += part1(tree.dirs[subdir])
    return sum

def part2(tree):
    global best_node_for_deletion
    global bytes_to_delete
    if(tree.size < best_node_for_deletion.size and tree.size > bytes_to_delete):
        best_node_for_deletion = tree
    for subdir in tree.dirs.keys():
        if(subdir != '..'): # avoid looping
            part2(tree.dirs[subdir])
    return best_node_for_deletion.size

def main():
    # create filesystem root
    root = Inode('/', None)
    input_lines.pop(0)

    construct_tree(root)

    print(part1(root))

    global best_node_for_deletion
    global bytes_to_delete
    bytes_to_delete = (root.size - (BYTES_AVAILABLE - BYTES_REQUIRED))
    best_node_for_deletion = root
    print(part2(root))

if __name__ == '__main__':
    main()
