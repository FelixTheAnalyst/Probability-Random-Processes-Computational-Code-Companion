import os
import json

# Base directory
base_dir = "src"

# Chapter files
chapters = [
    "ch01_events_and_sigma_fields.ipynb",
    "ch02_random_variables_and_distributions.ipynb",
    "ch03_discrete_random_variables.ipynb",
    "ch04_continuous_random_variables.ipynb",
    "ch05_generating_functions.ipynb",
    "ch06_markov_chains.ipynb",
    "ch07_convergence_theorems.ipynb",
    "ch08_stationary_processes.ipynb",
    "ch09_spectral_representation.ipynb",
    "ch10_renewal_theory.ipynb",
    "ch11_queueing_theory.ipynb",
    "ch12_martingales.ipynb",
    "ch13_diffusions_and_ito_calculus.ipynb"
]

# Appendices
appendices = [
    "appendix_A_measure_theory.ipynb",
    "appendix_B_functional_analysis.ipynb",
    "appendix_C_common_distributions.ipynb",
    "appendix_D_computational_methods.ipynb"
]

# Preface, TOC, Bibliography
misc_files = ["preface.ipynb", "toc.ipynb", "bibliography.ipynb"]

# Solutions files
solutions = [f"solutions_ch{str(i).zfill(2)}.ipynb" for i in range(1, 14)]


# Function to create folders
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")

# Function to create empty Jupyter notebooks
def create_notebook(path):
    if not os.path.exists(path):
        notebook_content = {
            "cells": [],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(notebook_content, f, indent=2)
        print(f"Created notebook: {path}")
    else:
        print(f"Notebook already exists: {path}")

# Create main directory
create_folder(base_dir)

# Create chapter notebooks
chapters_dir = os.path.join(base_dir, "chapters")
create_folder(chapters_dir)
for file in chapters:
    create_notebook(os.path.join(chapters_dir, file))

# Create appendices
appendices_dir = os.path.join(base_dir, "appendices")
create_folder(appendices_dir)
for file in appendices:
    create_notebook(os.path.join(appendices_dir, file))

# Create misc notebooks
misc_files_dir = os.path.join(base_dir, "misc_files")
create_folder(misc_files_dir)
for file in misc_files:
    create_notebook(os.path.join(misc_files_dir, file))

# Create solutions folder and notebooks
solutions_dir = os.path.join(base_dir, "solutions")
create_folder(solutions_dir)
for file in solutions:
    create_notebook(os.path.join(solutions_dir, file))
    
print("\nJupyter notebook setup complete!")
