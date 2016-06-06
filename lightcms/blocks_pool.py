class BlocksPool:

    def __init__(self):
        self.blocks = set()

    def register(self, block):
        self.blocks.add(block)

blocks_pool = BlocksPool()
