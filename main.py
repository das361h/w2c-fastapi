from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#@app.get("/search/", response_model=list[schemas.RecipeBase])
#def search_recipes(ingredients: list[str], db: Session = Depends(get_db)):
#    recipes = crud.get_recipes_by_ingredients(db, ingredients)
#    return recipes

#@app.get("/recipe/{rid}", response_model=schemas.RecipeBase)
#def get_recipe(rid: str, db: Session = Depends(get_db)):
#    recipe = crud.get_recipe_by_id(db, rid)
#    if not recipe:
#        raise HTTPException(status_code=404, detail="Recipe not found")
#    return recipe
@app.get("/recipes/", response_model=List[schemas.RecipeBase])
def read_recipes(ingredients: List[str], db: Session = Depends(get_db)):
    recipes = crud.get_recipes_by_ingredients(db, ingredients)
    if not recipes:
        raise HTTPException(status_code=404, detail="No recipes found")
    return recipes

@app.get("/recipes/{rid}", response_model=schemas.RecipeBase)
def read_recipe(rid: str, db: Session = Depends(get_db)):
    recipe = crud.get_recipe_by_id(db, rid)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
