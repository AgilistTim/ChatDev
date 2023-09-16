# ChatDev Chrome Plugin User Manual

## Introduction

The ChatDev Chrome Plugin is a tool that securely accesses the Jira API and passes details to the ChatGPT 4 API, enabling users to chat with Jira in a context-specific manner. This plugin allows for seamless communication with Jira and provides a convenient way to interact with Jira data within the ChatGPT environment.

## Installation

To install the ChatDev Chrome Plugin, please follow these steps:

1. Open your Google Chrome browser.
2. Go to the Chrome Web Store.
3. Search for "ChatDev Chrome Plugin" in the search bar.
4. Click on the "Add to Chrome" button next to the ChatDev Chrome Plugin.
5. Confirm the installation by clicking on "Add extension" in the pop-up window.

## Dependencies

The ChatDev Chrome Plugin requires the following dependencies:

- Python 3.7 or higher
- tkinter 8.6
- requests 2.26.0

To install the dependencies, please run the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage

Once the ChatDev Chrome Plugin is installed, you can start using it by following these steps:

1. Open your Google Chrome browser.
2. Navigate to a Jira page.
3. Click on the ChatDev Chrome Plugin icon in the browser toolbar.
4. A chat window will appear, allowing you to interact with Jira using the ChatGPT 4 API.
5. Enter your message in the chat window and press Enter to send it.
6. The ChatGPT 4 API will process your message and provide a response based on the Jira context.
7. Continue the conversation by entering additional messages.

## Security

The ChatDev Chrome Plugin ensures the secure storage of API keys by using environment variables. The JIRA_API_KEY and CHATGPT_API_KEY environment variables should be set with the respective API keys before running the plugin. This ensures that the API keys are not exposed in the source code and are securely stored on the user's machine.

To set the environment variables, please follow these steps:

1. Open your terminal.
2. Run the following commands:

```
export JIRA_API_KEY=<your_jira_api_key>
export CHATGPT_API_KEY=<your_chatgpt_api_key>
```

Replace `<your_jira_api_key>` and `<your_chatgpt_api_key>` with your actual API keys.

## Troubleshooting

If you encounter any issues while using the ChatDev Chrome Plugin, please try the following troubleshooting steps:

1. Make sure you have set the JIRA_API_KEY and CHATGPT_API_KEY environment variables correctly.
2. Check your internet connection to ensure you can access the Jira and ChatGPT APIs.
3. Verify that you have installed the required dependencies listed in the requirements.txt file.
4. Restart your browser and try again.

If the issue persists, please contact our support team for further assistance.

## Conclusion

The ChatDev Chrome Plugin provides a seamless integration between Jira and the ChatGPT 4 API, allowing users to interact with Jira in a context-specific manner. By securely accessing the Jira API and passing details to the ChatGPT 4 API, this plugin enables efficient communication and enhances productivity within the Jira environment.

If you have any questions or feedback, please don't hesitate to reach out to our support team. We are here to help you make the most of the ChatDev Chrome Plugin.