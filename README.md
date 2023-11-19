# analyze-ur-youtube

Analyze your YouYube video.

# Runtimes and Package Managers

- runtime version 정보는 `.tool-versions` 파일에 명시되어 있습니다.

## Frontend

- nodejs 18.18.2
- npm 9.8.1

## Backend

- python 3.12.0
- pipenv 2023.11.15

# How to Run

## Frontend

```zsh
cd frontend
npm install
npm run dev
```

## Backend

```zsh
pip install pipenv
cd backend
pipenv install
pipenv run uvicorn main:app --reload
```
