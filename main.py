import requests

from const_data import url, professions, cities, experience_levels
from diagram import draw_diagram


def parametrs(citi: str, profession: str, ex_lvl: str) -> dict:
    return {
        'text': professions[profession],
        'area': cities[citi],  
        'experience': experience_levels[ex_lvl],
        'per_page': 0,
    }


def result_request_choice(parametr: dict) -> str:
    '''Получение количество вакансий'''
    response = requests.get(
        url = url,
        params= parametr,
    )
    return response.json()['found']



def main_dict() -> dict:
    result = {citi:{prof:list() for prof in professions} for citi in cities}
    for citi_name in cities:
        for prof in professions:
            for lvl in experience_levels:
                result[citi_name][prof].append(result_request_choice(parametrs(citi_name, prof, lvl)))
    return result



if __name__ == "__main__":
    res_dict = main_dict()
    print(res_dict)
    draw_diagram(res_dict)


