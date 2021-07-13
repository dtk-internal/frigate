import os
from ruamel.yaml import YAML

import frigate.gen

import pprint

if __name__ == "__main__":
    chartdir = "manifests/redis/"
    yaml = YAML()
    with open(os.path.join(chartdir, "values.yaml"), "r") as fh:
        values = yaml.load(fh.read())
    
    # TODO: picking up comments not working 
    var_list = list(frigate.gen.traverse(values, defaults_as_json=False))
    # TODO: simple render as yaml 
    pprint.pprint(var_list)
