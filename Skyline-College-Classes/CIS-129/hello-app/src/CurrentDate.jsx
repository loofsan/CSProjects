import './CurrentDate.css';

	const CurrentDate = () => { 
		const today = new Date(); 
		const formattedDate = today.toLocaleDateString();

		return ( 
			<div> Today's Date: {formattedDate}
			</div> 
			); 
		}; 

export default CurrentDate;

