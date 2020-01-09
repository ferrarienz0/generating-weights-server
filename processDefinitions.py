from typing import List


class Call:
    def __init__(self, data: dict):
        self.name: str = data['name']
        self.criteria: List[Criteria] = [Criteria(x) for x in data['criteria']]
        self.sucess: float = data['sucess']


class Criteria:
    def __init__(self, data: dict):
        self.name: str = data['name']
        self.score: float = data['score']
