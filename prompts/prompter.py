from prompts.constants import INSTRUCTION, SKELETON_END, SKELETON_START


def read_in(filename: str, directory: str):
    with open(directory + filename, "r") as file:
        return file.read()


def produce_prompt(directory):
    """
    Produce a ChatGPT prompt for a task based on a task and skeleton, with our custom "instructions" appended.
    """
    TASK = read_in("task.md", directory)
    SKELETON = read_in("skeleton.py", directory)

    PROMPT = INSTRUCTION + "\n" + TASK + "\n" + SKELETON_START + SKELETON + SKELETON_END
    return PROMPT
