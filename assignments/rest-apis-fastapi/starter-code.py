"""
FastAPI Starter Code - Building REST APIs with FastAPI

This file provides a basic structure to help you get started.
Fill in the missing implementations to complete the assignment tasks.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI application
app = FastAPI()

# Define a Pydantic model for data validation (for Task 3)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Task 1: Create your first GET endpoint
@app.get("/")
def read_root():
    """
    TODO: Return a welcome message in JSON format.
    Hint: Return a dictionary that will be converted to JSON.
    """
    pass


# Task 2: Create endpoints with path and query parameters
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    TODO: Return item information based on the item_id parameter.
    Hint: Use the item_id from the path parameter.
    """
    pass


@app.get("/search")
def search_items(query: str, limit: int = 10):
    """
    TODO: Search for items based on query string and limit results.
    Hint: Use query parameters to filter results.
    """
    pass


# Task 3: Create a POST endpoint with data validation
@app.post("/items/")
def create_item(item: Item):
    """
    TODO: Create a new item from the request JSON body.
    Hint: The item parameter will automatically validate against the Item model.
    Return the created item with an additional field.
    """
    pass


# To run the application, use:
# uvicorn starter-code:app --reload
#
# Then visit:
# http://localhost:8000/docs (interactive API documentation)
# http://localhost:8000 (your root endpoint)
