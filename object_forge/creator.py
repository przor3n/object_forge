# encoding: utf-8
import copy
import logging

from object_forge.definition import Definition


class Creator(object):
    ENVIRONMENT = "environment"

    def __init__(self):
        logging.info("Creator initialized")
        self.environment = dict()
        self.yamlobjects = dict()
        self.definitions = dict()

    def parse_yamlobject(self, object):
        logging.info("Parsing yaml objects")
        self.yamlobjects = object.get(Creator.ENVIRONMENT)
        self.compile_definitions()
        self.substitute_objects()
        return self.environment

    def compile_definitions(self):
        logging.info("Compiling definitions...")
        temp_env = copy.deepcopy(self.yamlobjects)

        defintions = {key: obj for key, obj in self.yamlobjects.items() if Definition.is_instance(obj)} # if Definition.is_instance(obj)

        try:
            for key, definition in defintions.items():

                build_object = definition.compile(temp_env)
                temp_env[key] = build_object

        except Exception as exp:
            logging.error("Compiling object definition failed")
            logging.error(exp)

        self.definitions = temp_env
        logging.info("Definitions compiled")

    def substitute_objects(self):
        logging.info("Substituting objects with environment")
        self.environment = copy.deepcopy(self.definitions)
