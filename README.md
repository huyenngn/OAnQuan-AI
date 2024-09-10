# Ô ăn quan AI

<!-- ![image](https://github.com/huyenngn/oanquan/actions/workflows/build-test.yml/badge.svg)
![image](https://github.com/huyenngn/oanquan/actions/workflows/lint.yml/badge.svg) -->

To play the game, check out the [demonstrator](http://34.44.129.232/).

# Quick Start

You can host the API server and the demonstrator on your own machine.

Create a `.env` file in the demo directory (optional):

```sh
echo "VITE_API_URL=http://{EXTERNAL_IP}:8000" >> demo/.env
```

Build and run the demonstrator with Docker:

```sh
docker compose build
docker compose up
```

The API server will be running at `http://localhost:8000` and the demonstrator will be served at `http://localhost`.

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
