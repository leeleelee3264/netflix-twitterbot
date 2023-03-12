from dataclasses import dataclass


@dataclass
class Meta:
    total_items: int
    total_page: int
    per_page: int


@dataclass
class Content:
    title: str
    start_time: str
    image: str
