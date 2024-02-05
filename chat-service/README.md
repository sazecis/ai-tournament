# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Prerequisites for Chat Service

Before you can run the chat service, you need to have Node.js and npm (Node Package Manager) installed on your system. Node.js is a runtime environment that allows you to run JavaScript on the server side, and npm is a package manager for JavaScript that enables you to install and manage project dependencies. Follow these steps to install Node.js and npm:

### Installing Node.js and npm

- **Windows and macOS:**
  - Visit the [Node.js official website](https://nodejs.org/) and download the installer for your operating system. The installer includes both Node.js and npm.
  - Run the downloaded installer, following the prompts to install Node.js and npm. The installer will add `node` and `npm` commands to your system's PATH, making them accessible from any command prompt or terminal.

- **Linux:**
  - The installation process for Node.js and npm on Linux can vary depending on your distribution. For most distributions, you can install Node.js and npm using your package manager.
  - For Debian and Ubuntu based distributions, you can use the following commands:

```bash
    sudo apt update
    sudo apt install nodejs npm
```
    
  - For other distributions, please refer to the Node.js [installation instructions](https://nodejs.org/en/download/package-manager/) specific to your distribution.

### Verifying Installation

After installing, you can verify that Node.js and npm are correctly installed by running the following commands in your terminal or command prompt:

```bash
    node --version
    npm --version
```

These commands should display the installed versions of Node.js and npm, respectively.

### Starting the Chat Service

With Node.js and npm installed, navigate to the `chat-service` directory in your terminal or command prompt and run:

```bash
    npm install
```

This command installs all the dependencies defined in the `package.json` file. After the installation is complete, you can start the chat service by running:

```bash
    npm start
```

This will start the React application on a local development server, usually accessible via `http://localhost:3000` in your web browser.

By following these steps, you will have set up the necessary environment to run the chat service component of our project.


## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
