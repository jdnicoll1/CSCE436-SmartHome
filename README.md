CSCE 436 Semester Project Prototype - Smart Home System

This project intends to streamline smart home application use by allowing users to control systems using their hands

To run project (on windows machine/using powershell): **Note wsl won't be able to access webcam 
    1. Open project directory in command line 
    2. Create python virtual environment
        a. Make sure you are running Python 3.10 in powershell by typing: python --version
        b. Run: python -3.10 -m venv venv
        c. Run: .\venv\Scripts\activate
            - This will activate the virtual environment - helps with development since we are all on different machines
        d. Run: python -m pip install --upgrade pip 
        e. Run: pip install -r requirements.txt
        d. Run: main.py
    3. When developing - if adding any dependencies add them to requirements.txt using: pip freeze > requirements.txt
    
