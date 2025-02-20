
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next: Node = next

    def print(self):
        print(self.to_string())

    def to_string(self):
        return f"Node={self.val}"

class LinkedList:
    def __init__(self, node):
        self.root: Node = node
        self.end: Node = node

    def add(self, node: Node):
        self.end.next = node
        self.end = node

    def removeLast(self):
        node = self.root
        while node.next != self.end:
            node = node.next

        node.next = None
        self.end = node

    def removeFirst(self):
        self.root = self.root.next

    def reverse(self):
        prev = None
        curr = self.root

        while curr != None:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp

        self.root = prev

    def print(self):
        result = "["
        node = self.root
        while node != None:
            result += node.to_string() + ", "
            node = node.next

        result += "]"
        print(result)


if __name__ == "__main__":
    print("Init list")
    root: Node = Node(1, None)
    list: LinkedList = LinkedList(root)
    list.print()

    print("Add node")
    list.add(Node(2, None))
    list.print()

    print("Remove last")
    list.removeLast()
    list.print()

    print("Remove first")
    list.add(Node(2, None))
    list.print()
    list.removeFirst()
    list.print()

    print("Reverse list")
    list.add(Node(3, Node(4, None)))
    list.print()
    list.reverse()
    list.print()
