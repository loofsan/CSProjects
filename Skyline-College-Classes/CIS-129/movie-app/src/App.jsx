import { useState } from "react";
import MovieList from "../components/MovieList";
import Header from "../components/Header";
import Footer from "../components/Footer";
import "./App.css";

// pure function to add a new movie
const addMovie = (movieList, movie) => [...movieList, movie];

// pure function to delete a movie
const deleteMovie = (movieList, id) =>
  movieList.filter((movie) => movie.id !== id);

// define an array of initial movies
const initialMovies = [
  { id: 1, name: "Wizard of Oz", year: 1939 },
  { id: 2, name: "The Matrix", year: 1999 },
  { id: 3, name: "Wicked", year: 2024 },
  { id: 4, name: "The Godfather", year: 1972 },
];

const App = () => {
  const [movies, setMovies] = useState(initialMovies);

  const handleAddMovie = () => {
    const newId =
      movies.length > 0 ? Math.max(...movies.map((m) => m.id)) + 1 : 1;

    setMovies(
      addMovie(movies, {
        id: newId,
        name: "Inception",
        year: 2010,
      }),
    );
  };

  const handleDeleteMovie = (id) => setMovies(deleteMovie(movies, id));

  return (
    <>
      <Header />

      <main className="main-content">
        <MovieList
          movies={movies}
          onAdd={handleAddMovie}
          onDelete={handleDeleteMovie}
        />
      </main>

      <Footer />
    </>
  );
};

export default App;
