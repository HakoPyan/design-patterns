# Main idea: allows an object to alter its behavior when its internal state changes (finite-state machine)
from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    YELLOW = 'Yellow'


class TrafficLightState(ABC):
    @abstractmethod
    def next(self, light):
        pass

    @abstractmethod
    def get_color(self):
        pass


class YellowState(TrafficLightState):
    def next(self, light):
        light.current_state = RedState()

    def get_color(self):
        return Color.YELLOW


class GreenState(TrafficLightState):
    def next(self, light):
        light.current_state = YellowState()

    def get_color(self):
        return Color.GREEN


class RedState(TrafficLightState):
    def next(self, light):
        light.current_state = GreenState()

    def get_color(self):
        return Color.RED


class TrafficLight:
    current_state = GreenState()

    def next(self):
        self.current_state.next(self)

    def get_color(self):
        return self.current_state.get_color()
