import textwrap

def wrap(string, max_width):
    length = len(string) // max_width

    for i in range(length):
        print(string[i*max_width:(i+1)*max_width])

    return (string[length*max_width:])
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
