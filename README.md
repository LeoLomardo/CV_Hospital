# ICU Patient Monitoring with Computer Vision

This project uses **Computer Vision** to monitor ICU patients in real time, detecting their body position (e.g., lying, sitting, leaving the bed) and generating alerts to help prevent falls and accidents.

All the instructions were created for the Windows environment, simply because I had to choose between macOS and Windows.

## Requirements

- Python **3.11** (strictly required)
- `pip`
- Windows (tested) or other platforms with equivalent configuration

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Make Sure Python 3.11 is Installed

Run this command to verify:

```bash
python3.11 --version
```

Or, using the Windows launcher:

```bash
py -3.11 --version
```

> If not installed, [download Python 3.11 here](https://www.python.org/downloads/release/python-3110/) and ensure you check "Add Python to PATH" during installation.

### 3. Create a Virtual Environment with Python 3.11

```bash
py -3.11 -m venv .venv_311
```

### 4. Activate the Environment

- On **CMD**:

```cmd
.venv_311\Scripts\activate.bat
```

> If you see an error about execution policies, run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```


## Notes

- The system updates bed detection dynamically every few frames, you can change that.
- Alerts are triggered when a patient moves legs outside the bed or leaves it.

## Author

Leo Lomardo – [contact@leolomardo.com]

