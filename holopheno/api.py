# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/read_data.ipynb.

# %% auto 0
__all__ = ['read_data']

# %% ../nbs/read_data.ipynb 3
def read_data(data, X = None, Y = None):
    from .classes import HoloPheno
    holo_obj = HoloPheno(data, X, Y)
    return holo_obj

