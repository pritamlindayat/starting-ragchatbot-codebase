"""
Shared pytest fixtures for all backend tests.

sys.path is managed by [tool.pytest.ini_options] pythonpath in pyproject.toml,
which adds both backend/ and backend/tests/ before any test module is imported.
"""

import pytest
from unittest.mock import MagicMock

from vector_store import SearchResults


@pytest.fixture
def sample_search_results():
    """SearchResults with one document and full metadata"""
    return SearchResults(
        documents=["This is lesson content about Python basics"],
        metadata=[{"course_title": "Intro to Python", "lesson_number": 1}],
        distances=[0.1],
    )


@pytest.fixture
def empty_search_results():
    """SearchResults with no documents"""
    return SearchResults(
        documents=[],
        metadata=[],
        distances=[],
    )


@pytest.fixture
def error_search_results():
    """SearchResults carrying an error message"""
    return SearchResults.empty("Search error: connection refused")


@pytest.fixture
def mock_vector_store():
    """MagicMock VectorStore with get_lesson_link pre-configured"""
    store = MagicMock()
    store.get_lesson_link.return_value = "https://example.com/lesson/1"
    return store
