import { useEffect, useState } from "react";
import "./MovieForm.css";

const MovieForm = ({
  movies,
  selectedMovie,
  onAdd,
  onEdit,
  onDelete,
  onCancel,
}) => {
  const [name, setName] = useState("");
  const [year, setYear] = useState("");

  useEffect(() => {
    if (selectedMovie && selectedMovie.mode === "edit") {
      setName(selectedMovie.name);
      setYear(selectedMovie.year);
    } else {
      setName("");
      setYear("");
    }
  }, [selectedMovie]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name.trim() || !year) return;
    if (selectedMovie && selectedMovie.mode === "edit") {
      onEdit({ id: selectedMovie.id, name: name.trim(), year: Number(year) });
    } else {
      const newId =
        movies.length > 0 ? Math.max(...movies.map((m) => m.id)) + 1 : 1;
      onAdd({ id: newId, name: name.trim(), year: Number(year) });
    }
    setName("");
    setYear("");
  };

  return (
    <div className="movie-form">
      <h2>
        {selectedMovie?.mode === "edit"
          ? "Edit Movie"
          : selectedMovie?.mode === "delete"
            ? "Delete Movie"
            : "Add Movie"}
      </h2>

      {selectedMovie?.mode === "delete" ? (
        <div className="delete-confirm">
          <p>
            Are you sure you want to delete{" "}
            <strong>{selectedMovie.name}</strong>?
          </p>
          <div className="form-buttons">
            <button className="btn" onClick={() => onDelete(selectedMovie.id)}>
              Yes, Delete
            </button>
            <button className="btn" onClick={onCancel}>
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Name</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div className="form-group">
            <label>Year</label>
            <input
              type="number"
              value={year}
              onChange={(e) => setYear(e.target.value)}
            />
          </div>
          <div className="form-buttons">
            <button type="submit" className="btn">
              {selectedMovie?.mode === "edit" ? "Update" : "Add Movie"}
            </button>
            <button type="button" className="btn" onClick={onCancel}>
              Cancel
            </button>
          </div>
        </form>
      )}
    </div>
  );
};

export default MovieForm;
