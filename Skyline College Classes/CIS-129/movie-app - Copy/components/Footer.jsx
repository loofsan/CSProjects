import "./Footer.css";

const Footer = ({ appName }) => {
  return (
    <footer className="footer">
      <p>© {appName}. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
