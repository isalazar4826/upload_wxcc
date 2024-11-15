
# Audio File Replacement Application in Webex Contact Center

This Flask application allows users to upload and replace audio files via a `PUT` request to the Cisco Webex Contact Center API. Users can upload an audio file through a web interface, and the application sends this file to the API to replace an existing audio file.

## Project Description

This project consists of a basic web server built with Flask that:
1. Allows users to upload audio files from te PC through a web form.
2. Makes a request to the Cisco API to replace an existing audio file in the Webex Contact Center system.
   
- This is the API https://developer.webex-cx.com/documentation/audio-files/v1/update-audio-file-by-id

This application is useful for managing audio files in contact center systems, enabling easy administration of audio messages and other files needed for user communication.

## Code Structure

- `app.py`: Main application code that handles file uploads, validation, and communication with the Cisco API.
- `uploads/`: Folder where uploaded files are temporarily saved.
- `templates/index.html`: HTML template containing the file upload form.

## Requirements

- Python 3.6 or higher
- Flask
- Requests

## Installation

1. Clone this repository.
2. Install the dependencies:

    ```bash
    pip install flask requests
    ```

3. Create an `uploads/` folder in the project root directory (this will be created automatically upon the first run).

## Configuration

Modify the values in `app.py`:

- `{YOUR ORG ID}`: Your organization ID in Webex Contact Center.
- `{ID FILE TO REPLACE}`: The ID of the audio file you want to replace in the Cisco API.
- `{Your TOKEN}`: Authentication token for the Cisco Webex Contact Center API.

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Open `http://localhost:5000` in your browser to access the upload form.

3. Select the audio file you want to upload and replace.

4. Once the file has been successfully uploaded, the application will display a confirmation message.

## Function Descriptions

### `upload_file`

The main route (`/`) that handles file uploads. It validates that the file is present, saves it to the `uploads/` folder, and then calls the `replace_audio_file` function to send it to the Cisco API.

### `replace_audio_file`

A function that makes a `PUT` request to the Cisco API to replace the audio file. It sends both the file and a JSON object containing the required audio information for the API.

## Additional Notes

- Make sure the authentication token is up-to-date and has the necessary permissions.
- Verify the audio file type and ensure the MIME type (`audio/mpeg`) matches the file you’re uploading.
- The structure of `audio_file_info` may vary according to the Cisco API specifications; check the API documentation for more details.
