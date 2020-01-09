from typing import List

from workers import Inputter
from processDefinitions import Call

calls: List[Call] = Inputter.readAndConvertJSON('data.json')
