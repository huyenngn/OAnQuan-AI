# Ô ăn quan AI

![image](https://github.com/huyenngn/oanquan/actions/workflows/build-test.yml/badge.svg)
![image](https://github.com/huyenngn/oanquan/actions/workflows/lint.yml/badge.svg)

A web-based game of Ô ăn quan with AI player.

# Development

To set up a development environment, clone the project and install it into a virtual environment.

```sh
git clone https://github.com/huyenngn/oanquan
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
python -m oanquan_ai
```

The backend server will be running at `http://localhost:8000` and the live frontend will be served at `http://localhost:5173`.
