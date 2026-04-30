// import the useState hook from the React module
import { useState } from 'react'

// import the components for the page layout
import Header from './components/layout/Header';
import Main from './components/layout/Main';
import Sidebar from './components/layout/Sidebar';
import Footer from './components/layout/Footer';

// import the components for displaying the movie list and form
import MovieList from './components/movies/MovieList';
import MovieForm from './components/movies/MovieForm';

// import the CSS for the App component
import './App.css';

// app name to display in the header and footer
const appName = 'My Movies';

// sample movies to populate app on load
const initialMovies = [
    { id: 1, name: "Wicked", year: 2024 },
    { id: 2, name: "The Matrix", year: 1999 },
];

const App = () => {
    // set up two state variables, their setter functions, and initial values
    const [movies, setMovies] = useState(initialMovies);
    const [selectedMovie, setSelectedMovie] = useState(null);

    /**********************************************/
    /* event handlers for MovieList and MovieForm */
    /**********************************************/

    // add a new movie
    const handleAdd = (newMovie) => {
        setMovies((prev) => [...prev, newMovie]);   // updates MovieList
    };

    // select a movie and specify the mode (edit or delete)
    const handleSelect = (movie, mode) => {
        setSelectedMovie({...movie, mode});      // updates MovieForm
    };

    // edit a movie
    const handleEdit = (updatedMovie) => {
        setMovies((prev) =>           // updates MovieList
            prev.map((movie) =>
                movie.id === updatedMovie.id ? updatedMovie : movie
            )
        );
        setSelectedMovie(null);       // updates MovieForm to add mode
    };

    // delete a movie
    const handleDelete = (id) => {
        setMovies((prev) =>           // updates MovieList
            prev.filter((movie) => 
                movie.id !== id
            )
        );
        setSelectedMovie(null);       // updates MovieForm to add mode
    };

    // cancel edit or delete
    const handleCancel = () => {
        setSelectedMovie(null);       // updates MovieForm to add mode
    };

    return (
        <div className="container">
            <Header text={appName} />
            <Main>
                <MovieList 
                    movies={movies} 
                    onSelect={handleSelect}
                />
            </Main>
            <Sidebar>
                <MovieForm 
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