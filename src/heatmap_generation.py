import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from lobe_mapping import lobe_mapping

def create_lung_mapping(values):
    lung_mappings = []
    for level in values:
        lung_mapping = []
        for row in range(lobe_mapping.shape[0]):
            lung_mapping_row = []
            for col in range(lobe_mapping.shape[1]):
                lung_mapping_row.append(level[lobe_mapping[row,col]])
            lung_mapping.append(lung_mapping_row)
        lung_mappings.append(lung_mapping)
    return np.array(lung_mappings)

def create_heatmap(values, titles, color_scheme, vmin, vmax, label=None):
    color_scheme.set_bad(color='black')
    fig, axs = plt.subplots(1, 4, figsize=(10, 5))
    for i in range(4):
        heatmap = axs[i].imshow(values[i], cmap=color_scheme, vmin=vmin, vmax=vmax)
        axs[i].set_title(titles[i])
        axs[i].axis('off')
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.70])
    fig.colorbar(heatmap, ax=axs, cax=cbar_ax, label=label, orientation='vertical')
    plt.tight_layout()
    plt.subplots_adjust(right=0.9, wspace=0.1)
    plt.show()

# POROSITY
porosity_values = [
    {'U': 0.657, 'M': 0.657, 'L': 0.657, 'B': np.nan}, # Healthy
    {'U': 0.723, 'M': 0.706, 'L': 0.697, 'B': np.nan}, # Mild/Moderate
    {'U': 0.828, 'M': 0.807, 'L': 0.787, 'B': np.nan}, # Severe
    {'U': 0.896, 'M': 0.856, 'L': 0.822, 'B': np.nan}  # Extreme
]
porosity_data = create_lung_mapping(porosity_values)
titles = [
    'Healthy Lungs\nLobal Porosity', 
    'Mild/Moderate Emphysema\nLobal Porosity', 
    'Severe Emphysema\nLobal Porosity', 
    'Extreme Emphysema\nLobal Porosity'
]
create_heatmap(porosity_data, titles, cm.viridis_r, 0.65, 0.90)

# DIFFUSIVITY
diffusivity_values = [
    {'U': 639.06, 'M': 639.06, 'L': 639.06, 'B': np.nan}, # Healthy
    {'U': 484.95, 'M': 520.69, 'L': 540.73, 'B': np.nan}, # Mild/Moderate
    {'U': 324.98, 'M': 348.60, 'L': 374.99, 'B': np.nan}, # Severe
    {'U': 277.19, 'M': 299.98, 'L': 331.30, 'B': np.nan}  # Extreme
]
diffusivity_data = create_lung_mapping(diffusivity_values)
titles = [
    'Healthy Lungs\nLobal $CO_2$ Diffusivity Capacity', 
    'Mild/Moderate Emphysema\nLobal $CO_2$ Diffusivity Capacity', 
    'Severe Emphysema\nLobal $CO_2$ Diffusivity Capacity', 
    'Extreme Emphysema\nLobal $CO_2$ Diffusivity Capacity'
]
create_heatmap(diffusivity_data, titles, cm.gist_heat, 250, 650, 'mL/min/mmHg')
