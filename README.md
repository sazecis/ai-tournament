## Overview

This project is designed to facilitate real-time chat communication through a client-server architecture. It is comprised of three main components, each residing in its own dedicated directory:

- `chat-client`: This directory contains the implementation of the chat client. It is built using Python and incorporates socket.io for communication. Within this directory, there is:
  - A Python socket.io client that establishes and maintains a connection with the chat server.
  - A command-line interface (CLI) for single-threaded chat communication, enabling to interact with an LLM which you configure.
  - A collection of games that can be played together with miltiple LLMs.

- `chat-server`: This directory houses the chat server, which is implemented using Flask and Flask-SocketIO in Python. It acts as the central hub for message exchange between clients.

- `chat-service`: In this directory, you will find the front-end React application that provides a user interface for chat dialogue. This web-based service allows users to interact with the chat system through a graphical interface, improving accessibility and usability.

Additionally, there is a `logs` folder that contains text files logging interactions between GPTs. These logs are crucial for monitoring and analyzing the behavior of the chatbots within the system.

## Directory Structure
```plaintext
project-root/
│
├── chat-client/
│ ├── Python socket.io client
│ ├── Single-threaded chat command line
│ └── Games
│
├── chat-server/
│ └── Python Flask SocketIO chat server
│
├── chat-service/
│ └── React web server for UI chat dialogue
│
└── logs/
└── Interaction logs between GPTs
```

## Getting Started

This project is organized into separate components, each with its own dedicated folder and `README.md` file. These individual `README.md` files contain detailed instructions on installation, configuration, and usage specific to that component. To get started with a particular part of the project, please refer to its corresponding `README.md`:

- **chat-client:** [chat-client/README.md](./chat-client/README.md) - Contains information on setting up and using the Python socket.io client, the command-line interface for chat, and the included games.

- **chat-server:** [chat-server/README.md](./chat-server/README.md) - Provides details on how to set up and run the Python Flask SocketIO chat server.

- **chat-service:** [chat-service/README.md](./chat-service/README.md) - Offers guidance on setting up the React web server for the UI chat dialogue.

For logging interactions between GPTs, refer to the logs stored in the `logs` folder. This folder does not contain a `README.md` as it is primarily used for storage of log files.

Please follow the links above to find more about each component and how to get them up and running.


## Contributing

We welcome contributions from the community! If you would like to contribute to this project, please follow these steps:

1. **Fork the Repository**
   - Navigate to the GitHub page of this project.
   - Click on the "Fork" button at the top right corner to create a copy of this repository in your GitHub account.

2. **Clone Your Forked Repository**
   - Clone the forked repository to your local machine to make changes.
   - Use the command `git clone https://github.com/your_username/project-name.git`, replacing `your_username` with your GitHub username and `project-name` with the name of this project.

3. **Create a New Branch**
   - Move into the newly cloned directory using `cd project-name`.
   - Create a new branch for your changes with `git checkout -b your-branch-name`, replacing `your-branch-name` with a descriptive name for your branch.

4. **Make Your Changes**
   - Implement your changes, fixes, or improvements in your branch.
   - Ensure to follow the project's coding standards and guidelines.

5. **Commit Your Changes**
   - Stage your changes with `git add .` or `git add path/to/your/file`.
   - Commit your changes with a meaningful commit message using `git commit -m "A brief description of your changes"`.

6. **Push Your Changes**
   - Push your changes to your forked repository with `git push origin your-branch-name`.

7. **Submit a Pull Request**
   - Go to your forked repository on GitHub.
   - Click on "Pull Request" and then on "New Pull Request".
   - Select your branch and provide a detailed description of your changes and the reasons for them.
   - Submit your pull request.

Your pull request will be reviewed by the maintainers, and they will provide feedback or merge it after a thorough review.

Please note that contributing to this project means you agree to abide by its contribution guidelines and code of conduct.

## Code of Conduct

This project adheres to a Code of Conduct to ensure a welcoming and inclusive environment for everyone who wants to contribute or participate in discussions, issues, and pull requests. By participating in this project, you agree to abide by its terms.

### Our Standards

We are committed to providing a friendly, safe, and welcoming environment for all.

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [your email]. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident.

## License

This project is licensed under the Apache License, Version 2.0 (the "License"); you may not use this project's files except in compliance with the License. A copy of the License is located in the `LICENSE.txt` file in the root directory of this project.

You may also obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
