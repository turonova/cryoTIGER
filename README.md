# 🐯 cryoTIGER ❄️
**T**ilt **I**nterpolation **G**enerator for **E**nhanced **R**econstruction in Cryo-Electron Tomography

📄 Published in [*Communications Biology*](https://www.nature.com/articles/s42003-025-08961-5)

## ⚙️ Installation

*   Get cryoTIGER source codes

```
git clone https://github.com/turonova/cryoTIGER
cd cryoTIGER
```

## 💡 Code Acknowledgments

This project makes use of code from [FILM: Frame Interpolation for Large Motion](https://github.com/google-research/frame-interpolation), authored by [Google Research](https://github.com/google-research). Their work provided a basis for running an interpolator in this project and we use their code in the `eval` folder as well as in the `example_train_config` folder.


### Using environment.yml

*   Create cryoTIGER conda environment using .yml file

```
conda env create -f environment.yml
```

Note: Depending on your system, this can take some time due to the installation of large libraries like Tensorflow.

### Using pip

* The following dependencies should be installed:
    * tensorflow>=2.6.2
    * tensorflow-datasets>=4.4.0
    * tensorflow-addons>=0.15.0
    * gin-config>=0.5.0
    * parameterized>=0.8.1
    * mediapy>=1.0.3
    * scikit-image>=0.19.1
    * apache-beam>=2.34.0
    * google-cloud-bigquery-storage>=1.1.0 # Suppresses a harmless error from beam
    * natsort>=8.1.0
    * gdown>=4.5.4
    * tqdm>=4.64.1
    * cryocat>=0.2.0
    * ipykernel>=6.29.5
 
* Install cryoTIGER using requirements.txt

```
pip3 install -r requirements.txt
```

* **Note:** To enable GPU support, add the Conda environment's library path to the `LD_LIBRARY_PATH` environment variable using the following command: `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/`


## 🧠 Pre-trained Models

*   Create a directory with pre-trained models.

```
mkdir -p <models>
```

*   Download pre-trained models from 
    [owncloud](https://oc.biophys.mpg.de/owncloud/s/MFi6Q7rCFYLAqFT)
    and put them into `<models>`.

The downloaded folder should have the following structure:

```
<models>/<cryoTIGER_model>/
<models>/<pre-trained_Vimeo-90K_data_model>/
```

## 🚀 Running cryoTIGER

*   To demonstrate the cryoTIGER tilt interpolation framework, we provide a Jupyter Notebook
*   **Note:** If you move this notebook to a different folder, make sure that the `eval` directory is still accessible (e.g., by updating the Python path or using relative imports correctly). For best results, keep the notebook within the original project structure.


```
cryoTIGER_interpolation.ipynb
```

* Input: dose-filtered tilt series in .mrc format
```
<tutorial_data>/<experimental_TS>
```
* Output: interpolated dose-filtered tilt series in .mrc format
```
<tutorial_data>/<interpolated_TS>
```

* To obtain the aligned tilt series for input to cryoTIGER, we recommend using the IMOD `newstack` command:
```
newstack -bin 2 -InputFile /path/to/input/{TOMO_ID}_dose-filt.st \
            -xform /path/to/input/alignment_files/{TOMO_ID}.xf -origin -nearest \
            -output /path/to/output/{TOMO_ID}_dose-filt_ali_bin2.mrc
```

## 📜 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 📚 Citation

### APA format

Majtner, T., et al. (2025). cryoTIGER: deep-learning based tilt interpolation generator for enhanced reconstruction in cryo electron tomography. *Communications Biology, 8*, 1443. Nature Publishing Group. https://doi.org/10.1038/s42003-025-08961-5

### BibTeX entry

```bibtex
@article{Majtner2025cryoTIGER,
  author = {Tomáš Majtner and Jan Philipp Kreysing and Maarten W. Tuijtel and Sergio Cruz-León and Jiasui Liu and Gerhard Hummer and Martin Beck and Beata Turoňová},
  title = {{cryoTIGER: deep-learning based tilt interpolation generator for enhanced reconstruction in cryo electron tomography}},
  journal = {{Communications Biology}},
  volume = {8},
  article = {1443},
  year = {2025},
  doi = {10.1038/s42003-025-08961-5},
  url = {https://www.nature.com/articles/s42003-025-08961-5},
  publisher = {Nature Publishing Group}
}
