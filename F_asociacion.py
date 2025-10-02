from itertools import product
import math

# Esta función recibe un arreglo de posiciones desordenadas y las ordena de acuerdo al orden de los cluster. 

def combinaciones_con_posiciones(arreglo_principal):
    n = len(arreglo_principal[0])  
    for combinacion in product(range(n), repeat=len(arreglo_principal)):
        if len(set(combinacion)) == len(arreglo_principal):
            valores_combinados = [arreglo_principal[i][pos] for i, pos in enumerate(combinacion)]
            yield combinacion, valores_combinados


def itera (new_pos, last_position, um):
    if len(last_position) != 0:
        dfish = []
        new_cluster = []
        c = 0
        for i in range(len(new_pos)):
            df = []
            for j in range(len(last_position)):
                d = int(math.sqrt((new_pos[i][0] - last_position[j][0]) ** 2 + (new_pos[i][1] - last_position[j][1]) ** 2))
                if d > 200:
                    d = 200
                df.append(d)
            dfish.append(df)
        #print(dfish)
        if len(new_pos) > len(last_position):
            for m in range(len(dfish) - len(last_position)):
                val_max = []
                for n in range(len(dfish)):
                    minimo = min(dfish[n])
                    val_max.append(minimo)
                mayor = max(val_max)
                idx = val_max.index(mayor)
                new_cluster.append(new_pos[idx])
                dfish.pop(idx)
                new_pos.pop(idx)
        m_suma = 100000000000
        for posicion, valores in combinaciones_con_posiciones(dfish):
            suma = 0
            for vc in valores:
                suma += vc**2
            if suma < m_suma:
                m_val = valores
                m_suma = suma
                p_obj = posicion
        add_pos = []
        for val in range(len(last_position)):
            add_pos.append([0, 0])
        for val in range(len(p_obj)):
            if m_val[val] <= um:
                add_pos[p_obj[val]] = new_pos[val]
    else:
        add_pos = new_pos
        new_cluster = new_pos

    return add_pos, new_cluster





"""

new_pos = [[500, 500], [600, 600]]

last_position = [[498, 495], [205, 202], [600, 600]]


pos, nc = itera(new_pos, last_position, 50)

print("Las posiciones ",pos, "se agregan en ese orden")
print("Los nuevos candidatos de cluster son ", nc)

"""