# Academic Artificial Intelligence Collaboration Graph Builder

This project builds a co-authorship graph using research paper metadata from OpenAlex, using PySpark and NetworkX inside Databricks.

## Features

- Ingest author/paper data from OpenAlex
- Store data in Delta Lake tables
- Build a co-authorship graph using NetworkX
- Run analytics (PageRank, components, etc.)

## Technologies

- Databricks Community Edition
- Apache Spark (PySpark)
- NetworkX
- Delta Lake

## Structure

- `notebooks/`: All notebooks (in `.py` format)
- `libs/`: Utility modules (e.g., parsing helpers)
- `data/`: Notes on how/where data is stored
