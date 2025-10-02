from F_asociacion import itera as asociacion
from F_pred_kalman import Filtro as kf
from F_pred_kalman import Filtro_no_measure as kf2
from F_pred_AIC2 import orderData as g_pred
from F_pred_AIC_lineal2 import orderData as g_pred_lin
from F_Just_PLOT_AIC import orderData as PLOT_AIC
from F_Just_PLOT_RANSAC import orderData as PLOT_RANSAC
from F_comparar_AIC_RAN import graficar
import matplotlib.pyplot as plt
import cv2
import os
import random
import torch
import math
import copy
import csv

colores = []
for i in range(15000):
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    colores.append([a, b, c])


# Todos estos arreglos son para guardar los valores de las mediciones, prediciones (AIC, RANSAC, KALMAN) y mas datos
# para la obtención de las gráficas de posición, errores, etc. 
med = []
med_totales = []
fmed = []
fmed_totales = []

med_clus = []
med_totales_clus = []
fmed_clus = []
fmed_clus_totales = []

posiciones_fil = []
posiciones_totales_fil = []
fposiciones_fil = []
fposiciones_fil_totales = []

posiciones_fil_nc = []
posiciones_totales_fil_nc = []
fposiciones_fil_nc = []
fposiciones_fil_nc_totales = []

posiciones_AIC = []
posiciones_totales_AIC = []
fmed_AIC = []
fmed_AIC_totales = []

posiciones_RAN = []
posiciones_totales_RAN = []
fmed_RAN = []
fmed_RAN_totales = []

pred_alg = []
pred_totales_alg = []
fpred_alg = []
fpred_alg_totales = []

pred_alg_t1 = []
pred_totales_alg_t1 = []
fpred_alg_t1 = []
fpred_alg_t1_totales = []

pred_alg_t2 = []
pred_totales_alg_t2 = []
fpred_alg_t2 = []
fpred_alg_t2_totales = []

pred_alg_t3 = []
pred_totales_alg_t3 = []
fpred_alg_t3 = []
fpred_alg_t3_totales = []

pred_kal = []
pred_totales_kal = []
fpred_kal = []
fpred_kal_totales = []

pred_kal_t1 = []
pred_totales_kal_t1 = []
fpred_kal_t1 = []
fpred_kal_t1_totales = []

pred_kal_t2 = []
pred_totales_kal_t2 = []
fpred_kal_t2 = []
fpred_kal_t2_totales = []

pred_kal_t3 = []
pred_totales_kal_t3 = []
fpred_kal_t3 = []
fpred_kal_t3_totales = []

velocidades = []
velocidades_totales = []

nd_posiciones = []
nd_aux_posiciones = []
parametrosX = []
parametrosY = []
p_upd = []
x_upd = []
Q = []

# Tamaño para considerar un cluster
tc = 5
c = 0
m = 50

# Modelo de yolo
model = torch.hub.load("ultralytics/yolov5", "custom", "C:/Users/varel/Documents/MCR/3/Seminario de tesis/Zebrafish detection/resize/model/yolov5s.pt")

numero_caso = 5

if numero_caso == 1:
    # CAMILA 1 (video a analizar)
    capture = cv2.VideoCapture("C:/Users/varel/Documents/MCR/4/Seminario de tesis/carros/C5/camila_1.mp4")
    folder = "camila"
    # Frames entre los que se hace el análisis
    ci = 10
    cf = 100
    # Frames en los que no hay mediciones (para estos experimentos, siempre hay mediciones, pero quito entre el frame 30-40 para
    # poder probar al completo el algoritmo)
    # Si se quiere omitir, puede poner los valores ndi y ndf con el mismo valor para que siempre haya detecciones
    ndi = 30
    ndf = 40

elif numero_caso == 2:
    # CAMILA 1 (video a analizar)
    capture = cv2.VideoCapture("C:/Users/varel/Documents/MCR/4/Seminario de tesis/carros/C5/camila_1.mp4")
    folder = "camila_completo"
    # Frames entre los que se hace el análisis
    ci = 10
    cf = 100
    # Frames en los que no hay mediciones (para estos experimentos, siempre hay mediciones, pero quito entre el frame 30-40 para
    # poder probar al completo el algoritmo)
    # Si se quiere omitir, puede poner los valores ndi y ndf con el mismo valor para que siempre haya detecciones
    ndi = 40
    ndf = 40
