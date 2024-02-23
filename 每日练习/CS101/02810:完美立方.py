N = int(input())

result = []
for a in range(2, N + 1):
    cube_a = pow(a, 3)
    for d in range(2, a):
        cube_d = pow(d, 3)
        for c in range(2, d + 1):
            cube_c = pow(c, 3)
            for b in range(2, c + 1):
                cube_b = pow(b, 3)
                if cube_b + cube_c + cube_d == cube_a:
                    result.append((a, b, c, d))
result.sort()
for a,b,c,d in result:
    print(f"Cube = {a}, Triple = ({b},{c},{d})")