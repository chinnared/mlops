from mlflow import MlflowClient

def register_model(model_name, model_uri, run_id):

    client = MlflowClient()

    try:
        client.create_registered_model(model_name)
    except:
        pass

    version = client.create_model_version(
        name=model_name,
        source=model_uri,
        run_id=run_id
    )

    return int(version.version)


def promote_model(model_name, version):
    client = MlflowClient()

    client.set_registered_model_alias(
        name=model_name,
        alias="prod",
        version=str(version)
    )