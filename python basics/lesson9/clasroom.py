def func_nomi(t_yil, h_yil=2025):
    yosh = h_yil - t_yil
    v_yetgan = False
    if yosh >= 18:
        v_yetgan=True
    return dict(yosh=yosh, voyaga_yetgan=v_yetgan)
print(func_nomi(t_yil=2009))
print(func_nomi(t_yil=2003, h_yil=2025))
print(func_nomi(t_yil=2005))