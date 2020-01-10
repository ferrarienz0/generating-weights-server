# Native imports
from typing import Dict
from pathlib import Path

# Custom imports
import matplotlib.pyplot as plt

__LOCAL = Path(__file__).parents[1].joinpath('output').joinpath('graphs')


def plotMap(finalMap: Dict[dict, dict]):
    for key in finalMap.keys():
        plt.title(f'Outros comparados a {key}')
        plt.ylabel(f'Peso')
        plt.xlabel(f'Critérios')

        ticks: list = []

        for key_ in finalMap[key]:
            plt.plot(finalMap[key][key_], 'o')
            ticks.append(key_)

        # Graph style
        plt.grid(color='gray', linestyle='-', linewidth=1)
        plt.yticks(range(-9, 10))
        plt.xticks(range(len(finalMap[key])), ticks)

        plt.savefig(__LOCAL.joinpath(f'{key}.png'))
        plt.close()
