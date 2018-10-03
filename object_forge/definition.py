# encoding: utf-8
import importlib
import logging

from os import path

from object_forge.references import ReferenceExpression


class Definition(object):
    """
    Definition of object class.
    It is used for creating an object from it's definition.
    """
    REFERENCE_PREFIX="@"

    def __init__(self, klass, arguments, calls):
        self.expr_parser = ReferenceExpression()
        self.klass = klass
        self.arguments = arguments
        self.calls = calls
        self.environment = dict()
        self.args = None
        self.compiled = None

    def parse_variables(self):
        """
        Parse arguments given in config.
        It substitutes refreneces for theire values.
        :return:
        """
        logging.info("Parsing variables")
        if isinstance(self.arguments, list):
            self.args = self.expand_references(self.arguments)


        if isinstance(self.arguments, dict):
            values = self.expand_references(list(self.arguments.values()))
            self.args = dict(zip(self.arguments.keys(), values))

    def expand_references(self, values):
        """
        Substitute objects for references in arguments
        :param values: list of arguments with references
        :return: list of arguments
        """
        self.expr_parser = ReferenceExpression() # TODO: why __init__ doesn't do it?
        logging.info("Expanding references")
        for i, value in enumerate(values):
            value_is_reference = isinstance(value, str) \
                                 and value.startswith(Definition.REFERENCE_PREFIX)

            if value_is_reference:
                values[i] = self.expr_parser.eval(value, self.environment)

        return values

    def create_object(self):
        """
        Divide class path on module name and class.
        Import module, get class and create a new object
        from it with given arguments
        :return:
        """
        logging.info("Creating object")
        # use this later:
        # https://docs.python.org/3/library/functions.html#__import__
        try:
            module_path, _, class_name = self.klass.rpartition('.')
            imported_module = importlib.import_module(module_path)

            klass = getattr(imported_module, class_name)
            if isinstance(self.args, list):
                self.compiled = klass(*self.args)

            if isinstance(self.args, dict):
                self.compiled = klass(**self.args)

        except ImportError as error:
            logging.error("Import error")
            logging.error(error)
        except Exception as exception:
            logging.error("Import exception")
            logging.error(exception)

    def compile(self, environment):
        """
        Parse variables and create an object and return it
        :param environment: dict with loaded objects to reference
        :return: created object
        """
        logging.info("Compiling definition")
        self.environment = environment
        self.parse_variables()
        self.create_object()
        return self.compiled

    @staticmethod
    def is_instance(x):
        """
        check if object is instance of Definition
        :param x: any
        :return: boolean
        """
        return isinstance(x, Definition)
