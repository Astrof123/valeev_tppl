
class Notation:
    def notation2(self, example: str) -> str:
        stack = []
        num = ""

        for i in range(len(example) - 1, -1, -1):
            if example[i] in ["+", "-", "*", "/"]:
                if len(stack) <= 1:
                    raise SyntaxError("The expression is not correctly composed. Not enough numbers.")

                left = stack[-1]
                op = example[i]
                right = stack[-2]

                stack.pop(-1)
                stack.pop(-1)

                if op in ["*", "/"]:
                    if len(right.split()) > 1 and len(left.split()) > 1:
                        stack.append(f"({left}) {op} ({right})")
                    elif len(right.split()) > 1:
                        stack.append(f"{left} {op} ({right})")

                else:
                    stack.append(f"{left} {op} {right}")

            elif example[i] == " ":
                if num == "":
                    continue
                stack.append(num)
                num = ""
            elif example[i].isdigit():
                num = example[i] + num

        return stack[0]