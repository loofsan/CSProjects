import './FormButtons.css';

const FormButtons = ({ isEditing, isDeleting, onCancel }) => (
    <>
        <button type="submit" className="btn">
            {isDeleting ? 'Delete' : isEditing ? 'Update' : 'Add'}
        </button>
        {(isDeleting || isEditing) && (
            <button type="button" className="btn" onClick={onCancel}>
                Cancel
            </button>
        )}
    </>
);

export default FormButtons;