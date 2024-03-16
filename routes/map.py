from fastapi import APIRouter, Body, Query
from typing import Annotated

from database.database import *
from models.student import Student
from schemas.student import Response, UpdateStudentModel


router = APIRouter()


@router.get("/categories", response_description="Categories retrieved", response_model=Response)
async def get_categories():
    categories = await retrieve_categories()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Category data retrieved successfully",
        "data": categories,
    }


async def retrieve_categories():
    '''
    This function retrieves the categories from the database
    
    Args:
    q (list[str] | None): The query parameter
    
    Returns:
    dict: The categories retrieved
        {
            name: str,
            id: str
        }
    '''
    pass


@router.get("/markers", response_description="Markers retrieved", response_model=Response)
async def get_markers(category: Annotated[list[str] | None, Query()] = None):
    markers = await retrieve_markers(category)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Marker data retrieved successfully",
        "data": markers,
    } 


async def retrieve_markers(category):
    '''
    This function retrieves the markers from the database
    
    Args:
    category (list[str] | None): List of category ids to filter the markers, if None all markers are retrieved
    
    Returns:
    dict: The markers retrieved
        {
            name: str,
            lat: str,
            lng: str,
            category: str
        }
    '''
    pass