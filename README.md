# Ô ăn quan AI

![image](https://github.com/huyenngn/oanquan/actions/workflows/build-test.yml/badge.svg)
![image](https://github.com/huyenngn/oanquan/actions/workflows/lint.yml/badge.svg)

An Ô ăn quan AI.

# Quick Start

Clone, then build and run the API with Docker:

```sh
docker build . -t api
docker run -d -p 8000:8000 api
```

Clone, then build and run the demonstrator with Docker:

```sh
docker build demo -t demo
docker run -d -p 8080:8080 demo
```

The API server will be running at `http://localhost:8000` and the demonstrator will be served at `http://localhost:8080`.

# Development

To set up a development environment, clone the project and install it into a virtual environment.

```sh
git clone https://github.com/huyenngn/OAnQuan-AI.git
cd oanquan
python -m venv .venv

source .venv/bin/activate

pip install -e '.[docs,test]'
```

To develop the frontend, use the following command:

```sh
cd demo
npm install
npm run dev
```

To run the backend, use the following command:

```sh
python -m oanquan_ai.api
```

The backend server will be running at `http://localhost:8000` and the live frontend will be served at `http://localhost:5173`.
