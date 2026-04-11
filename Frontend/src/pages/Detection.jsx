import { useState } from "react";
import axios from "axios";
import ResultDisplay from "../components/ResultDisplay";

function Detection() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Upload image");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://localhost:8081/predict", // ✅ make sure matches backend
        formData,
      );

      setResult(response.data);
      setLoading(false);
    } catch (error) {
      alert("Backend not connected");
      setLoading(false);
    }
  };

  return (
    <div className="section">
      <div className="card">
        <h2>AI Detection Module</h2>

        <input
          type="file"
          onChange={(e) => {
            setFile(e.target.files[0]);
            setPreview(URL.createObjectURL(e.target.files[0]));
          }}
        />

        {preview && <img src={preview} width="250" alt="preview" />}

        <button onClick={handleUpload}>
          {loading ? "Analyzing..." : "Analyze Image"}
        </button>

        {result && <ResultDisplay result={result} />}
      </div>
    </div>
  );
}

export default Detection;
