import "./Header.css";

const Header = ({ appName }) => {
  return (
    <header className="header">
      <h1>{appName}</h1>
      <p>Favorite songs marked with a star</p>
    </header>
  );
};

export default Header;
