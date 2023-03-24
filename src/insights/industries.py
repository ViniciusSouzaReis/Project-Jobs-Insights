from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    all_industries = set()
    for industries in data:
        if industries["industry"]:
            all_industries.add(industries["industry"])
    return all_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_list = jobs
    industry_type = industry
    industries_list = list()
    for industries in jobs_list:
        if industries["industry"] == industry_type:
            industries_list.append(industries)
    return industries_list
