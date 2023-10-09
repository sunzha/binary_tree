from __future__ import annotations
from typing import TypeVar, Generic, Callable
from data_structures.linked_list import LinkedList
T = TypeVar("T")

class BinaryTreeNode(Generic[T]):
    def __init__(self, key: T = None):
        self.key = key
        self.left: BinaryTreeNode[T] = None
        self.right: BinaryTreeNode[T] = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __repr__(self) -> str:
        return str(self.key)
    
class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        self.root: BinaryTreeNode[T] = None
    
    def get_leaf(self) -> LinkedList[BinaryTreeNode[T]]:
        """ Returns a list of all of the leaf nodes in the current binary tree
        
        
        :Returns:
            LinkedList[BinaryTreeNode[T]]: The list of leaf nodes
        
        :Complexity: _description_
        """
        leaf_list = LinkedList()
        self.get_leaf_aux(self.root, leaf_list)
        return leaf_list


    def get_leaf_aux(self, current: BinaryTreeNode[T], leaf_list: LinkedList[BinaryTreeNode[T]]) -> BinaryTreeNode:
        return NotImplementedError
    
    def LCA(self, key1: T, key2: T) -> BinaryTreeNode:
        """ Returns the node with the lowest key that has both nodes x and y has descendents.
        Assume that key1 is the key of x and key2 is the key of y and that nodes x and y definitely
        exist. 
        
        :Input:
            key1 (T): node x's key
            key2 (T): node y's key
        
        :Returns:
            BinaryTreeNode: The lowest common ancestor of node x an dy. 
        
        :Complexity: _description_
        """
        return self.LCA_aux(self.root, key1, key2)
    
    def LCA_aux(self, current: BinaryTreeNode[T], key1: T, key2: T) -> BinaryTreeNode:
        return NotImplementedError

    def is_empty(self) -> bool:
        return self.root is None

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = BinaryTreeNode(3)
    tree.root.left = BinaryTreeNode(4)
    tree.root.left.right = BinaryTreeNode(5)
    tree.root.right = BinaryTreeNode(2)
    tree.root.right.right = BinaryTreeNode(-1)
    tree.root.right.left = BinaryTreeNode(7)
    print(tree.return_leaf_max_val(6))
