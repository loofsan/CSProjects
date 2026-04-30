import "./MovieList.css";
import { FaTrash, FaPencilAlt } from "react-icons/fa";

const MovieList = ({ movies, onSelect }) => {
  return (
    <div className="movie-list">
      {movies.length === 0 ? (
        <p className="no-movies">No movies yet.</p>
      ) : (
        movies.map((movie) => (
          <div key={movie.id} className="movie-item">
            <span className="movie-title">
              {movie.name} ({movie.year})
            </span>
            <div className="movie-actions">
              <button
                className="icon-btn delete-btn"
                onClick={() => onSelect(movie, "delete")}
                title="Delete"
              >
                <FaTrash />
              </button>
              <button
                className="icon-btn edit-btn"
                onClick={() => onSelect(movie, "edit")}
                title="Edit"
              >
                <FaPencilAlt />
              </button>
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default MovieList;
