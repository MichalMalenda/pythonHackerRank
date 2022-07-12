import textwrap
def wrap(string, max_width):
    out = ' \n'.join(textwrap.wrap(string,max_width))
    return out

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)