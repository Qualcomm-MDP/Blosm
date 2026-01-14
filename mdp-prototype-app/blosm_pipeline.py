#!/usr/bin/env python3

import bpy
import os
import inspect
import subprocess
import shutil
from pathlib import Path

def run_pipeline(scene):
    
    # Enable blosm add on
    bpy.ops.preferences.addon_enable(module="blosm")

    #for op in dir(bpy.ops.blosm):
    #    print(op)

    current_file = Path(__file__)
    print(current_file)

    # Parent directory of the script
    cwd = current_file.parent.parent
    print(cwd)
    
    # Delete everything in the scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    

    # Get the horizontal and vertical radius for a region
    hor_radius = 0.00462
    vert_radius = 0.001925
    
    coords_path = cwd / "coords.txt"
    
    coords = []
    with open(coords_path, "r") as f:
        for line in f:
            coords.append(line.strip())

    # Get the central coordinate that the region revolves around
    cclat =  float(coords[0]) # input("Enter central coordinate lat: ")
    cclon =  float(coords[1]) # input("Enter central coordinate long: ")

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

    # Path to export the GLB file
    output_path = cwd / "public/model.glb"
    model_path = cwd / "src/app/components/three/Model.jsx"
    model_dir = cwd / "src/app/components/three/"
    
    print(model_dir)
    print(output_path)
    print(model_path)
    
    # Delete the file if it already exists
    if os.path.isfile(model_path):
        os.remove(model_path)
        print("File removed.")
    else:
        print("File does not exist, nothing to remove.")

    # Export everything in the current scene
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),     
        export_format='GLB',      
        export_apply=True,       
    )
    
    subprocess.run(["npx", "gltfjsx@6.5.3", f"{str(output_path)}", "-o", f"{str(model_path)}"],
        capture_output=True,
        text=True,
        check=True
    )
    
    print("Created the component!")
    
bpy.app.handlers.load_post.append(run_pipeline)