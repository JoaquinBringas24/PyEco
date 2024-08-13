import json
import pathlib
from flask import jsonify, redirect, render_template, request, url_for
from flask.blueprints import Blueprint
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import ColumnDataSource

CUR_PATH = pathlib.Path(__file__).resolve().parent.parent

with open("config.json") as config_file:
    config = json.load(config_file)
    config_file.close()

regression_blueprint = Blueprint("regression", __name__)

@regression_blueprint.post("/api/regression/upload")
def uploadData():
    file = request.files['data']
    
    if config["CACHE"]:
        file.save(f"{CUR_PATH}/cache/datasets/{file.filename}")
        data = pd.read_csv(f"{CUR_PATH}/cache/datasets/{file.filename}")

    else:

        file.save(f"{CUR_PATH}/cache/datasets/data.csv")

        data = pd.read_csv(f"{CUR_PATH}/cache/datasets/data.csv")

    return render_template("regression.html", data=data.to_html(classes="display", table_id="myTable"),
                           variables=list(data.columns))


@regression_blueprint.post("/api/regression/compute")
def computeRegression():

    x = request.form["dependent"]
    y = request.form["independent"]

    data = pd.read_csv(f"{CUR_PATH}/cache/datasets/data.csv")

    print(request.files)

    results = smf.ols(f"{y} ~ {x}", data=data).fit()

    coeffs = list(results.params)

    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,examine,help"

    p = figure(tools=TOOLS)

    source = ColumnDataSource(data)

    p.scatter(x=x, y=y, size=5, source=source)
    
    y_regress = [coeffs[0] + coeffs[1] * i for i in data[x]]

    p.line(x=data[x], y=y_regress, color="red", legend_label="Regression", name="regression", line_width=2)

    print(CUR_PATH)

    return render_template("regression.html",
                            data=coeffs,
                            graph=file_html(p, CDN, title=y),
                            variables=list(data.columns))