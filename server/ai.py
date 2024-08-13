from flask import render_template
import torch
from flask.blueprints import Blueprint
from flask import request
import pathlib
import json
import pandas as pd

CUR_PATH = pathlib.Path(__file__).resolve().parent.parent

with open("config.json") as config_file:
    config = json.load(config_file)
    config_file.close()



ai_blueprint = Blueprint("ai", __name__)

@ai_blueprint.get('/ai')
def IA():
    return render_template("ia.html")

@ai_blueprint.post("/api/ai/upload")
def uploadData():
    file = request.files['data']
    
    if config["CACHE"]:
        file.save(f"{CUR_PATH}/cache/datasets/{file.filename}")
        data = pd.read_csv(f"{CUR_PATH}/cache/datasets/{file.filename}")

    else:

        file.save(f"{CUR_PATH}/cache/datasets/data.csv")

        data = pd.read_csv(f"{CUR_PATH}/cache/datasets/data.csv")

    return render_template("ia.html", data=data.to_html(classes="display", table_id="myTable"),
                           variables=list(data.columns))

