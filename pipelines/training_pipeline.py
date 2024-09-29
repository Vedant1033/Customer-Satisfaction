from zenml import pipelines
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.evaluation import evalutate_model

@pipelines()
def train_pipeline(data_path):
    df=ingest_df(data_path)
    df=clean_df(df)
    evalutate_model(df)


