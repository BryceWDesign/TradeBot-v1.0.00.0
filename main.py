import time
import random
from core.flow_reactor import FlowReactor

def simulate_trade_stream(flow: FlowReactor, duration=10):
    """
    Simulate a stream of random buy/sell trades over a fixed duration.
    Replace this with real websocket data in future steps.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        is_buy = random.choice([True, False])
        flow.register_trade(is_buy)

        action = flow.get_signal()
        if action:
            print(f"[{time.strftime('%X')}] ACTION TRIGGERED: {action}")
            # Cooldown to prevent repeated triggers
            time.sleep(1)
            # Reset the rolling window
            flow.buy_events.clear()
            flow.sell_events.clear()

        time.sleep(random.uniform(0.1, 0.3))  # Simulate trade frequency

if __name__ == "__main__":
    print("Starting TradeBot Flow Reactor...")
    reactor = FlowReactor(buy_threshold=3, sell_threshold=3, window_seconds=1.0)
    simulate_trade_stream(reactor, duration=30)
    print("Simulation complete.")
