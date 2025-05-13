from sqlalchemy.orm import Session
from models import Recipe

def get_recipes_by_ingredients(db: Session, ingredients: list[str]):
    return db.query(Recipe).filter(Recipe.ribs.contains(ingredients)).all()

def get_recipe_by_id(db: Session, rid: str):
    return db.query(Recipe).filter(Recipe.rid == rid).first()
