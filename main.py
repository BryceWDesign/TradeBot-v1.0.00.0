import time
import random
import json
from core.flow_reactor import FlowReactor

def load_config(path="config/config.json"):
    with open(path, "r") as f:
        return json.load(f)

def simulate_trade_stream(flow, config):
    start_time = time.time()
    cooldown = config["cooldown_seconds"]
    min_interval = config["min_trade_interval"]
    max_interval = config["max_trade_interval"]
    duration = config["simulation_duration_seconds"]

    print("Simulation started...")
    while time.time() - start_time < duration:
        is_buy = random.choice([True, False])
        flow.register_trade(is_buy)

        action = flow.get_signal()
        if action:
            print(f"[{time.strftime('%X')}] ACTION TRIGGERED: {action}")
            time.sleep(cooldown)
            flow.buy_events.clear()
            flow.sell_events.clear()

        time.sleep(random.uniform(min_interval, max_interval))

    print("Simulation complete.")

if __name__ == "__main__":
    print("Starting TradeBot Flow Reactor...")
    config = load_config()
    reactor = FlowReactor(
        buy_threshold=config["buy_threshold"],
        sell_threshold=config["sell_threshold"],
        window_seconds=config["window_seconds"]
    )
    simulate_trade_stream(reactor, config)
