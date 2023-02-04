import os
import matplotlib.pyplot as plt

def save_fig(name: str, extension="jpg", resolution=300) :
    """save plot image"""
    BASE_PATH = "plot_images"
    path = f'{BASE_PATH}/{name}.{extension}'
    plt.savefig(path, format=extension, dpi=resolution)