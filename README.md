# selenium-py-grid-devcontainer

Demo project that shows how to launch a Python dev container for VS Code with a Selenium Grid sidecar container.

Useful for debugging Python Selenium tests that are written to execute on a Grid server environment.

After opening this project in VS Code, and launching the dev container when prompted:

* Files in the `tests/` directory should be runnable/debuggable with Pytest using the controls in VS Code's `Testing` (Test Explorer) view
* The grid server's VNC port should be mapped to your host at `localhost:5900`, so you can point a VNC client and watch tests execute in Chrome
