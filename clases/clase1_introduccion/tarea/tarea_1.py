import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#=============={  un periódico lista los siguientes precios para carros usados  , para un compacto extranjero con edad x_1 medido en años y con un precio de venta x_2  medido en miles de dolares}==============# 


#=============={  Vectores  }==============# 

x1 = [1,2,3,3,4,5,6,7,9,11]
x2 = [18.95 , 19.0 , 17.95 , 15.54 , 14.00 ,12.95 , 8.94 , 7.49 , 6.00 , 3.99]


#=============={  Media De los vectores  }==============# 

media_x1 = np.mean(x1)
media_x2 = np.mean(x2)

#=============={  Covarianza  }==============# 

cov_x1_x2 = sum( (x1 - media_x1)*(x2 - media_x2 )   )/10
print(cov_x1_x2)

#=============={  Imprimir  }==============# 

plt.plot(x1 , x2)
plt.show()

