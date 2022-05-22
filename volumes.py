#!/usr/bin/env python
# coding: utf-8

# Ce notebook regroupe une liste de fonctions utiles pour le calcul des biovolumes de notre projet.

# In[ ]:


# volume d'une ellipse
def volume_ell(h,d) :
    return pi/6 * d^2 * h 

# volume d'une ellipse à trois axes 
def volume_trel(h, d1, d2) :
    return pi/6 * d1 * d2 * h

# volume d'une boîte 
def volume_box(l, w, h) :
    return l*w*h

# volume d'un cyclindre 
def volume_tube(h, d) :
    return pi/4 * d^2 * h

# volume d'un cône 
def volume_con(h, d) :
    return pi/12 * d^2 * h

# volume d'un double cône 
def volume_doco(h, d) :
    return pi/12 * d^2 * h

# volume d'une sphère 
def volume_sphe(d) :
    return pi/6 * d^3

# volume prisme rhomboïde 
def volume_rhp(d1, d2, h): 
    return d1*d2*h/2

