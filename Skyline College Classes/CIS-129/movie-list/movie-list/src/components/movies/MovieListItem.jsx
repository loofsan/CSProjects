import Icon from "../common/Icon";
import "./MovieListItem.css";

const MovieListItem = ({ movie, onSelect }) => (
    movie? (
        <li className="movie-list-item">
            {movie.name} ({movie.year})
            <Icon 
                title="Edit" 
                className="icon fa fa-pencil" 
                onClick={() => onSelect(movie, 'edit')} 
            />
            <Icon
                title="Delete" 
                className="icon fa fa-trash" 
                onClick={() => onSelect(movie, 'delete')} 
            /> 
        </li>
    ) : (
        <li className="movie-list-empty">
            No movies yet. Add your first one!
        </li>
    )
);

export default MovieListItem;