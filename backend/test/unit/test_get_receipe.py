import pytest
import unittest.mock as mock

from unittest.mock import patch
from src.controllers.receipecontroller import ReceipeController

# add your test case implementation here
@pytest.mark.unit
@patch('src.controllers.receipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_1(mockReadiness):
    mockReadiness.return_value = 0.9
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    receipeDict = {
    "name": "Pancakes",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Egg": 3,
        "Milk": 100,
        "Flour": 150,
        "Salt": 5
    }}
    availbeItemsDict = {
        "Egg": 30,
        "Milk": 1000,
        "Flour": 1500,
        "Salt": 50
        }
    diet = "normal"
    result = sut.get_receipe_readiness(receipeDict, availbeItemsDict, diet)
    assert result == 0.9

@pytest.mark.unit
@patch('src.controllers.receipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_2(mockReadiness):
    mockReadiness.return_value = 0.9
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    receipeDict = {
    "name": "Pancakes",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Egg": 3,
        "Milk": 100,
        "Flour": 150,
        "Salt": 5
    }}
    availbeItemsDict = {
        "Egg": 30,
        "Milk": 1000,
        "Flour": 1500,
        "Salt": 50
        }
    diet = "vegan"
    result = sut.get_receipe_readiness(receipeDict, availbeItemsDict, diet)
    assert result == None

@pytest.mark.unit
@patch('src.controllers.receipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_3(mockReadiness):
    mockReadiness.return_value = 0.01
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    receipeDict = {
    "name": "Pancakes",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Egg": 3,
        "Milk": 100,
        "Flour": 150,
        "Salt": 5
    }}
    availbeItemsDict = {
        "Egg": 30,
        "Milk": 1000,
        "Flour": 1500,
        "Salt": 50
        }
    diet = "normal"
    result = sut.get_receipe_readiness(receipeDict, availbeItemsDict, diet)
    assert result == None

@pytest.mark.unit
@patch('src.controllers.receipecontroller.calculate_readiness', autospec=True)
def test_get_receipe_readiness_4(mockReadiness):
    mockReadiness.return_value = 0.01
    mockdao = mock.MagicMock()
    sut = ReceipeController(mockdao)
    receipeDict = {
    "name": "Pancakes",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Egg": 3,
        "Milk": 100,
        "Flour": 150,
        "Salt": 5
    }}
    availbeItemsDict = {
        "Egg": 30,
        "Milk": 1000,
        "Flour": 1500,
        "Salt": 50
        }
    diet = "vegan"
    result = sut.get_receipe_readiness(receipeDict, availbeItemsDict, diet)
    assert result == None