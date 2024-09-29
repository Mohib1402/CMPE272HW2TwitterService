# Mastodon Service

This project implements a web service that interacts with the Mastodon API to programmatically create, retrieve, and delete posts. The service is built using **Flask** as the web framework and **Mastodon.py** for API interactions.

### Contributors
- [Mohibkhan Pathan](https://github.com/Mohib1402) (Initial Twitter Service development, later renamed to Mastodon Service)
- [Praful John](https://github.com/Praful-John2409) (Enhancements and new functionality)

## Features
1. **Create a Post**: Users can create new posts via the web interface, which are posted to Mastodon using the `status_post` method.
2. **Retrieve All Posts**: Fetch all posts from the Mastodon timeline using `timeline_home` and display them in the web interface.
3. **Retrieve a Post by ID**: Fetch a specific post by its ID and display it.
4. **Delete a Post**: Delete a specific post by its ID.
5. **Input Validation**: Ensure posts are non-empty and valid IDs are provided.
6. **Rate Limit Handling**: Handle Mastodon API rate limits by showing appropriate error messages.
7. **Unit Testing**: Ensure correctness of API interactions through mocked unit tests.

## Technologies
- **Python**: Programming language for backend logic.
- **Flask**: Web framework for creating routes and serving HTML pages.
- **Mastodon.py**: Library for interacting with the Mastodon API.
- **HTML/CSS**: For front-end layout and design.

## Project Structure

- `app.py`: Main application file containing the Flask routes and logic to interact with Mastodon.
- `index.html`: HTML file for the web interface where users can create, retrieve, and delete posts.
- `test_app.py`: Unit tests for the application, using `unittest.mock` to simulate Mastodon API responses.

## Setup Instructions

### Prerequisites
1. Python 3.x
2. Mastodon Developer Account ([Mastodon API Docs](https://docs.joinmastodon.org/))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mohib1402/CMPE272HW2TwitterService.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CMPE272HW2TwitterService
   ```
3. Install the required packages:
   ```bash
   pip install Mastodon.py
   ```

4. Create a `.env` file with your Mastodon API credentials:
   ```
   MASTODON_API_BASE_URL="https://mastodon.social"
   MASTODON_ACCESS_TOKEN="your_access_token_here"
   ```

5. Run the Flask app:
   ```bash
   pip install Flask #if you already don't have Flask
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage
- **Create a Post**: Enter the text for your post in the input box and click "Post".
- **Retrieve All Posts**: Click "Retrieve All" to fetch all the posts from your Mastodon timeline.
- **Retrieve a Post by ID**: Enter the ID of the post you want to retrieve and click "Retrieve by ID".
- **Delete a Post**: Click the delete button next to any post to delete it from Mastodon.

## Work Done

### Mohibkhan Pathan:
- Set up the initial Twitter (renamed Mastodon) service.
- Created backend routes for creating, retrieving, and deleting posts using Mastodon API.
- Developed the HTML and inline CSS for the web interface.

### Praful John:
- Added the functionality to retrieve a post by its **Post ID**.
- Enhanced the UI to display the **Post ID** next to each post.
- Handled **input validation** and **rate limit errors**.
- Developed comprehensive **unit tests** for the API interactions using `unittest.mock`.

## Screenshots

### 1. Modified UI to Show Post ID
[Post ID Display](https://github.com/Mohib1402/CMPE272HW2TwitterService/blob/main/MastodonServiceDoc.docx)

### 2. Retrieval by Post ID
[Retrieve by ID](https://github.com/Mohib1402/CMPE272HW2TwitterService/blob/main/MastodonServiceDoc.docx)

### 3. Input Validation and Error Handling
[Validation](https://github.com/Mohib1402/CMPE272HW2TwitterService/blob/main/MastodonServiceDoc.docx)

### 4. Unit Tests Passing
[Unit Tests](https://github.com/Mohib1402/CMPE272HW2TwitterService/blob/main/MastodonServiceDoc.docx)

## Unit Testing
The following unit tests are implemented in `test_app.py`:
1. **test_create_post**: Mocks `mastodon.status_post` to simulate post creation and checks for successful redirects.
2. **test_retrieve_all_posts**: Mocks `mastodon.timeline_home` to simulate fetching all posts and checks for correct display.
3. **test_retrieve_post_by_id**: Mocks `mastodon.status` to fetch a specific post by ID and checks for correct display.
4. **test_delete_post**: Mocks `mastodon.status_delete` to simulate post deletion and checks for successful redirects.

### Running Tests:
To run the unit tests:
```bash
python -m unittest test_app.py
```

## Error Handling
- **Rate Limit Handling**: If the Mastodon API returns a rate limit error (429), the app will display a user-friendly error message.
- **Input Validation**: Ensures that posts are not empty and post IDs are valid before making API requests.
