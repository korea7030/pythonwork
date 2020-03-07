class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data # 마지막 글자를 나타내는 flag 역할. 마지막인 경우 전체 단어를 저장
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
        # string의 마지막 글자 차례이면 노드의 data필드에 저장하려는 문자열 전체를 저장(마지막 여부 설정)
        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # string의 마지막 글자에 도달한 경우 curr_node에 data가 있다면 string이 트라이에 존재하는 것으로 판단
        if (curr_node.data != None):
            return True

    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # bfs 로 prefix subtrie를 순회하며 data가 있는 노드들(=완전한 단어)를 찾는다.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)

            queue += list(curr.children.values())

        return result


if __name__== '__main__':
    trie = Trie()
    trie.insert('start')
    trie.search('start')
    result = trie.starts_with('st')
    print(result)