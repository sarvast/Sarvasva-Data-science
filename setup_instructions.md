# AIML Environment Setup Guide

## Option 1: Anaconda Installation (Recommended)

1. **Download Anaconda:**
   - Visit: https://www.anaconda.com/download
   - Download Python 3.10+ version for Windows

2. **Install Anaconda:**
   - Run installer as Administrator
   - Add to PATH when prompted

3. **Create Environment:**
   ```bash
   conda create -n aiml python=3.10
   conda activate aiml
   conda install jupyter pandas numpy matplotlib scikit-learn
   ```

4. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

## Option 2: VS Code with Jupyter Extension

1. **Install Extensions:**
   - Python extension
   - Jupyter extension

2. **Install Python packages:**
   ```bash
   pip install jupyter pandas numpy matplotlib scikit-learn
   ```

## Option 3: Google Colab (Temporary Solution)

1. Upload your .ipynb files to Google Drive
2. Open with Google Colab
3. Upload data.json when needed

## Current Status
- ✅ Jupyter notebooks created
- ✅ Data files ready
- ❌ Python environment not configured