elif numero_caso == 3:
    
    capture = cv2.VideoCapture("C:/Users/varel/Documents/MCR/4/Seminario de tesis/carros/C5/cruce_1.mp4")
    folder = "cruce1_NS"
    ci = 0
    cf = 200

    ndi = 130
    ndf = 150
elif numero_caso == 4:
    
    capture = cv2.VideoCapture("C:/Users/varel/Documents/MCR/4/Seminario de tesis/carros/C5/cruce_2.mp4")
    folder = "cruce2_NS"
    ci = 0
    cf = 200

    ndi = 47
    ndf = 105

elif numero_caso == 5:
    
    capture = cv2.VideoCapture("C:/Users/varel/Documents/MCR/4/Seminario de tesis/carros/C5/curvas.mp4")
    folder = "curvas_NS"
    ci = 50
    cf = 250

    ndi = 105
    ndf = 105


while c < cf:
    print("Frame: ", c)
    ret, frames = capture.read()
    frames = cv2.resize(frames, (640, 480))
    if c < cf and c > ci:
        alto, ancho, canales = frames.shape
        detect = model(frames)
        # En el primer frame, se inicializan los arreglos
        if c == ci + 1:
            d = []
            # Detecciones con Yolo
            labels, cord_thres = detect.xyxyn[0][:, -1].numpy(), detect.xyxyn[0][:, :-1].numpy()
            for i in range(len(cord_thres)):
                if int(labels[i]) == 0:
                    x_min = cord_thres[i][0]
                    x_max = cord_thres[i][2]
                    y_min = cord_thres[i][1]
                    y_max = cord_thres[i][3]
                    cx = (x_min * ancho) + ((ancho * (x_max - x_min)) / 2)
                    cy = (y_min * alto) + ((alto * (y_max - y_min)) / 2)
                    d.append([cx, cy])
            for cd in d:
                # Inicializo los arreglos para los objetos detectados en el primer frame
                nd_posiciones.append(0)
                nd_aux_posiciones.append(10)

                # Parametros de AIC
                parametrosX.append([0, 0])
                parametrosY.append([0, 0])

                # Parametros para kalman
                velocidades.append([[0, 0]])
                p_upd.append([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
                x_upd.append([cd[0], cd[1], 0, 0])
                Q.append([20, 100])

                # Cluster con 10 posiciones (como no hay 10 posiciones, solo agrego un arreglo, al final esto no influye
                # pues estos arreglos se descartan)
                med_clus.append([[0]])
                
                # Frame en el que se juntan esas 10 detecciones
                fmed_clus.append([c])

                # Se agrega la medición encontrada por Yolo
                med.append([cd])

                # Frame de la detección
                fmed.append([c])

                # Posiciones filtadas (Ya no se uso)
                posiciones_fil.append([[0]])
                fposiciones_fil.append([c])

                posiciones_fil_nc.append([cd])
                fposiciones_fil_nc.append([c])

                # Predicciones con AIC para graficar su comportamiento
                posiciones_AIC.append([[0]])
                fmed_AIC.append([c])

                # Predicciones con RANSAC para graficar su comportamiento
                posiciones_RAN.append([[0]])
                fmed_RAN.append([c])

                # Predicciones del algoritmo en t0, t1, t2 y t3 (puede ser AIC o RANSAC)
                pred_alg.append([cd])
                pred_alg_t1.append([cd])
                pred_alg_t2.append([cd])
                pred_alg_t3.append([cd])

                # Predicciones del kalman en t0, t1, t2 y t3
                pred_kal.append([cd])
                pred_kal_t1.append([cd])
                pred_kal_t2.append([cd])
                pred_kal_t3.append([cd])

                # Frames de las predicciones del algoritmo en t0, t1, t2 y t3
                fpred_alg.append([c])
                fpred_alg_t1.append([c])
                fpred_alg_t2.append([c])
                fpred_alg_t3.append([c])

                # Frames de las predicciones de kalman en t0, t1, t2 y t3
                fpred_kal.append([c])
                fpred_kal_t1.append([c])
                fpred_kal_t2.append([c])
                fpred_kal_t3.append([c])
        # De la segunda vuelta en adelante, se van agregando y asociando nuevas posiciones
        else:
            d = []
            if c < ndi or c > ndf:
                # Se hace la deteccion con yolo
                labels, cord_thres = detect.xyxyn[0][:, -1].numpy(), detect.xyxyn[0][:, :-1].numpy()
                for i in range(len(cord_thres)):
                    if int(labels[i]) == 0:
                        x_min = cord_thres[i][0]
                        x_max = cord_thres[i][2]
                        y_min = cord_thres[i][1]
                        y_max = cord_thres[i][3]
                        cx = (x_min * ancho) + ((ancho * (x_max - x_min)) / 2)
                        cy = (y_min * alto) + ((alto * (y_max - y_min)) / 2)
                        d.append([cx, cy])
            last_value = []
            # Se hace la asociacion. Se toma en cuenta las mediciones encontradas (d) las ultimas posiciones de todos los cluster
            # existentes (last_value) y el umbral para saber que tan cerca debe estar una nueva medicion a un cluster para considerar
            # que puede ser asociado (m). Si no hay detecciones, se agrega un arreglo vacio
            for cl in med:
                last_value.append(cl[len(cl) - 1])
            if len(d) != 0:
                np, nc = asociacion(d, last_value, m)
            else:
                np = []
                for posi in range(len(last_value)):
                    np.append([0, 0])
                    nc = []
            erase_c = []
            for num_c in range(len(med)):
                # Si el tamaño de los cluster, es menor a tc (5 en este caso) el cluster aun no es considerado para analizarlo
                # con AIC, RANSAC y KALMAN, lo unico que se hace, es ir guardando en los arreglos, los valores asociados.
                if len(med[num_c]) < tc:
                    if np[num_c][0] != 0 and np[num_c][1] != 0:

                        nd_posiciones[num_c] = 0
                        nd_aux_posiciones[num_c] = 10

                        med[num_c].append(np[num_c])
                        fmed[num_c].append(c)

                        med_clus[num_c].append([[0]])
                        fmed_clus[num_c].append(c)

                        posiciones_fil[num_c].append([[0]])
                        fposiciones_fil[num_c].append(c)

                        posiciones_AIC[num_c].append([[0]])
                        fmed_AIC[num_c].append(c)

                        posiciones_RAN[num_c].append([[0]])
                        fmed_RAN[num_c].append(c)

                        pred_kal[num_c].append(np[num_c])
                        fpred_kal[num_c].append(c)

                        pred_alg[num_c].append(np[num_c])
                        fpred_alg[num_c].append(c)

                        pred_kal_t1[num_c].append(np[num_c])
                        fpred_kal_t1[num_c].append(c)

                        pred_alg_t1[num_c].append(np[num_c])
                        fpred_alg_t1[num_c].append(c)

                        pred_kal_t2[num_c].append(np[num_c])
                        fpred_kal_t2[num_c].append(c)

                        pred_alg_t2[num_c].append(np[num_c])
                        fpred_alg_t2[num_c].append(c)

                        pred_kal_t3[num_c].append(np[num_c])
                        fpred_kal_t3[num_c].append(c)

                        pred_alg_t3[num_c].append(np[num_c])
                        fpred_alg_t3[num_c].append(c)

                        posiciones_fil_nc[num_c].append(np[num_c])
                        fposiciones_fil_nc[num_c].append(c)

                    else:
                        erase_c.append(num_c)
                # Cuando tc sea > 5, ya empieza el analisis
                else:
                    # Si hay medición asociada al cluster, entra aquí
                    if np[num_c][0] != 0 and np[num_c][1] != 0:
                        # Si el tamaño del cluster es mayor a 9, se toman solo los ultimos 9 valores para hacer las predicciones
                        if len(med[num_c]) > 9:
                            cl_pred = copy.deepcopy(med[num_c])
                            cl_pred = cl_pred[-9:]
                        else:
                            cl_pred = copy.deepcopy(med[num_c])

                        ########################################################################################

                        # Como hay medicion, las predicciones obtenidas de kalman son x_upd, p_upd (actualizaciones) para t0
                        X_upd, P_upd, predk, p_predk = kf(np[num_c], p_upd[num_c], x_upd[num_c], Q[num_c][0], Q[num_c][1])
                        x_upd[num_c] = X_upd
                        p_upd[num_c] = P_upd

                        p_pred = copy.deepcopy(p_predk)
                        x_pred = copy.deepcopy(predk)
                        pQ = Q[num_c][0]
                        vQ = Q[num_c][1]

                        # Se hacen las predicciones para t1
                        for ik in range(2):
                            # print("UNO")
                            x_pred, p_pred = kf2(p_pred, x_pred, pQ, vQ)
                            pQ += 20
                            vQ += 50
                        pred_t1k = [x_pred[0], x_pred[1]]

                        p_pred = copy.deepcopy(p_predk)
                        x_pred = copy.deepcopy(predk)
                        pQ = Q[num_c][0]
                        vQ = Q[num_c][1]

                        # Se hacen las predicciones para t2
                        for ik in range(3):
                            # print("DOS")
                            x_pred, p_pred = kf2(p_pred, x_pred, pQ, vQ)
                            pQ += 20
                            vQ += 50
                        pred_t2k = [x_pred[0], x_pred[1]]

                        p_pred = copy.deepcopy(p_predk)
                        x_pred = copy.deepcopy(predk)
                        pQ = Q[num_c][0]
                        vQ = Q[num_c][1]

                        # Se hacen las predicciones para t3
                        for ik in range(4):
                            x_pred, p_pred = kf2(p_pred, x_pred, pQ, vQ)
                            pQ += 20
                            vQ += 50
                        pred_t3k = [x_pred[0], x_pred[1]]
                        ###################################################################

                        ###################################################################
                        posAIC = PLOT_AIC(cl_pred)
                        posRANSAC = PLOT_RANSAC(cl_pred, len(cl_pred))
                        #print("R", posRANSAC)
                        #print("AIC", posAIC)

                        # Se hacen las predicciones para t0. Para t1, t2, y t3 con los parametros linealizados
                        
                        pred, XX, YY = g_pred(cl_pred, len(cl_pred))
                        #print(cl_pred, XX, YY)
                        pred_t1 = g_pred_lin(cl_pred, XX, YY, len(cl_pred) + 1)
                        pred_t2 = g_pred_lin(cl_pred, XX, YY, len(cl_pred) + 2)
                        pred_t3 = g_pred_lin(cl_pred, XX, YY, len(cl_pred) + 3)

                        # Se actualizan los valores de los parametros XX y YY
                        parametrosX[num_c] = XX
                        parametrosY[num_c] = YY
                        nd_posiciones[num_c] = 0
                        nd_aux_posiciones[num_c] = 10
                        ###################################################################

                        # Se agregan los valores de mediciones, predicciones, etc.
                        med[num_c].append(np[num_c])
                        fmed[num_c].append(c)
                        #print(cl_pred)
                        med_clus[num_c].append(cl_pred)
                        fmed_clus[num_c].append(c)
                        #print(med_clus[num_c])
                        #print(med_totales_clus)
                        posiciones_fil[num_c].append(cl_pred)
                        fposiciones_fil[num_c].append(c)

                        posiciones_AIC[num_c].append(posAIC[0])
                        fmed_AIC[num_c].append(c)

                        posiciones_RAN[num_c].append(posRANSAC[0])
                        fmed_RAN[num_c].append(c)

                        pred_kal[num_c].append(predk)
                        fpred_kal[num_c].append(c)

                        pred_alg[num_c].append(pred)
                        fpred_alg[num_c].append(c)

                        pred_kal_t1[num_c].append(pred_t1k)
                        fpred_kal_t1[num_c].append(c)

                        pred_alg_t1[num_c].append(pred_t1)
                        fpred_alg_t1[num_c].append(c)

                        pred_kal_t2[num_c].append(pred_t2k)
                        fpred_kal_t2[num_c].append(c)

                        pred_alg_t2[num_c].append(pred_t2)
                        fpred_alg_t2[num_c].append(c)

                        pred_kal_t3[num_c].append(pred_t3k)
                        fpred_kal_t3[num_c].append(c)

                        pred_alg_t3[num_c].append(pred_t3)
                        fpred_alg_t3[num_c].append(c)

                        posiciones_fil_nc[num_c].append(np[num_c])
                        fposiciones_fil_nc[num_c].append(c)

                    # No hay medición aosciado al cluster, entra aquí
                    else:
                        # Si el tamaño del cluster es mayor a 9, se toman solo los ultimos 9 valores para hacer las predicciones
                        if len(med[num_c]) > 9:
                            cl_pred = copy.deepcopy(med[num_c])
                            cl_pred = cl_pred[-9:]
                            t = nd_aux_posiciones[num_c]
                            #print("MAYOR A 9")
                        else:
                            cl_pred = copy.deepcopy(med[num_c])
                            t = len(cl_pred)
                            #print("MENOR A 9")
                        nconteos = nd_posiciones[num_c]

                        ############################################################

                        # Las predicciones de kalman ahora se hacen con la funcion donde no se cuenta con mediciones. Para cada
                        # paso de tiempo, los paramatros de la matriz Q van aumentando (20 para el valor de ganancia de la
                        # posicion y 50 para la ganancia de la velocidad)
                        pQ = Q[num_c][0]
                        vQ = Q[num_c][1]
                        predk, ppred = kf2(p_upd[num_c], x_upd[num_c], pQ, vQ)

                        x_upd[num_c] = predk
                        p_upd[num_c] = ppred
                        Q[num_c][0] = pQ + 20
                        Q[num_c][1] = vQ + 50

                        p_pred = ppred
                        x_pred = predk
                        pQ = Q[num_c][0]
                        vQ = Q[num_c][1]
                        for ik in range(2):
                            x_pred, p_pred = kf2(p_pred, x_pred, pQ, vQ)
                            pQ += 20
                            vQ += 50
                        pred_t1k = [x_pred[0], x_pred[1]]

                        p_pred = ppred
                        x_pred = predk
                        pQ = Q[num_c][0]
                        vQ = Q[num_c][1]
                        for ik in range(3):
                            x_pred, p_pred = kf2(p_pred, x_pred, pQ, vQ)
                            pQ += 20
                            vQ += 50
                        pred_t2k = [x_pred[0], x_pred[1]]

                        p_pred = ppred
                        x_pred = predk
                        pQ = Q[num_c][0]
                        vQ = Q[num_c][1]
                        for ik in range(4):
                            x_pred, p_pred = kf2(p_pred, x_pred, pQ, vQ)
                            pQ += 20
                            vQ += 50
                        pred_t3k = [x_pred[0], x_pred[1]]

                        ############################################################

                        ############################################################

                        posAIC = PLOT_AIC(cl_pred)
                        posRANSAC = PLOT_RANSAC(cl_pred, len(cl_pred))
                        # print("NO")

                        # Las predicciones con el algoritmo se hacen desde t0 con los parametros liniealizados. En este caso, no
                        # podemos sacar los parametros porque no tenemos informacion de la ultima deteccion. Por lo que los 
                        # parametros que se toman son los ultimos obtenidos antes de que ya no hubiera detecciones. 
                        pred = g_pred_lin(cl_pred, parametrosX[num_c], parametrosY[num_c], t)
                        pred_t1 = g_pred_lin(cl_pred, parametrosX[num_c], parametrosY[num_c], t + 1)
                        pred_t2 = g_pred_lin(cl_pred, parametrosX[num_c], parametrosY[num_c], t + 2)
                        pred_t3 = g_pred_lin(cl_pred, parametrosX[num_c], parametrosY[num_c], t + 3)

                        ############################################################

                        # Se agregan los valores de las mediciones y las predicciones 
                        med[num_c].append(pred)
                        fmed[num_c].append(c)

                        med_clus[num_c].append(cl_pred)
                        fmed_clus[num_c].append(c)

                        posiciones_fil[num_c].append(cl_pred)
                        fposiciones_fil[num_c].append(c)

                        posiciones_AIC[num_c].append(posAIC[0])
                        fmed_AIC[num_c].append(c)

                        posiciones_RAN[num_c].append(posRANSAC[0])
                        fmed_RAN[num_c].append(c)

                        pred_kal[num_c].append(predk)
                        fpred_kal[num_c].append(c)

                        pred_alg[num_c].append(pred)
                        fpred_alg[num_c].append(c)

                        pred_kal_t1[num_c].append(pred_t1k)
                        fpred_kal_t1[num_c].append(c)

                        pred_alg_t1[num_c].append(pred_t1)
                        fpred_alg_t1[num_c].append(c)

                        pred_kal_t2[num_c].append(pred_t2k)
                        fpred_kal_t2[num_c].append(c)

                        pred_alg_t2[num_c].append(pred_t2)
                        fpred_alg_t2[num_c].append(c)

                        pred_kal_t3[num_c].append(pred_t3k)
                        fpred_kal_t3[num_c].append(c)

                        pred_alg_t3[num_c].append(pred_t3)
                        fpred_alg_t3[num_c].append(c)

                        posiciones_fil_nc[num_c].append(np[num_c])
                        fposiciones_fil_nc[num_c].append(c)

                        nconteos += 1
                        nd_posiciones[num_c] = nconteos
                        if nconteos == tc:
                            erase_c.append(num_c)
                        if len(med[num_c]) > 9:
                            t += 1
                            nd_aux_posiciones[num_c] = t
            # Si pasan 5 frames, y hay cluster los cuales no se les asocia ninguna nueva deteccion, el cluster se cierra. Esto se
            # hace porque se considera que el objeto se dejo de ver en la imagen ocasionado por una oclusion o porque salió
            # de la imagen. 
            if len(erase_c) != 0:
                #print("Se borraron clusters")
                erase_c.sort(reverse=True)
                for ec in erase_c:
                    if len(med_clus[ec]) > 5:
                        velocidades_totales.append(velocidades[ec])

                        med_totales_clus.append(med_clus[ec])
                        fmed_clus_totales.append(fmed_clus[ec])

                        med_totales.append(med[ec])
                        fmed_totales.append(fmed[ec])

                        posiciones_totales_fil.append(posiciones_fil[ec])
                        fposiciones_fil_totales.append(fposiciones_fil[ec])

                        posiciones_totales_fil_nc.append(posiciones_fil_nc[ec])
                        fposiciones_fil_nc_totales.append(fposiciones_fil_nc[ec])

                        posiciones_totales_AIC.append(posiciones_AIC[ec])
                        fmed_AIC_totales.append(fmed_AIC[ec])

                        posiciones_totales_RAN.append(posiciones_RAN[ec])
                        fmed_RAN_totales.append(fmed_RAN[ec])

                        pred_totales_alg.append(pred_alg[ec])
                        fpred_alg_totales.append(fpred_alg[ec])

                        pred_totales_alg_t1.append(pred_alg_t1[ec])
                        fpred_alg_t1_totales.append(fpred_alg_t1[ec])

                        pred_totales_alg_t2.append(pred_alg_t2[ec])
                        fpred_alg_t2_totales.append(fpred_alg_t2[ec])

                        pred_totales_alg_t3.append(pred_alg_t3[ec])
                        fpred_alg_t3_totales.append(fpred_alg_t3[ec])

                        pred_totales_kal.append(pred_kal[ec])
                        fpred_kal_totales.append(fpred_kal[ec])

                        pred_totales_kal_t1.append(pred_kal_t1[ec])
                        fpred_kal_t1_totales.append(fpred_kal_t1[ec])

                        pred_totales_kal_t2.append(pred_kal_t2[ec])
                        fpred_kal_t2_totales.append(fpred_kal_t2[ec])

                        pred_totales_kal_t3.append(pred_kal_t3[ec])
                        fpred_kal_t3_totales.append(fpred_kal_t3[ec])

                    velocidades.pop(ec)
                    nd_posiciones.pop(ec)
                    nd_aux_posiciones.pop(ec)
                    parametrosX.pop(ec)
                    parametrosY.pop(ec)

                    med_clus.pop(ec)
                    fmed_clus.pop(ec)

                    med.pop(ec)
                    fmed.pop(ec)

                    posiciones_fil_nc.pop(ec)
                    fposiciones_fil_nc.pop(ec)

                    posiciones_fil.pop(ec)
                    fposiciones_fil.pop(ec)

                    posiciones_AIC.pop(ec)
                    fmed_AIC.pop(ec)

                    posiciones_RAN.pop(ec)
                    fmed_RAN.pop(ec)

                    pred_alg.pop(ec)
                    pred_alg_t1.pop(ec)
                    pred_alg_t2.pop(ec)
                    pred_alg_t3.pop(ec)

                    pred_kal.pop(ec)
                    pred_kal_t1.pop(ec)
                    pred_kal_t2.pop(ec)
                    pred_kal_t3.pop(ec)

                    fpred_alg.pop(ec)
                    fpred_alg_t1.pop(ec)
                    fpred_alg_t2.pop(ec)
                    fpred_alg_t3.pop(ec)

                    fpred_kal.pop(ec)
                    fpred_kal_t1.pop(ec)
                    fpred_kal_t2.pop(ec)
                    fpred_kal_t3.pop(ec)

                    Q.pop(ec)
                    p_upd.pop(ec)
                    x_upd.pop(ec)

            # Si se detecta una nueva posicion y no se asocia a ningun objeto en seguimiento, se inicializa un nuevo cluster. 
            # Esto se hace cuando un objeto sale de una oclusion o cuando va a entrado a la imagen. 
            if len(nc) != 0:
                for nuevos_c in nc:
                    nd_posiciones.append(0)
                    nd_aux_posiciones.append(10)

                    parametrosX.append([0, 0])
                    parametrosY.append([0, 0])

                    velocidades.append([[0, 0]])
                    p_upd.append([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
                    x_upd.append([nuevos_c[0], nuevos_c[1], 0, 0])
                    Q.append([20, 100])

                    med_clus.append([[0]])
                    fmed_clus.append([c])

                    med.append([nuevos_c])
                    fmed.append([c])

                    posiciones_fil.append([[0]])
                    fposiciones_fil.append([c])

                    posiciones_fil_nc.append([nuevos_c])
                    fposiciones_fil_nc.append([c])

                    posiciones_AIC.append([[0]])
                    fmed_AIC.append([c])

                    posiciones_RAN.append([[0]])
                    fmed_RAN.append([c])

                    pred_alg.append([nuevos_c])
                    pred_alg_t1.append([nuevos_c])
                    pred_alg_t2.append([nuevos_c])
                    pred_alg_t3.append([nuevos_c])

                    pred_kal.append([nuevos_c])
                    pred_kal_t1.append([nuevos_c])
                    pred_kal_t2.append([nuevos_c])
                    pred_kal_t3.append([nuevos_c])

                    fpred_alg.append([c])
                    fpred_alg_t1.append([c])
                    fpred_alg_t2.append([c])
                    fpred_alg_t3.append([c])

                    fpred_kal.append([c])
                    fpred_kal_t1.append([c])
                    fpred_kal_t2.append([c])
                    fpred_kal_t3.append([c])


    c += 1

for ec in range(len(med)):
    if len(med_clus[ec]) > 5:
        velocidades_totales.append(velocidades[ec])

        med_totales_clus.append(med_clus[ec])
        fmed_clus_totales.append(fmed_clus[ec])

        med_totales.append(med[ec])
        fmed_totales.append(fmed[ec])

        posiciones_totales_fil.append(posiciones_fil[ec])
        fposiciones_fil_totales.append(fposiciones_fil[ec])

        posiciones_totales_fil_nc.append(posiciones_fil_nc[ec])
        fposiciones_fil_nc_totales.append(fposiciones_fil_nc[ec])

        posiciones_totales_AIC.append(posiciones_AIC[ec])
        fmed_AIC_totales.append(fmed_AIC[ec])

        posiciones_totales_RAN.append(posiciones_RAN[ec])
        fmed_RAN_totales.append(fmed_RAN[ec])

        pred_totales_alg.append(pred_alg[ec])
        fpred_alg_totales.append(fpred_alg[ec])

        pred_totales_alg_t1.append(pred_alg_t1[ec])
        fpred_alg_t1_totales.append(fpred_alg_t1[ec])

        pred_totales_alg_t2.append(pred_alg_t2[ec])
        fpred_alg_t2_totales.append(fpred_alg_t2[ec])

        pred_totales_alg_t3.append(pred_alg_t3[ec])
        fpred_alg_t3_totales.append(fpred_alg_t3[ec])

        pred_totales_kal.append(pred_kal[ec])
        fpred_kal_totales.append(fpred_kal[ec])

        pred_totales_kal_t1.append(pred_kal_t1[ec])
        fpred_kal_t1_totales.append(fpred_kal_t1[ec])

        pred_totales_kal_t2.append(pred_kal_t2[ec])
        fpred_kal_t2_totales.append(fpred_kal_t2[ec])

        pred_totales_kal_t3.append(pred_kal_t3[ec])
        fpred_kal_t3_totales.append(fpred_kal_t3[ec])

# De aqui para abajo todo son temas de graficacion
"""
###
myFile3 = open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/med_clus_nf.csv", 'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(med_totales_clus)

myFile3 = open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/frames_nf.csv", 'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(fmed_totales)

myFile3 = open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/med_nf.csv", 'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(med_totales)

myFile3 = open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/predt0_nf.csv", 'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_alg)

myFile3 = open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/predt1_nf.csv", 'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_alg_t1)

myFile3 = open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/predt2_nf.csv", 'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_alg_t2)

myFile3 = open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/predt3_nf.csv", 'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_alg_t3)

myFile3 = open(
    "C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/kalt0.csv",
    'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_kal)

myFile3 = open(
    "C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/kalt1.csv",
    'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_kal_t1)

myFile3 = open(
    "C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/kalt2.csv",
    'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_kal_t2)

myFile3 = open(
    "C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/kalt3.csv",
    'w')
with myFile3:
    writer = csv.writer(myFile3)
    writer.writerows(pred_totales_kal_t3)
###
"""
for i in range(len(med_totales)):
    print("******")
    print("OBJETO ", i)
    #print("Medicion")
    #print(med_totales[i])
    print(fmed_totales[i])
    #print("Medicion cluster")
    print(len(med_totales_clus[i]))
    #print("Prediccion t0 kal")
    #print(pred_totales_kal[i])
    #print("Prediccion t1 kal")
    #print(pred_totales_kal_t1[i])
    """
    print("Medicion filtrada")
    print(posiciones_totales_fil_nc[i])
    print(fposiciones_fil_nc_totales[i])
    print("Medicion filtrada cluster")
    print(posiciones_totales_fil[i])
    print(fposiciones_fil_totales[i])
    print("AIC")
    print(posiciones_totales_AIC[i])
    print(fmed_AIC_totales[i])
    print("RANSAC")
    print(posiciones_totales_RAN[i])
    print(fmed_RAN_totales[i])
    print("Prediccion t0 alg")
    print(pred_totales_alg[i])
    print(fpred_alg_totales[i])
    print("Prediccion t1 alg")
    print(pred_totales_alg_t1[i])
    print(fpred_alg_t1_totales[i])
    print("Prediccion t2 alg")
    print(pred_totales_alg_t2[i])
    print(fpred_alg_t2_totales[i])
    print("Prediccion t3 alg")
    print(pred_totales_alg_t3[i])
    print(fpred_alg_t3_totales[i])
    print("Prediccion t0 kal")
    print(pred_totales_kal[i])
    print(fpred_kal_totales[i])
    print("Prediccion t1 kal")
    print(pred_totales_kal_t1[i])
    print(fpred_kal_t1_totales[i])
    print("Prediccion t2 kal")
    print(pred_totales_kal_t2[i])
    print(fpred_kal_t2_totales[i])
    print("Prediccion t3 kal")
    print(pred_totales_kal_t3[i])
    print(fpred_kal_t3_totales[i])
    """




"""
# Abre el archivo CSV en modo lectura
GT = []
GT_totales = []
with open("C:/Users/varel/Documents/MCR/4/Seminario de tesis/fotos_peces/RESULTADOS/Nuevo_Alg/FILTROS_NO_FILTROS/camila/GT.csv", newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    # Itera a través de las filas del archivo CSV
    for fila in lector_csv:
        # fila es una lista de valores en la fila
        if len(fila) != 0:
            GT.append([int(fila[0]), int(fila[1])])

#print("TA", len(GT))
posGT = []
for i in range(len(GT)):
    if i >= 11 and i <= 34:
        #print(GT[i])
        posGT.append(GT[i])
#print(posGT)

posGT2 = []
for i in range(len(GT)):
    if i >= 41 and i <= 99:
        #print(GT[i])
        posGT2.append(GT[i])
#print(posGT2)

GT_totales.append(posGT)
GT_totales.append(posGT2)
GX, GY = [], []
#print(GT_totales)
for i in GT_totales:
    for m in i:
        GX.append(m[0])
        GY.append(m[1])

plt.scatter(GX, GY, s=25, color="blue", marker="o", label="GT")
plt.plot(GX, GY, color="blue")
plt.savefig("C:/Users/varel/Documents/Tesis/" + folder + "/posicionesGT/GT.jpg")
plt.clf()
"""
graficar(med_totales_clus, posiciones_totales_AIC, posiciones_totales_RAN, med_totales, pred_totales_alg, pred_totales_alg_t1,
         pred_totales_alg_t2, pred_totales_alg_t3, pred_totales_kal, pred_totales_kal_t1, pred_totales_kal_t2, pred_totales_kal_t3,
        folder)


