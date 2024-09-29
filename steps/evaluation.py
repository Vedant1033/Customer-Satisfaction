import logging
import pandas as pd
from zenml import step


@step
def evalutate_model(df: pd.DataFrame) -> None:
    """
    Evaluates the model on the ingested ata.
    Args:
        df:the ingested data
    """
    pass