import time
from datetime import datetime, timezone
from pathlib import Path
import copy
from scripts.helper_functions import (
    initialise_notebook,
    type_to_terminal,
    create_parent_name,
    prompts,
)


def main():

    type_to_terminal(prompts["introduction"])
    experimentalist_name = input()
    time.sleep(0.7)
    first_name = experimentalist_name.split()[0]
    type_to_terminal(f"Hello {first_name}.")
    time.sleep(0.6)
    type_to_terminal(f"This is Brandon. Welcome to The Matrix")
    time.sleep(0.6)
    type_to_terminal("Let's start an experiment.")
    type_to_terminal("...")

    fridge_name = input(prompts["fridge_prompt"])
    device_name = input(prompts["device_prompt"])
    experiment_name = input(prompts["experiment_prompt"])

    now = datetime.now(timezone.utc)
    date_today = now.strftime("%Y%m%d_%H%M%S")

    parent_name = create_parent_name(
        date_today, fridge_name, device_name, experiment_name
    )
    notebook_name = copy.deepcopy(parent_name)

    print("Creating directories...")
    Path("./" + parent_name + "/data").mkdir(parents=True)
    Path("./" + parent_name + "/scripts").mkdir(parents=True)
    initialise_notebook(notebook_name, parent_name)

    print(f"Experiment directory made at: {parent_name}")


if __name__ == "__main__":
    main()
