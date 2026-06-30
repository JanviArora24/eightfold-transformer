import json
import os


def save_output(data, config):

    final_output = {}

    for key, value in data.items():

        obj = {
            "value": value["value"]
        }

        if config["include_source"]:

            obj["source"] = value["source"]

        if config["include_confidence"]:

            obj["confidence"] = value["confidence"]

        final_output[key] = obj

    os.makedirs("../output", exist_ok=True)

    with open("../output/output.json","w") as file:

        json.dump(final_output,file,indent=4)