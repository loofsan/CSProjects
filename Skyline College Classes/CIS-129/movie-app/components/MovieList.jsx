import { useState } from "react";
import "./MovieList.css";

const MovieList = ({ movies, onAdd, onDelete }) => {
  const [activeId, setActiveId] = useState(null);

  return (
    <div className="movie-list">
      <ul>
        {movies.length === 0 ? (
          <li>There are no movies.</li>
        ) : (
          movies.map((movie) => (
            <li
              key={movie.id}
              className={activeId === movie.id ? "active" : ""}
              onClick={() => setActiveId(movie.id)}
            >
              {movie.name} ({movie.year})
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  onDelete(movie.id);
                }}
              >
                Delete
              </button>
            </li>
          ))
        )}
      </ul>

      {/* <button className="add-movie-btn" onClick={onAdd}>
        Add Movie
      </button> */}
    </div>
  );
};

export default MovieList;
