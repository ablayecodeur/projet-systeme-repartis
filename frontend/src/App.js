import React, { useEffect, useState } from "react";

// En dev via docker-compose : http://localhost:8000/api/produits/
// En cluster Minikube : IP + NodePort du service backend (voir .env)
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000/api/produits/";

function App() {
  const [produits, setProduits] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((response) => response.json())
      .then((data) => setProduits(data))
      .catch((error) => console.error("Erreur :", error));
  }, []);

  return (
    <div style={{ padding: "40px" }}>
      <h1>Liste des Produits</h1>
      <ul>
        {produits.map((produit) => (
          <li key={produit.id}>
            <strong>{produit.nom}</strong> - {produit.prix} €
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;