import matplotlib.pyplot as plt

def graficar(POS, AIC, RAN, MED, PRED, PREDT1, PREDT2, PREDT3, KAL, KALT1, KALT2, KALT3, folder):
    for n_obj in range(len(POS)):
        e0, e1, e2, e3, et = [], [], [], [], []
        e0k, e1k, e2k, e3k = [], [], [], []
        eA0, eA1, eA2, eA3 = [], [], [], []
        eA0k, eA1k, eA2k, eA3k = [], [], [], []
        error_A0, error_A1, error_A2, error_A3 = 0, 0, 0, 0
        error_A0K, error_A1K, error_A2K, error_A3K = 0, 0, 0, 0
        for n_clus in range(len(POS[n_obj])):
            if n_clus > 4 and n_clus <= len(POS[n_obj]) - 7:
                x, y, xAIC, yAIC, xRAN, yRAN, t = [], [], [], [], [], [], []
                xt, yt, tt = [], [], []
                xp, yp, tp = [], [], []
                xk, yk = [], []
                
                

                if n_clus == 5:
                    xt.append(MED[n_obj][5][0])
                    xt.append(MED[n_obj][6][0])
                    xt.append(MED[n_obj][7][0])
                    xt.append(MED[n_obj][8][0])

                    yt.append(MED[n_obj][5][1])
                    yt.append(MED[n_obj][6][1])
                    yt.append(MED[n_obj][7][1])
                    yt.append(MED[n_obj][8][1])

                    xp.append(PRED[n_obj][5][0])
                    xp.append(PREDT1[n_obj][5][0])
                    xp.append(PREDT2[n_obj][5][0])
                    xp.append(PREDT3[n_obj][5][0])

                    yp.append(PRED[n_obj][5][1])
                    yp.append(PREDT1[n_obj][5][1])
                    yp.append(PREDT2[n_obj][5][1])
                    yp.append(PREDT3[n_obj][5][1])

                    xk.append(KAL[n_obj][5][0])
                    xk.append(KALT1[n_obj][5][0])
                    xk.append(KALT2[n_obj][5][0])
                    xk.append(KALT3[n_obj][5][0])

                    yk.append(KAL[n_obj][5][1])
                    yk.append(KALT1[n_obj][5][1])
                    yk.append(KALT2[n_obj][5][1])
                    yk.append(KALT3[n_obj][5][1])

                    tp.append(5)
                    tp.append(6)
                    tp.append(7)
                    tp.append(8)

                    tt.append(5)
                    tt.append(6)
                    tt.append(7)
                    tt.append(8)

                    ee0 = ((MED[n_obj][5][0] - PRED[n_obj][5][0]) ** 2 + (MED[n_obj][5][1] - PRED[n_obj][5][1]) ** 2) * (1 / 30)
                    ee1 = ((MED[n_obj][6][0] - PREDT1[n_obj][5][0]) ** 2 + (MED[n_obj][6][1] - PREDT1[n_obj][5][1]) ** 2) * (1 / 30)
                    ee2 = ((MED[n_obj][7][0] - PREDT2[n_obj][5][0]) ** 2 + (MED[n_obj][7][1] - PREDT2[n_obj][5][1]) ** 2) * (1 / 30)
                    ee3 = ((MED[n_obj][8][0] - PREDT3[n_obj][5][0]) ** 2 + (MED[n_obj][8][1] - PREDT3[n_obj][5][1]) ** 2) * (1 / 30)

                    ee0k = ((MED[n_obj][5][0] - KAL[n_obj][5][0]) ** 2 + (MED[n_obj][5][1] - KAL[n_obj][5][1]) ** 2) * (1 / 30)
                    ee1k = ((MED[n_obj][6][0] - KALT1[n_obj][5][0]) ** 2 + (MED[n_obj][6][1] - KALT1[n_obj][5][1]) ** 2) * (1 / 30)
                    ee2k = ((MED[n_obj][7][0] - KALT2[n_obj][5][0]) ** 2 + (MED[n_obj][7][1] - KALT2[n_obj][5][1]) ** 2) * (1 / 30)
                    ee3k = ((MED[n_obj][8][0] - KALT3[n_obj][5][0]) ** 2 + (MED[n_obj][8][1] - KALT3[n_obj][5][1]) ** 2) * (1 / 30)

                    e0.append(ee0)
                    e1.append(ee1)
                    e2.append(ee2)
                    e3.append(ee3)

                    e0k.append(ee0k)
                    e1k.append(ee1k)
                    e2k.append(ee2k)
                    e3k.append(ee3k)

                    et.append(n_clus)

                    error_A0 += ee0
                    error_A1 += ee1
                    error_A2 += ee2
                    error_A3 += ee3

                    error_A0K += ee0k
                    error_A1K += ee1k
                    error_A2K += ee2k
                    error_A3K += ee3k

                    eA0.append(error_A0)
                    eA1.append(error_A1)
                    eA2.append(error_A2)
                    eA3.append(error_A3)

                    eA0k.append(error_A0K)
                    eA1k.append(error_A1K)
                    eA2k.append(error_A2K)
                    eA3k.append(error_A3K)

                elif n_clus == 6:
                    xt.append(MED[n_obj][6][0])
                    xt.append(MED[n_obj][7][0])
                    xt.append(MED[n_obj][8][0])
                    xt.append(MED[n_obj][9][0])

                    yt.append(MED[n_obj][6][1])
                    yt.append(MED[n_obj][7][1])
                    yt.append(MED[n_obj][8][1])
                    yt.append(MED[n_obj][9][1])

                    xp.append(PRED[n_obj][6][0])
                    xp.append(PREDT1[n_obj][6][0])
                    xp.append(PREDT2[n_obj][6][0])
                    xp.append(PREDT3[n_obj][6][0])

                    yp.append(PRED[n_obj][6][1])
                    yp.append(PREDT1[n_obj][6][1])
                    yp.append(PREDT2[n_obj][6][1])
                    yp.append(PREDT3[n_obj][6][1])

                    xk.append(KAL[n_obj][6][0])
                    xk.append(KALT1[n_obj][6][0])
                    xk.append(KALT2[n_obj][6][0])
                    xk.append(KALT3[n_obj][6][0])

                    yk.append(KAL[n_obj][6][1])
                    yk.append(KALT1[n_obj][6][1])
                    yk.append(KALT2[n_obj][6][1])
                    yk.append(KALT3[n_obj][6][1])

                    tp.append(6)
                    tp.append(7)
                    tp.append(8)
                    tp.append(9)

                    tt.append(6)
                    tt.append(7)
                    tt.append(8)
                    tt.append(9)

                    ee0 = ((MED[n_obj][6][0] - PRED[n_obj][6][0]) ** 2 + (MED[n_obj][6][1] - PRED[n_obj][6][1]) ** 2) * (1 / 30)
                    ee1 = ((MED[n_obj][7][0] - PREDT1[n_obj][6][0]) ** 2 + (MED[n_obj][7][1] - PREDT1[n_obj][6][1]) ** 2) * (1 / 30)
                    ee2 = ((MED[n_obj][8][0] - PREDT2[n_obj][6][0]) ** 2 + (MED[n_obj][8][1] - PREDT2[n_obj][6][1]) ** 2) * (1 / 30)
                    ee3 = ((MED[n_obj][9][0] - PREDT3[n_obj][6][0]) ** 2 + (MED[n_obj][9][1] - PREDT3[n_obj][6][1]) ** 2) * (1 / 30)

                    ee0k = ((MED[n_obj][6][0] - KAL[n_obj][6][0]) ** 2 + (MED[n_obj][6][1] - KAL[n_obj][6][1]) ** 2) * (1 / 30)
                    ee1k = ((MED[n_obj][7][0] - KALT1[n_obj][6][0]) ** 2 + (MED[n_obj][7][1] - KALT1[n_obj][6][1]) ** 2) * (1 / 30)
                    ee2k = ((MED[n_obj][8][0] - KALT2[n_obj][6][0]) ** 2 + (MED[n_obj][8][1] - KALT2[n_obj][6][1]) ** 2) * (1 / 30)
                    ee3k = ((MED[n_obj][9][0] - KALT3[n_obj][6][0]) ** 2 + (MED[n_obj][9][1] - KALT3[n_obj][6][1]) ** 2) * (1 / 30)

                    e0.append(ee0)
                    e1.append(ee1)
                    e2.append(ee2)
                    e3.append(ee3)

                    e0k.append(ee0k)
                    e1k.append(ee1k)
                    e2k.append(ee2k)
                    e3k.append(ee3k)

                    et.append(n_clus)

                    error_A0 += ee0
                    error_A1 += ee1
                    error_A2 += ee2
                    error_A3 += ee3

                    error_A0K += ee0k
                    error_A1K += ee1k
                    error_A2K += ee2k
                    error_A3K += ee3k

                    eA0.append(error_A0)
                    eA1.append(error_A1)
                    eA2.append(error_A2)
                    eA3.append(error_A3)

                    eA0k.append(error_A0K)
                    eA1k.append(error_A1K)
                    eA2k.append(error_A2K)
                    eA3k.append(error_A3K)

                elif n_clus == 7:
                    xt.append(MED[n_obj][7][0])
                    xt.append(MED[n_obj][8][0])
                    xt.append(MED[n_obj][9][0])
                    xt.append(MED[n_obj][10][0])

                    yt.append(MED[n_obj][7][1])
                    yt.append(MED[n_obj][8][1])
                    yt.append(MED[n_obj][9][1])
                    yt.append(MED[n_obj][10][1])

                    xp.append(PRED[n_obj][7][0])
                    xp.append(PREDT1[n_obj][7][0])
                    xp.append(PREDT2[n_obj][7][0])
                    xp.append(PREDT3[n_obj][7][0])

                    yp.append(PRED[n_obj][7][1])
                    yp.append(PREDT1[n_obj][7][1])
                    yp.append(PREDT2[n_obj][7][1])
                    yp.append(PREDT3[n_obj][7][1])

                    xk.append(KAL[n_obj][7][0])
                    xk.append(KALT1[n_obj][7][0])
                    xk.append(KALT2[n_obj][7][0])
                    xk.append(KALT3[n_obj][7][0])

                    yk.append(KAL[n_obj][7][1])
                    yk.append(KALT1[n_obj][7][1])
                    yk.append(KALT2[n_obj][7][1])
                    yk.append(KALT3[n_obj][7][1])

                    tp.append(7)
                    tp.append(8)
                    tp.append(9)
                    tp.append(10)

                    tt.append(7)
                    tt.append(8)
                    tt.append(9)
                    tt.append(10)

                    ee0 = ((MED[n_obj][7][0] - PRED[n_obj][7][0]) ** 2 + (MED[n_obj][7][1] - PRED[n_obj][7][1]) ** 2) * (1 / 30)
                    ee1 = ((MED[n_obj][8][0] - PREDT1[n_obj][7][0]) ** 2 + (MED[n_obj][8][1] - PREDT1[n_obj][7][1]) ** 2) * (1 / 30)
                    ee2 = ((MED[n_obj][9][0] - PREDT2[n_obj][7][0]) ** 2 + (MED[n_obj][9][1] - PREDT2[n_obj][7][1]) ** 2) * (1 / 30)
                    ee3 = ((MED[n_obj][10][0] - PREDT3[n_obj][7][0]) ** 2 + (MED[n_obj][10][1] - PREDT3[n_obj][7][1]) ** 2) * (1 / 30)

                    ee0k = ((MED[n_obj][7][0] - KAL[n_obj][7][0]) ** 2 + (MED[n_obj][7][1] - KAL[n_obj][7][1]) ** 2) * (1 / 30)
                    ee1k = ((MED[n_obj][8][0] - KALT1[n_obj][7][0]) ** 2 + (MED[n_obj][8][1] - KALT1[n_obj][7][1]) ** 2) * (1 / 30)
                    ee2k = ((MED[n_obj][9][0] - KALT2[n_obj][7][0]) ** 2 + (MED[n_obj][9][1] - KALT2[n_obj][7][1]) ** 2) * (1 / 30)
                    ee3k = ((MED[n_obj][10][0] - KALT3[n_obj][7][0]) ** 2 + (MED[n_obj][10][1] - KALT3[n_obj][7][1]) ** 2) * (1 / 30)

                    e0.append(ee0)
                    e1.append(ee1)
                    e2.append(ee2)
                    e3.append(ee3)

                    e0k.append(ee0k)
                    e1k.append(ee1k)
                    e2k.append(ee2k)
                    e3k.append(ee3k)

                    et.append(n_clus)

                    error_A0 += ee0
                    error_A1 += ee1
                    error_A2 += ee2
                    error_A3 += ee3

                    error_A0K += ee0k
                    error_A1K += ee1k
                    error_A2K += ee2k
                    error_A3K += ee3k

                    eA0.append(error_A0)
                    eA1.append(error_A1)
                    eA2.append(error_A2)
                    eA3.append(error_A3)

                    eA0k.append(error_A0K)
                    eA1k.append(error_A1K)
                    eA2k.append(error_A2K)
                    eA3k.append(error_A3K)

                elif n_clus == 8:
                    xt.append(MED[n_obj][8][0])
                    xt.append(MED[n_obj][9][0])
                    xt.append(MED[n_obj][10][0])
                    xt.append(MED[n_obj][11][0])

                    yt.append(MED[n_obj][8][1])
                    yt.append(MED[n_obj][9][1])
                    yt.append(MED[n_obj][10][1])
                    yt.append(MED[n_obj][11][1])

                    xp.append(PRED[n_obj][8][0])
                    xp.append(PREDT1[n_obj][8][0])
                    xp.append(PREDT2[n_obj][8][0])
                    xp.append(PREDT3[n_obj][8][0])

                    yp.append(PRED[n_obj][8][1])
                    yp.append(PREDT1[n_obj][8][1])
                    yp.append(PREDT2[n_obj][8][1])
                    yp.append(PREDT3[n_obj][8][1])

                    xk.append(KAL[n_obj][8][0])
                    xk.append(KALT1[n_obj][8][0])
                    xk.append(KALT2[n_obj][8][0])
                    xk.append(KALT3[n_obj][8][0])

                    yk.append(KAL[n_obj][8][1])
                    yk.append(KALT1[n_obj][8][1])
                    yk.append(KALT2[n_obj][8][1])
                    yk.append(KALT3[n_obj][8][1])

                    tp.append(8)
                    tp.append(9)
                    tp.append(10)
                    tp.append(11)

                    tt.append(8)
                    tt.append(9)
                    tt.append(10)
                    tt.append(11)

                    ee0 = ((MED[n_obj][8][0] - PRED[n_obj][8][0]) ** 2 + (MED[n_obj][8][1] - PRED[n_obj][8][1]) ** 2) * (1 / 30)
                    ee1 = ((MED[n_obj][9][0] - PREDT1[n_obj][8][0]) ** 2 + (MED[n_obj][9][1] - PREDT1[n_obj][8][1]) ** 2) * (1 / 30)
                    ee2 = ((MED[n_obj][10][0] - PREDT2[n_obj][8][0]) ** 2 + (MED[n_obj][10][1] - PREDT2[n_obj][8][1]) ** 2) * (1 / 30)
                    ee3 = ((MED[n_obj][11][0] - PREDT3[n_obj][8][0]) ** 2 + (MED[n_obj][11][1] - PREDT3[n_obj][8][1]) ** 2) * (1 / 30)

                    ee0k = ((MED[n_obj][8][0] - KAL[n_obj][8][0]) ** 2 + (MED[n_obj][8][1] - KAL[n_obj][8][1]) ** 2) * (1 / 30)
                    ee1k = ((MED[n_obj][9][0] - KALT1[n_obj][8][0]) ** 2 + (MED[n_obj][9][1] - KALT1[n_obj][8][1]) ** 2) * (1 / 30)
                    ee2k = ((MED[n_obj][10][0] - KALT2[n_obj][8][0]) ** 2 + (MED[n_obj][10][1] - KALT2[n_obj][8][1]) ** 2) * (1 / 30)
                    ee3k = ((MED[n_obj][11][0] - KALT3[n_obj][8][0]) ** 2 + (MED[n_obj][11][1] - KALT3[n_obj][8][1]) ** 2) * (1 / 30)

                    e0.append(ee0)
                    e1.append(ee1)
                    e2.append(ee2)
                    e3.append(ee3)

                    e0k.append(ee0k)
                    e1k.append(ee1k)
                    e2k.append(ee2k)
                    e3k.append(ee3k)

                    et.append(n_clus)

                    error_A0 += ee0
                    error_A1 += ee1
                    error_A2 += ee2
                    error_A3 += ee3

                    error_A0K += ee0k
                    error_A1K += ee1k
                    error_A2K += ee2k
                    error_A3K += ee3k

                    eA0.append(error_A0)
                    eA1.append(error_A1)
                    eA2.append(error_A2)
                    eA3.append(error_A3)

                    eA0k.append(error_A0K)
                    eA1k.append(error_A1K)
                    eA2k.append(error_A2K)
                    eA3k.append(error_A3K)

                elif n_clus >= 9 and n_clus <= len(POS[n_obj]) - 4:
                    xt.append(MED[n_obj][n_clus][0])
                    xt.append(MED[n_obj][n_clus + 1][0])
                    xt.append(MED[n_obj][n_clus + 2][0])
                    xt.append(MED[n_obj][n_clus + 3][0])

                    yt.append(MED[n_obj][n_clus][1])
                    yt.append(MED[n_obj][n_clus + 1][1])
                    yt.append(MED[n_obj][n_clus + 2][1])
                    yt.append(MED[n_obj][n_clus + 3][1])

                    xp.append(PRED[n_obj][n_clus][0])
                    xp.append(PREDT1[n_obj][n_clus][0])
                    xp.append(PREDT2[n_obj][n_clus][0])
                    xp.append(PREDT3[n_obj][n_clus][0])

                    yp.append(PRED[n_obj][n_clus][1])
                    yp.append(PREDT1[n_obj][n_clus][1])
                    yp.append(PREDT2[n_obj][n_clus][1])
                    yp.append(PREDT3[n_obj][n_clus][1])

                    xk.append(KAL[n_obj][n_clus][0])
                    xk.append(KALT1[n_obj][n_clus][0])
                    xk.append(KALT2[n_obj][n_clus][0])
                    xk.append(KALT3[n_obj][n_clus][0])

                    yk.append(KAL[n_obj][n_clus][1])
                    yk.append(KALT1[n_obj][n_clus][1])
                    yk.append(KALT2[n_obj][n_clus][1])
                    yk.append(KALT3[n_obj][n_clus][1])

                    tp.append(9)
                    tp.append(10)
                    tp.append(11)
                    tp.append(12)

                    tt.append(9)
                    tt.append(10)
                    tt.append(11)
                    tt.append(12)

                    ee0 = ((MED[n_obj][n_clus][0] - PRED[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus][1] - PRED[n_obj][n_clus][1]) ** 2) * (1 / 30)
                    ee1 = ((MED[n_obj][n_clus + 1][0] - PREDT1[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus + 1][1] - PREDT1[n_obj][n_clus][1]) ** 2) * (1 / 30)
                    ee2 = ((MED[n_obj][n_clus + 2][0] - PREDT2[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus + 2][1] - PREDT2[n_obj][n_clus][1]) ** 2) * (1 / 30)
                    ee3 = ((MED[n_obj][n_clus + 3][0] - PREDT3[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus + 3][1] - PREDT3[n_obj][n_clus][1]) ** 2) * (1 / 30)

                    ee0k = ((MED[n_obj][n_clus][0] - KAL[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus][1] - KAL[n_obj][n_clus][1]) ** 2) * (1 / 30)
                    ee1k = ((MED[n_obj][n_clus + 1][0] - KALT1[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus + 1][1] - KALT1[n_obj][n_clus][1]) ** 2) * (1 / 30)
                    ee2k = ((MED[n_obj][n_clus + 2][0] - KALT2[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus + 2][1] - KALT2[n_obj][n_clus][1]) ** 2) * (1 / 30)
                    ee3k = ((MED[n_obj][n_clus + 3][0] - KALT3[n_obj][n_clus][0]) ** 2 + (MED[n_obj][n_clus + 3][1] - KALT3[n_obj][n_clus][1]) ** 2) * (1 / 30)

                    e0.append(ee0)
                    e1.append(ee1)
                    e2.append(ee2)
                    e3.append(ee3)

                    e0k.append(ee0k)
                    e1k.append(ee1k)
                    e2k.append(ee2k)
                    e3k.append(ee3k)

                    et.append(n_clus)

                    error_A0 += ee0
                    error_A1 += ee1
                    error_A2 += ee2
                    error_A3 += ee3

                    error_A0K += ee0k
                    error_A1K += ee1k
                    error_A2K += ee2k
                    error_A3K += ee3k

                    eA0.append(error_A0)
                    eA1.append(error_A1)
                    eA2.append(error_A2)
                    eA3.append(error_A3)

                    eA0k.append(error_A0K)
                    eA1k.append(error_A1K)
                    eA2k.append(error_A2K)
                    eA3k.append(error_A3K)

                for n_pos in range(len(POS[n_obj][n_clus])):
                    # Posiciones
                    x.append(POS[n_obj][n_clus][n_pos][0])
                    y.append(POS[n_obj][n_clus][n_pos][1])

                    # Ransac
                    xRAN.append(RAN[n_obj][n_clus][n_pos][0])
                    yRAN.append(RAN[n_obj][n_clus][n_pos][1])

                    #AIC
                    xAIC.append(AIC[n_obj][n_clus][n_pos][0])
                    yAIC.append(AIC[n_obj][n_clus][n_pos][1])

                    t.append(n_pos)
                # Posiciones XY
                plt.scatter(x, y, s=25, color="blue", marker="o", label="pos")
                plt.plot(x, y, color="blue")
                plt.scatter(xAIC, yAIC, s=25, color="green", marker="o", label="AIC")
                plt.plot(xAIC, yAIC, color="green")
                plt.scatter(xRAN, yRAN, s=25, color="red", marker="o", label="RAN")
                plt.plot(xRAN, yRAN, color="red")
                plt.scatter(xt, yt, s=25, color="black", marker="o", label="RAN")
                plt.plot(xt, yt, color="black")
                plt.scatter(xp, yp, s=25, color="yellow", marker="o", label="RAN")
                plt.plot(xp, yp, color="yellow")
                plt.scatter(xk, yk, s=25, color="orange", marker="o", label="RAN")
                plt.plot(xk, yk, color="orange")
                plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/predicciones/pos_" + str(n_obj) + "_" + str(n_clus))
                plt.clf()

                # Posiciones X
                plt.scatter(t, x, s=25, color="blue", marker="o", label="pos")
                plt.plot(t, x, color="blue")
                plt.scatter(t, xAIC, s=25, color="green", marker="o", label="AIC")
                plt.plot(t, xAIC, color="green")
                plt.scatter(t, xRAN, s=25, color="red", marker="o", label="RAN")
                plt.plot(t, xRAN, color="red")
                plt.scatter(tt, xt, s=25, color="black", marker="o", label="RAN")
                plt.plot(tt, xt, color="black")
                plt.scatter(tp, xp, s=25, color="yellow", marker="o", label="RAN")
                plt.plot(tp, xp, color="yellow")
                plt.scatter(tp, xk, s=25, color="orange", marker="o", label="RAN")
                plt.plot(tp, xk, color="orange")
                plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/prediccionesXY/prediccionesX/pos_" + str(n_obj) + "_" + str(n_clus))
                plt.clf()

                # Posiciones Y
                plt.scatter(t, y, s=25, color="blue", marker="o", label="pos")
                plt.plot(t, y, color="blue")
                plt.scatter(t, yAIC, s=25, color="green", marker="o", label="AIC")
                plt.plot(t, yAIC, color="green")
                plt.scatter(t, yRAN, s=25, color="red", marker="o", label="RAN")
                plt.plot(t, yRAN, color="red")
                plt.scatter(tt, yt, s=25, color="black", marker="o", label="pos")
                plt.plot(tt, yt, color="black")
                plt.scatter(tp, yp, s=25, color="yellow", marker="o", label="pos")
                plt.plot(tp, yp, color="yellow")
                plt.scatter(tp, yk, s=25, color="orange", marker="o", label="pos")
                plt.plot(tp, yk, color="orange")
                plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/prediccionesXY/prediccionesY/pos_" + str(n_obj) + "_" + str(n_clus))
                plt.clf()

        # Error medicion y prediccion
        plt.plot(et, e0, color="blue")
        plt.plot(et, e0k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_e0")
        plt.clf()

        plt.plot(et, e1, color="blue")
        plt.plot(et, e1k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_e1")
        plt.clf()

        plt.plot(et, e2, color="blue")
        plt.plot(et, e2k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_e2")
        plt.clf()

        plt.plot(et, e3, color="blue")
        plt.plot(et, e3k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_e3")
        plt.clf()

        # Error acumulado medicion y prediccion
        plt.plot(et, eA0, color="blue")
        plt.plot(et, eA0k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_eA0")
        plt.clf()

        plt.plot(et, eA1, color="blue")
        plt.plot(et, eA1k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_eA1")
        plt.clf()

        plt.plot(et, eA2, color="blue")
        plt.plot(et, eA2k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_eA2")
        plt.clf()

        plt.plot(et, eA3, color="blue")
        plt.plot(et, eA3k, color="red")
        plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/errores/obj_" + str(n_obj) + "_eA3")
        plt.clf()
                

AIC = [[[0], [[0]], [[0]], [[0]], [[0]], [[1, 1]], [[2, 2], [3, 3]], [[4, 4], [5, 5], [6, 6]]]]
RAN = [[[0], [[0]], [[0]], [[0]], [[0]], [[1, 1]], [[2, 2], [3, 3]], [[4, 4], [5, 5], [6, 6]]]]
POS = [[[0], [[0]], [[0]], [[0]], [[0]], [[1, 1]], [[2, 2], [3, 3]], [[4, 4], [5, 5], [6, 6]]]]

#graficar(AIC, RAN, POS, "camila")