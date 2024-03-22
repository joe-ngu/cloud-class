# model_backend = "sqlite3"
model_backend = "datastore"

if model_backend == "datastore":
    from .model_datastore import FoodsModel
elif model_backend == "sqlite3":
    from .model_sqlite3 import FoodsModel
else:
    raise ValueError("No appropriate databackend configured.")

model = FoodsModel()

def get_model():
    return model
