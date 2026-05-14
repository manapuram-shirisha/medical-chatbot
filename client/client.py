import flwr as fl
from model import BERTSymptomExtractor
from preprocessing import load_data

print("Loading BERT...")
extractor = BERTSymptomExtractor()

print("Loading dataset...")
df = load_data()

print("Extracting features...")
X = [extractor.extract_features(text) for text in df['symptoms']]
y = df['disease'].values

class Client(fl.client.NumPyClient):

    def get_parameters(self, config):
        return []

    def fit(self, parameters, config):
        print("Training round running...")
        return [], len(X), {}

    def evaluate(self, parameters, config):
        print("Evaluating...")
        return 0.0, len(X), {}

print("Starting FL client...")
fl.client.start_numpy_client(server_address="localhost:8081", client=Client())