import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./Components/Navbar";
import Footer from "./Components/Footer";

import Home from "./pages/Home";
import About from "./pages/About";
import Precautions from "./pages/Precautions";
import Types from "./pages/Types";
import Detection from "./pages/Detection";

function App() {
  return (
    <Router>
      <div className="overlay">
        <Navbar />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/precautions" element={<Precautions />} />
          <Route path="/types" element={<Types />} />
          <Route path="/detection" element={<Detection />} />
        </Routes>

        <Footer />
      </div>
    </Router>
  );
}

export default App;
