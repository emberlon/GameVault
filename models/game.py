"""Game model used by the GameVault collection."""

from dataclasses import dataclass


@dataclass
class Game:
    title: str
    platform: str
    genre: str
    release_year: int
    completed: bool = False

    def __post_init__(self):
        self.title = self.title.strip()
        self.platform = self.platform.strip()
        self.genre = self.genre.strip()

        if not self.title:
            raise ValueError("Game title cannot be empty.")
        if self.release_year < 0:
            raise ValueError("Release year cannot be negative.")

    def __str__(self):
        status = "Completed" if self.completed else "Not completed"
        return (
            f"{self.title} ({self.release_year}) - {self.platform} "
            f"| {self.genre} | {status}"
        )
