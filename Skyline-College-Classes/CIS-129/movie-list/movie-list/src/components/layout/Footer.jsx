import './Footer.css';

const Footer = ({ text }) => (
    <footer className="footer">
        <p>© {text}. All rights reserved.</p>
    </footer>
);

export default Footer;