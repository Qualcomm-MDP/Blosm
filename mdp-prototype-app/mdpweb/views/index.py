import pathlib
import flask
import mdpweb
import subprocess
import os

print("mdpweb.views imported")

@mdpweb.app.route('/')
def show_index():
    context = {}
    return flask.render_template("index.html", **context)

@mdpweb.app.route('/render/', methods=['POST'])
def render_model():
    target = flask.request.args.get("target", "/")
    latitude = float(flask.request.form.get("lat", "").strip())
    longitdue = float(flask.request.form.get("lon", "").strip())

    # Path to export the GLB file
    output_path = "./coords.txt"

    with open(output_path, "w") as f: # Clear the output before writing into it again
        pass

    with open(output_path, "a") as f:
        f.write(f"{latitude}\n")
        f.write(f"{longitdue}")

    print("Command to run 3D model is received!")
    subprocess.run(["./bin/render3d", f"{latitude}", f"{longitdue}"],
        capture_output=True,
        text=True,
        check=True
    )

    # return flask.redirect(target)
    return flask.redirect(flask.url_for("show_index"))
