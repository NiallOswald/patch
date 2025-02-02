import openai

STANDARD_DELIMETER = (
    "--------------------------------------------------------------------------------"
)


def extract_code_from_completion(chat_completion: openai.ChatCompletion, path=""):
    sections = get_sections(str(chat_completion))

    code_blocks = Finder.find_by_rough_start(sections)

    if len(code_blocks) > 1:
        print("Warning: Multiple blocks found. Saving just the first")

    if len(code_blocks) != 0:
        save_to_file(code_blocks[0].replace("\\n", "\n"), path=path)


def get_sections(model_output_text: str, DELIMETER=STANDARD_DELIMETER):
    sections = model_output_text.split(DELIMETER)
    return sections


def save_to_file(content: str, path: str = ""):
    filename = "skeleton.py"
    with open(path + filename, "w", encoding="utf-8") as file:
        # What should be the correct encoding?
        file.write(content)


class Finder:

    @classmethod
    def find_by_rough_start(cls, sections: list[str]):
        PATTERN = "\\nclass"
        code_sections = []

        for section in sections:
            if section.find(PATTERN) != -1:
                code_sections.append(section)

        if len(code_sections) == 0:
            print("Finder: No code sections found.")
        elif len(code_sections) > 1:
            print("Finder: Many code sections found.")
        else:
            print("Finder: Exactly one code section found")

        return code_sections
