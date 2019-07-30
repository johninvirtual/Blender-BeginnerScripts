"""
    I am learning to use python scripting in blender
    and these codes are beginner stuffs
    
    The below code will create a array of cubes
    based on user input
    
    This creates separate cube objects
    not a single object with many cubes,
    so make sure that you have more memory to
    play with high numbers
    
    The user input should be given in the system console
    To open console go to window > toggle system console
"""


import bpy  # only works in blender

size = int(input("size of cube: "))  # get the size of cube
row = int(input("rows (x): "))  # get the number of rows
colomn = int(input("colomns (y): "))  # get the number of colomns
height = int(input("stacks (z): "))  # get the number of stack

row_gap = int(input("row gap : "))  # get the row gap
colomn_gap = int(input("colomn gap: "))  # get the colomn gap
height_gap = int(input("stack gap: "))  # get the stack gap

x = 0
y = 0
z = 0

for _ in range(row):
    for _ in range(colomn):
        for _ in range(height):
            bpy.ops.mesh.primitive_cube_add(size=size, location=(x, y, z))
            z += size + height_gap
        z=0
        y+= size + colomn_gap
    z=0
    y=0
    x+= size + row_gap
    
