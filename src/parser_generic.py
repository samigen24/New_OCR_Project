import abc
# from abc import ABC, abstractmethod
# module for abstract class


class Registration():
    def __init__(self, text):
        self.text = text

    @abc.abstractmethod
    def parse(self):
        pass
