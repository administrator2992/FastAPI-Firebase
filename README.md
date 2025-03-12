# FastAPI-Firebase
API App w/ Firebase Database

## Prerequirement
You need :
- Terminal/CMD
- Python >3.7

## Step 1 (Recommended)
Prepare the Python virtual environment 
```bash
python -m venv <your-env-name>
```
## Step 2 (Recommended)
Activate the Python virtual environment

| Platform | Shell      | Command to activate virtual environment          |
|----------|------------|------------------------------------------------|
| POSIX    | bash/zsh   | `$ source <venv>/bin/activate`                 |
|          | fish       | `$ source <venv>/bin/activate.fish`            |
|          | csh/tcsh   | `$ source <venv>/bin/activate.csh`             |
|          | pwsh       | `$ <venv>/bin/Activate.ps1`                    |
| Windows  | cmd.exe    | `C:\> <venv>\Scripts\activate.bat`              |
|          | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1`          |

## Step 3
Install the requirements
```bash
pip install -r requirements.txt
```

## Step 4
Download your firebase-adminsdk.json in your Firebase account after creating the project


## Step 5
Execute API app by using uvicorn
```bash
uvicorn main:app --reload --port <your-port>
```
## Step 6
Enter `http://<your-ip-network>:<your-port>/docs` to access Swagger UI

## Last Step
Viola, you can Create, Read, Update, and Delete (CRUD) the data through Swagger UI. Please check the schemas for the input
