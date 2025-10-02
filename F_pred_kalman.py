import numpy as np
import math


# Dos funciones, una retorna los valores predicción cuando no hay medicion, la otra retorna los valores de actualizacion
# cuando si hay medicion 

def Filtro_no_measure(p_upd, x_upd, pQ, vQ):
    pQ = 1
    vQ = 1
    t = 0
    dt = 1/30
    F = np.array([[1, 0, dt, 0],
                  [0, 1, 0, dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

    Q = np.array([[pQ, 0, 0, 0],
                  [0, pQ, 0, 0],
                  [0, 0, vQ, 0],
                  [0, 0, 0, vQ]])
    
    x_pre = np.matmul(F, np.transpose(x_upd))
    p_pre = np.matmul(np.matmul(F, p_upd), np.transpose(F)) + Q

    return x_pre, p_pre


def Filtro(med, p_upd, x_upd, pQ, vQ):
    
    pQ = 1
    vQ = 1

    dt = 1/30
    F = np.array([[1, 0, dt, 0],
                  [0, 1, 0, dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

    Q = np.array([[pQ, 0, 0, 0],
                  [0, pQ, 0, 0],
                  [0, 0, vQ, 0],
                  [0, 0, 0, vQ]])

    H = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0]])

    R = np.array([[24.1, 0],
                  [0, 24.8]])


    I = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])


    # Medicion
    x = med[0]
    y = med[1]

    z = [x, y]

    # Prediccion
    x_pre = np.matmul(F, np.transpose(x_upd))
    p_pre = np.matmul(np.matmul(F, p_upd), np.transpose(F)) + Q

    # Actualizacion
    y_t = np.transpose(z) - np.matmul(H, x_pre)
    s = np.matmul(np.matmul(H, p_pre), np.transpose(H)) + R
    k = np.matmul(np.matmul(p_pre, np.transpose(H)), np.linalg.inv(s))
    x_upd = x_pre + np.matmul(k, y_t)
    p_upd = np.matmul((I - np.matmul(k, H)), p_pre)


    return x_upd, p_upd, x_pre, p_pre
