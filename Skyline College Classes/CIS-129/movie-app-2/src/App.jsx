import { useState } from "react";

import Header from "./components/layout/Header";
import Main from "./components/layout/Main";
import Sidebar from "./components/layout/Sidebar";
import Footer from "./components/layout/Footer";

import MovieList from "./components/movies/MovieList";
import MovieForm from "./components/movies/MovieForm";

import "./App.css";

const appName = "My Movies";

const initialMovies = [
  { id: 1, name: "Wicked", year: 2024 },
  { id: 2, name: "The Matrix", year: 1999 },
];

const App = () => {
  const [movies, setMovies] = useState(initialMovies);
  const [selectedMovie, setSelectedMovie] = useState(null);

  const handleAdd = (newMovie) => {
    setMovies((prev) => [...prev, newMovie]);
  };

  const handleSelect = (movie, mode) => {
    setSelectedMovie({ ...movie, mode });
  };

  // edit a movie
  const handleEdit = (updatedMovie) => {
    setMovies(
      (
        prev, // updates MovieList
      ) =>
        prev.map((movie) =>
          movie.id === updatedMovie.id ? updatedMovie : movie,
        ),
    );
    setSelectedMovie(null); // updates MovieForm to add mode
  };

  // delete a movie
  const handleDelete = (id) => {
    setMovies(
      (
        prev, // updates MovieList
      ) => prev.filter((movie) => movie.id !== id),
    );
    setSelectedMovie(null); // updates MovieForm to add mode
  };

  // cancel edit or delete
  const handleCancel = () => {
    setSelectedMovie(null); // updates MovieForm to add mode
  };

  return (
    <div className="container">
      <Header text={appName} />
      <Main>
        <MovieList movies={movies} onSelect={handleSelect} />
      </Main>
      <Sidebar>
        <MovieForm
          movies={movies}
          selectedMovie={selectedMovie}
          onAdd={handleAdd}
          onEdit={handleEdit}
          onDelete={handleDelete}
          onCancel={handleCancel}
        />
      </Sidebar>
      <Footer text={appName} />
    </div>
  );
};

export default App;
