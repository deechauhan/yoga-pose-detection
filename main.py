"""Main camera launcher.

This launcher should be able to:
    1. Choose from multiple cameras
    2. Call any dependency to add overlay in realtime
"""
from controllers.launcher import run

if __name__ == "__main__":
    run()  # type: ignore[call-arg]
