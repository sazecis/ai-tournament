# Chat Server

This directory contains the chat server application for our project, implemented using Flask and SocketIO in Python. The chat server acts as the central communication hub between clients. Follow these instructions to set up and run the chat server.

## Prerequisites

Before you begin, ensure you have Python and `pip` installed on your system. This project requires Python 3.6 or newer.

### Installing Python and pip

- **Windows:** Download the latest version of Python from the [official website](https://www.python.org/downloads/). During installation, make sure to check the box that says "Add Python to PATH" to ensure the command line recognizes Python and pip commands.

- **macOS:** Python 2.7 is installed by default on macOS, but you can install Python 3 via Homebrew with the command `brew install python`. This will also install `pip` alongside Python 3.

- **Linux:** Most Linux distributions come with Python pre-installed. However, you may need to install Python 3 and pip using your package manager, for example, `sudo apt-get install python3 python3-pip` on Debian/Ubuntu.

## Setting Up the Environment

1. Open a terminal or command prompt.
2. Navigate to the project's `chat-server` directory.
3. Install the required dependencies using `pip`:

```bash
    pip install -r requirements.txt
```

## Starting the Chat Server

With the prerequisites installed and the environment set up, you can start the chat server by running the following command in the `chat-server` directory:

```bash
    python server.py
```

This will start the Flask server with SocketIO, listening for incoming connections from clients.

## Next Steps

Once the chat server is running, you can proceed to start the client applications. Refer to their respective README files for instructions:

- **Chat Client:** See the [chat-client README.md](../chat-client/README.md) for details on running the Python chat client.
- **Chat Service:** For the React web interface, check the [chat-service README.md](../chat-service/README.md).

### Important Notes

- Ensure the chat server is running before attempting to connect with the chat client or chat service to ensure successful communication between the components.
- The server configuration (e.g., port number) can be adjusted in `server.py` based on your specific requirements.

By following these steps, you have successfully set up and started the chat server, which is crucial for the operation of the entire chat application ecosystem.
