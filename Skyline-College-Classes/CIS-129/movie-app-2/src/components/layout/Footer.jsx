import "./Footer.css";

const Footer = ({ text }) => {
  return (
    <footer className="footer">
      <p>© {text}. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
