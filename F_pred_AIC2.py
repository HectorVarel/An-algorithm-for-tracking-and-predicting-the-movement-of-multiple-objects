from F_AIC import AIC
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import math
import matplotlib.pyplot as plt

def Ransac_q(x):
    x = list(x)
    param = RANSAC_QUAD(x)
    return param

def Ransac_l(x):
    x = list(x)
    param = RANSAC_LINEA(x)
    return param

def Ransac_z(x):
    x = list(x)
    param = RANSAC_ZERO(x)
    return param

def RANSAC_LINEA(x):
    # Aplica RANSAC para un modelo de línea, se pasa a través de todos los pares de puntos y se obtiene el que de menos error 
    t = []
    posi = []
    d_aux = 10000000
    for i in range(len(x)):
        t.append([i])
        posi.append([x[i], i])
    t = np.array(t)

    for n in range(len(x)):
        for nn in range(len(x)):
            if nn > n:
                tD = []
                dc = 0
                xp = [x[n], x[nn]]
                tp = [n, nn]
                #print(xp, tp)
                X = []
                for val in tp:
                    X.append([val])
                X = np.array(X)
                regr = LinearRegression()
                X_fit = np.arange(X.min(), X.max() + 2, 1)[:, np.newaxis]
                regr = regr.fit(X, xp)

                param_l = [regr.intercept_, regr.coef_[0]]

                pred_pos = []
                for t_p in range(len(x)):
                    x_p = param_l[0] + param_l[1] * t_p
                    pred_pos.append([x_p, t_p])
                TP = []
                XP = []
                for p in pred_pos:
                    XP.append(p[0])
                    TP.append(p[1])

                for pos in range(len(posi)):
                    d = math.sqrt((posi[pos][0] - pred_pos[pos][0]) ** 2 + (posi[pos][1] - pred_pos[pos][1]) ** 2)
                    dc += d
                    tD.append(d)
                if dc < d_aux:
                    d_aux = dc
                    tDaux = tD
                    TP_AUX = TP
                    XP_AUX = XP
                    tp_aux = tp
                    xp_aux = xp
                    param_l_AUX = param_l

    # La parte comentada es para ver las gráficas de como va haciendo el análisis de cada par de puntos
                """
                labelsPM = ["PM " + str(tp[0]), "PM " + str(tp[1])]
                
                plt.plot(t, x, linewidth=3, color='blue')
                plt.scatter(t, x, label='Cluster de posiciones (CP)', s=15, color='blue')
                plt.scatter(tp, xp, s=90, label='Puntos para construir el modelo', color='green')

                for ep in range(len(t)):
                    if ep not in tp:
                        plt.plot([t[ep][0], TP[ep]], [x[ep], XP[ep]], color="green")

                
                for ep in range(len(t)):
                    if ep == 0:
                        plt.plot([t[ep], TP[ep]], [x[ep], XP[ep]], label="Errores a cada posición", color="green")
                    else:
                        plt.plot([t[ep], TP[ep]], [x[ep], XP[ep]], color="green")
                    if ep not in tp:
                        #plt.rcParams["text.usetex"] = True
                        texto = "et"
                        if ep != 1 and ep != 5 and ep != 8:
                            plt.text((t[ep] + TP[ep]) / 2 + 0.25, (x[ep] + XP[ep]) / 2, texto, fontsize=14)
                        elif ep == 1:
                            plt.text((t[ep] + TP[ep]) / 2 + 0.25, (x[ep] + XP[ep]) / 2 - 1.5, texto, fontsize=14)
                        elif ep == 5:
                            plt.text((t[ep] + TP[ep]) / 2 - 0.38, (x[ep] + XP[ep]) / 2, texto, fontsize=14)
                        elif ep == 8:
                            plt.text((t[ep] + TP[ep]) / 2 + 0.05, (x[ep] + XP[ep]) / 2, texto, fontsize=14)
                # plt.scatter([9, 10, 11], new_pre, s=10, label='training points', color='orange')
                """
                #plt.scatter(TP, XP, label="Predicciones de posiciones (PP)", s=15, color='red')
                #plt.plot(TP, XP, color='red')

                """
                for tpi in range(len(tp)):
                    if tpi == 0:
                        plt.text(tp[tpi], xp[tpi], labelsPM[tpi], fontsize=14)
                    else:
                        plt.text(tp[tpi] - 0.35, xp[tpi] + 1, labelsPM[tpi], fontsize=14)
                plt.plot(TP, XP, color='red')
                """
                #plt.xlabel('t', fontsize=14, fontweight='bold')
                #plt.ylabel('z(t)', fontsize=14, fontweight='bold')
                #plt.tick_params(axis="x", labelsize=11.5)
                #plt.tick_params(axis="y", labelsize=11.5)

                #plt.legend()
                #plt.savefig("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RANSAC_LINEA/" + str(tp[0]) + str(
                #    tp[1]) + ".jpg")
                #plt.clf()
            #plt.show()
            #"""

    return param_l_AUX, tDaux

