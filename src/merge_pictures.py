import tkinter as tk
from tkinter import filedialog
import os
import glob
import SimpleITK as sitk
import numpy as np


class MergePictures:
    def __init__(self, nir_path, faf_path, cfp_path, out_path):
        self.nir_path = nir_path
        self.faf_path = faf_path
        self.cfp_path = cfp_path
        self.out_path = out_path

    def __call__(self, pid):
        nir_pid = glob.glob(os.path.join(self.nir_path, pid) + "*")
        faf_pid = glob.glob(os.path.join(self.faf_path, pid) + "*")
        cfp_pid = glob.glob(os.path.join(self.cfp_path, pid) + "*")

        nir_tif = sitk.ReadImage(nir_pid)
        faf_tif = sitk.ReadImage(faf_pid)
        cfp_tif = sitk.ReadImage(cfp_pid)

        nir_tif_array = sitk.GetArrayViewFromImage(nir_tif)
        nir_tif_array = np.moveaxis(nir_tif_array, np.argmin(nir_tif_array.shape), -1)
        faf_tif_array = sitk.GetArrayViewFromImage(faf_tif)
        faf_tif_array = np.moveaxis(faf_tif_array, np.argmin(faf_tif_array.shape), -1)
        cfp_tif_array = sitk.GetArrayViewFromImage(cfp_tif).squeeze()

        stacked = np.concatenate([nir_tif_array, faf_tif_array, cfp_tif_array], -1)
        stacked = sitk.GetImageFromArray(stacked)

        writer = sitk.ImageFileWriter()
        writer.SetImageIO("MetaImageIO")
        writer.SetFileName(os.path.join(self.out_path, pid))
        writer.Execute(stacked)


if __name__ == "__main__":
    nir_path = "/home/alessandro/Documents/Radboudumc/Code/stack-image-modalities/NIR"
    faf_path = "/home/alessandro/Documents/Radboudumc/Code/stack-image-modalities/FAF"
    cfp_path = "/home/alessandro/Documents/Radboudumc/Code/stack-image-modalities/CFP"
    out_path = (
        "/home/alessandro/Documents/Radboudumc/Code/stack-image-modalities/merged"
    )
    mp = MergePictures(nir_path, faf_path, cfp_path, out_path)
    mp("280_OD")
    print()
