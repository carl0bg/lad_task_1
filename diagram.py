import matplotlib.pyplot as plt
import numpy as np

from const_data import colors, experience_levels


def plot_city_data(city, professions, ax):
    '''Построение отдельного города'''
    bar_width = 0.2  # ширина столбца
    index = np.arange(len(professions))  # позиции для профессий

    for i, (level, color) in enumerate(zip(experience_levels, colors)):
        values = [professions[prof][i] for prof in professions]
        bars = ax.bar(index + i * bar_width, values, bar_width, label=level, color=color)
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom')

    ax.set_title(city)
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(professions.keys(), rotation=45, ha="right")
    ax.set_ylabel('Количество вакансий')
    ax.legend()


def draw_diagram(data: dict):
    '''Формирует диаграммы получившихся данных'''
    fig, axes = plt.subplots(1, 3, figsize=(15, 6), sharey=True)

    for i, (city, professions) in enumerate(data.items()):
        plot_city_data(city, professions, axes[i])

    plt.tight_layout()
    plt.show()
