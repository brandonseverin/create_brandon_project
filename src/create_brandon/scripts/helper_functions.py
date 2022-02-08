import os
import sys
from random import gauss
import time
from pathlib import PurePath
import nbformat as nbf

prompts = {
    "introduction": "Hello, who am I talking to?",
    "fridge_prompt": "Name of the fridge: ",
    "device_prompt": "Name of the device: ",
    "experiment_prompt": "Name of the experiment: ",
}

# TODO(@Brandon): Add docstrings to all functions

# Typing speed in words per minute
# 1 word per minute --> 5 characters/min
def wpm_to_cps(typing_speed):
    assert isinstance(
        typing_speed, (int, float)
    ), f"typing_speed is neither int nor float, it is {type(typing_speed)}"
    cps = typing_speed * 5 / 60
    return cps


def type_to_terminal(output, typing_speed=70, deviation=5):
    output = str(output)
    for character in output:
        wpm = gauss(typing_speed, deviation)
        cps = wpm_to_cps(wpm)
        print(character, end="", flush=True)
        time.sleep(1 / cps)

    print("")


def create_parent_name(
    date_today, fridge_name=None, device_name=None, experiment_name=None
):
    parent_name = (
        (date_today + "_" + fridge_name + "_" + device_name + "_" + experiment_name)
        .lower()
        .replace(" ", "_")
    )

    return parent_name


def initialise_notebook(notebook_name=None, directory=None, content=None):
    if notebook_name == None:
        notebook_name = "Untitled"

    nb = nbf.v4.new_notebook()
    text = content if content != None else "# Untitled "

    code = ""

    nb["cells"] = [nbf.v4.new_markdown_cell(text), nbf.v4.new_code_cell(code)]

    file_path = PurePath(directory).joinpath(notebook_name + ".ipynb")
    with open(file_path, "w") as f:
        nbf.write(nb, f)

