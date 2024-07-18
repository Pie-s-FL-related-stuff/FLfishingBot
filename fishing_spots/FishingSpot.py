from abc import abstractmethod


class FishingSpot:
    @staticmethod
    @abstractmethod
    def refresh():
        pass

    @staticmethod
    @abstractmethod
    def reposition():
        pass

    @staticmethod
    @abstractmethod
    def reset():
        pass
