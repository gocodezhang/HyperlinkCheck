from typing import TypedDict, Optional


class UrlContext(TypedDict):
    title: list[str]
    summary: str
    body: str
    check_code: int


class ValidationResult(TypedDict):
    keywords: list[str]
    scores: list[int]


class PassageContext(TypedDict):
    linked_str: str
    sentence: str
    three_sentences: str | None
