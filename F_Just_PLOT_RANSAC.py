from F_AIC import AIC
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import math


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
    # print(x)
    t = []
    posi = []
    d_aux = 10000000
    for i in range(len(x)):
        t.append([i])
        posi.append([x[i], i])
    t = np.array(t)
    allData = []
    key_dicc = []

    for n in range(len(x)):
        for nn in range(len(x)):
            if nn > n:
                # print(x[n], x[nn])
                tD = []
                tD2 = []
                dc = 0
                xp = [x[n], x[nn]]
                tp = [n, nn]
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
                    # print(d)
                    dc += d
                    tD.append(str(round(d, 2)))
                    tD2.append(d)
                # allData.append([str(i) + str(j) + str(k), xp, tp, XP, TP, dc])
                if dc < d_aux:
                    d_aux = dc
                    # sec = [i, j, k]
                    tDaux = tD
                    tDaux2 = tD2
                    TP_AUX = TP
                    XP_AUX = XP
                    tp_aux = tp
                    xp_aux = xp
                    param_l_AUX = param_l
                    # print("SECUENCIA", sec)
    """
            labelsPM = ["PM " + str(tp[0]), "PM " + str(tp[1])]
            plt.scatter(tp, xp, s=65, label='Puntos para construir el modelo', color='green')
            plt.plot(t, x, linewidth=3, color='blue')
            plt.scatter(t, x, label='Puntos Asociados (PA)', s=15, color='blue')
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

            plt.scatter(TP, XP, label="Puntos del modelo (PM)", s=15, color='red')


            for tpi in range(len(tp)):
                if tpi == 0:
                    plt.text(tp[tpi], xp[tpi], labelsPM[tpi], fontsize=14)
                else:
                    plt.text(tp[tpi] - 0.35, xp[tpi] + 1, labelsPM[tpi], fontsize=14)
            plt.plot(TP, XP, color='red')

            plt.xlabel('t', fontsize=14, fontweight='bold')
            plt.ylabel('x(t)', fontsize=14, fontweight='bold')
            plt.tick_params(axis="x", labelsize=11.5)
            plt.tick_params(axis="y", labelsize=11.5)

            plt.legend()
            plt.savefig("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RANSAC_LINEA/" + str(tp[0]) + str(
                tp[1]) + ".jpg")
            plt.clf()
            #plt.show()
            """

    return param_l_AUX, tDaux, tDaux2


def RANSAC_ZERO(x):
    # print(x)
    t = []
    posi = []
    d_aux = 10000000
    for i in range(len(x)):
        t.append([i])
        posi.append([x[i], i])
    # print(posi)
    pred_pos = []
    for i in x:
        dc = 0
        for j in range(len(x)):
            pred_pos.append([i, j])
        for pos in range(len(posi)):
            # print(posi[pos], pred_pos[pos])
            d = math.sqrt((posi[pos][0] - pred_pos[pos][0]) ** 2 + (posi[pos][1] - pred_pos[pos][1]) ** 2)
            # print(d)
            dc += d
        # allData.append([str(i) + str(j) + str(k), xp, tp, XP, TP, dc])
        if dc < d_aux:
            d_aux = dc
            param_z_AUX = [i]
            # print("RA", param_z_AUX)
    """
    for n in range(len(x)):
        tD = []
        dc = 0
        xp = [x[n]]
        tp = [n]
        X = []
        for val in tp:
            X.append([val])
        X = np.array(X)
        regr = LinearRegression()
        quadratic = PolynomialFeatures(degree=0)
        X_zero = quadratic.fit_transform(X)
        X_fit = np.arange(X.min(), X.max() + 2, 1)[:, np.newaxis]
        regr = regr.fit(X_zero, xp)

        param_z = [regr.intercept_]

        pred_pos = []
        for t_p in range(len(x)):
            x_p = param_z[0]
            pred_pos.append([x_p, t_p])
        TP = []
        XP = []
        for p in pred_pos:
            XP.append(p[0])
            TP.append(p[1])

        for pos in range(len(posi)):
            d = math.sqrt((posi[pos][0] - pred_pos[pos][0]) ** 2 + (posi[pos][1] - pred_pos[pos][1]) ** 2)
            # print(d)
            dc += d
            tD.append(d)
        #allData.append([str(i) + str(j) + str(k), xp, tp, XP, TP, dc])
        if dc < d_aux:
            d_aux = dc
            #sec = [i, j, k]
            tDaux = tD
            TP_AUX = TP
            XP_AUX = XP
            tp_aux = tp
            xp_aux = xp
            param_z_AUX = param_z
            # print("SECUENCIA", sec)
    """
    """
            labelsPM = ["PM " + str(tp[0]), "PM " + str(tp[1])]
            plt.scatter(tp, xp, s=65, label='Puntos para construir el modelo', color='green')
            plt.plot(t, x, linewidth=3, color='blue')
            plt.scatter(t, x, label='Puntos Asociados (PA)', s=15, color='blue')
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

            plt.scatter(TP, XP, label="Puntos del modelo (PM)", s=15, color='red')


            for tpi in range(len(tp)):
                if tpi == 0:
                    plt.text(tp[tpi], xp[tpi], labelsPM[tpi], fontsize=14)
                else:
                    plt.text(tp[tpi] - 0.35, xp[tpi] + 1, labelsPM[tpi], fontsize=14)
            plt.plot(TP, XP, color='red')

            plt.xlabel('t', fontsize=14, fontweight='bold')
            plt.ylabel('x(t)', fontsize=14, fontweight='bold')
            plt.tick_params(axis="x", labelsize=11.5)
            plt.tick_params(axis="y", labelsize=11.5)

            plt.legend()
            plt.savefig("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RANSAC_LINEA/" + str(tp[0]) + str(
                tp[1]) + ".jpg")
            plt.clf()
            #plt.show()
            """

    return param_z_AUX


