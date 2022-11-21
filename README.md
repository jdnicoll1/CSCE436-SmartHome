CSCE 436 Semester Project Prototype - Smart Home System__

This project intends to streamline smart home application use by allowing users to control systems using their hands__

To run project (on windows machine/using powershell): **Note wsl won't be able to access webcam__
    1. Open project directory in command line__
    2. Create python virtual environment__
        a. Make sure you are running Python 3.10 in powershell by typing: python --version__
        b. Run: python -3.10 -m venv venv__
        c. Run: .\venv\Scripts\activate__
            - This will activate the virtual environment - helps with development since we are all on different machines__
        d. Run: python -m pip install --upgrade pip__
        e. Run: pip install -r requirements.txt__
        d. Run: main.py__
    3. When developing - if adding any dependencies add them to requirements.txt using: pip freeze > requirements.txt__
    
