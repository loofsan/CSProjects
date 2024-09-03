def city_country(city, country, population=""):
	if population: 
		formatted_name = f"{city}, {country} - population: {population}"

		return(f"{formatted_name.title()}")
	else: 
		formatted_name = f"{city}, {country}"

		return(f"{formatted_name.title()}")

