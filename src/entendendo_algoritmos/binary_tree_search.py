from __future__ import annotations


class Node:
    def __init__(self, value: int):
        self.val: int = value  # Guarda o valor
        self.left: Node | None = None  # Ponteiro para o filho esquerdo (menor)
        self.right: Node | None = None  # Ponteiro para o filho direito (maior)

    @staticmethod
    def insert_value(root: Node | None, value: int) -> Node:

        if root is None:
            return Node(value)

        if value < root.val:
            root.left = Node.insert_value(root.left, value)
        else:
            root.right = Node.insert_value(root.right, value)

        return root

    @staticmethod
    def remove_value(root: Node | None, value: int) -> None:
        
        if root is None:
            return print("Raiz não encontrada")
        
        elif value < root.val:
            remove_value(root.left, value)
            
        elif value > root.val:
            remove_value(root.right, value)
            
        else:
            
            if root.left is None and root.right is None:
                root = None
                return
            
            if root.left and root.right is None:
                root = root.left
                return
            
            if root.left is None and root.right:
                root = root.right
                return

        # Decisão de projeto, se ele for um pai que tem dois filhos tem que decidir se quer o maior ou menor para substitui-lo;
        minRight = findMin(root.left)
        root = minRight
        
