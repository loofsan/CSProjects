import './FormInput.css';

const FormInput = ({ label, name, value, onChange, ...props }) => (
    <>
        <label className="form-label" htmlFor={name}>{label}</label>
        <input
            className="form-input"
            type="text" 
            id={name}
            name={name}
            value={value}
            onChange={onChange}
            {...props}  // Spread operator to include any additional props
        />
    </>
);

export default FormInput;