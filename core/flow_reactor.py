import time
from collections import deque

class FlowReactor:
    def __init__(self, buy_threshold=3, sell_threshold=3, window_seconds=1.0):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.window_seconds = window_seconds
        self.buy_events = deque()
        self.sell_events = deque()

    def _prune(self, events):
        """Remove old events outside the rolling window."""
        now = time.time()
        while events and (now - events[0]) > self.window_seconds:
            events.popleft()

    def register_trade(self, is_buy: bool):
        """Register a new trade tick."""
        now = time.time()
        if is_buy:
            self.buy_events.append(now)
            self._prune(self.buy_events)
        else:
            self.sell_events.append(now)
            self._prune(self.sell_events)

    def get_signal(self):
        """Check if buy/sell pressure has crossed the threshold."""
        self._prune(self.buy_events)
        self._prune(self.sell_events)

        if len(self.buy_events) >= self.buy_threshold:
            return "BUY"
        elif len(self.sell_events) >= self.sell_threshold:
            return "SELL"
        else:
            return None
