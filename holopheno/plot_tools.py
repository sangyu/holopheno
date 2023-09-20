# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/plot_tools.ipynb.

# %% auto 0
__all__ = ['scatter_with_ellipse', 'confidence_ellipse', 'regscatter', 'unit_vector', 'angle_between', 'plot_3d_scatter',
           'setFont', 'scale_with_columns', 'generate_x_y_dist']

# %% ../nbs/plot_tools.ipynb 3
def scatter_with_ellipse(data, x, y, group_by):
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_style('white')
    if group_by:
        conditions = data[group_by].unique()
        print('Plotting for the conditions ' + group_by + ':')
        datasets = []
        for i in range(len(conditions)):
            print(conditions[i])
            datasets.append(data.loc[data[group_by]==conditions[i]])
        
        fig, axes = plt.subplots( 1, len(datasets), figsize = [ 5+ 5*len(conditions), 7])
    
        # for i in axes:
        #     i.set_ylim(-0.2, 1.5)
            # i.set_xlim(-0.5, 3)
        for i in range(len(datasets)):
            scale = regscatter(datasets[i], x = x, y = y, ax = axes[i], color = 'k')
            # angles = plot_eigen_vectors(datasets[i], x = x, y = y, ax = axes[i], scale = scale, plot_vs = [0], aspect = None)
    else:
        fig, axes = plt.subplots(1, 1, figsize = [5, 5])
        scale = regscatter(data, x = x, y = y, ax = axes, color = 'k')
        # angles = plot_eigen_vectors(data, x = x, y = y, ax = axes, scale = scale, plot_vs = [0], aspect = None)
    fig.tight_layout()
    # fig.savefig('speedvolumeellipses.png', dpi = 300)
    return fig



# %% ../nbs/plot_tools.ipynb 4
def confidence_ellipse(x, y, ax, n_std=3.0, plotVector = True, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    import numpy as np
    from matplotlib.patches import Ellipse
    import matplotlib.transforms as transforms
    import matplotlib.pyplot as plt
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)
    arrow1 = ax.arrow(0, 0, ell_radius_x , 0, width = 0.02)
    arrow2 = ax.arrow(0, 0, 0, ell_radius_y, width = 0.02)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)
    
    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)
    ellipse.set_transform(transf + ax.transData)
    arrow1.set_transform(transf + ax.transData)
    arrow2.set_transform(transf + ax.transData)
    ax.plot(mean_x, mean_y, 'o', color = 'orangered')
    scale = [scale_x, scale_y]
    return scale, ax.add_patch(ellipse)
    
def regscatter(data, x, y, ax, n_std = 2, scatter = True, fit_reg = False, plot_ellipse = True, show_title = True, 
               color = 'gray', ellipseColor = 'red',**kwargs):
    import scipy 
    import seaborn as sns
    # if aspect:
    #     ax.set_aspect(aspect)
    ax.axvline(c='grey', lw=1)
    ax.axhline(c='grey', lw=1)
    corr_results = scipy.stats.linregress(data[x], data[y])
    if show_title:
        ax.set_title(y + ' = ' + str(round(corr_results.slope, 2)) +  ' x ' + x  + ' + ' 
                     + str(round(corr_results.intercept, 2)) + ' , r = ' + str(round(corr_results.rvalue, 2)))
    # ax.plot(data[x].mean(), data[y].mean(), 'r.', markersize = 10)
    scale = None
    if plot_ellipse:
        scale, ellipse = confidence_ellipse(data[x], data[y],  ax, edgecolor= ellipseColor, facecolor = 'w',  alpha = 0.2, n_std = n_std)
    sns.regplot(x = x, y = y, data = data, ax = ax, scatter = scatter, fit_reg= fit_reg, color = color)
    return scale

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    import numpy as np
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    import numpy as np
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return 180-np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))[1]

def plot_3d_scatter(data, metrics, color_by, palette):
    import seaborn as sns
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    sns.set(style = "whitegrid")
    f_scatter_3d = plt.figure()
    ax = f_scatter_3d.add_subplot(projection='3d')    
    ax.set_xlabel(metrics[0])
    ax.set_ylabel(metrics[1])
    ax.set_zlabel(metrics[2])
    if palette:
        ax.scatter(data[metrics[0]], data[metrics[1]], data[metrics[2]], color = [palette[i] for i in data[color_by]])
    else:
        ax.scatter(data[metrics[0]], data[metrics[1]], data[metrics[2]])
    f_scatter_3d.show()
    return f_scatter_3d



# %% ../nbs/plot_tools.ipynb 5
def setFont(fontSelection, fontSize, fontWeight = 'normal'):
    import matplotlib as mpl
    from matplotlib import rcParams
    # mpl.font_manager._rebuild()
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = [fontSelection]
    rcParams['font.size'] = fontSize 
    rcParams['font.weight'] = fontWeight

# %% ../nbs/plot_tools.ipynb 6
def scale_with_columns(data):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaled_data = pd.DataFrame(scaler.fit_transform(data), columns = data.columns)
    return scaled_data
    

# %% ../nbs/plot_tools.ipynb 7
def generate_x_y_dist(N = 100, x_range = [0, 100], y_range = [0, 200]):
    import random
    import pandas as pd
    data = pd.DataFrame(columns = ['x', 'y'], index = range(0, N))
    data['x'] = np.linspace(x_range[0], x_range[1], num = N) + [random.randint(-100, 100)/2 for i in range(N)]
    data['y'] = np.linspace(y_range[0], y_range[1], num = N) + [random.randint(-100, 100)/2 for i in range(N)]
    return data
