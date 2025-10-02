import numpy as np

def AIC(posiciones, n):

    x = []
    y = []
    c = 0
    t = []
    for pos in posiciones:
        x.append(pos[0])
        y.append(pos[1])
        t.append(c)
        c += 1
    t = np.transpose(t)

    ##### MODELO LINEAL (X) #####
    
    k = 2
    A = np.zeros((n, k))
    for i in range(len(x)):
        A[i, 0] = t[i]**1
        A[i, 1] = t[i]**0

    xg = np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(A), A)), np.transpose(A)), x)
    xl = xg

    RSS = np.matmul(np.transpose(x - np.matmul(A, xg)), (x - np.matmul(A, xg)))

    AIC = 2 * k + n * np.log(RSS/n)

    AICclx = AIC + ((2 * k**2 + 2 * k) /(n - k - 1))

    #### MODELO PARABOLA (X) ####

    k = 3
    A = np.zeros((n, k))
    for i in range(len(x)):
        A[i, 0] = t[i] ** 2
        A[i, 1] = t[i] ** 1
        A[i, 2] = t[i] ** 0


    xg = np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(A), A)), np.transpose(A)), x)
    xq = xg

    RSS = np.matmul(np.transpose(x - np.matmul(A, xg)), (x - np.matmul(A, xg)))

    AIC = (2 * k) + (n * np.log(RSS / n))

    AICcqx = AIC + ((2 * (k ** 2) + 2 * k) / (n - k - 1))

    #### MODELO ZERO (X) ####

    k = 1
    A = np.zeros((n, k))
    for i in range(len(x)):
        A[i, 0] = t[i] ** 0

    xg = np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(A), A)), np.transpose(A)), x)
    xz = xg

    RSS = np.matmul(np.transpose(x - np.matmul(A, xg)), (x - np.matmul(A, xg)))

    AIC = (2 * k) + (n * np.log(RSS / n))
    AICczx = AIC + ((2 * (k ** 2) + 2 * k) / (n - k - 1))

    #print("AICczx", xz)

    #plt.plot(t, x, linewidth=3, label="Detecciónes", color='green')
    #plt.scatter(t, x, s=30, color='green')

    #plt.plot(t, xgraf, linewidth=3, label="Ajuste modelo lineal", color='red')
    #plt.scatter(t, xgraf, s=30, color='red')

    #plt.xlabel('t', fontsize=14, fontweight='bold')
    #plt.ylabel('x(t)', fontsize=14, fontweight='bold')
    #plt.tick_params(axis="x", labelsize=11.5)
    #plt.tick_params(axis="y", labelsize=11.5)
    #plt.legend()
    #for i in range(len(x)):
    #    if i != 6:
    #        plt.text(t[i], x[i], "    " + labels[i])
    #    else:
    #        plt.text(t[i], x[i] - 1.5, labels[i])

    #plt.legend(["lx =" + str(AICclx) + "   qx =" + str(AICcqx)])
    #plt.show()
    #plt.savefig("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/AIC/x/" + str(con) + ".jpg")
    #plt.clf()

    # Obtengo parámetros para el modelo con menor AIC (X)

    if AICclx < AICcqx and AICclx < AICczx:
        px = xl
    elif AICcqx < AICclx and AICcqx < AICczx:
        px = xq
    else:
        px = xz
    ################################
    #### MODELO LINEAL (Y) ####
    k = 2
    A = np.zeros((n, k))
    for i in range(len(x)):
        A[i, 0] = t[i] ** 1
        A[i, 1] = t[i] ** 0

    xg = np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(A), A)), np.transpose(A)), y)
    xl = xg

    RSS = np.matmul(np.transpose(y - np.matmul(A, xg)), (y - np.matmul(A, xg)))

    AIC = 2 * k + n * np.log(RSS / n)

    AICcly = AIC + ((2 * k ** 2 + 2 * k) / (n - k - 1))
    #print(con)
    #print("AICcly", AICcly)

    #### MODELO PARABOLA (Y) ####

    k = 3
    A = np.zeros((n, k))
    for i in range(len(x)):
        A[i, 0] = t[i] ** 2
        A[i, 1] = t[i] ** 1
        A[i, 2] = t[i] ** 0

    xg = np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(A), A)), np.transpose(A)), y)
    xq = xg
    RSS = np.matmul(np.transpose(y - np.matmul(A, xg)), (y - np.matmul(A, xg)))

    AIC = (2 * k) + (n * np.log(RSS / n))

    AICcqy = AIC + ((2 * (k ** 2) + 2 * k) / (n - k - 1))

    #### MODELO ZERO (Y) ####
    k = 1
    A = np.zeros((n, k))
    for i in range(len(x)):
        A[i, 0] = t[i] ** 0

    #print(A)

    xg = np.matmul(np.matmul(np.linalg.pinv(np.matmul(np.transpose(A), A)), np.transpose(A)), y)
    xz = xg

    RSS = np.matmul(np.transpose(y - np.matmul(A, xg)), (y - np.matmul(A, xg)))

    AIC = 2 * k + n * np.log(RSS / n)

    AICczy = AIC + ((2 * k ** 2 + 2 * k) / (n - k - 1))

    # Obtengo parámetros para el modelo con menor AIC (Y)
    if AICcly < AICcqy and AICcly < AICczy:
        py = xl
    elif AICcqy < AICcly and AICcqy < AICczy:
        py = xq
    else:
        py = xz

    return px, py


"""
pos = [[301, 417], [295, 416], [286, 414], [287, 414], [274, 410], [265, 409], [259, 407], [252, 406], [244, 404], [238, 403], [230, 402], [232, 402], [222, 398], [217, 396], [215, 394],
       [206, 393], [201, 391], [196, 389], [191, 387], [185, 385],
       [192, 386], [194, 385], [188, 385], [185, 381], [195, 377], [196, 377], [209, 373], [221, 370], [228, 368], [238, 367], [246, 368]]

for i in range(23):
    posiciones = pos[:5]
    #print(posiciones)
    AICclx, AICcqx, AICcl = AIC(posiciones, len(posiciones))
    pos.pop(0)

#table = np.zeros((4, 23))
"""
