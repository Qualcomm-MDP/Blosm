import bpy
import os
import inspect

# Enable blosm add on
bpy.ops.preferences.addon_enable(module="blosm")

#for op in dir(bpy.ops.blosm):
#    print(op)

# Delete everything in the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Get the horizontal and vertical radius for a region in GPS decimals
hor_radius = 0.00462
vert_radius = 0.001925

# Get a specific coordinate for the region, will also be the central coordinate
cclat = 42.292055 # cclat stands for central latitude
cclon = -83.7147 # cclong stands for cetnral longitude

# Calculate the coords region that we want to have
max_lat = float(cclat) + vert_radius
min_lat = float(cclat) - vert_radius

max_long = float(cclon) + hor_radius
min_long = float(cclon) - hor_radius

coords = (min_long, min_lat, max_long, max_lat)

# Set some context variables that are called by the Blosm operators
bpy.context.scene.blosm.dataType = "osm"
bpy.context.window_manager.clipboard = f"coords={min_long},{min_lat},{max_long},{max_lat}"

# Sets the coordinates
bpy.ops.blosm.paste_extent('INVOKE_DEFAULT')

# Loads in the 3D render model
bpy.ops.blosm.import_data()

# Export it out as a glb file for now, that way if we want we can show it off in a next,js app

# Path to export the GLB file. Designate a place in which you want the model.glb file to export to and put the path in output_path
output_path = "" # TODO fill this out

# Delete the file if it already exists
if os.path.isfile(output_path):
    os.remove(output_path)
    print("File removed.")
else:
    print("File does not exist, nothing to remove.")

# Export everything in the current scene
bpy.ops.export_scene.gltf(
    filepath=output_path,     
    export_format='GLB',      
    export_apply=True,       
)

