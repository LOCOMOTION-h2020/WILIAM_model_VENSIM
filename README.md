# pywiliam

The pywiliam model is a translation of the [WILIAM Integrated Assessment Model (IAM)](https://www.locomotion-h2020.eu/locomotion-models/locomotion-iams/) to Python. The package also includes a command line interface (CLI) to facilitate configuring and launching simulations, and a plot tool to visualize simulation results.

The WILIAM model was developed in the [Vensim software](https://vensim.com/), in the context of the H2020 LOCOMOTION project. The translation to Python was done using the [PySD](https://pysd.readthedocs.io/en/master/) Python library.


| :warning: WARNING                                                                 |
|:----------------------------------------------------------------------------------|
| The present release of pywiliam is based on WILIAM v1.1, which is still under heavy development. To get support or to report issues, please contact gir.geeds@uva.es    |

# How to install
We recommend installing all project dependencies in a Python virtual environment. Here, we show how this is done using conda package manager. Conda comes preinstalled with the [Anaconda Python distribution](https://www.anaconda.com/download).

Add conda-forge channel:

```bash
conda config --add channels conda-forge
```

To create a virtual environment using conda, run:

```bash
conda create --name wiliam python=3.11 --file requirements.txt
```

The previous command created a virtual environment named `wiliam`. To activate it, run:

```bash
conda activate wiliam
```

To run the wiliam model, you need to be inside the virtual environment, but if you want to exit it, run:

```bash
conda deactivate
```

# The command line interface

A wiliam simulation using default parameters can be run by simpply typing:

```code
    python run.py
```

However, more precise results can be obtained by passing arguments to the `run.py` script. To see all available options, run:

```code
    python run.py -h
```

Additionally, if the user only wants to play with scenario parameters, a good initialisation speedup may be achieved by loading the model parameters from a binary file, as follows:

```code
    python run.py -e wiliam/model_parameters/model_parameters.nc
```

# Creating a new scenario

To create a new scenario, duplicate the scenario_parameters.xlsx file and give it a descriptive name (eu_green_deal.xlsx).

To run a simulation with the newly created scenario, run:

```code
    python run.py -x eu_green_deal
```

# Plotting simulation results

If the `-p` argument is passed to the CLI, a graphical user interface will load automatically after the simulation ends, which lets the users plot the results:

```code
python run.py -h
```


Alternatively, the plot tool may be launch in standalone mode, by running:

```code
python plot_tool.py
```


# Exporting simulation results to netCDF

By default, simulation results are sotred in netCDF files (.nc extension).

A Jupyter Notebook is available in the tools folder (`deserialize_simulation_results.ipynb`) with instructions on how to export the simulation data to csv files.

# Acknowledgements
The development of the WILIAM model and its translation to Python were supported by the European Union through the funding of the LOCOMOTION project under the Horizon 2020 research
and innovation programme (grant agreement No 821105).