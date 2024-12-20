# conftest.py
import pytest
import importlib


@pytest.fixture
def solutions():
    """Dynamically import and return the solution class."""
    problem_name = pytest.problem_name  # This will be set in the test file
    method_names = pytest.method_names  # This will be set in the test file
    module = importlib.import_module(problem_name)
    obj = getattr(module, "Solution")()
    return [getattr(obj, name) for name in method_names]
