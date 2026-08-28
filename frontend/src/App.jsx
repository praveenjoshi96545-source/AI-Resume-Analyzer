import { useState } from "react";
import "./App.css";

function App() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  function selectFile(event) {
    setFile(event.target.files[0]);
  }

  async function uploadResume() {

    if (!file) {
      alert("Please select your resume");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    
    setLoading(true);
    setError(null);
    setResult(null);

    try {

      const response = await fetch(
        "http://127.0.0.1:5000/upload",
        {
          method: "POST",
          body: formData
        }
      );

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      if (data.error) {
        setError(data.error);
      } else {
        setResult(data);
      }

    } catch (error) {
      console.error("Error:", error);
      setError(error.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">

      <h1>AI Resume Analyzer</h1>

      <p>
        Upload your resume and check your ATS score
      </p>

      <input
        type="file"
        accept=".pdf"
        onChange={selectFile}
      />

      <br />

      <button onClick={uploadResume} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {error && (
        <div className="error">
          <h3>Error: {error}</h3>
        </div>
      )}

      {result && (

        <div className="result">

          <h2>
            ATS Score: {result.ats_score}/100
          </h2>

          <h2>
            AI Job Match: {result.ai_match_score}%
          </h2>


          <h3>Skills Found</h3>

          <div>

            {result.skills.map((skill, index) => (

              <span className="skill" key={index}>
                {skill}
              </span>

            ))}

          </div>


          <h3>Recommended Jobs</h3>

          {result.recommended_jobs.map((job, index) => (

            <div className="job" key={index}>

              <h4>{job.job}</h4>

              <p>
                Match: {job.match}%
              </p>

              <p>
                Skills: {job.skills.join(", ")}
              </p>

            </div>

          ))}

        </div>

      )}

    </div>
  );
}

export default App;