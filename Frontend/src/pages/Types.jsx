import Oral1 from "../assets/oral1.jpg";
import Oral2 from "../assets/oral2.jpg";
import Oral3 from "../assets/oral3.jpg";
import Oral4 from "../assets/oral4.jpg";

function Types() {
  return (
    <div className="section">
      <h2 style={{ textAlign: "center", marginBottom: "30px" }}>
        Types of Oral Cancer
      </h2>

      <div className="gallery">
        <div className="type-card">
          <img src={Oral1} alt="Squamous Cell Carcinoma" />
          <h4>Squamous Cell Carcinoma</h4>
          <p>
            Accounts for nearly 90% of oral cancers. Develops in the thin, flat
            squamous cells lining the oral cavity.
          </p>
        </div>

        <div className="type-card">
          <img src={Oral2} alt="Oral Leukoplakia" />
          <h4>Oral Leukoplakia</h4>
          <p>
            A white patch or plaque that may become precancerous if not treated.
          </p>
        </div>

        <div className="type-card">
          <img src={Oral3} alt="Tongue Cancer" />
          <h4>Tongue Cancer</h4>
          <p>
            Malignancy affecting anterior or posterior tongue region, often
            linked to tobacco use.
          </p>
        </div>

        <div className="type-card">
          <img src={Oral4} alt="Mouth Cancer" />
          <h4>Mouth Cancer</h4>
          <p>
            Malignant growth occurring in the lips, gums, cheeks, floor of mouth
            or palate.
          </p>
        </div>
      </div>
    </div>
  );
}

export default Types;
