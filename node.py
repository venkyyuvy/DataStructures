class Node:
    def __init__(self, name):
        self.name=name
        self.nxt_node=None
        self.prv_node=None
    
    def __repr__(self) -> str:
        return str(self.name)
