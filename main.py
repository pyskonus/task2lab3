import json

result = []


def search(key, iterable):
    if isinstance(iterable, list):
        for element in iterable:
            search(key, element)
    elif isinstance(iterable, dict):
        for element in iterable:
            if element == key:
                result.append(iterable[element])
            else:
                search(key, iterable[element])


def main():
    File = input('Input the file name (for example, "info"): ')
    key = input("Input the key you're searching for: ")
    dct = json.load(open(File + '.json', encoding="utf-8"))
    search(key, dct)
    print(result)

    return result

if __name__ == "__main__":
    main()
