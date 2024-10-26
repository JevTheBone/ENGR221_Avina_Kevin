import pytest

from box import Box

# Write your tests here, we need at least 3 tests for our Box class

@pytest.fixture
def defaultBox():
    return Box()

@pytest.mark.add
# Test functionallity for add method
def test_add(defaultBox):
    # Assign key, value pair to add
    nickname = "GreedyRapooh"
    species = "Gengar"
    # Assert entry was added successfully
    assert defaultBox.add(nickname, species) == True

@pytest.mark.find
# Test functionallity for find method
def test_find(defaultBox):
    # Assign key, value pair to find
    nickname = "Charla"
    species = "Charizard"
    # Add values into our box
    defaultBox.add(nickname, species)
    # Assert the value we added is found and it doesn't return None
    assert defaultBox.find(nickname, species) != None

@pytest.mark.findEntryByNickname
# Test functionallity for findEntryByNickname method
def test_findEntryByNickname(defaultBox):
    # Assign key, value pairs to find
    nickname = "Pikachu"
    species = "Electric"
    defaultBox.add(nickname, species)
    # Assert the value we added is found by only using the nickname
    assert defaultBox.findEntryByNickname(nickname) != None