def RANSAC_ZERO(x):
    # Aplica RANSAC para un modelo de grado 0, se pasa a través de cada punto y se obtiene el que de menos error
    t = []
    posi = []
    d_aux = 10000000
    for i in range(len(x)):
        t.append([i])
        posi.append([x[i], i])
    pred_pos = []
    for i in x:
        dc = 0
        for j in range(len(x)):
            pred_pos.append([i, j])
        for pos in range(len(posi)):
            d = math.sqrt((posi[pos][0] - pred_pos[pos][0]) ** 2 + (posi[pos][1] - pred_pos[pos][1]) ** 2)
            dc += d
        if dc < d_aux:
            d_aux = dc
            param_z_AUX = [i]
    return param_z_AUX

def RANSAC_QUAD(x):
    # Aplica RANSAC para un modelo de grado 2, se pasa a través de la combinación de puntos (3 puntos) posibles 
    # y cuya combinación no se repita y se obtiene el que de menos error
    t = []
    posi = []
    d_aux = 10000000
    for i in range(len(x)):
        t.append([i])
        posi.append([x[i], i])
    t = np.array(t)
    allData = []

    for i in range(len(t)-2):
        for j in range(i + 1, len(t)-1):
            for k in range(j + 1, len(t)):
                tD = []
                dc = 0
                xp = [x[i], x[j], x[k]]
                tp = [i, j, k]
                X = []
                for val in tp:
                    X.append([val])
                X = np.array(X)
                ################################################################
                regr = LinearRegression()
                quadratic = PolynomialFeatures(degree=2, include_bias=False)
                X_quad = quadratic.fit_transform(X)

                X_fit = np.arange(X.min(), X.max() + 2, 1)[:, np.newaxis]

                regr = regr.fit(X_quad, xp)
                param_q = [regr.intercept_, regr.coef_[0], regr.coef_[1]]

                pred_pos = []
                for t_p in range(len(x)):
                    x_p = param_q[0] + param_q[1] * t_p + param_q[2] * t_p ** 2
                    pred_pos.append([x_p, t_p])
                TP = []
                XP = []
                for p in pred_pos:
                    XP.append(p[0])
                    TP.append(p[1])

                for pos in range(len(posi)):
                    d = math.sqrt((posi[pos][0] - pred_pos[pos][0]) ** 2 + (posi[pos][1] - pred_pos[pos][1]) ** 2)
                    #print(d)
                    dc += d
                    tD.append(d)
                allData.append([str(i) + str(j) + str(k), xp, tp, XP, TP, dc])

                if dc < d_aux:
                    d_aux = dc
                    sec = [i, j, k]
                    tDaux = tD
                    TP_AUX = TP
                    XP_AUX = XP
                    tp_aux = tp
                    xp_aux = xp
                    param_q_AUX = param_q
    # La parte comentada es para ver las gráficas de como va haciendo el análisis de cada conjunto de puntos
    """
                labelsPM = ["PM " + str(tp[0]), "PM " + str(tp[1]), "PM " + str(tp[2])]
                plt.plot(t, x, linewidth=3, label="Puntos Asociados (PA)", color='blue')
                plt.scatter(t, x, s=30, color='blue')

                for ep in range(len(t)):
                    if ep == 0:
                        plt.plot([t[ep], TP[ep]], [x[ep], XP[ep]], label="Errores a cada posición", color="green")
                    else:
                        plt.plot([t[ep], TP[ep]], [x[ep], XP[ep]], color="green")
                    if ep not in tp:
                        if ep != 3 and ep != 5 and ep != 7:
                            plt.text((t[ep] + TP[ep])/2 + 0.25, (x[ep] + XP[ep])/2, "et", fontsize=14)
                        elif ep == 3:
                            plt.text((t[ep] + TP[ep]) / 2 - 0.32, (x[ep] + XP[ep]) / 2 + 0.2, "et", fontsize=12)
                        elif ep == 5:
                            plt.text((t[ep] + TP[ep]) / 2 + 0.15, (x[ep] + XP[ep]) / 2, "et", fontsize=14)
                        elif ep == 7:
                            plt.text((t[ep] + TP[ep]) / 2 , (x[ep] + XP[ep]) / 2 + 0.22, "et", fontsize=12)

                # plt.scatter([9, 10, 11], new_pre, s=10, label='training points', color='orange')

                plt.scatter(TP, XP, s=35, label="Puntos del modelo (PM)", color='red')
                plt.scatter(tp, xp, s=35, color='black', label="Puntos para construir el modelo")
                for tpi in range(len(tp)):
                    plt.text(tp[tpi], xp[tpi], labelsPM[tpi], fontsize=14)
                plt.plot(TP, XP, linewidth=3, color='red')

                plt.xlabel('t', fontsize=14, fontweight='bold')
                plt.ylabel('x(t)', fontsize=14, fontweight='bold')
                plt.tick_params(axis="x", labelsize=11.5)
                plt.tick_params(axis="y", labelsize=11.5)
                plt.legend()

                plt.savefig("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RANSAC_QUAD/" + str(tp[0]) + str(tp[1]) + str(tp[2]) +".jpg")
                plt.clf()
                #plt.show()


    #new_pre = [196, 209, 221]
    #dt = 0
    #for pos in range(len(new_pre)):
    #    d = math.sqrt((new_pre[pos] - XP_AUX[pos + 9]) ** 2)
    #    dt += d
    #    print(d)
    #print(dt)
    #plt.plot(t, x, label='training points', color='blue')
    #plt.scatter(t, x, s=10, label='training points', color='black')

    #plt.scatter([9, 10, 11], new_pre, s=10, label='training points', color='orange')

    #plt.scatter(TP_AUX, XP_AUX, s=35, label='training points', color='red')
    #plt.scatter(tp_aux, xp_aux, s=35, label='training points', color='green')
    #plt.plot(TP_AUX, XP_AUX, label='training points', color='red')

    #plt.savefig("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RANSAC_QUAD/foto" + str(i) + ".jpg")
    #plt.clf()
    #plt.show()
    """

    return param_q_AUX

