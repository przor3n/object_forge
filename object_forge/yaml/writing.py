# encoding: utf-8
import yaml
from object_forge import EXAMPLES_DIR
from object_forge.yaml.reading import load_yaml


def save_yaml(data, filename=None):
    if filename:
        yaml.dump(data, open(filename, 'w'),
                  default_flow_style=False,
                  indent=2)
    else:
        return yaml.dump(data)


if __name__ == "__main__":
    filename = EXAMPLES_DIR / "adv_object.yml"
    outputfile = EXAMPLES_DIR / "basic_object.yml"

    data = load_yaml(filename.as_posix())
    out = save_yaml(data, outputfile.as_posix())
