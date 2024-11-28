class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = 0  # To track the level of the node in the tree

class ObscureBST:

    def __init__(self, comparison_func=None):
        self.root = None
        self.comparison_func = comparison_func if comparison_func else self.default_comparison
    
    def default_comparison(self, a, b):
        """Default comparison function (standard BST behavior)."""
        return a - b
    
    def insert(self, value):
        """Insert a new value into the tree using the custom comparison."""
        if not self.root:
            self.root = Node(value)
            self.root.level = 0  # Root is always at level 0111
        else:
            self._insert(self.root, value, 0)
    
    def _insert(self, current_node, value, level):
        """Helper function to recursively insert a node."""
        level += 1
        if self.comparison_func(value, current_node.value) < 0:
            # Value is less, go left
            if current_node.left is None:
                current_node.left = Node(value)
                current_node.left.level = level
            else:
                self._insert(current_node.left, value, level)
        else:
            # Value is greater, go right
            if current_node.right is None:
                current_node.right = Node(value)
                current_node.right.level = level
            else:
                self._insert(current_node.right, value, level)

    def search(self, value):
        """Search for a value in the tree."""
        return self._search(self.root, value)

    def _search(self, node, value):
        """Helper function to recursively search for a value."""
        if node is None:
            return False
        if node.value == value:
            return True
        if self.comparison_func(value, node.value) < 0:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def delete(self, value):
        """Delete a node with the specified value."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        """Helper function to delete a node."""
        if node is None:
            return node
        if self.comparison_func(value, node.value) < 0:
            node.left = self._delete(node.left, value)
        elif self.comparison_func(value, node.value) > 0:
            node.right = self._delete(node.right, value)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has two children, replace with the in-order successor
                node.value = self._min_value_node(node.right).value
                node.right = self._delete(node.right, node.value)
        return node
    
    def _min_value_node(self, node):
        """Get the node with the smallest value (in-order successor)."""
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
    
    def inorder_traversal(self):
        """Traverse the tree in-order.""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        ""Helper function for in-order traversal.""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def display(self):
        """Display the tree in a structured way."""
        self._display(self.root)

    def _display(self, node):
        """Helper function to print the tree structure."""""
        if node:
            print(f"Value: {node.value}, Level: {node.level}")
            self._display(node.left)
            self._display(node.right)

# Example usage
def main():
    print("Obscure Binary Search Tree")
    bst = ObscureBST()

    while True:
        print("\nMenu:")
        print("1. Insert Value")
        print("2. Search Value")
        print("3. Delete Value")
        print("4. Inorder Traversal")
        print("5. Display Tree")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = int(input("Enter value to insert: "))
            bst.insert(value)
        elif choice == "2":
            value = int(input("Enter value to search: "))
            found = bst.search(value)
            print("Found!" if found else "Not Found!")
        elif choice == "3":
            value = int(input("Enter value to delete: "))
            bst.delete(value)
        elif choice == "4":
            result = bst.inorder_traversal()
            print("Inorder Traversal:", result)
        elif choice == "5":
            bst.display()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
