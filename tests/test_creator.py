# encoding: utf-8
from animals import Vet
from object_forge import EXAMPLES_DIR
from object_forge import Creator
from object_forge.yaml import load_yaml


class TestCreator(object):
    def create_environment(self, file):
        parameters = EXAMPLES_DIR / file
        yamlobject = load_yaml(parameters.as_posix())

        creator = Creator()
        return creator.parse_yamlobject(yamlobject)

    def test_creator_basic_load(self):
        environment = self.create_environment("params.yml")

        kot = environment.get('kot')
        assert kot == "miau"

        ryba = environment.get('ryba')
        assert ryba == "blop"

        krowa = environment.get('krowa')
        assert krowa == "muuuu"

    def test_creator_basic_objects(self):
        environment = self.create_environment("basic_object.yml")

        answer = "Hi, I'm John. I'm 67 old"

        vet = environment.get('vet')
        assert isinstance(vet, Vet)
        assert vet.speak() == answer

    

    def test_creator_adv_objects(self):
        environment = self.create_environment("adv_object.yml")

        answer = "Hi, I'm Mark. I'm 67 old"

        vet_help = environment.get('vet_help')
        assert isinstance(vet_help, Vet)

        kot = environment.get('animals_kot')
        assert kot.speak() == "miau"

    def test_creator_cmplx_objects(self):
        environment = self.create_environment("cmplx_object.yml")

        farm = environment.get('farm')
        animals = ['krowa', 'ryba', 'kot']

        assert isinstance(farm, dict)
        assert len(farm) == 3

        for animal in animals:
            assert farm[animal].speak() == environment.get(animal)
       
    def test_reference_fold(self):
        environment = self.create_environment("reference_and_function.yml")

        farm = environment.get('farm')

        assert farm.get('john') == "Hi, I'm John. I'm 67 old"