def orderData(posiciones, t):
    x, y = [], []
    for i in posiciones:
        x.append(i[0])
        y.append(i[1])

    # Calcula Ransac para una linea (para X y para Y)
    XX, ex = Ransac_l(x)
    
    XX = XX[::-1]
    YY, ey = Ransac_l(y)
    YY = YY[::-1]

    # Si se detecta un outlier, se calculan los modelos de regresion lineal (para X y para Y)
    def valor_mas_alto(arr, umbral):
        return any(x > umbral for x in arr)
    if valor_mas_alto(ex, 5):
        XX, YYx = AIC(posiciones, len(posiciones))

    if valor_mas_alto(ey, 5):
        XXx, YY = AIC(posiciones, len(posiciones))

    # Los variables XX y YY contienen los parametros del modelo (2 para un modelo lineal, 3 para un modelo de curva)
    # se obtienen las predicciones en el tiempo "t" 
    #XX, YY = AIC(posiciones, len(posiciones))
    pos = get_pred(XX, YY, t)
    
    #pos = []
    #YY = []
    return pos, XX, YY

def get_pred(XX, YY, t):

    
    if len(XX) == 2:
        x = XX[1] + XX[0] * t
        labelx = "X_lineal"
    elif len(XX) == 3:
        x = XX[2] + XX[1] * t + XX[0] * t ** 2
        labelx = "X_cuadrado"
    elif len(XX) == 1:
        x = XX[0]
        labelx = "X_Zero"
    if len(YY) == 2:
        y = YY[1] + YY[0] * t
        labely = "Y_lineal"
    elif len(YY) == 3:
        y = YY[2] + YY[1] * t + YY[0] * t ** 2
        labely = "Y_cuadrado"
    elif len(YY) == 1:
        y = YY[0]
        labely = "Y_Zero"
    pos = [x, y]
    """
    for tt in range(t+3):
        if len(XX) == 2:
            x = XX[1] + XX[0] * tt
            vxi = XX[0]
            labelx = "X_lineal"
        elif len(XX) == 3:
            x = XX[2] + XX[1] * t + XX[0] * t ** 2
            vxi = XX[1] + 2 * XX[0] * tt
            labelx = "X_cuadrado"
        elif len(XX) == 1:
            x = XX[0]
            vxi = 0
            labelx = "X_Zero"
        if len(YY) == 2:
            y = YY[1] + YY[0] * t
            vyi = YY[0]
            labely = "Y_lineal"
        elif len(YY) == 3:
            y = YY[2] + YY[1] * t + YY[0] * t ** 2
            vyi = YY[1] + 2 * YY[0] ** tt
            labely = "Y_cuadrado"
        elif len(YY) == 1:
            y = YY[0]
            vyi = 0
            labely = "Y_Zero"
        print("Vx: ", vxi, " Vy: ", vyi)
    """
    return pos

#posiciones = [[190, 400], [200, 400], [230, 400], [270, 400], [245, 400.0], [230, 400.0], [250., 400.0], [350, 400], [245, 400]]
#x = []

#for i in posiciones:
#    x.append(i[0])

#pp = orderData(posiciones, len(posiciones))
#pp = orderData(posiciones, 9)
#print(pp)