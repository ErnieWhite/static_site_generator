def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        block = block.strip("\n ")
        if block == "":
            continue
        cleaned_blocks.append(block)
    return cleaned_blocks

