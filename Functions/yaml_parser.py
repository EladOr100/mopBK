import yaml


def yaml_data_parser(yaml_path, data):
    with open(yaml_path, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        return cfg[data]

