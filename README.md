# PhotoRestore – Old Photograph Restoration

A Python-based photograph restoration application that uses **OpenCV Image Inpainting** to detect and reconstruct damaged regions in vintage photographs.

The project combines traditional image processing techniques with a refined **Streamlit "Vintage Studio" web interface**, allowing users to upload damaged photographs, inspect detected damage masks, compare before-and-after results, and download high-resolution restored images.

---

## Features

- **Vintage Studio Interface:** Elegant, archival-inspired UI with warm ivory palette, typography hierarchy, and distraction-free single-page flow.
- **Light & Dark Mode:** Integrated instant theme switcher in the top navigation preserving the Vintage Studio identity in both palettes without losing uploaded photos or restoration state.
- **Format Support:** Upload damaged photographs in **JPG**, **JPEG**, and **PNG** formats, or test directly with bundled archival sample photographs.
- **Robust State Management:** Preserves uploaded photos, restoration results, and damage masks across Streamlit reruns and file downloads without redundant computations.
- **Automatic Damage Detection:** Segment potential surface scratches and tears using intensity thresholding.
- **Morphological Mask Refinement:** Expands detected damage boundaries using a $7 \times 7$ dilation kernel.
- **Alexandru Telea Inpainting:** Reconstructs damaged regions using Fast Marching Method (`cv2.INPAINT_TELEA`) with a 4-pixel radius.
- **Side-by-Side Comparison:** Large, aligned before-and-after photo panels preserving original proportions.
- **Damage Mask Visualization:** Collapsible inspection drawer showing the exact binary mask used for inpainting.
- **High-Resolution Export:** Download the restored image directly in JPEG format.
- **Unit Test Suite:** Automated verification tests ensuring algorithm parameters and output structures remain strictly preserved.

---

## Tech Stack

- **Language:** Python 3.10+
- **Frontend / UI:** Streamlit
- **Image Processing:** OpenCV (`opencv-python`)
- **Numerical Operations:** NumPy
- **Testing:** Python `unittest`
- **Visualization & Research:** Matplotlib, Jupyter Notebook

---

## Project Structure

```text
PhotoRestore/
│
├── app.py                                  # Main Streamlit application entry point
├── restoration.py                          # Core image restoration engine (unmodified)
│
├── ui/                                     # Vintage Studio UI module
│   ├── __init__.py                         # Package initialization
│   ├── styles.py                           # Typography, color tokens, and custom CSS
│   └── components.py                       # Modular layout components (header, hero, cards)
│
├── assets/                                 # Static assets & photograph samples
│   ├── logo.png                            # Vintage Studio emblem
│   └── sample_images/                      # Preserved archival test photographs
│       ├── damaged_04.jpg
│       ├── damaged_05.jpg
│       ├── damage_03.png
│       ├── Original Damaged Photo.png
│       └── Restored.png
│
├── notebooks/                              # Experimental research
│   └── restoration_experiments.ipynb       # Jupyter notebook with algorithm steps
│
├── tests/                                  # Test suite
│   └── test_restoration.py                 # Unit tests for restoration engine
│
├── .streamlit/                             # Streamlit configuration
│   └── config.toml                         # Theme colors and server options
│
├── requirements.txt                        # Python dependencies
├── README.md                               # Project documentation
└── .gitignore                              # Git exclusion rules
```

---

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 or higher installed.
- Git installed.
- Visual Studio Code (or your preferred IDE).

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Prithviraj383/Old-Photograph-Restoration.git
cd Old-Photograph-Restoration
```

### 2. Create a virtual environment

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

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will launch in your default browser at:

```text
http://localhost:8501
```

---

## Running the Test Suite

Run the automated tests to verify the restoration engine and parameter integrity:

```bash
python -m unittest tests/test_restoration.py
```

---

## Running the Jupyter Notebook

The experimental notebook exploring each stage of the inpainting algorithm is located in `notebooks/`:

1. Open the project folder in VS Code.
2. Navigate to `notebooks/restoration_experiments.ipynb`.
3. Select your virtual environment Python kernel (`venv`).
4. Execute the cells sequentially.

---

## How It Works

The restoration engine is based on classical computer vision inpainting:

1. **Grayscale Conversion:** The input BGR image is converted to grayscale (`cv2.COLOR_BGR2GRAY`) to isolate luminance from color fading.
2. **Thresholding:** Pixels with an intensity value exceeding 195 are classified as potential scratch/tear damage (`cv2.threshold` with `cv2.THRESH_BINARY`).
3. **Damage Mask Generation:** A binary matrix is generated where white pixels ($255$) indicate regions requiring reconstruction.
4. **Mask Dilation:** A $7 \times 7$ rectangular structuring element (`np.ones((7, 7), np.uint8)`) expands damage borders by 1 iteration to cover scratch perimeters.
5. **TELEA Inpainting:** The Fast Marching Method (`cv2.inpaint` with `cv2.INPAINT_TELEA` and radius $4$) synthesizes values within damaged regions from neighboring undamaged pixels.

---

## Known Limitations

- **Threshold Sensitivity:** The current algorithm identifies damage through brightness thresholding ($> 195$). Scratches that are darker than their surroundings or low in contrast may not be detected automatically.
- **Large Missing Regions:** Best suited for narrow cracks, scratches, and dust marks. Large structural voids cannot be plausibly synthesized without semantic priors.
- **Bright Photograph Details:** Naturally bright elements (e.g., white clothing, clouds) that exceed the 195 threshold may be marked for inpainting.
- **Traditional Computer Vision:** The application intentionally does not use deep learning or generative diffusion models; it does not hallucinate missing facial features.

---

## License & Academic Note

This project was developed for an academic Image Processing subject. All restoration algorithms are deterministic and implemented with OpenCV.
