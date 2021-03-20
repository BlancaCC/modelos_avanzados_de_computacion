Blanca Cano Camarero   

# Demuestra que los siguientes criterios de aceptación son equivalentes   


|            | Criterio 1                                                | Criterio 2                    |
|:-----------|:----------------------------------------------------------|:------------------------------|
| Aceptación | Para en un estado final                                   | Se para (en cualquier estado) |
| Rechazo    | Para por falta de transiciones o se mueve indefinidamente | Se mueve indefinidamente      |


## Demostración   


Los demostraremos por una doble implicación.   

### Condición suficiente   

Sea $\mathcal L$ un lenguaje aceptado por $M$ una MT por el primer criterio, veamos que existe otra MT, $N$ que lo acepta por el lenguaje.   

Cualquier palabra que acepte $M$ es porque se para en un estado final, en particular se detiene, luego también será aceptada por $N = M$.  


Si una palabra es rechazada por $M$ entonces es porque se mueve indefinidamente o le faltan transiciones, para el primer caso el criterio de rechazo es 
igual para ambos criterios, sin embargo una palabra que fuera rechazada por falta de transiciones en el criterio 1, sería aceptada en el criterio 2. 
Para solucionar esto a partir de $M$ construiremos $N$ de tal forma que toda palabra que fuera rechada en $M$ por falta de transiciones ahora en $N$ se mueva indefinidamente.   

Llamemos  $N$ a la modifición de  $M$,  que contiene un nuevo estado $q_r$ y para cualquier par $(q, a)$ con $q$ un estado y $a \in B$ 
que no tengan una transición definida añadiremos la transición $\delta(q,a) = (q_r, a, D)$.  

Finalmente añadiremos también  la transición que esté continuamente en movimiento: $\delta (q_r,a) = (q_r, a, D)$.   

Acabamos por tanto de probar que si $\mathcal L$ es un lenguaje aceptado por $M$ una MT por el primer criterio, existe otra MT, $N$ que acepta $\mathcal L$ por el segundo criterio.   




### Condición necesaria   

Sea $\mathcal L$ un lenguaje aceptado por $N$ una MT por el segundo criterio, veamos que existe otra MT, $M$ que acepta a $\mathcal L$ por el primer criterio.   


Si una palabra es aceptada por $N$ entonces es porque para un cierto par  $(q,a)$ de estado y letra del alfabeto no existe ninguna transición definidad. 
Denotemos ahora a $M$ con la MT que además de tener los mismos estados, transiciones y alfabetos que $N$ añade el estado final  $qf$ y las transiciones $\delta(q,a) = (q_f, a, D).$  

De esta forma toda palabra aceptada por $N$ lo es también por $N.$  

Cualquier palabra que sea rechazada por $N$, será será porque se mueva indefinidamente; que es también un método de rechazo para el primer criterio, esto, 
toda palabra rechazado por $N$ también lo será por $M$.  

Hemos probado por tanto que para cualquier lenguaje $\mathcal L$  aceptado por $N$ una MT por el segundo criterio, existe otra MT, $M$ que acepta a $\mathcal L$ por el primer criterio.  
