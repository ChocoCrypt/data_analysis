#Linea copiada del chat de Zoom
dat <- iris[iris$Species=="setosa",1:4]
head(dat)

#Cargo los datos en las variables que dice el enunciado
X1 = dat$Sepal.Length
X2 = dat$Sepal.Width
X3 = dat$Petal.Length
X4 = dat$Petal.Width

#Datos ...
n = 50
p = 4

X1mean = mean(X1)
X2mean = mean(X2)
X3mean = mean(X3)
X4mean = mean(X4)

#convierto los datos en una matriz

X = as.matrix(dat)
S = var(X)

#INTERVALOS DE CONFIANZA COPIADO DEL ARCHIVO HTML DEL CURSO PARA SABER SI ESTÁ EN LA REGION
#no sirve para nada pero igual lo puse en este ejercicio para seguir la logica de una muestra
inRegion <- function(mu, X.mean, Sinv, n, alpha){
  critical.value <- (p*(n-1))/(n-p)*qf(1-alpha,p,n-p)
  return(n*t(X.mean-mu)%*%Sinv%*%(X.mean-mu) > critical.value)
}



#INTERVALOS DE BONFERRONI SON :
b = 4
alpha = 0.25 #95%
t.bonf <- qt(1-alpha/(2*b),df=n-1)

l1b = X1mean
(u1b <- X1mean + t.bonf * sqrt(S[1]/n))
(l2b <- X2mean - t.bonf * sqrt(S[2]/n))

#valor que seguro se encuentra....
valor = 2.5

