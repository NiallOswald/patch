class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        # We allocate a single array sized for all stacks combined.
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.array = [None] * (num_stacks * stack_size)

        # tops[i] tracks the \'top index\' within the sub-stack for stack i.
        # Initialize each stack top at -1 to indicate an empty stack.
        self.tops = [-1] * num_stacks

    def abs_index(self, stack_index):
        """
        Convert (stack_index, top_within_stack) into an absolute index
        within self.array.
        """
        return stack_index * self.stack_size + self.tops[stack_index]

    def push(self, stack_index, data):
        """
        Attempt to push \'data\' onto the specified stack.
        Raises an exception if the stack is full.
        """

        # Check if the top pointer is at the last valid position.
        if self.tops[stack_index] == self.stack_size - 1:
            raise Exception("Stack is full!")

        # ─────────────────────────────────────────────────
        # Intentional Logical Error Here:
        # We use abs_index(...) before incrementing tops[stack_index].
        # This causes the very first insertion to write at an invalid index.
        # ─────────────────────────────────────────────────
        self.array[self.abs_index(stack_index)] = data

        # Increment top pointer AFTER using abs_index...
        self.tops[stack_index] += 1

    def pop(self, stack_index):
        """
        Pop the top item from the specified stack.
        Raises an exception if the stack is empty.
        """
        if self.tops[stack_index] == -1:
            raise Exception("Stack is empty!")

        value = self.array[self.abs_index(stack_index)]
        self.array[self.abs_index(stack_index)] = None
        self.tops[stack_index] -= 1

        return value
