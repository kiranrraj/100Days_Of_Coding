# Title  : Simplify Path
# Author : Kiran raj R.
# Date   : 20/07/2025

# Given a string path, which is an absolute path (starting with a '/'), simplify it to the canonical path.
# In a Unix-style file system:
# - A period '.' refers to the current directory.
# - A double period '..' refers to the directory up a level.
# - Any multiple slashes '//' are treated as a single slash '/'.

# The canonical path should have the following format:
# - The path starts with a single slash '/'.
# - Any two directories are separated by a single slash '/'.
# - The path does not end with a trailing '/'.
# - The path only contains the directories on the path from the root directory to
#   the target directory (i.e., no '.' or '..').

def simplify_path(path: str) -> str:
    # Use a list as a stack to keep track of directory names.
    stack = []
    
    # Split the path by slashes. This will handle multiple slashes automatically and also give us the directory names.
    components = path.split('/')

    # Iterate over each component in the path.
    for component in components:
        # If the component is '..', we need to go up one level.
        # This is simulated by popping from the stack if it's not empty.
        if component == '..':
            if stack:
                stack.pop()
        # If the component is not empty and not '.', it's a valid directory name.
        # We push it onto the stack.
        elif component and component != '.':
            stack.append(component)
            
    # After processing all components, join the stack elements with slashes
    # and prepend a slash for the root to form the canonical path.
    # The result is "/" if the stack is empty.
    return "/" + "/".join(stack)


path1 = "/home/"
print(f"Original Path: {path1}")
print(f"Simplified Path: {simplify_path(path1)}") 

path2 = "/../"
print(f"\nOriginal Path: {path2}")
print(f"Simplified Path: {simplify_path(path2)}")

path3 = "/home//foo/"
print(f"\nOriginal Path: {path3}")
print(f"Simplified Path: {simplify_path(path3)}") 

path4 = "/a/./b/../../c/"
print(f"\nOriginal Path: {path4}")
print(f"Simplified Path: {simplify_path(path4)}")
