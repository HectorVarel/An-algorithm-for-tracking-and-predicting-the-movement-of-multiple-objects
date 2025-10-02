# Formulas para linealizar
def orderData(posiciones, XX, YY, t):

    if len(XX) == 2 or len(XX) == 1:
        XX = XX
    else:
        #XX = XX
        XX = [(XX[1] + (2 * XX[0] * len(posiciones))),
              XX[2] + XX[1] * (len(posiciones)) + XX[0] * (len(posiciones)) ** 2 - len(posiciones) * (
                      XX[1] + (2 * XX[0] * len(posiciones)))]

    if len(YY) == 2 or len(YY) == 1:
        YY = YY
    else:
        #YY = YY
        YY = [(YY[1] + (2 * YY[0] * len(posiciones))),
              YY[2] + YY[1] * (len(posiciones)) + YY[0] * (len(posiciones)) ** 2 - len(posiciones) * (
                      YY[1] + (2 * YY[0] * len(posiciones)))]

    pos = get_pred(XX, YY, t)
    return pos


def get_pred(XX, YY, t):
    if len(XX) == 3 or len(XX) == 2:
        x = XX[1] + XX[0] * t  
    elif len(XX) == 1:
        x = XX[0]
    if len(YY) == 3 or len(YY) == 2:  
        y = YY[1] + YY[0] * t
    elif len(YY) == 1:
        y = YY[0]
    pos = [x, y]

    return pos
