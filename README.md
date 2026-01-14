# Blosm Pipeline

This is the first initial draft of the blosm pipeline that I was working on. To use it, you will first need to install Blender (5.0 is the latest and will work with this):

https://www.blender.org/

Go to their website, and click the download. Follow the instructions to download Blender onto your machine.

Once Blender is installed, download the Blosm extension. Here is a good YouTube tutorial to get started:

[https://www.youtube.com/watch?v=ym9HtWzTc9o](url)

Blosm Github: [https://github.com/vvoovv/blosm?tab=readme-ov-file](url)

Don't worry about the Google API Keys and stuff like that for now, that stuff deals with texturing.

The script will render out the 3D mesh of the city in Blender and will also export out a .glb file of the 3D mehs named model.glb. Designate a directory where you will want it to output to
and append model.glb to the end of the directory. Paste that path into the TODO field named output_path. 

Note that there are still issues when rendering regions far away, like New York City as they generate extremely far away in the Blender environment.

To ensure that the script works properly, make sure to run the python script within the Blender environment. Running it in a regular text editor like VSCode will not work as the Python S
script requires some Blender specfic modules, so make sure that you open up Blender and then run the Python script within the Text Editor. Here is a quick YouTube tutorial to set it up:

[https://www.youtube.com/watch?v=cyt0O7saU4Q](url)

Once you have it setup, you can just click the play button to run the script and the mesh should render out. Sometimes there are 504 Gateway Timeout errors that arise, and is more of 
an issue with the data source. If this happens, just wait for a little bit before trying to run the script again.

Here are some basic latitude longitude coordinates that work fine and are representative of North Campus: 
- 42.292055 -83.7147
- 42.288915 -83.71501
To get your own latitude longitude, you can go on google maps and right click on a location to get its latitude longitude coorindates.

