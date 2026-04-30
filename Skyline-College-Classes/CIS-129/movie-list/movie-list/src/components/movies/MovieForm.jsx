// import functions
import { useState, useEffect } from 'react'
import { v4 as getUniqueID } from 'uuid';

// import components and CSS
import FormInput from '../common/FormInput';
import FormButtons from '../common/FormButtons';
import './MovieForm.css';

const MovieForm = ({ selectedMovie, onAdd, onEdit, onDelete, onCancel }) => {
    // state variables
    const [name, setName] = useState(''); 
    const [year, setYear] = useState(''); 

    // effect to prefill the form. this effect runs when
    // the component mounts and when selectedMovie changes
    useEffect(() => {
        if (selectedMovie) {
            setName(selectedMovie.name);
            setYear(selectedMovie.year.toString()); // convert year to string for input
        } else {
            setName('');
            setYear('');
        }
    }, [selectedMovie]);  // dependency array 

    // determine whether movie is being added, edited, or deleted
    const isEditing = selectedMovie?.mode === 'edit';
    const isDeleting = selectedMovie?.mode === 'delete';
    const isAdding = !selectedMovie;
  
    // event handler to submit form
    const handleSubmit = (e) => {
        // prevent default form submission behavior
        e.preventDefault();

        // add, edit, or delete movie
        if (isAdding) {
            onAdd({ id: getUniqueID(), name, year: +year }); // convert year to number
        } else if (isEditing) {
            onEdit({ ...selectedMovie, name, year: +year }); // convert year to number
        } else if (isDeleting) { 
            onDelete(selectedMovie.id);
        }

        // reset form fields
        setName('');
        setYear('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="movie">
                <h2>
                    {isAdding && "Add Movie"}
                    {isEditing && "Edit Movie"}
                    {isDeleting && "Confirm Delete"}
                </h2>
                <FormInput
                    label="Name"
                    name="name"
                    value={name}                              // state variable
                    onChange={(e) => setName(e.target.value)} // state setter
                    placeholder="Name"
                    disabled={isDeleting}  // make read-only if deleting
                    required
                />
                <FormInput
                    label="Year"
                    type="number"
                    name="year"
                    value={year}                              // state variable
                    onChange={(e) => setYear(e.target.value)} // state setter
                    placeholder="Year"
                    disabled={isDeleting}  // make read-only if deleting
                    required
                />
            </div>
            <FormButtons
                isEditing={isEditing}
                isDeleting={isDeleting}
                onCancel={onCancel} 
            />
        </form>
    )
}

export default MovieForm;