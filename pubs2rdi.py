import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    KAUST Publications to RDI
    =========================

    Exporting KAUST publications to explore if they align with the RDI priorities.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    import duckdb as ddb
    import polars as pl
    import sqlglot
    import os

    from dotenv import load_dotenv
    return (mo,)


@app.cell
def _():
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * FROM
        """
    )
    return


if __name__ == "__main__":
    app.run()
