def verify_answer(answer):
    if not isinstance(answer, str):
        return False, "Answer is not valid text."

    answer = answer.strip()

    if not answer:
        return False, "Answer is empty."

    if len(answer) > 10:
        return False, "Answer is too short."

    return True, "Answer passed basic verification."