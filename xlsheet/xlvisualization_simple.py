import bpy  # this module is blender specific
import openpyxl  # importing openpyxl -- can be installed via pip

# loading the workbook
wb = openpyxl.load_workbook(filename = r"E:\BigProjects\Blender\XL\data.xlsx")
sheet = wb["Sheet1"]

# makeTitle function
def makeTitle(title, mesh, size):
    """
    This function creates a Title block on every cube object
    """
    txt = title.value
    x = mesh[i].location.x
    y = mesh[i].location.y
    z = mesh[i].location.z
    bpy.ops.object.text_add(radius=.7*size, rotation=(1.5708,0,1.5708),location=(x,y-size,z+size))
    ob=bpy.context.object
    ob.data.body = txt


mesh=[]  # initializing a list to store mesh data
name_ext = ""  # initializing a string to store mesh name extension. eg:- cube.001 -- .001 is the extension
ext=0  # increment value in name extension
gap=0  # intializing gap value. increment value inside for loop
i=0  # initializing i to access mesh data


for row in range(1,sheet.max_row+1):
    cell = sheet.cell(row,2)
    title = sheet.cell(row,1)
    bpy.ops.mesh.primitive_cube_add(size=int(cell.value), location=(0,gap,0))
    mesh.append(bpy.data.objects["Cube"+name_ext])
    makeTitle(title, mesh, cell.value)
    i+=1  # incrementing i for next mesh data
    gap+=100  # set the gap value between cube here
    ext+=1
    name_ext = f".00{ext}"
    print(ext)

