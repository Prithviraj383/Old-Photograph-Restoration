# PhotoRestore – Old Photograph Restoration

A Python-based photograph restoration application that uses **OpenCV Image Inpainting** to detect and reconstruct damaged regions in old photographs.

The project combines traditional image processing techniques with an interactive **Streamlit web interface**, allowing users to upload damaged photographs, restore them, compare results, and download the restored images.

## Features

- Upload damaged photographs in JPG, JPEG, and PNG formats.
- Automatic detection of potential damaged regions using thresholding.
- Generate and refine damage masks using image processing techniques.
- Restore selected regions using OpenCV's TELEA inpainting algorithm.
- View original and restored photographs side by side.
- Visualize the detected damage mask.
- Download the restored photograph.
- Explore the underlying restoration process through a Jupyter notebook.

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **Image Processing:** OpenCV
- **Numerical Operations:** NumPy
- **Visualization:** Matplotlib
- **Development Environment:** VS Code, Jupyter Notebook

## Project Structure

```text
PhotoRestore/
│
├── app.py                                  # Streamlit application
├── restoration.py                          # Image restoration logic
├── requirements.txt                        # Python dependencies
├── .gitignore
├── README.md
│
├── Inpainting to Restore Damaged Photos.ipynb
│
├── damaged_01.jpg
└── damaged_02.jpg
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 installed.
- Git installed.
- Visual Studio Code (recommended).
- Python and Jupyter extensions in VS Code (for notebook usage).

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Prithviraj383/Old-Photograph-Restoration.git
```

Navigate into the project directory:

```bash
cd Old-Photograph-Restoration
```

### 2. Create a virtual environment

Create an isolated Python environment:

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install all required packages:

```bash
pip install -r requirements.txt
```

### 5. Run the application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your default browser. If it does not, open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## Running the Jupyter Notebook

The original restoration implementation is also available as a Jupyter notebook.

1. Open the project folder in VS Code.
2. Open `Inpainting to Restore Damaged Photos.ipynb`.
3. Select the Python interpreter from the project's `venv`.
4. Select the corresponding notebook kernel.
5. Run the notebook cells.

## How It Works

The restoration process uses OpenCV's image inpainting functionality.

1. **Grayscale Conversion:** Convert the input photograph into grayscale.
2. **Thresholding:** Identify potential damaged regions based on pixel intensity.
3. **Mask Generation:** Create a binary mask identifying regions selected for restoration.
4. **Mask Dilation:** Expand the selected regions to cover surrounding damaged pixels.
5. **Image Inpainting:** Reconstruct the masked regions using the TELEA algorithm.

The application uses the `cv2.inpaint()` function with `cv2.INPAINT_TELEA`.

**Note:** The current implementation uses brightness-based thresholding. Consequently, it may not accurately detect every type of scratch or damage, especially when damaged regions have similar brightness to their surroundings.

## Limitations

- Works best for relatively small scratches and damaged regions.
- Large missing sections may not be reconstructed accurately.
- Automatic damage detection can mistakenly select naturally bright regions.
- The current implementation does not perform AI-based face restoration or photograph colorization.

## Future Improvements

- Interactive manual damage selection.
- Improved automatic damage detection.
- Adjustable restoration parameters.
- Side-by-side interactive image comparison.
- Advanced restoration techniques for faces and severely damaged photographs.

## License

This project is intended for educational and learning purposes.