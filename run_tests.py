# run_tests.py
import pytest
import sys

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode == "ui":
        pytest.main(["-s", "test/test_ui.py"])
    elif mode == "api":
        pytest.main(["-s", "test/test_api.py"])
    else:
        pytest.main(["-s", "test/"])
