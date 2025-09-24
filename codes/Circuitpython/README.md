# CircuitPython Setup
Download and install [Thonny](https://thonny.org/).  

Download and install [CircuitPython](https://circuitpython.org/downloads)

---

### 1. Connect Your Board & Enter Bootloader
- Plug the board into your computer using a data USB cable
- Enter Bootloader depending on your board by
    - Press hold and release the reset button on your board
    - Press the reset button on your board twice rapidly

### 2. Download Required Libraries
If your board requires extra libraries:
- Download the [CircuitPython Library](https://circuitpython.org/libraries).  
- Unzip the bundle
- Copy the required `.mpy` files or library folders into the `lib` folder on **CIRCUITPY**.

### 3.  Place Code
Take the `code.py` from the repo and place it into the root of **CIRCUITPY**.  

### 4. Edit & Save Code
Open `code.py` in Thonny, or another editor. Make any custom modifications you need at this point. Save the file, the board will automatically restart and run the code.


The Taiko Controller should be ready to use.