import bpy  # this module is blender specific
import openpyxl

def makeTitle(title, mesh, size):
    txt = title.value
    x = mesh[i].location.x
    y = mesh[i].location.y
    z = mesh[i].location.z
    bpy.ops.object.text_add(radius=.7*size, rotation=(1.5708,0,1.5708),location=(x,y-size,z+size))
    ob=bpy.context.object
    ob.data.body = txt


horizontal = []
vertical = []

wb = openpyxl.load_workbook(filename = r"E:\BigProjects\Blender\XL\data.xlsx")
sheet = wb["Sheet1"]

ext = ""
a=0
b=0
i=0
mesh=[]
for row in range(1,sheet.max_row+1):
    cell = sheet.cell(row,2)
    title = sheet.cell(row,1)
    bpy.ops.mesh.primitive_cube_add(size=int(cell.value), location=(0,b,0))
    mesh.append(bpy.data.objects["Cube"+ext])
    makeTitle(title, mesh, cell.value)
    i+=1
    b+=100
    a+=1
    ext = f".00{a}"
    print(ext)

