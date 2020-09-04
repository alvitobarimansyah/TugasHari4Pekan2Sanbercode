# soal no 1

Jelaskan prosess yang terjadi dalam grouping data menggungkan method groupby() dari pandas

ketika melakukan grouping ada beberapa proses yang terjadi secara berurutan, yaitu :

Splitting : Memisahkan data kedalam suatu group berdasarkan kriteria tertentu.
Applying : Melakukan suatu operasi terhadap sekumpulan data di group-group tersebut.
Combining : Menggabungkan data menjadi suatu struktur baru

# soal no 2

import pandas as pd
df = pd.read_csv('diamonds.csv')
df.drop('Unnamed: 0', axis = 1, inplace=True)

df.groupby('cut').mean()

# soal no 3

import pandas as pd
df = pd.read_csv('diamonds.csv')
df.drop('Unnamed: 0', axis = 1, inplace=True)

df.groupby(['cut', 'color']).agg({'carat':'mean', 'table':'mean', 'price':'mean'})

# soal no 4

import pandas as pd
import numpy as np

df = pd.read_csv('diamonds.csv')
df.drop('Unnamed: 0', axis = 1, inplace=True)

def median(x):
    return np.median(x)

df.groupby(['cut', 'color']).agg(['mean', median])

# soal no 5

import pandas as pd
df = pd.read_csv('diamonds.csv')
df.drop('Unnamed: 0', axis = 1, inplace=True)

df.groupby('cut').agg({'price':'max', 'carat':'min'})

# soal no 6

import pandas as pd
import numpy as np

df = pd.read_csv('diamonds.csv')
df.drop('Unnamed: 0', axis = 1, inplace=True)

def std(x):
    return np.std(x, ddof = 1)

def max_min(x):
    return np.ptp(x)

df.groupby('cut').agg({'price':max_min, 'carat':std})
