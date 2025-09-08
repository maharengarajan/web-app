# web-app

# download uv
``` bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

# create virtual environment
``` bash
uv venv
``` 

# activate virtual environment
``` bash
.venv\Scripts\activate
``` 

# initialize uv
``` bash
uv init
```

# install requirements
``` bash
uv add -r requirements.txt
```

# run test cases
``` bash
python -m pytest tests/test_calculator.py
```

# run the app locally
``` bash
uv run app.py
```