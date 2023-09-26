# holopheno

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
pip install holopheno
```

## How to use

``` python
import holopheno
import pandas as pd
from palmerpenguins import load_penguins


penguins = load_penguins()

penguins.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | species | island    | bill_length_mm | bill_depth_mm | flipper_length_mm | body_mass_g | sex    | year |
|-----|---------|-----------|----------------|---------------|-------------------|-------------|--------|------|
| 0   | Adelie  | Torgersen | 39.1           | 18.7          | 181.0             | 3750.0      | male   | 2007 |
| 1   | Adelie  | Torgersen | 39.5           | 17.4          | 186.0             | 3800.0      | female | 2007 |
| 2   | Adelie  | Torgersen | 40.3           | 18.0          | 195.0             | 3250.0      | female | 2007 |
| 3   | Adelie  | Torgersen | NaN            | NaN           | NaN               | NaN         | NaN    | 2007 |
| 4   | Adelie  | Torgersen | 36.7           | 19.3          | 193.0             | 3450.0      | female | 2007 |

</div>

### You can use holopheno to easily visualize scatters of individual data points in the chosen dimensions

To do that, you need to first tell indicate which are the independent
variable columns and which are the dependent variable columns in the
dataframe

``` python
x_columns = ['species', 'island', 'sex']
y_columns = [
                    'bill_length_mm', 
                   'bill_depth_mm', 
                   'flipper_length_mm', 
                   'body_mass_g', 
                  ]
```

### `.read_data()` constructs a holophno object and gives you some basic info about the data

``` python
penguins_h = holopheno.read_data(penguins, x = x_columns, y = y_columns)
```

    Data info: 

    sample_size 333
    unique species values ['Adelie' 'Gentoo' 'Chinstrap']
    unique island values ['Torgersen' 'Biscoe' 'Dream']
    unique sex values ['male' 'female']