def RANSAC_QUAD(x):
    t = []
    posi = []
    d_aux = 10000000
    for i in range(len(x)):
        t.append([i])
        posi.append([x[i], i])
    t = np.array(t)
    allData = []
    key_dicc = []

    for i in range(len(t) - 2):
        for j in range(i + 1, len(t) - 1):
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
                    # print(d)
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
                    # print("SECUENCIA", sec)
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

    """
    XX_AIC, YY_AIC = AIC(posiciones, len(posiciones))
    XX_AIC = [[], []]
    YY_AIC = [[], []]
    
    if len(XX_AIC) == 1:
        XX = Ransac_z(x)
    elif len(XX_AIC) == 2:
        XX, ex = Ransac_l(x)
        XX = XX[::-1]
    else:
        XX = Ransac_q(x)
        XX = XX[::-1]

    if len(YY_AIC) == 1:
        YY = Ransac_z(y)
    elif len(YY_AIC) == 2:
        YY, ey = Ransac_l(y)
        YY = YY[::-1]
    else:
        YY = Ransac_q(y)
        YY = YY[::-1]

    e = [ex, ey]
    """

    """
    XXl, exl, xldaux = Ransac_l(x)
    XXq, exq, xqdaux = Ransac_q(x)
    YYl, eyl, yldaux = Ransac_l(y)
    YYq, eyq, yqdaux = Ransac_q(y)

    #print("errores", xldaux, xqdaux, yldaux, yqdaux)

    def valor_mas_alto(arr, umbral):
        return any(x > umbral for x in arr)

    umbral = 5

    if exl < exq:
        if valor_mas_alto(xldaux, umbral):
            XX = XXl
            XX = XX[::-1]
            leg_x = "RANSAC"
        else:
            XX, YYx = AIC(posiciones, len(posiciones))
            #XX = XX[::-1]
            leg_x = "AIC"
    else:
        if valor_mas_alto(xqdaux, umbral):
            XX = XXq
            XX = XX[::-1]
            leg_x = "RANSAC"
        else:
            XX, YYx = AIC(posiciones, len(posiciones))
            #XX = XX[::-1]
            leg_x = "AIC"

    if eyl < eyq:
        if valor_mas_alto(yldaux, umbral):
            YY = YYl
            YY = YY[::-1]
            leg_y = "RANSAC"
        else:
            XXx, YY = AIC(posiciones, len(posiciones))
            #YY = YY[::-1]
            leg_y = "AIC"
    else:
        if valor_mas_alto(yqdaux, umbral):
            YY = YYq
            YY = YY[::-1]
            leg_y = "RANSAC"
        else:
            XXx, YY = AIC(posiciones, len(posiciones))
            #YY = YY[::-1]
            leg_y = "AIC"
    """

    # CASO 3
    XX, ex, exx = Ransac_l(x)
    XX = XX[::-1]
    YY, ey, eyy = Ransac_l(y)
    YY = YY[::-1]

    e = [ex, ey]
    """
    def valor_mas_alto(arr, umbral):
        return any(x > umbral for x in arr)

    if valor_mas_alto(exx, 5):
        XX, YYx = AIC(posiciones, len(posiciones))

    if valor_mas_alto(eyy, 5):
        XXx, YY = AIC(posiciones, len(posiciones))

    # XX, YY = AIC(posiciones, len(posiciones))
    """
    pos = get_pred(XX, YY, t)
    return pos, e

def print_vel(XXi, YYi, t):
    for i in range(t):
        if len(XXi) == 2:
            x = XXi[1] + XXi[0] * t
            vxi = XXi[0]
            labelx = "X_lineal"
        elif len(XXi) == 3:
            x = XXi[2] + XXi[1] * t + XXi[0] * t ** 2
            vxi = XXi[1] + 2 * XXi[0] * t
            labelx = "X_cuadrado"
        elif len(XXi) == 1:
            x = XXi[0]
            vxi = 0
            labelx = "X_Zero"
        if len(YYi) == 2:
            y = YYi[1] + YYi[0] * t
            vyi = YYi[0]
            labely = "Y_lineal"
        elif len(YYi) == 3:
            y = YYi[2] + YYi[1] * t + YYi[0] * t ** 2
            vyi = YYi[1] + 2 * YYi[0] ** t
            labely = "Y_cuadrado"
        elif len(YYi) == 1:
            y = YYi[0]
            vyi = 0
            labely = "Y_Zero"
        print("Vx: ", vxi, " Vy: ", vyi)

def get_pred(XX, YY, tt):
    pos = []
    for t in range(tt):
        #print("T ", t)
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
        pos.append([x, y])
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

#posiciones = [[190, 400], [200, 400], [210, 400], [220, 400], [229.99999999999983, 400.0], [239.99999999999983, 400.0], [249.99999999999983, 400.0], [260, 400], [270, 400]]
#pp = orderData(posiciones)
#print(pp)