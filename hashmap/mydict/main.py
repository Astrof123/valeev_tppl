class Ploc:
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values

    def analyzer(self, key: str):
        signs = []
        numbers = []

        i = 0
        current_number = ""
        while i < len(key):
            if key[i] == ">":
                if i + 1 == len(key):
                    raise KeyError("Incorrect key specified")
                if key[i + 1] == "=":
                    signs.append(key[i] + key[i+1])
                    i += 2
                else:
                    signs.append(key[i])
                    i += 1

            elif key[i] == "<":
                if i + 1 == len(key):
                    raise KeyError("Incorrect key specified")
                if key[i + 1] == "=":
                    signs.append(key[i] + key[i + 1])
                    i += 2
                elif key[i + 1] == ">":
                    signs.append(key[i] + key[i + 1])
                    i += 2
                else:
                    signs.append(key[i])
                    i += 1

            elif key[i] == "=":
                signs.append(key[i])
                i += 1

            elif key[i].isspace():
                i += 1
            elif key[i].isdigit() or key[i] == '.':
                current_number += key[i]
                i += 1
            else:
                if current_number.count(".") > 1 or current_number.count(".") == len(current_number):
                    raise KeyError("Incorrect key specified")

                numbers.append(float(current_number))
                current_number = ""
                i += 1

        if current_number.count(".") > 1 or current_number.count(".") == len(current_number):
            raise KeyError("Incorrect key specified")

        numbers.append(float(current_number))

        if len(signs) != len(numbers):
            raise KeyError("Incorrect key specified")

        return signs, numbers


    def searcher(self, signs, numbers):
        result = {}
        for j, key in enumerate(self.keys):
            key_numbers = key.replace("(", '').replace(")", '').split(', ')
            if len(key_numbers) == len(signs):
                flag = True

                for i in range(len(signs)):
                    if not key_numbers[i].isdigit():
                        flag = False
                        break

                    match signs[i]:
                        case '>':
                            if not (int(key_numbers[i]) > numbers[i]):
                                flag = False
                            break
                        case '<':
                            if not (int(key_numbers[i]) < numbers[i]):
                                flag = False
                            break
                        case '>=':
                            if not (int(key_numbers[i]) >= numbers[i]):
                                flag = False
                            break
                        case '<=':
                            if not (int(key_numbers[i]) <= numbers[i]):
                                flag = False
                            break
                        case '=':
                            if not (int(key_numbers[i]) == numbers[i]):
                                flag = False
                            break
                        case '<>':
                            if not (int(key_numbers[i]) != numbers[i]):
                                flag = False
                            break

                if flag:
                    result[key] = self.values[j]

        return result


    def __getitem__(self, key):
        if isinstance(key, str):
            if len(key) < 2:
                raise KeyError("The key length must be more than two")

            signs, numbers = self.analyzer(key)

            return self.searcher(signs, numbers)
        else:
            raise KeyError("Only string type can be specified")


class Iloc:
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.values[key]
        else:
            raise KeyError("Only int type can be specified")

class MyDict(dict):
    def __init__(self):
        super().__init__()
        self.keys = []
        self.values = []
        self.iloc = Iloc(self.keys, self.values)
        self.ploc = Ploc(self.keys, self.values)

    def bubble_sort(self):
        n = len(self.keys)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.keys[j] > self.keys[j + 1]:
                    self.keys[j], self.keys[j + 1] = self.keys[j + 1], self.keys[j]
                    self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]

    def __setitem__(self, key, value):
        self.keys.append(key)
        self.values.append(value)
        self.bubble_sort()

        return super().__setitem__(key, value)