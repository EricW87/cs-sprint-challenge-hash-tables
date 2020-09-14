# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    files_dict = {}
    result = []
    for f in files:
        if f[-1] == '/':
            continue

        sfiles = f.split('/')
        if sfiles[-1] in files_dict:
            files_dict[sfiles[-1]].append(f)
        else:
            files_dict[sfiles[-1]] = [f]

    for q in queries:
        if q in files_dict:
            for i in files_dict[q]:
                result.append(i)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
