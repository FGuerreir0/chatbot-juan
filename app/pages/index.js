import React, { useState, useRef, useEffect } from "react";
import Cat from "../components/Cat"; // Assuming you have a Cat component

export default function TalkingCatApp() {
  const [text, setText] = useState("");
  const [isSpeaking, setIsSpeaking] = useState(false);
  const synthRef = useRef(null);

  useEffect(() => {
    if (typeof window !== "undefined") {
      synthRef.current = window.speechSynthesis;
    }
  }, []);

  const speakText = () => {
    if (text.trim() === "" || !synthRef.current) return;

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.onstart = () => {
      setIsSpeaking(true);
    };
    utterance.onend = () => {
      setIsSpeaking(false);
    };
    synthRef.current.speak(utterance);
  };

  return (
    <div className="app-container">
      <div className="cat-container">
        <Cat isSpeaking= {isSpeaking} />
      </div>
      <input
        type="text"
        placeholder="Type something for the cat to say..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="text-input"
      />
      <button onClick={speakText} className="speak-button">Speak</button>
    </div>
  );
}