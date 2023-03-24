from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    higher_salary = []
    for salary in data:
        if salary["max_salary"].isnumeric():
            higher_salary.append(int(salary["max_salary"]))
    return max(higher_salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    lower_salary = []
    for salary in data:
        if salary["min_salary"].isnumeric():
            lower_salary.append(int(salary["min_salary"]))
    return min(lower_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    min = "min_salary"
    max = "max_salary"
    if min not in job or max not in job:
        raise ValueError
    if not str(job[min]).isdigit() or not str(job[max]).isdigit():
        raise ValueError
    if int(job[min]) > int(job[max]):
        raise ValueError
    if not str(salary).lstrip("-").isdigit():
        raise ValueError
    return int(job[min]) <= int(salary) <= int(job[max])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    salary_list = list()
    for salary_range in jobs:
        try:
            if matches_salary_range(salary_range, salary):
                salary_list.append(salary_range)
        except ValueError:
            print("Erro!")
    return salary_list
