import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div className="navbar">
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/precautions">Precautions</Link>
      <Link to="/types">Types of Cancer</Link>
      <Link to="/detection">Detection</Link>
    </div>
  );
}

export default Navbar;
