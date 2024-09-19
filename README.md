# Movie Recommender Engine

A content-based Movie Recommender System built using Python. This project leverages natural language processing and machine learning techniques to recommend movies similar to a selected movie. The core functionalities are implemented in `Preprocessing.py`, while `app.py` handles the deployment using Streamlit, providing an interactive web interface.

## Demo
[![YouTube](http://i.ytimg.com/vi/f7QgOaZI24Y/hqdefault.jpg)](https://www.youtube.com/watch?v=f7QgOaZI24Y)

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [API Setup](#api-setup)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Content-Based Recommendations**: Recommends movies based on content similarity using cosine similarity.
- **Interactive Web Interface**: Users can select a movie and receive top 5 similar movie recommendations with posters.
- **Movie Posters**: Fetches and displays movie posters using The Movie Database (TMDB) API.
- **Deployment Ready**: Easily deployable using Streamlit for web applications.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nnilayy/Movie-Recommender-Engine.git
   cd Movie-Recommender-Engine
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   uv venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up TMDB API Key**

   - Obtain an API key from [TMDB](https://www.themoviedb.org/documentation/api).
   - **Option 1 (Development)**: Create a `.env` file in the root directory and add:

     ```env
     TMDB_API_KEY=your_api_key_here
     ```

     *Ensure that `python-dotenv` is installed.*

   - **Option 2 (Production/Streamlit Sharing)**: Add the API key to Streamlit secrets.

     ```ini
     # In .streamlit/secrets.toml
     TMDB_API_KEY = "your_api_key_here"
     ```

## Usage

1. **Data Preprocessing**

   Run the `Preprocessing.py` script to process the dataset and generate necessary pickle files for the recommendation engine.

   ```bash
   python Preprocessing.py
   ```

   *This script will generate `movie_dict.pkl` and `similarity.pkl` inside the `model_files` directory.*

2. **Run the App**

   ```bash
   streamlit run app.py
   ```

3. **Interact with the App**

   - Access the app at `http://localhost:8501` in your web browser.
   - Select a movie from the dropdown menu.
   - View the top 5 recommended movies along with their posters.

## Project Structure

```
Movie-Recommender-Engine/
── app.py
── Preprocessing.py
── requirements.txt
── README.md
── model_files/
│   ├── movie_dict.pkl
│   ── similarity.pkl
── .env
```

- **app.py**: The Streamlit app handling user interactions and displaying recommendations.
- **Preprocessing.py**: Script for preprocessing data and building the recommendation model.
- **requirements.txt**: Lists all Python dependencies.
- **model_files/**: Directory containing serialized model files.
- **.env**: File containing environment variables (not included in the repository).

## API Setup

To fetch movie posters, the app uses TMDB API. Follow these steps to set up:

1. **Register on TMDB**

   - Sign up at [TMDB](https://www.themoviedb.org/signup) to create an account.
   - Navigate to [API section](https://www.themoviedb.org/documentation/api) and apply for an API key.

2. **Add API Key to the Project**

   - As mentioned in the [Installation](#installation) section, add your API key using one of the options.

3. **Modify `app.py` (If Necessary)**

   - Ensure that `tmdb_api_key` is correctly set in `app.py`.

     ```python
     # If using .env file
     from dotenv import load_dotenv
     load_dotenv()
     tmdb_api_key = os.getenv('TMDB_API_KEY')
     ```

     ```python
     # If using Streamlit secrets
     tmdb_api_key = st.secrets["TMDB_API_KEY"]
     ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Changes**

   ```bash
   git commit -m "Add your message"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- **Datasets**: The dataset used for this project is sourced from [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
- **Inspiration**: This project is inspired by the Movie Recommendation systems commonly seen on platforms like Netflix and Amazon Prime.
- **Libraries and Tools**:
  - [Pandas](https://pandas.pydata.org/)
  - [NumPy](https://numpy.org/)
  - [Scikit-Learn](https://scikit-learn.org/stable/)
  - [Streamlit](https://streamlit.io/)
  - [NLTK](https://www.nltk.org/)

## Contact

- **Author**: Nilay Kumar Bhatnagar
- **Email**: nnilayy.work@gmail.com
