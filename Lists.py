if __name__ == '__main__':
    N = int(input())
    alist = []
    for n in range(N):
        val = list(input().split())
        if val[0] == "insert":
            alist.insert(int(val[1]), int(val[2]))
        elif val[0] == "append":
            alist.append(int(val[1]))
        elif val[0] == "print":
            print(alist)
        elif val[0] == "remove":
            alist.remove(int(val[1]))
        elif val[0] == "sort":
            alist.sort()
        elif val[0] == "pop":
            alist.pop()
        elif val[0] == "reverse":
            alist = alist[::-1]
    
