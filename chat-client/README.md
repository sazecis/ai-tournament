# Chat Client

This directory contains the chat client application for our project. It is built using Python and utilizes Socket.IO for real-time communication. Follow the steps below to set up your environment and run the chat client.

## Prerequisites

Before you begin, ensure you have Python and `pip` installed on your system. This project requires Python 3.6 or newer.

### Installing Python and pip

- **Windows:** Download the latest version of Python from the [official website](https://www.python.org/downloads/). During installation, make sure to check the box that says "Add Python to PATH" to ensure the command line recognizes Python and pip commands.

- **macOS:** Python 2.7 is installed by default on macOS, but you can install Python 3 via Homebrew with the command `brew install python`. This will also install `pip` alongside Python 3.

- **Linux:** Most Linux distributions come with Python pre-installed. However, you may need to install Python 3 and pip using your package manager, for example, `sudo apt-get install python3 python3-pip` on Debian/Ubuntu.

## Setting Up a Virtual Environment

It's recommended to use a virtual environment for Python projects. This keeps dependencies required by different projects in separate places. To create a virtual environment, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project's `chat-client` directory.
3. Run the following command to create a virtual environment named `venv`:

```bash
    python3 -m venv venv
```

4. Activate the virtual environment:
   - **Windows:**
   
         venv\Scripts\activate

   - **macOS/Linux:**
   
         source venv/bin/activate

   You should now see `(venv)` in the terminal, indicating that the virtual environment is active.

## Installing Dependencies

With the virtual environment activated, install the project dependencies using `pip`:

```bash
    pip install -r requirements.txt
```

This command reads the `requirements.txt` file in the current directory and installs all the listed packages.

# AI Engine API Keys

To integrate AI functionalities into the chat client, you will need to set up API keys for various AI engines. Follow the instructions below to prepare your environment.

## Setup

Create a folder within the `chat-client` directory named `keys`. Inside this folder, you will create files to store your API keys securely. The `keys` folder is already added to `.gitignore` so your keys won't be added to the repo.

### OpenAI ChatGPT API Key

1. **File Creation**: In the `keys` folder, create a file named `chatgpt_api.py`.
2. **Content**: Add the following code to `chatgpt_api.py`, replacing `"string API key of OpenAI"` with your actual OpenAI API key.

    ```python
    key="string API key of OpenAI"
    ```

#### How to Get an OpenAI API Key

- Visit the OpenAI website and sign up for an account or log in if you already have one.
- Navigate to the API section and follow the instructions to subscribe to a plan. OpenAI provides different subscription plans, including free tiers with limited usage.
- Once subscribed, you will be able to access your API key. Copy this key and use it in the `chatgpt_api.py` file.

### GCP Vertex AI API Key

1. **File Creation**: In the `keys` folder, create another file named `gemini_api.py`.
2. **Content**: Add the following code to `gemini_api.py`, replacing the placeholders with your GCP project ID and the location of the key file.

    ```python
    project_id="GCP project id"
    key_location="location of the file received from GCP required for VertexAI"
    ```

#### What is GCP and Vertex AI?

**Google Cloud Platform (GCP)** is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products. **Vertex AI** is a managed machine learning platform by Google Cloud that allows you to easily build, deploy, and scale AI models.

#### How to Create a GCP Project and Obtain Vertex AI API Keys

- Visit the [Google Cloud Console](https://console.cloud.google.com/) and sign in with your Google account.
- Create a new project by selecting "IAM & Admin" > "Create a Project". Follow the prompts to set up your new project.
- Once your project is created, navigate to the "APIs & Services" dashboard. Here, you can enable the APIs you need, such as Vertex AI.
- To access Vertex AI services, you'll need to create service account credentials. Go to "IAM & Admin" > "Service Accounts", create a new service account, and assign it a role that grants access to Vertex AI services.
- After creating the service account, create a key for it (in JSON format). This key file is what you'll reference in the `gemini_api.py` file as `key_location`.
- Remember to enable billing for your GCP project to use Vertex AI services.

Ensure that the API keys and credentials are kept secure and are not exposed publicly in your repository. Always refer to the official documentation of OpenAI and Google Cloud for the most up-to-date and detailed instructions.


## Running the Chat Client

Before you can run the chat client, you must ensure that the `chat-server` is up and running. Please refer to the [chat-server README.md](../chat-server/README.md) for instructions on how to start the chat server.

### Starting the Chat Client

The chat client can be started with a specific argument to select the AI engine or simulation mode you wish to use. Here are the available options:

- `ChatGPT`: Starts the chat client using the ChatGPT engine for generating responses.
- `Gemini`: Utilizes the Gemini engine for response generation.
- `Simulator<N>`: Launches a client simulator allowing manual responses to messages, where `<N>` is a numeric value that specifies the simulation instance for differentiation.

#### Command to Start the Chat Client

To run the chat client, navigate to the `chat-client` directory in your terminal or command prompt. Use the following command structure, replacing `<EngineOrMode>` with your chosen option (`ChatGPT`, `Gemini`, or `Simulator<N>`):

```bash
    python chat_client.py <EngineOrMode>
```

#### Examples

- To start the chat client with the ChatGPT engine:

```bash
      python chat_client.py ChatGPT
```

- To use the Gemini engine:

```bash
      python chat_client.py Gemini
```

- To launch a simulator instance (for example, simulator number 1):

```bash
      python chat_client.py Simulator1
```

### Important Notes

- Ensure that your API keys for the ChatGPT and Gemini engines are correctly set up in the `keys` directory before attempting to use these engines.
- The simulator mode does not require an internet connection or API keys, as it is intended for testing and manual interaction. Multiple Simulator instances can be started.

By following these instructions, you can easily switch between different engines or simulation modes to best suit your testing or usage scenarios.

## Other Options

Aside from the standard chat functionalities, this application offers several unique features that enhance the interaction with AI engines and the engagement level of the platform.

### Chat Directly with AI Engines

To chat directly with one of the engines:

- Start the interaction using the `chat.py` script.

  To switch between the AI engines (e.g., from Gemini to ChatGPT), you need to change the class in the `chat.py` code. For example, you can modify the script to use a different class for the engine you wish to interact with. ChatGPT can be used directly from OpenAI. However, for the Gemini engine, I created this chat platform to facilitate the interaction.

### Allow the AIs to Play Games Together

The platform also allows AI engines to play games against each other:

- To initiate a game, use the `lets_play.py` script. For example, to start a game of knock-knock, you would run this script. You can see a list of available games in `games/games.py`.

  To switch between games, modify the `lets_play.py` script by changing the game variable. For example:
    
```bash
      game=Games.KnockKnock
```

- Another game available is `black_jack.py`, which is a moderated game with a dealer. Please note, this is in an early prototype phase and might not have full functionality yet.

#### Examples

To start a direct chat with an AI engine, navigate to the `chat-client` directory and run:

```bash
    python chat.py
```

To let AIs play a game together, first check the available games in `games/games.py`, then run:

```bash
    python lets_play.py
```

And to try out the prototype game of Black Jack:

```bash
    python black_jack.py
```

### Important Notes

- Remember to adjust the AI engine settings in `chat.py` and `lets_play.py` as needed to switch between engines or games.
- The `black_jack.py` game is an early prototype and may not fully represent the final intended functionality.

This section expands your chat application's capabilities beyond simple message exchanges, offering engaging and dynamic interactions between users and AI or AI vs. AI in gaming scenarios.


## Conclusion

You have now set up and configured the chat client for our project. For more details on how to use the chat client, refer to the following sections of this README.


