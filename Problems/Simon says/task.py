def what_to_do(instructions):
    if "Simon says" in instructions:
        intro = instructions[:instructions.find("Simon says") - 1]
        outro = instructions[instructions.find("Simon says") + 11:]

        if instructions.find("Simon says") == 0:
            if "Simon says" in intro:
                return f"I {outro}"
            else:
                return f"I {intro}"
        elif (instructions.find("Simon says") + 10) < len(instructions):
            return "I won't do it!"

        if "Simon says" in intro:
            return f"I {outro}"
        else:
            return f"I {intro}"

    else:
        return "I won't do it!"
