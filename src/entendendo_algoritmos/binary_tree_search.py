from __future__ import annotations


class Node:

    def __init__(self, value: int):
        self.val: int = value  # Guarda o valor numérico do nó
        self.left: Node | None = (
            None  # Ponteiro para o filho esquerdo (valores menores)
        )
        self.right: Node | None = (
            None  # Ponteiro para o filho direito (valores maiores)
        )

    @staticmethod
    def insert_value(root: Node | None, value: int) -> Node:
        # CASO BASE: Se o lugar estiver vazio (None), encontramos a posição correta!
        # Criamos um novo nó aqui e o retornamos para o pai linkar em left ou right.
        if root is None:
            return Node(value)

        # Se o valor que queremos inserir for MENOR que o valor do nó atual:
        if value < root.val:
            # Descemos para a esquerda. O 'root.left' vai receber o resultado da inserção lá embaixo.
            root.left = Node.insert_value(root.left, value)
        else:
            # Se for MAIOR ou IGUAL, descemos para a direita.
            root.right = Node.insert_value(root.right, value)

        # Devolvemos o próprio nó atual (sem alterações na estrutura dele) para manter a árvore conectada
        return root

    @staticmethod
    def find_min(root: Node) -> Node:
        """Função auxiliar para encontrar o menor valor a partir de um ponto da
        árvore. Na árvore binária de busca, o menor valor SEMPRE estará o máximo
        possível para a esquerda.
        """
        current = root
        # Enquanto existir um nó mais à esquerda, nós caminhamos para ele
        while current.left is not None:
            current = current.left
        return current  # Retorna o nó que não tem mais ninguém à sua esquerda

    @staticmethod
    def remove_value(root: Node | None, value: int) -> Node | None:
        # -------------------------------------------------------------------------
        # CASO 1: O elemento não existe na árvore
        # -------------------------------------------------------------------------
        if root is None:
            return None  # Chegamos ao fim de um caminho e não achamos o valor. Retorna None.

        # -------------------------------------------------------------------------
        # PASSO DE BUSCA: Navegamos pela árvore até encontrar o nó
        # -------------------------------------------------------------------------
        if value < root.val:
            # Se o valor buscado é menor, ele só pode estar na esquerda.
            # O ponteiro da esquerda é atualizado com o que a função retornar.
            root.left = Node.remove_value(root.left, value)
        elif value > root.val:
            # Se o valor buscado é maior, ele só pode estar na direita.
            root.right = Node.remove_value(root.right, value)

        # -------------------------------------------------------------------------
        # CASO 2: ENCONTRAMOS O NÓ! (value == root.val)
        # Aqui aplicamos as regras de exclusão baseadas nos filhos do nó.
        # -------------------------------------------------------------------------
        else:
            # SUB-CASO A: O nó não tem filho na esquerda (pode ser folha ou ter só o da direita)
            if root.left is None:
                # Se ele for folha, root.right é None, então retornamos None para o pai (deletando o nó).
                # Se ele tiver o filho da direita, retornamos esse filho. O pai vai apontar direto para ele,
                # pulando/excluindo o nó atual da memória.
                return root.right

            # SUB-CASO B: O nó tem filho na esquerda, mas NÃO tem na direita
            elif root.right is None:
                # Retornamos o filho da esquerda para o pai fazer a nova conexão.
                return root.left

            # SUB-CASO C: O nó tem DOIS filhos (Esquerda e Direita populados)
            # Não podemos simplesmente deletar o nó, senão a árvore se quebra inteira.
            else:
                # Estratégia: Pegamos o menor valor do lado DIREITO (Sucessor In-order)
                # Esse valor é perfeito porque é maior que tudo na esquerda e menor que o resto da direita.
                min_right = Node.find_min(root.right)

                # Em vez de destruir o nó atual, apenas COPIAMOS o valor do sucessor para ele.
                root.val = min_right.val

                # Agora que o valor foi substituído, ficamos com um valor "duplicado" na árvore.
                # Chamamos a função de remover novamente na subárvore DIREITA para apagar o nó original
                # de onde copiamos o valor (que agora sabemos que cai no Caso A ou B, sendo fácil deletar).
                root.right = Node.remove_value(root.right, min_right.val)

        # Devolvemos o nó atual modificado (ou não) para o pai atualizar sua referência
        return root

    @staticmethod
    def inorder_print(root: Node | None) -> None:
        """Imprime a árvore em ordem crescente (Esquerda -> Raiz -> Direita)"""
        if root:
            Node.inorder_print(root.left)  # Visita tudo à esquerda
            print(root.val, end=" ")  # Imprime o valor atual
            Node.inorder_print(root.right)  # Visita tudo à direita


# -------------------------------------------------------------------------
# TESTANDO O CÓDIGO
# -------------------------------------------------------------------------
# raiz = None
# valores = [50, 30, 70, 20, 40, 60, 80]

# # Inserindo os valores na árvore
# for v in valores:
#     raiz = Node.insert_value(raiz, v)

# print("Árvore em ordem:")
# Node.inorder_print(raiz)  # Saída: 20 30 40 50 60 70 80

# # Exemplo de remoção de nó com 2 filhos (o 50)
# raiz = Node.remove_value(raiz, 50)

# print("\nÁrvore após remover o 50:")
# Node.inorder_print(raiz)  # Saída: 20 30 40 60 70 80
