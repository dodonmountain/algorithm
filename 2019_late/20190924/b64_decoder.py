import base64
for t_case in range(int(input())):
    arr = input()
    r = base64.b64decode(arr)
    res = r.decode('UTF-8')
    print('#{} {}'.format(t_case+1, res))