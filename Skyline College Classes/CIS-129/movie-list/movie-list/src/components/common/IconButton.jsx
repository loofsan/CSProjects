import './IconButton.css';

const IconButton = ({ title, iconClass, onClick }) => {
    return (
        <button 
            className="icon-btn" 
            type="button"
            aria-label={title}
            title={title}
            onClick={onClick}>
            <i className={iconClass} aria-hidden="true"></i>
        </button>
    );
};

export default IconButton;