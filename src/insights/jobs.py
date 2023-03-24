from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as jobs_file:
        data = list(csv.DictReader(jobs_file))
        return data


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    data = read(path)
    jobs = list()
    for job in data:
        if job["job_type"] not in jobs:
            jobs.append(job["job_type"])
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    jobs_list = jobs
    type_str = job_type
    new_job_list = list()
    for job in jobs_list:
        if job["job_type"] == type_str:
            new_job_list.append(job)
    return new_job_list
