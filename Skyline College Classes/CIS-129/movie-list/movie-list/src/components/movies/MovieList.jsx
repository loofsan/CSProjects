import MovieListItem from "./MovieListItem";  
import "./MovieList.css"; 

const MovieList = ({ movies, onSelect }) => (
    <ul className="movie-list">
        {movies.length === 0 ? (
            <MovieListItem movie={null} />
        ) : (
            movies.map((movie) => 
            <MovieListItem 
                key={movie.id} 
                movie={movie} 
                onSelect={onSelect}
            />
            )
        )}
    </ul>
);

export default MovieList;