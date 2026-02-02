"use client";

import { useState } from "react";

type Recipe = {
  title: string;
  ingredients: string[];
  steps: string[];
};

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [recipe, setRecipe] = useState<Recipe | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };
  const handleSubmit = async () => {
    if (!file) return;

    setLoading(true);
    setRecipe(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      console.log("API response:", data);

      if (!data.recipe?.ingredients || !data.recipe?.steps) {
        throw new Error("Invalid recipe response");
      }
      setRecipe(data.recipe);
    } catch (err) {
      console.error(err);
      alert("Error uploading video");
    } finally {
      setLoading(false);
    }
  };


  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="bg-white p-8 rounded-xl shadow-md w-full max-w-md">
        <h1 className="text-xl font-semibold mb-4">
          Upload a cooking video
        </h1>

        <input
          type="file"
          accept="video/*"
          onChange={handleFileChange}
          className="mb-4"
        />

        <button
          onClick={handleSubmit}
          disabled={!file || loading}
          className="w-full bg-black text-white py-2 rounded-lg disabled:opacity-50"
        >
          {loading ? "Processing..." : "Generate Recipe"}
        </button>

        {recipe && (
          <>
            <h3 className="font-medium">Ingredients</h3>
            <ul className="list-disc list-inside mb-2">
              {recipe.ingredients.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>
          </>
        )}

        {recipe && (
          <>
            <h3 className="font-medium">Steps</h3>
            <ol className="list-decimal list-inside">
              {recipe.steps.map((step, i) => (
                <li key={i}>{step}</li>
              ))}
            </ol>
          </>
        )}
        
      </div>
    </main>
  );
}



