import flwr as fl

def start():
    strategy = fl.server.strategy.FedAvg()

    fl.server.start_server(
        server_address="localhost:8081",
        config=fl.server.ServerConfig(num_rounds=3),
        strategy=strategy,
    )

if __name__ == "__main__":
    start()