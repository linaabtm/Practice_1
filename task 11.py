melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455,'Si': 1415, 'Be': 1287}
[print(abs(melt[a]-melt[b])) for [a,b] in [map(str,input().split())]]
