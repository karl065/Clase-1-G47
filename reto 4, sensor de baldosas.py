QC = []

baldosas_a_revisar, guardadas_por_sensor = input().split()
baldosas_a_revisar = int(baldosas_a_revisar)
guardadas_por_sensor = int(guardadas_por_sensor)
    

def revision_sensor():
    
    baldosas_sensor = []
    
    bald_s1, bald_s2, bald_s3, bald_s4, bald_s5 = input().split()
  
    bald_s1 = baldosas_sensor.append(int(bald_s1))
    bald_s2 = baldosas_sensor.append(int(bald_s2))
    bald_s3 = baldosas_sensor.append(int(bald_s3))
    bald_s4 = baldosas_sensor.append(int(bald_s4))
    bald_s5 = baldosas_sensor.append(int(bald_s5))
    
        
    return baldosas_sensor

def total_de_fallas(baldosas_sensor):
     
    total_de_fallas = {}
      
    for n in revision_sensor():
      if n in total_de_fallas :
        total_de_fallas[n] += 1
      else:
         total_de_fallas[n] = 0
    
    if total_de_fallas.values() != 0:
        QC.append(sum(total_de_fallas.values()))
    
    return QC

def fallas_sensor():
    total_de_fallas = {}
    
    for n in guardadas_por_sensor():
          if n in total_de_fallas:
            total_de_fallas[n] += 1
          else:
            total_de_fallas[n] = 0
    print(total_de_fallas) 
                
        

if __name__ == "__main__":
    baldosas_sensor = revision_sensor()
    total_de_fallas(baldosas_sensor)
    fallas_sensor
