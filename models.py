"""
Pydantic models used for request and response validation.
"""
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Category(str, Enum):
    """
    Categories of grammar mistakes detected by the model.
    """
    grammar = "Grammar"
    spelling = "Spelling"
    punctuation = "Punctuation"
    capitalization = "Capitalization"
    vocabulary = "Vocabulary"


class Mistake(BaseModel):
    """
    Represents a single grammar mistake and its correction.
    """
    original: str = Field(
        ...,
        description="Incorrect text."
    )

    replacement: str = Field(
        ...,
        description="Suggested correction."
    )

    category: Category = Field(
        ...,
        description="Type of grammar mistake."
    )

    reason: str = Field(
        ...,
        description="Explanation of the correction."
    )


class GrammarRequest(BaseModel):
    """
    Request body for grammar correction.
    """
    text: str = Field(
        ...,
        description="Input sentence to be corrected.",
        examples=["im happy"],
    )


class GrammarResponse(BaseModel):
    """
    Response returned after grammar correction.
    """
    language: str = Field(
        ...,
        description="Detected language."
    )

    corrected_text: str = Field(
        ...,
        description="Corrected version of the input."
    )

    has_errors: bool = Field(
        ...,
        description="Indicates whether any mistakes were found."
    )

    mistakes: List[Mistake] = Field(
        ...,
        description="List of detected grammar mistakes."
    )