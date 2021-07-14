from typing import List, Tuple, Any, Dict, Optional, cast
import os
import sys
from ruamel.yaml import YAML

import frigate.gen

import pprint

if __name__ == "__main__":
    chartdir = "manifests/redis/"
    yaml = YAML()
    with open(os.path.join(chartdir, "values.yaml"), "r") as fh:
        values = yaml.load(fh.read())

    # TODO: picking up comments not working; when working
    # second element of tuple should sometimes be a non empty string
    raw_var_list: List[Tuple[str, Optional[str], Any]] = cast(
        List[Tuple[str, Optional[str], Any]],
        list(frigate.gen.traverse(values, defaults_as_json=False)),
    )

    # raw_var_list is all that is needed for helm parser. below is just for stubbing
    var_list_for_yaml: List[Dict[str, Any]] = [
        {"name": el[0], "value": el[2]} for el in raw_var_list
    ]

    yaml.dump(var_list_for_yaml, sys.stdout)
