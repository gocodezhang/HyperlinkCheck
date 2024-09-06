from typing import TypedDict


class UrlContext(TypedDict):
    title: list[str]
    summary: str
    body: str
    check_code: int


class ValidationResult(TypedDict):
    keywords: list[str]
    scores: list[int]
