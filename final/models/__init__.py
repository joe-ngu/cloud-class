model_backend = "datastore"

if model_backend == "datastore":
    from .model_datastore import QuotesModel
else:
    raise ValueError("No appropriate databackend configured.")

model = QuotesModel()

def get_model():
    return model
