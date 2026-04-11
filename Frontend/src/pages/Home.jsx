function Home() {
  return (
    <div className="section">
      <div className="card">
        <h1>AI-Based Oral Cancer Detection System</h1>

        <p style={{ textAlign: "justify" }}>
          Oral cancer remains a major public health concern, particularly in
          regions where tobacco and alcohol use are widespread. Detecting
          malignant and precancerous changes at an early stage greatly increases
          the chances of effective treatment and survival.
        </p>

        <p style={{ textAlign: "justify" }}>
          In many cases, diagnosis depends on clinical expertise and manual
          evaluation of lesions, which can be subjective and prone to variation
          across practitioners. With the rapid growth of artificial intelligence
          and image-based deep learning, automated diagnostic systems are
          emerging as valuable tools to support healthcare professionals.
        </p>

        <p style={{ textAlign: "justify" }}>
          These systems not only provide consistent and accurate predictions but
          can also highlight the areas in medical images that influence
          decisions, thereby improving transparency and trust in AI-assisted
          healthcare.
        </p>

        <hr />

        <h3>Why AI in Oral Cancer Detection?</h3>
        <ul>
          <li>Early detection improves survival rate significantly.</li>
          <li>Reduces human diagnostic variability.</li>
          <li>Provides explainable visual evidence using Grad-CAM.</li>
          <li>Assists doctors as a decision-support system.</li>
        </ul>

        <hr />

        <h2>Global Oral Cancer Statistics</h2>

        <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
          <div className="card" style={{ flex: "1", minWidth: "200px" }}>
            <h3>377,000+</h3>
            <p>New cases reported globally each year</p>
          </div>

          <div className="card" style={{ flex: "1", minWidth: "200px" }}>
            <h3>177,000+</h3>
            <p>Annual deaths worldwide</p>
          </div>

          <div className="card" style={{ flex: "1", minWidth: "200px" }}>
            <h3>80%</h3>
            <p>Survival rate when detected early</p>
          </div>
        </div>

        <hr />

        <h2>Why Early Detection Matters?</h2>

        <p style={{ textAlign: "justify" }}>
          Early-stage oral cancer can often be treated successfully with minimal
          invasive procedures. However, late-stage detection significantly
          reduces survival rates and requires aggressive treatment. AI-assisted
          screening systems help identify suspicious lesions at an earlier
          stage.
        </p>
      </div>
    </div>
  );
}

export default Home;
