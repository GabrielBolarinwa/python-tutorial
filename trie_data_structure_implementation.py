class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word: str):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def delete(self, word: str):
        self.__delete(self.root, word, 0)

    def has_prefix(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

    def starts_with(self, prefix):
        words = []
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return words
            current_node = current_node.children[char]

        def __dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append("".join(path))

            for char, child_node in current_node.children.items():
                __dfs(child_node, path + [char])

        __dfs(current_node, list(prefix))

        return words

    def list_words(self):
        words = []

        def __dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append("".join(path))

            for char, child_node in current_node.children.items():
                __dfs(child_node, path + [char])

        __dfs(self.root, [])

        return words

    def __delete(self, current_node: Node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False

            current_node.is_end_of_word = False

            return len(current_node.children) == 0
        c = word[index]
        node = current_node.children.get(c)

        if node is None:
            return False

        delete_current_node = self.__delete(node, word, index + 1)
        if delete_current_node:
            del current_node.children[c]
            return len(current_node.children) == 0 and not current_node.is_end_of_word

        return False


if __name__ == "__main__":
    trie = Trie()

    trie.insert("hello")
    trie.insert("henry")
    trie.insert("mike")
    trie.insert("minimal")
    trie.insert("minimum")

    print(trie.list_words())
    print(trie.has_prefix("mi"))
    print(trie.starts_with("mi"))
    trie.delete("minimal")
    print(trie.starts_with("mi"))
    print(trie.search("minimum"))
    print(trie.search("minimal"))
    print(trie.search("mini"))
    trie.insert("mini")
    print(trie.starts_with("mi"))
