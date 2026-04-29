#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Materi 1 : implementasi graph
#======================================================

graph = {
    'A':['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'D'],
    'D':['B', 'C'],
}

for node in graph:
    print(node, '->', graph[node])
