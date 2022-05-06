import cv2 as cv

# começando pela leitura da imagem
# NÃO ESQUECER DE PASSAR O SRC POR LINHA DE COMANDO DEPOIS

src = cv.imread('digital.jpg')
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
rows, cols = src_gray.shape
# min começa no máximo pra que eu possa diminuir ele pra o menor valor de fato
min_pixel_value = 255
# max começa no menor valor pra que eu possa de fato ir aumentando ele
max_pixel_value = 0
# definindo o menor valor
for i in range(rows):
    for j in range(cols):
        if min_pixel_value >= src_gray[i, j]:
            min_pixel_value = src_gray[i, j]
        if max_pixel_value <= src_gray[i, j]:
            max_pixel_value = src_gray[i, j]
            
threshold = int((max_pixel_value + min_pixel_value) / 2)
final_threshold_min_value_array = []
final_threshold_max_value_array = []
aux_value1 = 0
aux_value2 = 0

for i in range(rows):
    for j in range(cols):
        if src_gray[i, j] >= threshold:
            final_threshold_max_value_array.append(src_gray[i, j])
        if src_gray[i, j] < threshold:
            final_threshold_min_value_array.append(src_gray[i, j])
for i in range(len(final_threshold_min_value_array)):
    aux_value1 += final_threshold_min_value_array[i]

u1 = aux_value1 / len(final_threshold_min_value_array)
for i in range(len(final_threshold_max_value_array)):
    aux_value2 += final_threshold_max_value_array[i]
u2 = aux_value2 / len(final_threshold_max_value_array)

final_threshold = int((u1 + u2) / 2)

while final_threshold > threshold:
    for i in range(rows):
        for j in range(cols):
            if src_gray[i, j] >= threshold:
                final_threshold_max_value_array.append(src_gray[i, j])
            if src_gray[i, j] < threshold:
                final_threshold_min_value_array.append(src_gray[i, j])
    for i in range(len(final_threshold_min_value_array)):
        aux_value1 += final_threshold_min_value_array[i]
    u1 = aux_value1 / len(final_threshold_min_value_array)
    for i in range(len(final_threshold_max_value_array)):
        aux_value2 += final_threshold_max_value_array[i]
    u2 = aux_value2 / len(final_threshold_max_value_array)
    final_threshold = (u1 + u2) / 2
for i in range(rows):
    for j in range(cols):
        if src_gray[i, j] > final_threshold:
            src_gray[i, j] = max_pixel_value
cv.imshow('Teste', src_gray)
cv.waitKey(0)