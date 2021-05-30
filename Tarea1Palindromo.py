#!/usr/bin/env python
# coding: utf-8

# ## Tarea 1 Geoinformatica
# - Gustavo Daniel Cruz Gutiérrez
# - Crear un algoritmo que identifique si una cadena de caracteres es palíndroma y que al final te diga.

# In[10]:


palabra1 = input("Escriba la palabra en minusculas")
palabrax1=(palabra1.replace(' ', ''))
palabra2 = palabra1[::-1]
palabrax2=(palabra2.replace(' ', ''))
if palabrax1==palabrax2:
    print(palabra1, "si es palindromo")
else:
    print(palabra1, "no es palindromo")


# In[ ]:




