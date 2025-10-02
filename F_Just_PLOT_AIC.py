from F_AIC import AIC

def orderData(posiciones):
    XX, YY = AIC(posiciones, len(posiciones))

    pos = get_pred(XX, YY, posiciones)
    return pos, XX, YY


def get_pred(XX, YY, posiciones):
    tt = len(posiciones)
    pos = []
    print("T ", tt)
    for t in range(tt):
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

    return pos

#posiciones = [[190, 400], [200, 400], [210, 400], [220, 400], [229.99999999999983, 400.0], [239.99999999999983, 400.0], [249.99999999999983, 400.0], [260, 400], [270, 400]]
#pp = orderData(posiciones)
#print(pp)