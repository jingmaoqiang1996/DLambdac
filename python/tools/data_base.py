def Lum():
    return 63.6

def Br(mode):
    if mode == 'D0': return [0.03947, 0.00030]
    if mode == 'Lambdac': return [0.0624, 0.0028]
    if mode == 'Lambdac_Kst': return [0.0139, 0.0007]
