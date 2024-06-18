class OllamaModel:
    def __init__(self, name, model, modified_at, size, digest, details):
        self.name = name
        self.model = model
        self.modified_at = modified_at
        self.size = size
        self.digest = digest
        self.details = details

    def __repr__(self):
        return f"OllamaModel(name={self.name}, model={self.model}, modified_at={self.modified_at}, size={self.size}, digest={self.digest}, details={self.details})"