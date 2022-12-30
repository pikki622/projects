import pandas as pd


def sepal_area(upstream):
    """Compute sepal area
    """
    data = upstream['get']
    ft = data['sepal length (cm)'] * data['sepal width (cm)']
    return pd.DataFrame({'sepal area (cm2)': ft})


def petal_area(upstream):
    """Compute petal area
    """
    data = upstream['get']
    ft = data['petal length (cm)'] * data['petal width (cm)']
    return pd.DataFrame({'petal area (cm2)': ft})


def features(upstream):
    """Join raw data with generated features
    """
    first = upstream['get']
    sepal = upstream['sepal-area']
    petal = upstream['petal-area']
    df = first.join(sepal).join(petal)

    # make sure features are always generated in the same order
    df = df[sorted(df.columns)]

    return df
