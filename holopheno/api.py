# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/API/read_data.ipynb.

# %% auto 0
__all__ = ['read_data']

# %% ../nbs/API/read_data.ipynb 3
def read_data(data, x = None, y = None):
    from .classes import HoloPheno
    holo_obj = HoloPheno(data, x, y)
    return holo_obj

