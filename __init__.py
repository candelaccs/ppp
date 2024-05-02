def percent (fila_actualizada,writer,calle,tot):

        if int(fila_actualizada[tot])!= 0: #verifico NO estar dividiendo por 0
            tot_por = int(fila_actualizada[calle])/int(fila_actualizada[tot])*100 #utilizo fila actualizada porque es la que tiene los valores reemplazados
            fila_actualizada.append(tot_por) #añado el porcentaje 
            
        else:
            None # no existe el caso de que una poblacion tenga 0 habitantes  


def poblation_process (reader, writer):
    
    calle = 4 # me guardo los indices
    tot = 1
    
    for fila in reader: 
         
         fila_actualizada = [valor.replace('///', '0').replace('-', '0') for valor in fila] #reemplazo los valores en caso de que sean /// o -, caso contrario se deja el que esta
         percent(fila_actualizada, writer, calle, tot) 
         writer.writerow(fila_actualizada) #se añade la fila actualizada

def max_five_percent (data,max_percent):
     
     jurisdiction = 0
     poverty = 13
     aux = list(map(lambda x: [x[jurisdiction], x[poverty]], data))[2:] #solo tomo nombres y porcentajes en una lista
     max_percent.extend(aux) 
     percent = 1
     max_percent.sort(key=lambda x: x[percent], reverse=True)
     

def max_gender_jurisdiction (data, maxim):
     
     jurisdiction = 0
     men = 5
     women = 9
     
     aux = list(map(lambda x: [x[jurisdiction], x[men] ,x[women]], data))[2:] # con [:2] omito el header y el total
     men = 1 #actualizo
     women = 2 #idem
     aux2 = list(map(lambda x: [x[jurisdiction], abs(int(x[men]) - int(x[women]))], aux)) #uso funcion valor absoluto para que siempre me de positivo
     maxim.extend (max(aux2, key = lambda x: x[1]))  #calculo el max
     
     