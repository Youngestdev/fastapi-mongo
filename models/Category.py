from beanie import Document


class Category(Document):
    name: str
    description: str

    class Settings:
        name = "categories"

