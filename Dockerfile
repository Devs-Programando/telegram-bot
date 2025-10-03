# Use a slim and modern Python base image
FROM python:3.13-slim


WORKDIR /app


RUN pip install uv


COPY pyproject.toml ./

#não recomendo diretamente utilizar --system em produção ou no seu setup sem avaliar antes!
RUN uv pip install --system --no-cache .


COPY . .

# uv run utiliza o seu ambiente do uv, entenda que o uv pega para si a tarefa de gerenciar o ambiente e as deps do ambiente
CMD ["uv", "run", "python", "src/main.py"]
