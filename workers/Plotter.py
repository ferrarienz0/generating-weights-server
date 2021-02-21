# Native imports
from typing import Dict
from pathlib import Path

# Custom imports
import matplotlib.pyplot as plt

__LOCAL = Path(__file__).parents[1].joinpath('output').joinpath('graphs')

# Plota os gráficos de comparação
# e os salva localmente


def plotMap(finalMap: Dict[str, dict]):
    for key in finalMap.keys():
        plt.figure(figsize=(3 + len(finalMap[key]) * 1.35, 7))
        plt.title(f'Outros comparados a {key}')
        plt.ylabel(f'Peso')
        plt.xlabel(f'Critérios')

        ticks: list = []

        for index, key_ in enumerate(finalMap[key]):
            plt.plot(index, finalMap[key][key_], 'o')
            ticks.append(key_.replace(' ', '\n', 1))

        # Graph style
        plt.grid(color='gray', linestyle='-', linewidth=1)
        plt.yticks(range(-9, 10))
        plt.xticks(range(len(finalMap[key])), ticks)

        plt.savefig(__LOCAL.joinpath(f'{key}.png'))
        plt.close()
