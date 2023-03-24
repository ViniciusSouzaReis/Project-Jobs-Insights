from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as jobs_file:
        data = list(csv.DictReader(jobs_file))
        return data


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    jobs = list()
    for job in data:
        if job["job_type"] not in jobs:
            jobs.append(job["job_type"])
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_list = jobs
    type_str = job_type
    new_job_list = list()
    for job in jobs_list:
        if job["job_type"] == type_str:
            new_job_list.append(job)
    return new_job_list
