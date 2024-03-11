medida = float(input('Digite uma distância em metros: '))

dm = medida * 10
cm = dm * 10
mm = cm * 1
dam = medida / 10
hm = dam / 10
km = hm / 10
print('A Medida de {}mts corresponde a {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(medida, dm, cm, mm))
print('A medida de {}mts corresponde a: {}dam, {}hm e {}km'.format(medida, dam, hm, km))