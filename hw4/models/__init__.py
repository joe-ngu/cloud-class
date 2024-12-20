model_backend = "datastore"


#match model_backend:
#    case 'sqlite3':
#        from .model_sqlite3 import QuotesModel
#    case 'datastore':
#        from .model_datastore import QuotesModel
#    case _:
#        raise ValueError("No appropriate databackend configured.")

if model_backend == "sqlite3":
    from .model_sqlite3 import QuotesModel
elif model_backend == "datastore":
    from .model_datastore import QuotesModel
else:
    raise ValueError("No appropriate databackend configured.")

model = QuotesModel()

def get_model():
    return model
