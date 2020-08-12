def create_mesh(mesh_name):
    return bpy.data.meshes.new(name=mesh_name)
    
def create_object(object_name, mesh):
    return bpy.data.objects.new(object_name, mesh)
    
# mesh data
# line:
#     point_a = (x, y)
#     point_b = (x, y)
# circle requires 

def create_line_object(object_name, point_a, point_b):
    verts = [point_a, point_b]
    edges = [verts[0], verts[1]]
    line_mesh = create_mesh(object_name)
    line_mesh.from_pydata(verts, edges)
    line_object = create_object(object_name, line_mesh)
