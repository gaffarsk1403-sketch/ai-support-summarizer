import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

type Result = {
  case_id: string;
  summary: string;
  next_actions: string[];
};

function App() {
  const [message, setMessage] = useState("");
  const [notes, setNotes] = useState("");
  const [result, setResult] = useState<Result | null>(null);
  const [loading, setLoading] = useState(false);

  async function summarize() {
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://localhost:8000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          case_id: "DEMO-001",
          customer_message: message,
          agent_notes: notes || null,
        }),
      });

      if (!response.ok) throw new Error("Request failed");
      setResult(await response.json());
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page">
      <section className="card">
        <p className="eyebrow">AI support workflow</p>
        <h1>Support Case Summarizer</h1>
        <p className="subtitle">
          Turn a long customer conversation into a concise internal summary and next actions.
        </p>

        <label>Customer message</label>
        <textarea
          rows={8}
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          placeholder="Paste a customer message..."
        />

        <label>Agent notes</label>
        <textarea
          rows={4}
          value={notes}
          onChange={(event) => setNotes(event.target.value)}
          placeholder="Optional internal notes..."
        />

        <button disabled={loading || message.trim().length < 5} onClick={summarize}>
          {loading ? "Summarizing..." : "Generate summary"}
        </button>

        {result && (
          <section className="result">
            <h2>Summary</h2>
            <p>{result.summary}</p>

            <h2>Next actions</h2>
            <ul>
              {result.next_actions.map((action) => (
                <li key={action}>{action}</li>
              ))}
            </ul>
          </section>
        )}
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
