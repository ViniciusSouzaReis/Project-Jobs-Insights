from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
