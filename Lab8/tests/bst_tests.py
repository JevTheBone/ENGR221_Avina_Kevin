import pytest

from ..binarySearchTree import BinarySearchTree

@pytest.fixture 
# Define an empty BST for testing
def emptyTree():
    return BinarySearchTree()

@pytest.fixture 
# Define a BST for testing
# Should look like
#          5
#        /   \
#       3     8
#      /
#     1
def nonemptyTree():
    bst = BinarySearchTree()
    bst.insert(5, "five")
    bst.insert(8, "eight")
    bst.insert(3, "three")
    bst.insert(1, "one")
    return bst

####
# Custom Tests
####

@pytest.fixture
# Defining a complext BST for testing
def complexTree():
    bst = BinarySearchTree()
    bst.insert(5, "five")
    bst.insert(3, "three")
    bst.insert(8, "eight")
    bst.insert(4, "four")
    bst.insert(2, "two")
    bst.insert(7, "seven")
    bst.insert(9, "nine")
    bst.insert(6, "six")
    bst.insert(10, "ten")
    bst.insert(1, "one")
    return bst

####
# getRoot
####

@pytest.mark.getRoot
# getRoot functionality after deleting root from BST
def test_bst_getRoot_updatedComplexTreeRoot(complexTree):
    # Delete current root node
    complexTree.delete(5)
    # Should return 6
    assert complexTree.getRoot().key == 6

####
# Search
####

@pytest.mark.search
# Search functionality for complex BST not existing key
def test_bst_search_notInComplexTree(complexTree):
    assert complexTree.search(12) == None

@pytest.mark.search
# Search functionality for complex BST an existing key
def test_bst_search_inComplexTree(complexTree):
    assert complexTree.search(7).key == 7

####
# Delete
####

@pytest.mark.delete
# Delete functionality for complex BST
def test_bst_delete_complexTreeLeaf(complexTree, capfd):
    complexTree.delete(2)
    # Print the tree
    print(complexTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 2 removed
    assert out == "{(5, five), {(3, three), {(1, one), None, None}, {(4, four), None, None}}, {(8, eight), {(7, seven), {(6, six), None, None}, None}, {(9, nine), None, {(10, ten), None, None}}}}\n"

####
# findSuccessor
####

@pytest.mark.findSuccessor
# findSuccessor functionality for complex BST
def test_bst_findSuccessor_complexTree(complexTree):
    complexTree.delete(1)
    # Should return smallest value in the tree after deleting node 1
    assert complexTree.findSuccessor(complexTree.getRoot()).key == 2

####
# Lookup
####

@pytest.mark.lookup
# Lookup functionality for a BST
def test_bst_lookup_complexTreePresent(complexTree):
    try:
        # This should throw an exception
        complexTree.lookup(4)
    except:
        # If we got here, an exception was thrown
        assert False 

####
# End of Custom Tests
####

####
# isEmpty
####

@pytest.mark.isEmpty
# isEmpty functionality for a BST
def test_bst_isempty_true(emptyTree):
    # Should return True
    assert emptyTree.isEmpty()

@pytest.mark.isEmpty
# isEmpty functionality for a BST
def test_bst_isempty_false(nonemptyTree):
    # Should return False 
    assert not nonemptyTree.isEmpty()

####
# getRoot
####

@pytest.mark.getRoot
# getRoot functionality for a BST
def test_bst_getRoot_empty(emptyTree):
    # Should be None
    assert emptyTree.getRoot() is None 

@pytest.mark.getRoot
# getRoot functionality for a BST
def test_bst_getRoot_nonempty(nonemptyTree):
    # Should return 5
    assert nonemptyTree.getRoot().key == 5

####
# search
####

@pytest.mark.search
# search functionality for a BST
def test_bst_search_present(nonemptyTree):
    # Should return 3
    assert nonemptyTree.search(3).key == 3

@pytest.mark.search
# search functionality for a BST
def test_bst_search_absent(nonemptyTree):
    # Should return None
    assert nonemptyTree.search(4) is None

####
# lookup
####

@pytest.mark.lookup
# lookup functionality for a BST
def test_bst_lookup_present(nonemptyTree):
    # Should return "one"
    assert nonemptyTree.lookup(1) == "one"

@pytest.mark.lookup
# lookup functionality for a BST
def test_bst_lookup_notpresent(nonemptyTree):
    try:
        # This should throw an exception
        nonemptyTree.lookup(4)
    except:
        # If we got here, an exception was thrown
        assert True 

####
# findSuccessor
####

@pytest.mark.findSuccessor
# findSuccessor functionality for a BST
def test_bst_findSuccessor(nonemptyTree):
    # Should return smallest value in tree (1)
    assert nonemptyTree.findSuccessor(nonemptyTree.getRoot()).key == 1

####
# delete
####

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_leaf(nonemptyTree, capfd):
    # Delete a leaf
    nonemptyTree.delete(1)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 1 removed
    assert out == "{(5, five), {(3, three), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_child(nonemptyTree, capfd):
    # Delete a node with one child
    nonemptyTree.delete(3)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 3 removed
    assert out == "{(5, five), {(1, one), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_children(nonemptyTree, capfd):
    # Delete a node with two children
    nonemptyTree.delete(5)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 5 removed
    assert out == "{(8, eight), {(3, three), {(1, one), None, None}, None}, None}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_stick(nonemptyTree, capfd):
    # Delete so we are left with a stick
    nonemptyTree.delete(5)
    # Now delete so we are forced to change the root in Case 2
    nonemptyTree.delete(8)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 5 removed
    assert out == "{(3, three), {(1, one), None, None}, None}\n"
    
@pytest.mark.traverse
# traverse functionality for a BST
def test_bst_traverse(nonemptyTree, capfd):
    # Traverse the tree
    nonemptyTree.traverse()
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is in the expected order
    assert out == "(1, one)\n(3, three)\n(5, five)\n(8, eight)\n"